# GAIA Claude Code skills

The [Claude Code](https://docs.claude.com/en/docs/claude-code) skills we use to run this
project, shared in the open. Part of GAIA's practice of publishing how we work, not just
what we produce ([How we work](../../book/governance/how-we-work.md)).

A skill is a folder with a `SKILL.md` (name + description in the frontmatter, instructions
below) and any reference files it needs. Claude Code loads these automatically when you
work in this repo.

## Skills here

- **plain-voice** — strips LLM-tell vocabulary and phrasing from prose, so drafts read in
  the author's voice rather than an average of every abstract since 2023.

## Use one

Invoke by name (`/plain-voice`) or let it trigger on its own. To reuse a skill in your own
project, copy its folder into your `.claude/skills/`.

Everything else under `.claude/` (local settings, session state) stays private by
`.gitignore`; only this `skills/` directory is tracked.
