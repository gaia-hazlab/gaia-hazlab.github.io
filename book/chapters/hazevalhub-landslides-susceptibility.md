---
title: "L3: susceptibility mapping, Stehekin 2025"
short_title: L3 Susceptibility
description: Landslide track task L3. Models map the probability of slope failure before the 2025 Stehekin post-fire debris flows, scored against the failures that occurred.
---

Task L3 of the [landslide track](hazevalhub-landslides). The model receives terrain, soil,
vegetation and burn-severity layers and daily weather forcing for the Stehekin area, and returns
a raster of failure probability $P_f$ for the period before the 2025 post-fire debris flows.

## Test data

Failures from the 2025 events, mapped by post-event DEM or lidar differencing [@bernard2021] and
Sentinel-1 SAR [@mondini2021; @handwerger2022], with event times from the seismic detections in
[`gaia-stehekin-postfire-debrisflows`](https://github.com/gaia-hazlab/gaia-stehekin-postfire-debrisflows).
None of these labels enter the models.

## Metrics

| Metric | Definition |
|---|---|
| Brier score | Mean squared difference between $P_f$ and observed failure (0 or 1) per cell. Ranking metric; lower is better |
| ROC AUC | Area under the receiver operating curve of $P_f$ against mapped failures |
| IoU | Intersection over union of predicted and mapped failure areas, at the threshold the entry declares |

## Leaderboard

| Rank | Model | Brier score | ROC AUC | IoU | Source |
|---:|---|---:|---:|---:|---|
| | *No entries yet* | | | | |

Planned first entries: Landlab `LandslideProbability` [@strauch2018] run through
[`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow), a slope-only map,
and the Landlab model without the burn-severity layer.

## Limits

Stehekin is a validation case rather than a held-out test: the Landlab workflow was set up for
these events. A second debris-flow event, chosen before any model runs on it, is needed for a
real test.

## References
