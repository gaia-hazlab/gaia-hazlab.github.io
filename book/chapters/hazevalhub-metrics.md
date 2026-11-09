---
title: Metrics
description: Every metric used on the HazEvalHub leaderboards, its definition, and the tasks that use it.
---

Metrics used across [HazEvalHub](hazevalhub). "(rank)" marks the metric a task is ranked by.

| Metric | Definition | Used in |
|---|---|---|
| Pick recall | Share of analyst picks matched by a model pick within 0.5 s, per phase | [Earthquakes](https://seisscoped.org/QuakeScope/benchmark_summary.html) (rank) |
| F1 | Harmonic mean of precision and recall | [Landslides L1](#landslides-l1) (rank) |
| Accuracy | Share of test items given the correct class | [Landslides L1](#landslides-l1), [Agents](https://mdenolle.github.io/repere/) |
| Event recall | Share of catalog events matched by a detection within 60 s | [Landslides L2](#landslides-l2) (rank) |
| Class agreement | Share of matched events given the reference class | [Landslides L2](#landslides-l2) |
| Brier score | Mean squared difference between predicted probability and outcome (0 or 1); lower is better | [Landslides L3](#landslides-l3) (rank) |
| ROC AUC | Area under the receiver operating curve | [Landslides L3](#landslides-l3) |
| IoU | Intersection over union of predicted and mapped areas | [Landslides L3](#landslides-l3) |
| Completeness gain | Confirmed detections absent from every reference catalog, per station-month | [Thunderstorms](hazevalhub-thunderstorms) (rank) |
| Reliability | Observed frequency against predicted probability, by bin | [Thunderstorms](hazevalhub-thunderstorms), [Landslides L3](#landslides-l3) |
| Bias, RMSE | Mean and root-mean-square difference from gauges | [Atmospheric rivers R1](#rainfall-r1) |
| POD, CSI | Probability of detection and critical success index above a rainfall percentile | [Atmospheric rivers R1](#rainfall-r1) |
| Upper-quantile error | Error in the 95th and 99th percentiles of rainfall | [Atmospheric rivers R1](#rainfall-r1), [R2](#rainfall-r2) |
| CRPS | Continuous ranked probability score of a probabilistic forecast | [Atmospheric rivers R2](#rainfall-r2) |
| FSS | Fractions skill score above a threshold, over a neighbourhood | [Atmospheric rivers R2](#rainfall-r2) |
| Power spectrum | Spatial variance by wavelength, against Stage IV | [Atmospheric rivers R2](#rainfall-r2) |
| Cost | Parameters, memory, runtime per station-day; tokens and dollars for agents | [Landslides L1](#landslides-l1), [Agents](https://mdenolle.github.io/repere/) |
| Reproducibility | Whether a pinned submission scores the same twice | [Agents](https://mdenolle.github.io/repere/) |

Floods has no metrics yet.

## Planned, by pillar

Not implemented yet. Chapters elsewhere in this book refer to these.

| Pillar | Metrics |
|---|---|
| State (Pillar 1) | RMSE and bias against wells, soil-moisture sensors and ET; storm-response temporal correlation; physical consistency (mass balance, hydrostatic) |
| Nowcast (Pillar 2) | POD, FAR, CSI; IoU and Dice for mapped failures; Brier score and reliability; lead time to alert |
| Forecast (Pillar 3) | Skill against persistence and climatology; ROC and precision-recall at decision thresholds; cost–loss value; lead time against skill |
| Actionability | Decision thresholds; false-alarm cost; warning lead time |
| Frugality | Tokens and dollars per submission; skill per dollar; skill lift from domain skills |
