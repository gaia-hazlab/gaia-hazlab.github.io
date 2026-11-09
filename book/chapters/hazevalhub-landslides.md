---
title: Landslides
description: HazEvalHub landslide track. Three evaluation tasks for AI models, each with its test data and leaderboard.
---

Track of [HazEvalHub](hazevalhub). Metric definitions: [Metrics](hazevalhub-metrics).

| Task | Model output | Ranked by | Entries |
|---|---|---|---:|
| [L1 Event classification](#landslides-l1) | Class of a seismic trace | F1 | 7 |
| [L2 Continuous detection](#landslides-l2) | Event catalog from continuous data | su recall | 1 |
| [L3 Susceptibility](#landslides-l3) | Failure-probability raster | Brier score | 0 |

(landslides-l1)=
## L1: seismic event classification

Label a three-component trace as earthquake, explosion, surface event or noise.

**Test data.** Common test set of [@kharita2026]: 8,000 Pacific Northwest traces, 2,000 per
class [@ni2023]. No event shared with training data. Public; trace IDs not yet released.

```{include} includes/landslides-classification.md
```

(landslides-l2)=
## L2: continuous detection, Mount Rainier

Detect and label surface events and explosions in continuous data from stations within 50 km of
the summit, 2010 to 2025.

**Test data.** 3,269 surface events and 701 explosions from the PNSN catalog, 2010 to April 2026.
A match is a detection starting within 60 s of the PNSN origin time.

```{include} includes/landslides-detection.md
```

(landslides-l3)=
## L3: susceptibility, Stehekin 2025

Map failure probability $P_f$ before the 2025 Stehekin post-fire debris flows.

**Test data.** Failures mapped by DEM differencing [@bernard2021] and Sentinel-1 SAR
[@mondini2021; @handwerger2022], timed by seismic detections in
[`gaia-stehekin-postfire-debrisflows`](https://github.com/gaia-hazlab/gaia-stehekin-postfire-debrisflows).

| Rank | Model | Brier | ROC AUC | IoU | Source |
|---:|---|---:|---:|---:|---|
| | *No entries yet* | | | | |

## Adding a model

Open an issue or pull request on
[`gaia-hazlab/gaia-hazlab.github.io`](https://github.com/gaia-hazlab/gaia-hazlab.github.io)
with code and commit, training data, predictions, and runtime with hardware. L1 rows go in
[`data/hazevalhub/landslides_classification.csv`](https://github.com/gaia-hazlab/gaia-hazlab.github.io/blob/main/data/hazevalhub/landslides_classification.csv).

## References
