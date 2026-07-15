# GAIA CSSI Kickoff Plan

> **Transition:** GAIA HazLab (FFST / UW CRESST seed) → **NSF CSSI** multi-institution
> award. This is the master plan; each workstream has its own detailed doc. Dates are
> anchored to **award start = Y1 M0**; fill absolute dates when the notice of award lands.

## 0. North star

Ship a **FAIR, agentic, multi-hazard cyberinfrastructure** that predicts geohazard
susceptibility in real time — and *prove adoption* with automated metrics. Three
expansions define the CSSI relative to the seed grant:

1. **More geography** — add **Alaska** as a first-class region alongside Cascadia/WA.
2. **More modalities** — add **geodesy (GNSS: strain, reflectometry, TEC/PWV)**,
   **SAR/InSAR** (ASF partnership), and **infrasound** to the existing seismic +
   hydrology + weather stack. All indexed in the [Data Catalog](06-data-catalog.md).
3. **More agents & evals** — grow from one RSE agent to a **registry of research
   agents** with a rigorous **evaluation harness** (HazEvalHub Common-Task Framework).

## 1. The three workstreams (this folder)

| # | Workstream | Doc | Y1 headline deliverable |
|---|---|---|---|
| A | **Project coordination** | [01-project-coordination.md](01-project-coordination.md) | Coordination repo live; boards, labels, cadence, and automated nudges running. |
| B | **Website / book evolution** | [02-website-evolution.md](02-website-evolution.md) | Alaska region + geodesy + SAR/InSAR sections registered in `myst.yml` and building. |
| C | **AI tools & evals** | [03-ai-tools-and-evals.md](03-ai-tools-and-evals.md) | 3 CI-template repos passing tests; HazEvalHub CTF v0 with 1 hidden-test task. |
| — | **Metrics (cross-cutting)** | [04-metrics-observatory.md](04-metrics-observatory.md) | Metrics Observatory Action collecting D1–D5 weekly. |
| — | **Automation (cross-cutting)** | [05-automation-runbook.md](05-automation-runbook.md) | Gated workflows enabled; secrets set. |

## 2. First 90 days (kickoff sprint)

### Days 0–15 — Stand up the operating system
- [ ] Create/confirm GitHub org structure and the **`gaia-hazlab/coordination`** repo
      (or keep coordination here per [README](README.md) migration note).
- [ ] Enable gated automation: set secrets + `vars.ENABLE_AUTOMATION=true`
      ([05 runbook §1](05-automation-runbook.md)).
- [ ] Create the **GAIA Project** board, labels, milestones, issue templates (runbook §2).
- [ ] Slack: thematic channels (`#rc1`…, `#ci1`…, `#weekly-status`, `#metrics`,
      `#alaska`, `#geodesy`, `#sar-insar`); wire the weekly-status nudge.
- [ ] Google: stand up **`gaia.hazlab@gmail.com`** per
      [templates/gaia-google-account-runbook.md](templates/gaia-google-account-runbook.md)
      — shared Calendar, mail forwarding + filters, Drive layout. Create the **Roster
      Sheet** ([templates/participant-roster.md](templates/participant-roster.md)), the
      **intake Form** ([templates/onboarding-intake-form.md](templates/onboarding-intake-form.md)),
      and the voluntary **mailing lists** ([templates/mailing-list-setup.md](templates/mailing-list-setup.md)).
- [ ] Assign **RACI roles** ([01 §2](01-project-coordination.md)); publish the
      role↔person map to the private SharedDrive (not to git).

### Days 15–45 — Fill the skeleton
- [ ] Onboard all funded members + unsupported collaborators + partners
      (templates/onboarding-checklist.md, templates/partner-onboarding.md); collect via the
      **intake Form** → responses feed the People page
      ([templates/onboarding-intake-form.md](templates/onboarding-intake-form.md),
      [templates/profile-template.yaml](templates/profile-template.yaml)).
- [ ] Draft the **website IA change** as a tracked PR against `myst.yml` ([02](02-website-evolution.md)).
- [ ] Stand up **Metrics Observatory v0**: GitHub + Zenodo collectors; publish a stub
      dashboard panel ([04](04-metrics-observatory.md)).
