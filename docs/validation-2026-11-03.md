# 2026-11-03 Korean slop-signal validation

This update adds Korean punctuation and spacing signals, register preservation, reference-document matching, and paragraph-prose clichés to `write-for-work`. The material was adapted from [stop-slop-ko](https://github.com/leeandev/stop-slop-ko) commit `553be05`; the skill's [adaptation sources](../skills/write-for-work/references/plain-language.md#adaptation-sources) state what was adopted, narrowed, and left out.

## Exact scope

- `SKILL.md`: description trigger for matching a reference document's style; a register pointer beside "short declarative sentences"; review notes placed after the artifact under a label; a sharper pointer to `plain-language.md`; one final-check item.
- `references/plain-language.md`: sections for Korean punctuation and spacing (with keep cases from 한글 맞춤법), Register and sentence endings, and Matching a reference document; three sentence-repair rows; a paragraph-prose cliché table with keep conditions; a narrowed noun-fragment habit; the adaptation source.
- `references/style-and-integrity.md`: the report-sentence check points to the register rule, and the house-style section separates Korean revision checks from blanket punctuation bans.

`references/modes.md` and the invocation policy are unchanged. No script, hook, or mode was added to the skill.

Final skill hashes are in the [evidence record](../tests/behavior/evidence/2026-11-03-korean-slop/final.json) under `skill_sha256.new`. The previous version is `main` commit `f3ae4a7`, which includes PR #4 (visual explanations and PR evidence rules). PR #4 reached `main` before this change merged, so the final round reran both versions on the merged files.

## Cases and criteria

[`cases.json`](../tests/behavior/cases.json) has twelve synthetic cases. Each criterion records its source, whether it is required, and why.

| Case | What it tests |
| --- | --- |
| K1 | 개조식 de-slop: marks, particle spacing, table `—`, `성능·품질` |
| K2 | Blog prose: opener, lesson ending, hedged cause, `~습니다` |
| K3 | Clean specification left alone |
| K4 | Element-by-element tone matching |
| K5 | `—` inside a code span kept |
| K6 | 개조식 design-document body asked to be "자연스럽게" |
| K7 | Slide symbols, `회원·비회원`, review-note placement |
| K8 | Retrospective: scale value "매우 높음", specific lesson, real commitment |
| K9 | `1920×1080`, `1시간 만에`, spaced pair `수집 · 정제` |
| KP02, KP03, KP08 | Regression cases from [the earlier evaluation](../research/korean-writing-evaluation.json): predicate repair, noun-chain causality, polite notice keeping a deadline |

All twelve are development cases chosen while writing this change, not held-out evidence. K6 and K7 were added after the first five showed no difference between versions; the review-driven criterion changes before the final runs are listed under `criteria_revisions` in the record.

## Method

Each run sent one case's `request` as the user message to the Oh My Pi completion API with the default session model; the API did not return the model identifier. The system prompt contained all four skill files and said the user had invoked the skill. Runs had no tools or history. Each version ran each case three times: 72 runs per round.

[`checks.py`](../tests/behavior/checks.py) applies string checks to the revised artifact, excluding notes after it. Criteria a string cannot judge were judged by reading, with a reason stored per judgment; one string result was overridden with its reason. [`test_evaluation_evidence.py`](../tests/test_evaluation_evidence.py) recomputes the string checks from the stored outputs of `final.json` and checks the counts below. GitHub Actions was unavailable for this change, so these checks ran locally only.

## Observed results

Two rounds used the same cases and criteria. `pre-merge.json` compares `a92a97e` with the pre-merge files; `final.json` compares `f3ae4a7` with the merged files.

| Round | Version | Runs with every required criterion met | Advisory misses |
| --- | --- | --- | --- |
| pre-merge | Previous (`a92a97e`) | 31/36 | 8 |
| pre-merge | Updated | 36/36 | 1 |
| final | Previous (`f3ae4a7`) | 33/36 | 7 |
| final | Updated (merged) | 35/36 | 1 |

Required failures:

- K6, previous version, 3/3 runs in both rounds: `전송함`, `재처리함`, `반영됨` became `~한다` or `~된다`. This is the one consistent difference.
- KP08: the previous version kept the commanding `~할 것` in 1/3 pre-merge runs; the updated version did so in 1/3 final runs, offering the polite wording only as an alternative for external recipients. The new register rule names this case, so it does not reliably prevent the failure; it varies between runs in both versions.
- K2, previous version, 1/3 pre-merge runs: added "다만 같은 기간의 다른 변화가 영향을 줬을 가능성은 따로 확인하지 않았습니다", a claim the author never made. Not seen in the final round.

Advisory misses: across both rounds the previous version split joined pairs into two words (`성능·품질` in K1 5/6, `회원·비회원` in K7 5/6, `수집 · 정제` in K9 1/6) and opened K2 with a topic announcement in 4/6 runs. The updated version opened K2 with the source's filler or a topic announcement in 2/6 runs.

Other observations:

- K8: every run in both versions and rounds kept "매우 높음", the lesson, and the Friday commitment. The keep conditions added for paragraph prose were not stressed by a version that already behaved this way.
- K1: in the pre-merge round both versions flagged the undefined table `—` in 3/3 runs. In the development round the updated draft had flagged it in 0/2; that draft called the dash "not applicable", which the final keep case no longer does.
- KP08 and KP03: the updated version often adds a `※` note after a separator about a register change or an unverified consequence. These notes are longer than the output-behavior rules intend.
- KP03: the updated version keeps the source's noun-ending style (`~음`); the previous version writes `~다` or `~습니다`. Both meet the criterion.

## Review

Claude Opus 5.5 (xhigh) and GPT-6.1-sol (xhigh) reviewed the first draft adversarially; both verdicts were "approve with fixes". Their findings and the response:

| Finding | Change |
| --- | --- |
| `` `maxRetry` 값 `` used as a particle example although `값` is a noun | Example replaced with `` `maxRetry` 를 ``; nouns and bound nouns (제42항) listed as keep cases |
| Register rule applied to every operation, conflicting with existing politeness and predicate-repair rules | Scoped to polishing; register changes allowed for a named register, template, reference, format change, or wrong-for-reader source; one canonical definition |
| Em dash and middle dot rules stricter than 한글 맞춤법 | Marked as heuristics; norm-supported uses, attribute separators, and unspaced pairs kept |
| Prose clichés applied to all work writing | Moved to a paragraph-prose table with keep conditions for scale values, specific lessons, real commitments, and quoted subjects |
| Reference style vs punctuation checks undefined | Consistent marks in the reference win |
| Provenance misstated the conflict with stop-slop-ko; reused examples unstated | Rewritten, copyright line added |
| Evidence not reproducible; criteria lacked source and requiredness; K2 and K6 judged by phrase | `checks.py`, evidence test, criterion fields, re-judged criteria, rerun on the final files |
| No regression check against the earlier cases | KP02, KP03, KP08 added |

Not adopted: a test that fails whenever the skill hash differs from the evidence record. It would force a full rerun for every wording edit, which work-to-skill does not require for narrow changes. The record states which skill hashes it covers instead.

## Limits

- One host and one unidentified default model. Other models and hosts were not run.
- Twelve synthetic development cases, three runs each. The clear difference is in two rules, 개조식 endings and joined pairs; this does not show a general improvement in writing quality.
- Judgments are string checks plus one agent's reading, not a qualified Korean editor's assessment.
- The skill files were supplied in the system prompt, so whether an agent opens `plain-language.md` when it should, and whether it selects the skill automatically, were not tested.
- The development round in [`development.json`](../tests/behavior/evidence/2026-11-03-korean-slop/development.json) used an earlier skill draft and earlier, uncommitted check code; it is kept as history and is not covered by the evidence test.
