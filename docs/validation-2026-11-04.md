# 2026-11-04 adversarial-review update

This update fixes defects that two adversarial reviews found in `write-for-work` and in its 2026-11-03 evaluation. No change was requested in advance: Claude Opus 5.5 (xhigh) and GPT-6.1-sol (xhigh) audited the skill, its sources, and the recorded outputs, and a second round reviewed the applied diff. The previous version is `main` commit `fea72ad`.

## Exact scope

- `SKILL.md`: a pointer that reader-addressed commands such as `~할 것` are rewritten, not kept as a register; Review returns findings rather than a rewritten artifact; Output behavior names the result for each operation, limits notes to items the requester must resolve, and labels them (`검토 메모:`, `Note:`) instead of starting them with `※`; workflow step 6 compares in both directions; the ending check applies only where the source supports a conclusion.
- `references/plain-language.md`: the command rule with register matching and keep cases; conversion requests (`문장으로 풀어서`) versus `쉽게 풀어서`; modifiers stay attached; the `확인하시어` example keeps `~습니다`; the slot example keeps "채운다"; norm accuracy for particle and middle-dot spacing, comma-free 줄표 asides, and unit nouns after numerals; explicit punctuation requirements beat a reference's convention; two note triggers removed; the adaptation source.
- `references/modes.md`: operation, format, and evidence boundary beat mode preferences; mode outlines apply to Draft and Restructure while preservation checks apply to every operation; no forced mode for short messages; business-report and thread endings only when sourced.
- `references/style-and-integrity.md`: sentence case only for new or rewritten English headings.

Frontmatter, description, and invocation policy are unchanged. No mode, script, or permission was added.

## Review

| Round | Opus 5.5 | GPT-6.1-sol |
| --- | --- | --- |
| 1: audit of `fea72ad` | Revise: 6 major, 6 minor | Revise and re-review: 8 major, 3 minor |
| 2: audit of the applied diff | Do not merge: 1 blocker, 7 major, 2 minor | Revise and re-review: 7 major, 3 minor |

Both round-1 reviews traced the two known problems to skill wording. KP08 kept `~할 것` because the register rule's only exception example was an external notice. `※`-led notes appeared in 13 of 36 runs of the 2026-11-03 version and none of the earlier one; Opus traced them to the `※` example the 2026-11-03 update added. Round 2 found false-failing string checks (for example `"습니다" in a` rejects `부탁드립니다`), cases that repeated skill example sentences, overstated source attribution, and a mode rule that would have skipped preservation checks during Rewrite and Review. All of those were fixed before the runs below.

Adopted against the sources: the command rule is this skill's adaptation of 『쉬운 공문서 쓰기 길잡이』 21–23쪽, which covers documents for the public; extending it to internal notices comes from evaluation case KP08 and its observed failure, and the reference says so. Norm citations were rechecked on korean.go.kr on 2026-11-04.

Not adopted:

- Unifying mixed registers to the majority form (Opus round 1): no source supports it.
- More bound-noun guidance for `만`, `대로`, `뿐`: no observed failure.
- Discovery and reference-loading runs on an installed host, and a qualified Korean editor's blind judgment: not available in this change. Both remain gaps.

## Evaluation corrections

- The K6 string check missed `하루 1회 작성하는 정산 리포트`. Recomputed from the stored outputs, the 2026-11-03 updated version met every required criterion in 34 of 36 final-round runs, not 35. The [2026-11-03 record](validation-2026-11-03.md) and README now say so, and both 2026-11-03 JSON records note the correction.
- [`checks.py`](../tests/behavior/checks.py) ends the artifact only at a separator or a labeled note, not at ordinary words such as `확인`. Rerunning it on the 2026-11-03 outputs changed no stored result.
- [`test_evaluation_evidence.py`](../tests/test_evaluation_evidence.py) now requires exactly one run per variant, case, and repeat; counts a run as passing only when every required judgment is `pass`; and, for the latest record, requires a reading judgment wherever a criterion is flagged `reading_required`. Only the latest record's string checks are recomputed, so older records keep the results of the checks they were judged with.

## Cases and method

[`cases.json`](../tests/behavior/cases.json) keeps the twelve 2026-11-03 cases unchanged and adds ten:

| Case | What it tests |
| --- | --- |
| N1 | Internal notice in `~할 것` (KP08's source text without its context) |
| N2 | Checklist items stay 개조식 |
| N3 | `송부하오니 … 주시기 바랍니다` keeps `~습니다` |
| N4 | `월 1회` stays on the reflection, not the report |
| N5 | `문장으로 풀어 줘` converts 개조식 |
| N6 | Review only, no rewrite |
| N7 | Rewrite keeps heading, order, and table; adds no decisions or tests |
| N8 | The document's `※` line stays; notes do not start with `※` |
| N9 | Filling in a slot does not become finalizing |
| N10 | Two-way check: no added hedge, date, or cause |

The criteria were written before any run and revised once after round 2, before the runs. All ten are development cases written alongside the changes, not held-out evidence.

Each run sent one case's `request` to the Oh My Pi completion API with the default session model. The system prompt contained the four skill files of one version, as in 2026-11-03. Runs had no tools or history. Each version ran each case three times: 132 runs. String checks ran first. Criteria without a string check, or flagged `reading_required`, were judged by the API's `slow` model, which saw the request, the full response, and one criterion but not the variant. A failed string check fails the criterion. The authoring agent read every failure and a sample of passes and overrode no judgment. The [evidence record](../tests/behavior/evidence/2026-11-04-adversarial-review/final.json) stores outputs, hashes, judge prompt, and every judgment.

| Version | Runs with every required criterion met | Advisory misses |
| --- | --- | --- |
| Previous (`fea72ad`) | 59/66 | 0 |
| Updated | 66/66 | 0 |

Required failures, all in the previous version:

- N1, 3/3: kept `제출할 것`.
- KP08, 2/3: kept `~할 것`; one run offered the polite form only as an alternative.
- K6, 1/3: `하루 1회 생성되는 정산 리포트`.
- N8, 1/3: two `※`-led notes after the document.

Every other case passed 3/3 in both versions, including N2–N7, N9, and N10. Those cases guard against over-applying the new rules and did not separate the versions.

Notes after the artifact, all 66 runs per version:

| Measure | Previous | Updated |
| --- | --- | --- |
| Runs with a note | 27 | 27 |
| Mean note length (characters) | 171 | 93 |
| Notes starting with `※` | 18 | 0 |
| Notes explaining edits or kept text, beyond a one-line "no change" | 10 | 1 |

The one updated-version case (N7 repeat 3) reports a source claim it narrowed, which Output behavior allows.

Other observations:

- N3 repeat 2 (updated) dropped the "sending the attachment" clause. No criterion covers it.
- N4 repeat 3 (updated) ended its note with an offer to check the frequency's meaning. It meets the criteria but is closer to an offer than the rules intend.

## Limits

- One host, one unidentified executor model, and one unidentified judge model. Model judgment is not a qualified Korean editor's assessment.
- Twenty-two development cases, three runs each. The clear differences are the `~할 것` rule and `※`-led notes; this does not show a general improvement in writing quality.
- The skill files were supplied in the system prompt, so automatic selection and whether an agent opens `plain-language.md` were not tested.
