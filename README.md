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

## License

[MIT](LICENSE)
