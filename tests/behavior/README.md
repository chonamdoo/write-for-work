# Behavioral cases

[`cases.json`](cases.json) holds synthetic Korean requests for `write-for-work`. Each case has:

- `request`: the only text an executor receives as the user message.
- `acceptance`: evaluator-only criteria, each with its `source`, whether it is `required`, and the `reason`. Never send them to an executor.

Executors receive the skill package files explicitly in the system prompt and run without tools or conversation history. Run the previous skill version on the same requests when a change claims different behavior; a case that both versions pass shows no difference.

[`checks.py`](checks.py) holds the string checks. They read only the revised artifact, not notes after it, and cover only what a string can show. Other criteria are judged by reading, and each such judgment stores its reason.

Recorded runs live in [`evidence/`](evidence/). `final.json` is the record that [`test_evaluation_evidence.py`](../test_evaluation_evidence.py) verifies against the current `cases.json` and `checks.py`; it fails when either changes without a new record. `pre-merge.json` and `development.json` are earlier rounds kept as history. See [the validation record](../../docs/validation-2026-11-03.md) for results and limits.
