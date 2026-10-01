---
title: HazEvalHub
short_title: HazEvalHub
description: Where GAIA's evaluations of AI models for earthquakes, landslides, floods, thunderstorms, atmospheric rivers and agents are collected and held to a single benchmark-integrity standard.
---

:::{note}
**In progress.** Interim owner **Marine Denolle**; v0.5 target **2027-03-31**. Three tracks have
scores: agents and earthquakes on boards hosted elsewhere, landslides on this site.
Thunderstorms and atmospheric rivers have pages but no scores. Floods is planned.
:::

## What HazEvalHub is

HazEvalHub collects the leaderboards GAIA uses to compare AI models for hazard research, one
track per hazard plus one for AI agents. Each track page lists its tasks, the test set for each
task, the scoring rule, and one row per model.

There is no shared scorer and no hidden test set yet. Each track page states its own limits,
and [the nine rules](#the-nine-rules) below show which benchmark rules each track meets.

## Evaluation tracks

Each card opens that track's leaderboard.

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
:footer: **Live**: 2 of 3 tasks scored
```{image} ../img/hazevalhub/landslides.svg
:alt: Landslides icon
:width: 56px
```
Seismic event classification, continuous detection at Mount Rainier, and susceptibility mapping for the 2025 Stehekin debris flows.
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

Notes on the two external boards: [agents](hazevalhub-agents),
[earthquakes](hazevalhub-catalogs).

(the-nine-rules)=
## The standard: nine rules for a citable benchmark

Adapted from the review criteria of the NeurIPS and ICML *Datasets and Benchmarks* track. Each
column is our own assessment of one track.

| # | Rule | Earthquakes | Landslides | Floods | Thunderstorms | Atm. rivers | Agents |
|---|---|---|---|---|---|---|---|
| R1 | The task is fully specified before submissions open | No | No | — | No | No | No |
| R2 | The test set is hidden, and the board says so on every row | No | No | — | No | No | Partly: hidden splits exist, rows are not stamped |
| R3 | The scorer is public, deterministic and versioned | No | No | — | No | No | No |
| R4 | A trivial baseline is published first | No | No | — | No | No | No |
| R5 | A strong published baseline is published alongside it | **Yes** | Task L1 only | — | No | No | No |
| R6 | Contamination is addressed explicitly, in writing, per task | No | No | — | No | No | No |
| R7 | Splits are DOI-archived with a datasheet | No | No | — | No | No | No |
| R8 | The evaluation is separable from the group whose models it scores | **Yes** | No | — | No | No | No |
| R9 | Every row carries model version, split, date and cost | No | No | — | No | No | No |

A dash means the track has no surface to score yet.

Two rules are met in full, both on Earthquakes. The reasoning behind each rule and the planned
first tasks are in the [HazEvalHub CTF plan](https://github.com/gaia-hazlab/gaia-hazlab.github.io/blob/main/project_coordination/09-hazevalhub-ctf-plan.md).

## Metric families we intend to publish

Chapters across this book forward-reference metric definitions to HazEvalHub. Those definitions
will live here, by pillar and hazard. **None is implemented yet**; the table lists what is
planned.

| Pillar | Metrics |
|---|---|
| State (Pillar 1) | RMSE and bias against wells, soil-moisture sensors and ET; storm-response temporal correlation; physical consistency (mass balance, hydrostatic) |
| Nowcast (Pillar 2) | POD, FAR, CSI; IoU and Dice for mapped failures; Brier score and reliability; lead time to alert |
| Forecast (Pillar 3) | Skill against persistence and climatology; ROC and precision-recall at decision thresholds; cost–loss value; lead time against skill |
| Actionability | Decision thresholds; false-alarm cost; warning lead time |
| Frugality | Tokens and dollars per submission; skill per dollar; skill lift from domain skills |

Cost is scored because the models are meant to run over archives that span decades.

## Ownership and dates

**Interim owner:** Marine Denolle, until a permanent owner is named at kickoff.

**v0.5 target: 2027-03-31.** v0.5 means one hazard task with a hidden test set, a published
baseline and a public scorer.

The longest step is labelling. The planned seismic task needs a test set drawn from events after
the training window of the models it scores, labelled by two annotators with a third resolving
disagreements. Reusing the existing curated labels would be faster, but models trained on them
would be scored on data they have seen.
