---
title: "Landslides: leaderboard"
short_title: Landslides
description: Leaderboard for AI models in landslide research. Three tasks, from classifying the seismic signals of slope failures to mapping failure probability, each with a fixed test set and one row per model.
---

:::{note}
The landslide track of [HazEvalHub](hazevalhub), hosted on this site for now. Tasks L1 and L2
have entries; L3 has none yet. Test sets come from published work and will be revised; each
table names the version it was scored on.
:::

This page ranks AI models used in landslide research. A task fixes the input data, the test set
and the scoring rule. Each row is one model scored on that test set, with the source of the
numbers. QuakeXNet appears as one row among several. The first two tasks score data processing:
finding and labelling the seismic signals that slope failures produce. The third scores
modeling: predicting where slopes fail.

| Task | What the model does | Test set | Ranked by | Entries |
|---|---|---|---|---:|
| [L1](#task-l1) Seismic event classification | Labels a three-component trace as earthquake, explosion, surface event or noise | Common test set of [@kharita2026]: 8,000 traces, 2,000 per class | F1 | 7 |
| [L2](#task-l2) Continuous detection, Mount Rainier | Finds and labels surface events and explosions in continuous data, 2010 to 2025 | 3,970 PNSN-catalogued surface events and explosions near the summit | Surface-event recall | 1 |
| [L3](#task-l3) Susceptibility, Stehekin 2025 | Maps the probability of slope failure before the 2025 post-fire debris flows | Mapped failures and seismic detections from the 2025 events | Brier score | 0 |

(task-l1)=
## L1: seismic event classification

**Input.** A three-component waveform window from one station.

**Output.** One of four classes: earthquake, explosion, surface event, noise.

**Test set.** The common test set of [@kharita2026]: 8,000 three-component traces, 2,000 per
class, drawn from the curated Pacific Northwest dataset [@ni2023] with extra surface-event
recordings from nearby stations. No event in the test set appears in the training or validation
data. Feature-based models in the paper use the vertical component of the same traces.

**Scoring.** F1 as reported in Table 1 of the paper, then accuracy. Parameters, memory and the
time to process one day of 100 Hz data at one station come from Table 2, which covers the
deep-learning models only.

```{include} includes/landslides-classification.md
```

**Limits of this task.**

- The test set is public, so a model trained on the full curated dataset may have seen it. New
  entries must state their training data.
- The list of test trace IDs is not yet published as a separate file. Until it is, outside
  models cannot be scored on exactly these 8,000 traces.
- The paper also reports out-of-domain tests on global surface events from the Exotic Seismic
  Event Catalog and on near-field explosions. Those are candidates for two more tasks.

(task-l2)=
## L2: continuous detection, Mount Rainier

**Input.** Continuous waveforms from stations within 50 km of the Mount Rainier summit,
2010 to 2025.

**Output.** A catalog of network events, each with a start time and a class.

**Test set.** PNSN events labelled surface event (`su`) or explosion (`px`), 2010 to April 2026,
for which at least half of the reporting stations lie within 50 km of the summit: 3,269 surface
events and 701 explosions. A PNSN event counts as found if the model's catalog has an event
starting within 60 s of the PNSN origin time.

**Scoring.** Recall for surface events, then for explosions. The share of matched events that
the model gave the PNSN class is reported next to it.

```{include} includes/landslides-detection.md
```

The QuakeXNet catalog can be explored on its
[interactive map](https://akashkharita.github.io/pnw_seismic_event_detection/data/enveloc_dashboard.html).

**Limits of this task.**

- Precision is not scored. PNSN does not list every surface event, so a detection with no PNSN
  match may be a real event or a false one. Scoring precision needs an independently labelled
  sample of those detections.
- QuakeXNet was trained on data curated from PNSN, the same source as the reference labels.
- There is no baseline row yet. An STA/LTA detector run over the same stations and years would
  give one.
- The QuakeXNet row uses one fixed detection threshold. A threshold sweep would show recall
  against the number of detections.
- 2026 is partial. The PNSN list runs to 22 April 2026, and the model catalog may stop earlier:
  the copy in the repository's diagnostic notebook ends on 11 March.

(task-l3)=
## L3: landslide susceptibility, Stehekin 2025

**Input.** Terrain, soil, vegetation and burn-severity layers, and daily weather forcing, for
the Stehekin area before the 2025 post-fire debris flows.

**Output.** A raster of failure probability $P_f$.

**Test set.** Failures from the 2025 events, mapped by post-event DEM or lidar differencing
[@bernard2021] and Sentinel-1 SAR [@mondini2021; @handwerger2022], with event times from the
seismic detections in
[`gaia-stehekin-postfire-debrisflows`](https://github.com/gaia-hazlab/gaia-stehekin-postfire-debrisflows).

**Scoring.** Brier score on $P_f$, then ROC AUC. Intersection over union of the mapped failures
is reported at the probability threshold the entry declares.

| Rank | Model | Brier score | ROC AUC | IoU | Source |
|---:|---|---:|---:|---:|---|
| | *No entries yet* | | | | |

The first entries planned are Landlab `LandslideProbability` [@strauch2018] run through
[`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow), and two baselines: a
slope-only map, and the same Landlab model without the burn-severity layer.

**Limits of this task.** Stehekin is a validation case rather than a held-out test: the Landlab
workflow was set up for these events. A second debris-flow event, chosen before any model is run
on it, is needed for a real test.

## Adding a model

Open an issue or pull request on
[`gaia-hazlab/gaia-hazlab.github.io`](https://github.com/gaia-hazlab/gaia-hazlab.github.io)
with:

- a link to the code and the commit that produced the result;
- the training data used, so overlap with the test set can be checked;
- the predictions: per-trace classes and probabilities for L1, an event catalog for L2, a
  $P_f$ raster for L3;
- parameter count and processing time, with the hardware.

For L1 the row goes in
[`data/hazevalhub/landslides_classification.csv`](https://github.com/gaia-hazlab/gaia-hazlab.github.io/blob/main/data/hazevalhub/landslides_classification.csv);
[`scripts/hazevalhub/landslides_leaderboard.py`](https://github.com/gaia-hazlab/gaia-hazlab.github.io/blob/main/scripts/hazevalhub/landslides_leaderboard.py)
rebuilds the tables. There is no public scorer yet, so current rows come from published papers
or the authors' own runs, as the Source column says. How these tasks measure up against the
project's benchmark rules is in [the nine rules](#the-nine-rules).

## References
