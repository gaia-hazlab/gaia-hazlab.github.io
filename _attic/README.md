# `_attic/` — archive & repo cleanup (2026-08)

This directory holds files retired during the **repo-root cleanup** that accompanied the
CSSI kickoff and the "new members" website refresh. Nothing here is deleted from history —
it is archived so the working tree has a **single source of truth**.

## What was started (the plan)

The repo root had accumulated two copies of the site (root `index.html` etc. *and*
`website/`), stale planning docs, and code that moved to other repos. The cleanup:

1. **Serve the site from `website/` only.** GitHub Pages publishes `website/` (see
   `.github/workflows/deploy.yml` → `path: 'website'`). The root-level `index.html`,
   `dashboard.html`, `people.html`, `js/`, `images/` (sponsors + team), and `assets/`
   (hero videos) were **duplicates** of what `website/` already serves, so they are
   archived to [`site-root-duplicates/`](site-root-duplicates/) and removed from root.
2. **Retire stale planning docs** — `DOCS_ROADMAP.md`, `UPGRADE_PLAN.md`, and the twin
   editorial proposal → [`planning/`](planning/).
3. **Metrics Observatory moved to its own repo.** The collectors/data/workflow are
   archived under [`metrics-moved-to-own-repo/`](metrics-moved-to-own-repo/) and the
   root `.github/workflows/metrics-observatory.yml` is removed. The live board lives at
   `https://gaia-hazlab.github.io/metrics-observatory/` (linked from the book's Demos).
4. **Legacy book chapters & scratch** → [`book-chapters/`](book-chapters/),
   [`scratch/`](scratch/).
5. **New governance section** under `book/governance/` (how-we-work, organization,
   decisions, licensing, faq) registered under "How we work" in `myst.yml` — replacing
   the single old project-organization page.
6. **New site pages** — `website/funding.html`, `website/presentations.html` (+ PDFs),
   linked from the book's Demos part.
7. **`.gitignore` hygiene** — ignore `.claude/`, `.DS_Store`, `website/presentations/*.pptx`
   (commit PDFs + covers only; PPTX lives on Drive/FigShare), and the `_to_delete/`
   staging area.
8. **Team refresh** — `website/data/team.json` + new member photos (Tape, Mencin,
   Istanbulluoglu, Meyer, Kennedy, Angarita, West, Grapenthin, Mandava, Iyer).

## Review of the plan (verification pass)

Checked before finishing, all green:

- ✅ **Live site safe.** Pages serves `website/`, which is self-contained (index,
   dashboard, people, funding, presentations, data/team.json, images/sponsors + team all
   present). Deleting the root duplicates does **not** change the deployed site.
- ✅ **Nothing lost.** Every removed root file is archived here under `_attic/` and remains
   in git history.
- ✅ **No dangling references.** No remaining tracked file (outside `_attic/`) links to
   `DOCS_ROADMAP.md`, `UPGRADE_PLAN.md`, or the deleted root site paths.
- ✅ **Book builds green** — 31 pages, including all five `book/governance/` pages
   (`/licensing` renders).
- ⚠️→✅ **Fix applied:** `book/governance/licensing.md` was referenced in `myst.yml` but
   still **untracked** — it is now committed alongside the `myst.yml` change so CI does not
   break on a missing file.
- ⚠️→✅ **Cleanup:** `_to_delete/` (a bridge staging area holding a discarded
   `book/governance/index.md`; no such file is tracked) is removed from disk and gitignored.

## Recovering something

Everything here is a normal file — copy it back, or `git log -- _attic/<path>` to trace it.
If a whole subtree needs to return to root, `git mv` it back and re-register any book pages
in `myst.yml`.
