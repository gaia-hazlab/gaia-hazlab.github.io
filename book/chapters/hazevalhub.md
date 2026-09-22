---
title: HazEvalHub — evaluations held to one standard
short_title: HazEvalHub
description: Where GAIA's hazard and agent evaluations are collected and held to a single benchmark-integrity standard. Two tracks run today, both hosted outside the organisation.
---

:::{note}
**In progress.** Interim owner **Marine Denolle**; v0.5 target **2027-03-31**. Two tracks run
today — [agent evaluations](hazevalhub-agents) and
[seismic event catalog workflows](hazevalhub-catalogs) — and both are hosted outside the
`gaia-hazlab` organisation. The standard below is written and in force; the shared
infrastructure it describes is not built yet.
:::

## What HazEvalHub is

One place where the project's evaluations are collected, held to one standard, and findable by
someone who wants to check a claim rather than read about it. An evaluation that a reader cannot
inspect is worth less than no evaluation at all, because it spends credibility instead of
building it. That principle is why this page exists before the infrastructure does.

What exists today is two evaluations running elsewhere and the standard on this page. There is
no `gaia-hazlab/hazevalhub` repository, no shared scorer, and no hidden hazard test set. Each
track below states its own limits, and the scorecard in
[the nine rules](#the-nine-rules) marks which rules the project
currently meets.

## Evaluation tracks

Each track is a distinct kind of evaluation with its own data, metrics and community. Some run
on surfaces we maintain, some on surfaces a partner maintains, and some are not yet running at
all.

::::{grid} 1 1 2 2

:::{grid-item-card} Agent evaluations
:link: hazevalhub-agents
Scoring AI agents that do geoscience work — reading literature, driving scientific software,
orchestrating multi-step workflows — on accuracy, cost and reproducibility together.
**Live, hosted externally.**
:::

:::{grid-item-card} Seismic event catalog workflows
:link: hazevalhub-catalogs
Benchmarking the pickers and workflows that turn continuous seismic data into event catalogs,
against analyst arrivals across five study regions.
**Live, hosted externally; being reworked.**
:::

:::{grid-item-card} Flood surrogates
Surrogate models trained on physics-based flood simulations, scored under a Common Task
Framework against a hidden test set.
**In progress — no public surface yet.**
:::

:::{grid-item-card} Landslide deep-learning detection
Detection and susceptibility models scored on POD, FAR and CSI, and on spatial agreement with
mapped failures.
**In progress — no public surface yet.**
:::

::::

(the-nine-rules)=
## The standard: nine rules for a citable benchmark

Adapted from the NeurIPS and ICML *Datasets and Benchmarks* track, whose reviewers ask the
questions an outside reader asks. We publish the standard before the benchmarks exist, because a
standard is checkable and a promise is not. The right-hand column is our own scorecard, not an
aspiration.

| # | Rule | Where we stand |
|---|---|---|
| R1 | The task is fully specified before submissions open | Not met on either track |
| R2 | The test set is hidden, and the board says so on every row | Partly — agent track has hidden splits, rows are not stamped |
| R3 | The scorer is public, deterministic and versioned | Not met |
| R4 | A trivial baseline is published first | Not met on either track |
| R5 | A strong published baseline is published alongside it | Met on the catalog track only |
| R6 | Contamination is addressed explicitly, in writing, per task | Not met; the sharpest risk for the planned seismic task |
| R7 | Splits are DOI-archived with a datasheet | Not met |
| R8 | The evaluation is separable from the group whose models it scores | Met on the catalog track, not on the agent track |
| R9 | Every row carries model version, split, date and cost | Not met |

Two of nine. The full argument, the mitigation ladder for R8, and the seed-task designs are in
the [HazEvalHub CTF plan](https://github.com/gaia-hazlab/gaia-hazlab.github.io/blob/main/project_coordination/09-hazevalhub-ctf-plan.md).

## Metric families we intend to publish

Chapters across this book forward-reference metric definitions to HazEvalHub. Those definitions
will live here, scored per pillar and per hazard. **None is implemented yet** — the table below
is the intended scope, not a description of running code.

| Pillar | Metrics |
|---|---|
| State (Pillar 1) | RMSE and bias against wells, soil-moisture sensors and ET; storm-response temporal correlation; physical consistency (mass balance, hydrostatic) |
| Nowcast (Pillar 2) | POD, FAR, CSI; IoU and Dice for mapped failures; Brier score and reliability; lead time to alert |
| Forecast (Pillar 3) | Skill against persistence and climatology; ROC and precision-recall at decision thresholds; cost–loss value; lead time against skill |
| Actionability | Decision thresholds; false-alarm cost; warning lead time |
| Frugality | Tokens and dollars per submission; skill per dollar; skill lift from domain skills |

Frugality is a first-class axis rather than a footnote. A model that cannot be run cheaply
cannot be run across a fifteen-year archive, and a benchmark that ignores cost will rank such a
model first anyway.

## Ownership and dates

**Interim owner:** Marine Denolle. The permanent owner is a kickoff decision, and until it is
taken this page names a person rather than a role.

**v0.5 target: 2027-03-31.** v0.5 means one hazard task, one hidden test set, one published
baseline, scored by a public scorer — the first point at which a result here would be worth
citing in a paper.

The critical path is not software. It is a labelling campaign: the planned seismic task needs a
temporally disjoint test set, drawn from events after the training window of the models it will
score, labelled by at least two independent annotators with a third adjudicating. Relabelling
existing curated data would be cheaper and would produce a contaminated benchmark that measures
memorisation. Nothing else on the path takes as long or needs as many people.