- [ ] Seed the **Data Catalog** ([06](06-data-catalog.md)): define Alaska AOIs; run
      `collect_fdsn.py` for seismic + infrasound stations; stub the dashboard catalog tab.
- [ ] Confirm the **in-house postdoc** appointment and assign geodesy/SAR/eval ownership
      ([01 §2.1](01-project-coordination.md)); decide Google setup per [01 §5.1](01-project-coordination.md)
      (Gmail + one Sheet, no new Workspace).
- [ ] Define **HazEvalHub CTF v0**: one task, one hidden test set, one baseline
      ([03 §3](03-ai-tools-and-evals.md)).
- [ ] Ratify conventions: repo layout, container standard, licensing (MIT/BSD-3),
      provenance YAML + RO-Crate ([03 §4](03-ai-tools-and-evals.md)).

### Days 45–90 — Prove the loop
- [ ] First **monthly project-wide update** with AI-summarized notes archived to the
      private notes repo.
- [ ] First **quarterly survey** fired by Action; results feed M3/M4.
- [ ] First **quarterly newsletter** to the Announce list, metrics auto-pasted from
      `latest.json` ([templates/quarterly-newsletter.md](templates/quarterly-newsletter.md)).
- [ ] Alaska + geodesy + SAR stub pages merged and building green.
- [ ] 3 CI-template repos passing tests (D1 Y1 target = 3).
- [ ] Metrics Observatory reporting all D1–D5 rows automatically.
- [ ] Retro: what's automated, what still needs a human, what to cut.

## 3. Phase roadmap (Y1–Y5)

Aligned to the delivery/usage tables in [04-metrics-observatory.md](04-metrics-observatory.md).

| Phase | When | Coordination (A) | Website (B) | AI/Evals (C) |
|---|---|---|---|---|
| **P0 Kickoff** | Y1 Q1 | Repo, boards, cadence, nudges | IA restructure PR | CTF v0; 3 template repos |
| **P1 Foundations** | Y1 | Onboarding complete; monthly notes loop | Alaska + geodesy + SAR stubs live | Container registry design; 2 model cards |
| **P2 Scale** | Y2 | Partner quarterly summaries; 1st in-person (AGU 2026 Sun) | Regional pages fleshed; use cases | Registry opens (8 images); agents begin (D2) |
| **P3 Integration** | Y3 | Cross-CSSI interop (QuakeWorx, Landlab+ASPECT, HydroGen, VICTOR) | Multi-hazard cross-linking; SAR products | CTF leaderboards; derived-agent tracking (M2) |
| **P4 Broadening** | Y4 | 2nd in-person (AGU 2028 Sun); full workshop | 4-year-college friendly tutorials | Hackathon: build+cite+deploy agents |
| **P5 Sustain** | Y5 | Sustainability + handoff plan | Publication-grade pages | 18 template repos / 35 images / 12 agents (cum.) |

## 4. Governance snapshot

- **Lead PI:** Marine Denolle (UW) — overall coordination, NSF annual report compiler.
- **Thrust leads:** Research Components (RC) leads + Cyberinfrastructure (CI) leads,
  one per `#rc*` / `#ci*` channel.
- **Coordinator function:** rotating or staffed; owns cadence, templates, and the
  metrics report (can be an agent-assisted role — see [03](03-ai-tools-and-evals.md)).
- Decisions are made in the **Week-3 Science + CI Thrust Sync** and recorded as issues
  / Discussions; see [01 §3](01-project-coordination.md).

## 5. Definition of "kickoff done"

- Every funded member has submitted ≥1 weekly status via template.
- All five workstream docs have named owners and open milestones.
- The Metrics Observatory produces a table with real numbers, automatically.
- The website builds green with Alaska/geodesy/SAR stubs.
- The next four months of meetings are on the shared Calendar.

## Related

- Delivery mechanisms & metrics → [04-metrics-observatory.md](04-metrics-observatory.md)
- Docs science roadmap (separate, science-facing) → [../DOCS_ROADMAP.md](../DOCS_ROADMAP.md)
