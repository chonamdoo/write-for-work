# Write for Work

An agent skill for drafting, rewriting, and reviewing Korean and English work writing, including documentation, PR descriptions, reports, decision memos, and project updates.

한국어·영어 업무 문서, PR 설명, 주석, 보고서를 사실과 문체를 지키면서 읽기 쉽게 고칩니다.
한국어 문서에서는 번역투와 상투구, em dash, 공백 가운뎃점 나열, 조사 앞 공백 같은 "AI 티"를 고칩니다. 다듬기만 요청하면 `~함`/`~다`/`~습니다` 같은 종결어미와 개조식은 그대로 둡니다.

## Available skill

| Skill | Use |
| --- | --- |
| [write-for-work](skills/write-for-work/SKILL.md) | Draft, rewrite, restructure, review, or compare work writing while preserving facts, identifiers, register, and the author's voice. |

Editing prose does not authorize code changes, new comments, or publication.

## Use

### Install with npx (recommended)

Requires Node.js, npm (which provides `npx`), and Git. The [skills CLI](https://github.com/vercel-labs/skills) installs directly from this repository; `write-for-work` does not need a separate npm package.

Choose **one** installation scope:

**Project** — run from the project root to make the skill available in that project:

```sh
npx skills@latest add chonamdoo/write-for-work --skill write-for-work
```

**Global** — make the skill available across your projects:

```sh
npx skills@latest add chonamdoo/write-for-work --skill write-for-work -g
```

Select the agents you use when prompted. Before confirming, check for an existing `write-for-work` in your project, global, and plugin skill locations. Keep one installation route and scope per project and agent, and review any overwrite prompt instead of replacing a customized copy.

These commands fetch the default branch, not a pinned release. Update an npx-managed installation with `npx skills@latest update write-for-work`, then restart the agent if the change does not appear.

To install changes from a local checkout into Claude Code, run from the repository root. `-y` skips the installer's confirmation prompts, so use it only when no customized copy should be kept:

```sh
npx skills@latest add . --skill write-for-work -g --agent claude-code -y
```

### Manual installation

After the first version tag is pushed, the Release workflow publishes a skill-only archive and `SHA256SUMS` to [Releases](https://github.com/chonamdoo/write-for-work/releases). Check the archive against `SHA256SUMS`, extract the `write-for-work` directory, and install it with your agent's documented skill mechanism.

### Use the skill

Ask your agent to use `write-for-work` with your draft or notes. For example:

> Use write-for-work to rewrite this project update in clear, natural Korean while preserving the facts.

> 이 설계서 4장을 2장 문체에 맞춰 줘.

Files use the [Agent Skills format](https://agentskills.io/specification). Shared instructions do not guarantee identical outputs, automatic discovery, or tools across hosts.

## Evaluation

The [2026-11-04 validation record](docs/validation-2026-11-04.md) covers an update driven by two rounds of adversarial review (Claude Opus 5.5 and GPT-6.1-sol). It compares the previous and updated skill on twenty-two synthetic Korean cases, three runs each. The updated version met every required criterion in 66 of 66 runs and the previous `main` in 59 of 66. The differences: the previous version kept a commanding `~할 것` in a notice (N1 3/3, KP08 2/3 runs), once moved `하루 1회` onto the report, and once wrote `※`-led notes after the document. Across all runs the updated version wrote no `※`-led notes (previous: 18) and its notes averaged 93 characters (previous: 171). The other cases, including those that guard against over-applying the new rules, did not separate the versions.

The [2026-11-03 validation record](docs/validation-2026-11-03.md) covers the Korean slop-signal update on twelve cases. After a 2026-11-04 correction to one string check, that update met every required criterion in 34 of 36 final-round runs and the previous `main` in 33 of 36 (pre-merge round: 36 and 31). Its consistent difference was the 개조식 design-document body: the previous version changed `~함` to `~한다` in all three runs of both rounds. The earlier evaluation materials remain in [`research/`](research/).

These are development results from one host, judged by string checks and model reading, not proof of general writing quality or a qualified Korean editor's assessment. Automatic skill selection was not tested.

## Package layout

- [`skills/write-for-work/`](skills/write-for-work/) is the installable skill: `SKILL.md`, its `references/`, and the MIT license.
- [`tests/`](tests/) holds package checks and [behavioral cases](tests/behavior/) with their recorded evidence. Executors receive only each case's request.
- [`docs/`](docs/) holds validation records.
- [`research/`](research/) holds source investigations, earlier evaluation inputs and outputs, and scoring criteria.

Keep tests, evidence, and research outside the installable directory so agents do not receive evaluation material with the skill.

## Maintain and release

Install development dependencies with `python -m pip install -r requirements-dev.txt`. Run `python -m unittest discover -s tests -v` and `git diff --check`. CI runs the same checks and also checks committed whitespace against Git's empty tree. These are package checks, not writing-quality certification.

Use a topic branch and a reviewed PR. After checks and behavioral review, merge it, then push a version tag such as `v0.1.0` at the reviewed `main` commit. The Release workflow checks the tagged code and publishes a skill-only archive and `SHA256SUMS` to GitHub Releases. Do not move existing release tags.

## Sources

The skill adapts ideas from the sources listed in [its plain-language reference](skills/write-for-work/references/plain-language.md#adaptation-sources), including [stop-slop-ko](https://github.com/leeandev/stop-slop-ko) for Korean punctuation, register, and prose-cliché signals. Repository layout, validation, and release conventions follow [work-skills](https://github.com/chonamdoo/work-skills). These are background sources, not runtime dependencies or bundled copies.

## License

[MIT](LICENSE)

## Skill eval on every change

Run this locally before merging any change to the skill or its eval cases (it is not wired to GitHub Actions):

```bash
python3 evals/skill-eval/skill_eval.py evals/skill-eval/suite.json --base-ref origin/main
```

`skill_eval.py` gives each case in `evals/skill-eval/suite.json` to `claude -p` twice, once with the working-tree skill and once with the skill at `--base-ref`, each without tools. A separate judge call marks every required criterion. The run exits 1 when the working-tree required pass rate drops more than `max_drop` below base, or falls below `min_pass_rate`. Results go to `skill-eval-results.json`. Spend is capped by `max_usd`. `--dry-run` prints the call count; `--select ID,ID` and `--reps N` narrow the run. Requires a logged-in `claude` CLI.

Limits: one fixed case set, an LLM judge, and few repetitions. It catches regressions against the previous version, not held-out improvement.
