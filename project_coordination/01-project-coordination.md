# Project Coordination

> Governance, communication, meeting cadence, and the GitHub ⇄ Google split. Distilled
> from the GAIA Management & Coordination Plan into an operational, automatable form.
> **Principle:** low-cost (no paid PM tools), automated (reminders/surveys as Actions),
> distributed (shared ownership, transparent reporting).

## 1. System of record vs. human mirror

| Function | Primary (GitHub — automation) | Mirror (Google — human comfort) |
|---|---|---|
| Tasks & responsibilities | Issues + Project board + milestones | — |
| Async status | `#weekly-status` Slack thread → monthly export | Slack export archived to SharedDrive |
| Decisions & brainstorming | GitHub Discussions | Meeting notes (Docs) |
| Calendar / events | GitHub Pages events page (fed by Calendar) | **Google Calendar** (source) |
| Documents / slides / posters | DOIs (Zenodo/FigShare) linked from repo | **UW SharedDrive** (working copies) |
| Contact & routing | Repo README + CODEOWNERS | `gaia.ci@gmail.com` + Gmail filters |
| Reporting / surveys | Actions trigger the form; results → metrics | **Google Form** (collection UI) |

Rule of thumb: **if a machine needs to read it, it lives in GitHub; if only humans do,
Google is fine.** Anything that feeds a metric must have a machine-readable home.

## 2. Roles (RACI)

Assign a person to each role during kickoff; keep the **name↔role map on the private
SharedDrive**, not in git. Reference people by role in all public docs.

| Role | Responsible for | R/A |
|---|---|---|
| **Lead PI** | Overall coordination; NSF annual report; final decisions | A |
| **Co-PIs / Institution leads** | Milestones + budget per institution; local teams | R |
| **RC thrust leads** (`#rc*`) | Science components (soil/hydro, seismology, geodesy, SAR, hazards) | R |
| **CI thrust leads** (`#ci*`) | DataHub, ModelHub, HazEvalHub, agents, containers | R |
| **Coordinator** (staffed or rotating; agent-assisted) | Cadence, templates, notes, nudges | R |
| **Metrics lead** | Metrics Observatory; annual DOI archive | R |
| **Website lead** | `myst.yml` IA, deploy, dashboard | R |
| **Onboarding lead** | New members, collaborators, partners | R |
| **Partner liaisons** | OMAI, HydroFrame, AI2, ASF, EarthScope, AEC, CIG, SCEC, CRESCENT, ClasSH | C |

`R`=Responsible, `A`=Accountable, `C`=Consulted, `I`=Informed. Every open milestone
must name an accountable role.

## 3. Meeting cadence (monthly cycle)

Recorded with AI companion → notes cleaned, summarized (accomplishments, decisions,
action items, links to issues/slides), anonymized (except shout-outs), saved as
Markdown to a **private** notes repo (`gaia-hazlab/notes`, private).

| Week | Meeting | Who | Focus | Output |
|---|---|---|---|---|
| 1 | PI Coordination | PIs / co-PIs | Milestones, deliverables, budget, cross-institution timelines | Decisions → issues |
| 1 | Student/Postdoc Forum | Early-career | Tool sharing, practice talks, agent workflows, peer mentorship | Shout-outs |
| 2 | Virtual Office Hours | All (optional) | Troubleshooting, CI tool support, cross-thrust Q&A | FAQ → Discussions |
| 3 | Science + CI Thrust Sync | RC + CI leads | Integrate data/model/agent workflows; demos | **Decisions of record** |
| 4 | Project-Wide Update | All + collaborators | Recap, shout-outs, preview milestones | AI-summarized note (MD) |

**In-person:** Sunday before AGU **2026** and **2028**; full workshops in **Y4** and **Y5**.

## 4. Slack conventions

- **Channels:** one per thrust (`#rc1`…, `#ci1`…), plus `#weekly-status`, `#metrics`,
  `#general`, and expansion channels `#alaska`, `#geodesy`, `#sar-insar`.
- **`#weekly-status`:** async update thread. Funded members submit **≥ monthly**
  (weekly encouraged) using [templates/weekly-status.md](templates/weekly-status.md).
  Exported monthly → SharedDrive + summarized into a GitHub Discussion.
- **Nudges & surveys:** posted by Action/Slackbot, not by hand
  ([05 runbook §3–4](05-automation-runbook.md)).

## 5. Google Workspace setup

- **`gaia.ci@gmail.com`** — contact list + Calendar owner. Gmail filters route by
  subject keyword: `tool|container|software` → CI leads; `hydrology|seismology|geodesy|SAR|hazards`
  → RC leads; else → Lead PI. Canned auto-reply links the coordination repo + book.
- **Google Calendar** — members add talks/posters/tutorials with the standard entry
  (title, time/location, talk|poster, link). The website events page mirrors it.
- **UW SharedDrive** — working docs, final presentations (PDF), name↔role map,
  budget. Final talks also get a **FigShare DOI** tagged `GAIA`.
- **Google Form** — presentations/participation/feedback/workshop signups; the
  quarterly survey Action posts its link.

## 6. Onboarding

- **Funded members:** [templates/onboarding-checklist.md](templates/onboarding-checklist.md)
  — GitHub org, Slack, Calendar, weekly-status expectation, provenance/FAIR conventions.
- **Unsupported collaborators:** Slack + relevant channels; invited to monthly call and
  task-specific calls; may give virtual talks.
- **Partners:** [templates/partner-onboarding.md](templates/partner-onboarding.md).
  Technical/CI partners (OMAI, HydroFrame, AI2, ROM, ASF, EarthScope, AEC, CIG) get a
  dedicated channel + quarterly CI/agent summary + annual architecture sync. Community
  partners (ClasSH, SCEC, CRESCENT, ASF, EarthScope) get the mailing list + co-develop
  training. Cross-CSSI (QuakeWorx, Landlab+ASPECT, HydroGen, VICTOR) coordinate at CSSI
  PI meetings on interoperable CI.

## 7. Reporting

- **Weekly/monthly:** template → `#weekly-status` → monthly export → Discussion summary.
- **Quarterly:** survey Action → Google Form → M3/M4 metrics.
- **Annual:** NSF report compiled by Lead PI from
  [templates/nsf-annual-report-entry.md](templates/nsf-annual-report-entry.md) entries;
  metrics auto-pulled from the Observatory and DOI-archived.

## 8. Broader-community engagement

Continue the successful seisscoped Slack. Amplify via LinkedIn (events/papers), more
frequent website research updates, a YouTube channel (research updates, talks,
tutorials), and the public dashboard on GitHub Pages.
