import hashlib
import importlib.util
import itertools
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BEHAVIOR = ROOT / "tests" / "behavior"
EVIDENCE = BEHAVIOR / "evidence"
LATEST = EVIDENCE / "2026-11-04-adversarial-review" / "final.json"
JUDGMENTS = {"pass", "fail", "not-applicable"}
METHODS = {"string", "string+reading", "reading", "override"}


def load_checks():
    spec = importlib.util.spec_from_file_location("checks", BEHAVIOR / "checks.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_records():
    """Records that declare a run design are covered; exploratory records without one are history."""
    records = {}
    for path in sorted(EVIDENCE.glob("*/*.json")):
        record = json.loads(path.read_text(encoding="utf-8"))
        if "design" in record:
            records[path.relative_to(EVIDENCE).as_posix()] = record
    return records


class EvaluationEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_records()
        cls.cases_bytes = (BEHAVIOR / "cases.json").read_bytes()
        cls.cases = {case["id"]: case for case in json.loads(cls.cases_bytes)}
        cls.checks = load_checks()

    def test_latest_record_matches_current_cases(self):
        latest = self.records[LATEST.relative_to(EVIDENCE).as_posix()]
        self.assertEqual(latest["cases_sha256"], hashlib.sha256(self.cases_bytes).hexdigest())
        self.assertEqual(set(latest["design"]["cases"]), set(self.cases))
        for case in self.cases.values():
            for criterion in case["acceptance"]:
                self.assertTrue(criterion["criterion"].strip())
                self.assertTrue(criterion["source"].strip())
                self.assertIsInstance(criterion["required"], bool)
                self.assertTrue(criterion["reason"].strip())

    def test_runs_match_design_exactly(self):
        for name, record in self.records.items():
            with self.subTest(record=name):
                design = record["design"]
                for axis in ("variants", "cases", "repeats"):
                    self.assertTrue(design[axis], f"empty design axis {axis}")
                    self.assertEqual(len(design[axis]), len(set(design[axis])))
                self.assertTrue(set(design["cases"]) <= set(self.cases))
                self.assertEqual(set(record["summary"]), set(design["variants"]))
                expected = set(itertools.product(design["variants"], design["cases"], design["repeats"]))
                keys = [(run["variant"], run["case"], run["repeat"]) for run in record["runs"]]
                self.assertEqual(len(keys), len(set(keys)), "duplicate runs")
                self.assertEqual(set(keys), expected)

    def test_latest_string_checks_reproduce(self):
        # Older records keep the string results of the checks they were judged with.
        latest = self.records[LATEST.relative_to(EVIDENCE).as_posix()]
        self.assertEqual(latest["checks_sha256"], hashlib.sha256((BEHAVIOR / "checks.py").read_bytes()).hexdigest())
        for run in latest["runs"]:
            with self.subTest(variant=run["variant"], case=run["case"], repeat=run["repeat"]):
                expected = {str(i): ok for i, ok in self.checks.run(run["case"], run["output"]).items()}
                self.assertEqual(run["string_checks"], expected)

    def test_latest_reads_meaning_criteria(self):
        latest = self.records[LATEST.relative_to(EVIDENCE).as_posix()]
        for run in latest["runs"]:
            criteria = self.cases[run["case"]]["acceptance"]
            for index, judgment in run["judgments"].items():
                with self.subTest(variant=run["variant"], case=run["case"], repeat=run["repeat"], criterion=index):
                    if criteria[int(index)].get("reading_required"):
                        self.assertIn(judgment["method"], {"reading", "string+reading", "override"})
                    if index in run["string_checks"]:
                        self.assertIn(judgment["method"], {"string", "string+reading", "override"})

    def test_every_criterion_is_judged_consistently(self):
        for name, record in self.records.items():
            for run in record["runs"]:
                with self.subTest(record=name, variant=run["variant"], case=run["case"], repeat=run["repeat"]):
                    criteria = self.cases[run["case"]]["acceptance"]
                    self.assertEqual(set(run["judgments"]), {str(i) for i in range(len(criteria))})
                    for index, judgment in run["judgments"].items():
                        self.assertIn(judgment["judgment"], JUDGMENTS)
                        self.assertIn(judgment["method"], METHODS)
                        self.assertEqual(judgment["required"], criteria[int(index)]["required"])
                        if judgment["method"] == "string":
                            self.assertEqual(judgment["judgment"] == "pass", run["string_checks"][index])
                        else:
                            self.assertTrue(judgment["reason"].strip())
                        if judgment["method"] == "string+reading" and not run["string_checks"][index]:
                            self.assertEqual(judgment["judgment"], "fail")
                    required_pass = all(
                        j["judgment"] == "pass" for j in run["judgments"].values() if j["required"]
                    )
                    self.assertEqual(run["required_pass"], required_pass)

    def test_summary_counts(self):
        for name, record in self.records.items():
            for variant, summary in record["summary"].items():
                with self.subTest(record=name, variant=variant):
                    runs = [run for run in record["runs"] if run["variant"] == variant]
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
