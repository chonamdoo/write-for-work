# Write for Work

An agent skill for drafting, rewriting, and reviewing Korean and English work writing, including documentation, PR descriptions, reports, decision memos, and project updates.

## Use

### Install with npx (recommended)

Requires Node.js, npm (which provides `npx`), and Git. The [skills CLI](https://github.com/vercel-labs/skills) installs directly from this repository; `write-for-work` does not need a separate npm package or Homebrew.

Choose **one** installation scope:

**Project** — run from the project root to make the skill available in that project:

```sh
npx skills@latest add chonamdoo/write-for-work --skill write-for-work
```

**Global** — make the skill available across your projects:

```sh
npx skills@latest add chonamdoo/write-for-work --skill write-for-work -g
```

Select your coding agent when prompted by the installer.

### Use the skill

Ask your agent to use `write-for-work` with your draft or notes. For example:

> Use write-for-work to rewrite this project update in clear, natural Korean while preserving the facts.

## Package layout

- [`skills/write-for-work/`](skills/write-for-work/) is the installable skill: `SKILL.md`, its `references/`, and the MIT license. The installer discovers this directory automatically; the GitHub installation commands above are unchanged.
- [`research/`](research/) holds source investigations, evaluation inputs and outputs, and scoring criteria. Keep these outside the installable directory so agents do not receive evaluation material with the skill.

Evaluation snapshots retain their original content, hashes, and skill-relative paths. Moving the package does not change the writing instructions or invocation policy.

To install changes from a local checkout into Claude Code, run from the repository root:

```sh
npx skills@latest add . --skill write-for-work -g --agent claude-code -y
```

## License

[MIT](LICENSE)
