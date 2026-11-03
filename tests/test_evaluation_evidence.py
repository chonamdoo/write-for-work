import hashlib
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BEHAVIOR = ROOT / "tests" / "behavior"
RECORD = BEHAVIOR / "evidence" / "2026-11-03-korean-slop" / "final.json"
JUDGMENTS = {"pass", "fail", "not-applicable"}


def load_checks():
    spec = importlib.util.spec_from_file_location("checks", BEHAVIOR / "checks.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class EvaluationEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(RECORD.read_text(encoding="utf-8"))
        cls.cases_bytes = (BEHAVIOR / "cases.json").read_bytes()
        cls.cases = {case["id"]: case for case in json.loads(cls.cases_bytes)}
        cls.checks = load_checks()

    def test_record_matches_current_cases(self):
        self.assertEqual(self.record["cases_sha256"], hashlib.sha256(self.cases_bytes).hexdigest())
        for case in self.cases.values():
            for criterion in case["acceptance"]:
                self.assertTrue(criterion["criterion"].strip())
                self.assertTrue(criterion["source"].strip())
                self.assertIsInstance(criterion["required"], bool)
                self.assertTrue(criterion["reason"].strip())

    def test_string_checks_reproduce(self):
        for run in self.record["runs"]:
            with self.subTest(variant=run["variant"], case=run["case"], repeat=run["repeat"]):
                expected = {str(i): ok for i, ok in self.checks.run(run["case"], run["output"]).items()}
                self.assertEqual(run["string_checks"], expected)

    def test_every_criterion_is_judged_consistently(self):
        for run in self.record["runs"]:
            with self.subTest(variant=run["variant"], case=run["case"], repeat=run["repeat"]):
                criteria = self.cases[run["case"]]["acceptance"]
                self.assertEqual(set(run["judgments"]), {str(i) for i in range(len(criteria))})
                required_fail = False
                for index, judgment in run["judgments"].items():
                    self.assertIn(judgment["judgment"], JUDGMENTS)
                    self.assertEqual(judgment["required"], criteria[int(index)]["required"])
                    if judgment["method"] == "string":
                        self.assertEqual(judgment["judgment"] == "pass", run["string_checks"][index])
                    else:
                        self.assertTrue(judgment["reason"].strip())
                    required_fail |= judgment["required"] and judgment["judgment"] == "fail"
                self.assertEqual(run["required_pass"], not required_fail)

    def test_summary_counts(self):
        for variant, summary in self.record["summary"].items():
            runs = [run for run in self.record["runs"] if run["variant"] == variant]
            self.assertEqual(summary["runs"], len(runs))
            self.assertEqual(summary["required_pass"], sum(run["required_pass"] for run in runs))
            advisory = sum(
                1
                for run in runs
                for judgment in run["judgments"].values()
                if not judgment["required"] and judgment["judgment"] == "fail"
            )
            self.assertEqual(summary["advisory_fail"], advisory)


if __name__ == "__main__":
    unittest.main()
