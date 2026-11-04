# Behavioral cases

[`cases.json`](cases.json) holds synthetic Korean requests for `write-for-work`. Each case has:

- `request`: the only text an executor receives as the user message.
- `acceptance`: evaluator-only criteria, each with its `source`, whether it is `required`, and the `reason`. `reading_required: true` marks a criterion whose meaning a string cannot settle; it needs a reading judgment even when a string check exists. Never send criteria to an executor.

Executors receive the skill package files explicitly in the system prompt and run without tools or conversation history. Run the previous skill version on the same requests when a change claims different behavior; a case that both versions pass shows no difference.

[`checks.py`](checks.py) holds the string checks. They read only the revised artifact, which ends at a separator or a labeled note, and cover only what a string can show; a few named checks read the full response. A failed string check fails its criterion. Other criteria are judged by reading, and each such judgment stores its reason.

Recorded runs live in [`evidence/`](evidence/). Every record with a `design` field is checked by [`test_evaluation_evidence.py`](../test_evaluation_evidence.py): exactly one run per variant, case, and repeat, consistent judgments, and stored counts. Only the latest record, `2026-11-04-adversarial-review/final.json`, must match the current `cases.json` and `checks.py`; the test fails when either changes without a new record. Older records keep the string results of the checks they were judged with. `development.json` has no design and is history only. See the validation records in [`docs/`](../../docs/) for results and limits.
