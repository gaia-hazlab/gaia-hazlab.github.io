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

:::{div}
:class: hazard-icons
[![Earthquakes](../img/hazevalhub/earthquakes.svg)](https://seisscoped.org/QuakeScope/benchmark_summary.html "Earthquakes") [![Landslides](../img/hazevalhub/landslides.svg)](hazevalhub-landslides "Landslides") [![Floods](../img/hazevalhub/floods.svg)](hazevalhub-floods "Floods") [![Thunderstorms](../img/hazevalhub/thunderstorms.svg)](hazevalhub-thunderstorms "Thunderstorms") [![Atmospheric rivers](../img/hazevalhub/atmospheric-rivers.svg)](hazevalhub-rainfall "Atmospheric rivers") [![Agents](../img/hazevalhub/agents.svg)](https://mdenolle.github.io/repere/ "Agents")
:::

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

## Metrics

All metric definitions, and the tasks that use them, are on [Metrics](hazevalhub-metrics).

## Ownership and dates

**Interim owner:** Marine Denolle, until a permanent owner is named at kickoff.

**v0.5 target: 2027-03-31.** v0.5 means one hazard task with a hidden test set, a published
baseline and a public scorer.

The longest step is labelling. The planned seismic task needs a test set drawn from events after
the training window of the models it scores, labelled by two annotators with a third resolving
disagreements. Reusing the existing curated labels would be faster, but models trained on them
would be scored on data they have seen.
