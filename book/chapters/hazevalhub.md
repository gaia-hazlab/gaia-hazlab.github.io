---
title: HazEvalHub — evaluations held to one standard
short_title: HazEvalHub
description: Where GAIA's evaluations of AI models for earthquakes, landslides, floods, thunderstorms, atmospheric rivers and agents are collected and held to a single benchmark-integrity standard.
---

:::{note}
**In progress.** Interim owner **Marine Denolle**; v0.5 target **2027-03-31**. Six tracks, one
per hazard plus agents. Two boards run today, both hosted outside the `gaia-hazlab`
organisation, and their cards link straight to them: [Repère](https://mdenolle.github.io/repere/)
for agents and [QuakeScope](https://seisscoped.org/QuakeScope/benchmark_summary.html) for
earthquake phase pickers. Landslides has QuakeXNet detection results on its page here;
thunderstorms and atmospheric rivers have pages and no published scores yet. Floods is planned. The standard below is written and in force; the
shared infrastructure it describes is not built yet.
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

One card per track. Each opens the page or board where that track's evaluation lives. Some run on
surfaces we maintain, some on surfaces a partner maintains, and one is not yet running at all.

::::{grid} 1 2 3 3

:::{grid-item-card} Earthquakes
:link: https://seisscoped.org/QuakeScope/benchmark_summary.html
:footer: **Live**, hosted by SeisSCOPED
```{image} ../img/hazevalhub/earthquakes.svg
:alt: Earthquakes icon
:width: 56px
```
Deep-learning phase pickers scored against analyst arrivals across five study regions, on the QuakeScope board.
:::

:::{grid-item-card} Landslides
:link: hazevalhub-landslides
:footer: **Detection results live**, modeling in progress
```{image} ../img/hazevalhub/landslides.svg
:alt: Landslides icon
:width: 56px
```
QuakeXNet detection and classification of surface events, and Landlab failure-probability modeling validated on the 2025 Stehekin debris flows.
:::

:::{grid-item-card} Floods
:link: hazevalhub-floods
:footer: **Planned**
```{image} ../img/hazevalhub/floods.svg
:alt: Floods icon
:width: 56px
```
Surrogate models trained on physics-based flood simulations, scored under a Common Task Framework against a hidden test set.
:::

:::{grid-item-card} Thunderstorms
:link: hazevalhub-thunderstorms
:footer: **In progress**, board not yet published
```{image} ../img/hazevalhub/thunderstorms.svg
:alt: Thunderstorms icon
:width: 56px
```
Seismoacoustic thunderquake detectors scored on how many strikes they add to open lightning catalogs.
:::

:::{grid-item-card} Atmospheric rivers
:link: hazevalhub-rainfall
:footer: **In progress**, no scores yet
```{image} ../img/hazevalhub/atmospheric-rivers.svg
:alt: Atmospheric rivers icon
:width: 56px
```
Extreme rainfall: gridded precipitation products compared against gauges, and ACE2 forecasts downscaled to Stage IV.
:::

:::{grid-item-card} Agents
:link: https://mdenolle.github.io/repere/
:footer: **Live**, hosted externally
```{image} ../img/hazevalhub/agents.svg
:alt: Agents icon
:width: 56px
```
AI agents doing geoscience work, scored on accuracy, cost and reproducibility together on the Repère board.
:::

::::

The two live boards have companion pages that state what each one does and does not yet show:
[agent evaluations](hazevalhub-agents) and
[earthquake phase pickers](hazevalhub-catalogs).

(the-nine-rules)=
## The standard: nine rules for a citable benchmark

Adapted from the NeurIPS and ICML *Datasets and Benchmarks* track, whose reviewers ask the
questions an outside reader asks. We publish the standard before the benchmarks exist, because a
standard is checkable and a promise is not. The track columns are our own scorecard, not an
aspiration.

| # | Rule | Earthquakes | Landslides | Floods | Thunderstorms | Atm. rivers | Agents |
|---|---|---|---|---|---|---|---|
| R1 | The task is fully specified before submissions open | No | No | — | No | No | No |
| R2 | The test set is hidden, and the board says so on every row | No | No | — | No | No | Partly: hidden splits exist, rows are not stamped |
| R3 | The scorer is public, deterministic and versioned | No | No | — | No | No | No |
| R4 | A trivial baseline is published first | No | No | — | No | No | No |
| R5 | A strong published baseline is published alongside it | **Yes** | No | — | No | No | No |
| R6 | Contamination is addressed explicitly, in writing, per task | No | No | — | No | No | No |
| R7 | Splits are DOI-archived with a datasheet | No | No | — | No | No | No |
| R8 | The evaluation is separable from the group whose models it scores | **Yes** | No | — | No | No | No |
| R9 | Every row carries model version, split, date and cost | No | No | — | No | No | No |

A dash means the track has no surface to score yet.

Two of nine rules are met on any track, both of them on Earthquakes. The full argument, the mitigation ladder for R8, and the seed-task designs are in
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
