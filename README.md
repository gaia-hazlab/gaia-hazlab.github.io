# GAIA HazLab Website

[![Deploy GitHub Pages](https://github.com/gaia-hazlab/gaia-hazlab.github.io/workflows/Deploy%20GitHub%20Pages/badge.svg)](https://github.com/gaia-hazlab/gaia-hazlab.github.io/actions)

This repository contains the source code for the GAIA HazLab (Geophysical AI-driven Integration and Assimilation for Hazard Laboratory) website, hosted on GitHub Pages.

## Overview

GAIA HazLab is a platform for hazard assessment using machine learning and geospatial
analytics. The deployed site is assembled from two pieces:

- **Static site** (`website/`) — landing page (`index.html`), team page (`people.html`),
  dashboard, presentations, and funding/acknowledgments pages. Team members are rendered
  from `website/data/team.json`, sponsor and funder logos from `website/images/sponsors/`.
- **Jupyter Book** (`book/`, built into `website/book/`) — the documentation, organized in
  [myst.yml](myst.yml) into: Problem Statement, Science (digital-twin framework, Earth
  system science, hazards), Field Sites, Technology (DataHub, ModelHub, HazEvalHub, GAIA
  Agent), Demos, and How We Work (governance).

## Local Development

### Prerequisites

We recommend using [pixi](https://pixi.sh/dev/installation/) for a local development environment

### Setup

1. Clone the repository:
```bash
gh repo clone gaia-hazlab/gaia-hazlab.github.io
cd gaia-hazlab.github.io
```

1. Build the Jupyter Book & preview locally
```bash
pixi run serve-all
```

NOTE: `pixi task list` shows all available tasks, including `build-book`, `build-all`, `serve-book`, `serve-all`, `linkcheck`, and `spellcheck`.

## Adding Team Members

Team members are data-driven — both `index.html` and `people.html` render from the same
JSON file, so there is no HTML to edit.

1. Add a portrait to `website/images/team/`
   - Format: JPG or PNG
   - Size: at least 300x300px (square)
   - Naming: `firstname-lastname.jpg`

2. Add an entry to the `team_members` array in `website/data/team.json` with the person's
   name, photo path, role, title, affiliation, expertise, and contact links. See
   [website/data/README.md](website/data/README.md) for the full field list.

## Deployment

The website is automatically built and deployed to GitHub Pages using GitHub Actions when changes are pushed to the `main` branch.

## Structure

```
.
├── myst.yml               # MyST project config + table of contents
├── pixi.toml              # Environment and build tasks
├── gaia-book.css          # Custom book styling
├── book/                  # MyST / Jupyter Book source
│   ├── intro.md
│   ├── references.bib
│   ├── chapters/          # Content pages (science, hazards, hubs, field sites)
│   ├── governance/        # How we work, organization, decisions, licensing, FAQ
│   ├── graph/             # Knowledge graph data and generator
│   └── img/
├── website/               # Static site deployed to GitHub Pages
│   ├── index.html         # Landing page
│   ├── people.html        # Team members page
│   ├── dashboard.html
│   ├── funding.html
│   ├── presentations.html
│   ├── data/team.json     # Team roster, rendered by js/team-loader.js
│   ├── js/
│   ├── assets/
│   ├── images/            # team/ and sponsors/ logos
│   ├── presentations/
│   └── book/              # Built book copied here by build-all (git-ignored)
├── project_coordination/  # Public project-management docs (not part of the book)
├── data/catalog/          # Data catalog outputs
├── scripts/catalog/       # Catalog collection and build scripts
├── tools/docx/            # Word export helpers
├── review-logs/           # Dated output from persona review runs
├── _attic/                # Retired content kept for reference; not current
├── .claude/               # Claude Code agents, skills, and review personas
├── .github/workflows/     # deploy.yml plus automation workflows
├── AGENTS.md              # Instructions for AI coding agents
├── CLAUDE.md              # Claude Code pointer to AGENTS.md and .claude/
└── CONTRIBUTING.md        # Guidelines for human contributors
```

## AI Coding Agents

[AGENTS.md](AGENTS.md) is the shared instruction file for AI coding agents (Claude Code,
Copilot, Codex, Cursor). [CLAUDE.md](CLAUDE.md) points Claude Code at it and adds the
Claude-specific extras under `.claude/`.

### What is in `.claude/`

- **`.claude/skills/`** — skills Claude Code loads automatically when you work in this repo.
  Invoke by name (`/plain-voice`) or let them trigger on their own. See
  [.claude/skills/README.md](.claude/skills/README.md).
- **`.claude/agents/`** — ten persona-review subagents (`gaia-review-*`), auto-discovered by
  Claude Code and used when you ask for a GAIA persona review. Each is a thin prompt that
  reads its full specification from `.claude/gaia-review-personas/` at run time. Output goes
  to `review-logs/<date>/`.
- **`.claude/gaia-review-personas/`** — the persona specifications and the generator that
  produces the subagents. Self-contained and separately licensed (CC BY 4.0) so it can be
  reused outside this project.

Everything else under `.claude/` (local settings, session state) is git-ignored; see the
exception list at the bottom of [.gitignore](.gitignore).

### Which tools read what

| | `CLAUDE.md` | `AGENTS.md` | `.claude/skills/` | `.claude/agents/` |
|---|---|---|---|---|
| Claude Code (CLI) | auto | via pointer | auto | auto |
| Claude Code (VS Code extension) | auto | via pointer | auto | auto |
| GitHub Copilot | no | yes | no | no |
| Codex, Cursor | no | yes | no | no |

The CLI and the VS Code extension are the same engine and behave identically. `CLAUDE.md` is
loaded into context automatically at the start of a session; `AGENTS.md` is read because
`CLAUDE.md` links to it. Tools other than Claude Code ignore `.claude/` entirely, so anything
every agent needs to know belongs in `AGENTS.md`.

### Regenerating the personas

The ten `personas/*/SKILL.md` files and the ten `agents/gaia-review-*.md` files are
generated. Edit `spec.py` (what differs between personas) or `build.py` (what they share),
then regenerate **from the `.claude/` directory**:

```bash
cd .claude && python3 gaia-review-personas/build.py
```

Editing a generated file directly works until the next regeneration silently reverts it. See
[.claude/gaia-review-personas/BUILDING.md](.claude/gaia-review-personas/BUILDING.md).

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, or open
an issue or pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- GitHub: [gaia-hazlab](https://github.com/gaia-hazlab)
- Website: [https://gaia-hazlab.github.io](https://gaia-hazlab.github.io)

## Acknowledgments

- Based on the [UW Hackweek Splashpage Template](https://github.com/uwhackweek/splashpage-template)
- Inspired by the [GeoSMART Website](https://github.com/geo-smart/website-2024)
- Built with [Jupyter Book](https://jupyterbook.org)
