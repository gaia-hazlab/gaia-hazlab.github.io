# GAIA Project Coordination

> **Operating system for the GAIA NSF CSSI project.** This directory holds the
> living coordination plan for transitioning GAIA HazLab from the **FFST / UW CRESST
> seed grant** to the **NSF CSSI** award and beyond — team, cadence, website
> evolution, AI tooling, and the automated metrics that prove impact.
>
> **Design principle: agentic-first, low-cost, automated.** GitHub is the system of
> record and automation engine; Google Workspace is the human-friendly mirror for
> members who prefer it. Every recurring coordination task should be a scheduled
> Action, a template, or a bot — not a person's memory.

## What's here

| File | Purpose | Owner |
|---|---|---|
| [00-kickoff-plan.md](00-kickoff-plan.md) | The 90-day kickoff and the multi-year phase roadmap. **Start here.** | Lead PI |
| [01-project-coordination.md](01-project-coordination.md) | Governance, roles (RACI), meeting cadence, GitHub ⇄ Google split, partner onboarding. | Lead PI + Coordinator |
| [02-website-evolution.md](02-website-evolution.md) | Structural changes to the website/book: Alaska region, geodesy, SAR/InSAR processing. | Website lead |
| [03-ai-tools-and-evals.md](03-ai-tools-and-evals.md) | Agent tooling, HazEvalHub Common-Task Framework, evaluation harness, model cards. | CI / eval leads |
| [04-metrics-observatory.md](04-metrics-observatory.md) | Delivery (D1–D5) and usage (M1–M4) metrics, data sources, automation. | Metrics lead |
| [05-automation-runbook.md](05-automation-runbook.md) | Concrete GitHub Actions, bots, crons, and required secrets. Maps to `.github/`. | CI infra lead |
| [templates/](templates/) | Reusable Markdown: weekly status, monthly report, meeting notes, NSF entry, onboarding. | All |

## Protection & publication policy

- **This directory (`project_coordination/`) is tracked and public.** It contains no
  budget figures, no personal contact details, and no unreleased science. It is safe
  on a public GitHub repo and is the source of truth for coordination.
- **Raw source docs (`project_docs/*.pdf`, `*.docx`, …) are git-ignored** (see the
  repo `.gitignore`). They carry NSF/budget/personnel material and stay off git by
  default. To publish one, add an explicit `!project_docs/<file>` exception.
- **Nothing here is deployed to the website.** The site build (`pixi run build-ci`)
  only renders files registered in [`myst.yml`](../myst.yml) and uploads `website/`.
  `project_coordination/` is intentionally *not* in the MyST ToC, so it never ships
  to `gaia-hazlab.github.io`.
- Keep individuals' emails and phone numbers out of these files. Reference people by
  **role** (e.g. "CI infra lead") and keep the name↔role mapping in the private
  coordination assets (Google/UW SharedDrive), not here.

## Migration note (topology)

Per the Management & Coordination Plan, GAIA will eventually run a dedicated
**GAIA Coordination Repository** (`gaia-hazlab/coordination`). These files are written
to lift cleanly into that repo: all links are relative, and no content depends on the
website build. For the kickoff we keep them here to move fast; migration is a `git mv`
plus repointing the automation runbook's `repo:` fields.

## How to use this during kickoff

1. Read [00-kickoff-plan.md](00-kickoff-plan.md) and assign the RACI roles in
   [01-project-coordination.md](01-project-coordination.md).
2. Enable automation: follow [05-automation-runbook.md](05-automation-runbook.md) to
   add secrets and flip `vars.ENABLE_AUTOMATION` to `true`.
3. Stand up the boards, labels, and issue templates (runbook §2).
4. Kick off the website restructure ([02](02-website-evolution.md)) and eval harness
   ([03](03-ai-tools-and-evals.md)) as Y1 milestones.
