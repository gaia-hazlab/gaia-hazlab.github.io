# AGENTS.md

Instructions for AI coding agents (Copilot, Claude Code, Codex, Cursor, etc.) working in
this repository. Human contributors should read [CONTRIBUTING.md](CONTRIBUTING.md) instead.

## What this repo is

Source for the **GAIA HazLab** website (`gaia-hazlab.github.io`): a MyST/Jupyter Book site
plus a static splashpage, built and deployed via GitHub Actions to GitHub Pages.

## Layout

- `book/` — MyST Jupyter Book source (chapters, governance docs, references). Table of
  contents lives in [myst.yml](myst.yml), not `book/_toc.yml`.
- `website/` — static HTML/CSS/JS site (splashpage, dashboard, people page) that the built
  book gets copied into at `website/book/`.
- `project_coordination/` — public project-management docs (governance, roadmap, metrics,
  automation runbook). Not part of the MyST ToC; never deployed to the site. Start at
  [project_coordination/README.md](project_coordination/README.md).
- `data/catalog/`, `scripts/catalog/` — data catalog inputs and generation scripts.
- `.claude/agents/`, `.claude/skills/` — Claude Code persona-review agents and skills used
  to work on this project; see [.claude/skills/README.md](.claude/skills/README.md).
- `review-logs/` — dated output from persona review runs.
- `_attic/` — retired/archived content kept for reference. Do not build on it or treat it
  as current; check with the user before resurrecting anything from here.
- `_build/` — generated Jupyter Book output. Never edit by hand; git-ignored.

## Build & preview

Uses [pixi](https://pixi.sh) for environment + tasks (see [pixi.toml](pixi.toml)):

```bash
pixi run serve-book     # live-preview the book only
pixi run build-book      # build book to _build/html
pixi run build-all       # build book + assemble into website/book (matches CI)
pixi run serve-all       # serve the full assembled website/ locally
pixi run linkcheck       # jupyter book build --check-links
pixi run spellcheck      # codespell
```

`build-ci` is what GitHub Actions runs for deployment — prefer `build-all` locally since it
does the same assembly steps.

## Conventions

- Content pages are Markdown (MyST flavor) under `book/chapters/`; register new pages in
  the `toc:` in [myst.yml](myst.yml), not by adding files alone.
- Keep `project_coordination/` free of budget figures, personal contact info, and
  unreleased science — it's public. Reference people by role, not name/email.
- Governance/process docs live in `book/governance/`; the acknowledgement wording for NSF
  awards in [book/governance/how-we-work.md](book/governance/how-we-work.md) must be used
  verbatim when cited elsewhere.
- Run `pixi run spellcheck` and `pixi run linkcheck` before considering doc changes done.
- Don't hand-edit `_build/` or treat `_attic/` content as authoritative.

## Persona reviews

`.claude/agents/gaia-review-*.md` define reviewer personas (CTO, PhD student, program
officer, etc.) used to audit the site/book from an outside-audience perspective. Results
are filed under `review-logs/<date>/`. Use these when asked for a "GAIA persona review" or
similar.
