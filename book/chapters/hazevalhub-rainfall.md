---
title: "Atmospheric rivers: extreme rainfall"
short_title: Atmospheric rivers
description: Evaluating gridded precipitation products against gauges, and the downscaling of ACE2 AI weather forecasts to Stage IV resolution, on the extreme-rainfall events that drive Pacific Northwest hazards.
---

:::{note}
**In progress, no scores published yet.** The atmospheric-river track of
[HazEvalHub](hazevalhub). Two benchmarks: a comparison of rainfall datasets led by Nicoleta
Cristea, and a model that downscales ACE2 forecasts to Stage IV led by Brandon Kerns. Links to
both will be added when their results are public. The forcing context is on
[Ocean–Atmosphere Coupling](ocean-atmosphere-coupling).
:::

## Why this track scores extremes

An atmospheric river matters to a landslide or flood model through the few hours of heaviest
rain, not through the storm total. A precipitation product or a forecast can have a small mean
error and still miss those hours. Every metric on this page is therefore reported above a set of
extreme thresholds, as well as on average.

(rainfall-r1)=
## Benchmark 1: rainfall datasets

**What is compared.** Gridded precipitation products used as forcing elsewhere in GAIA, among
them PRISM, Stage IV, CONUS404 and HRRR. Each is staged through
[`gaia-data-downloaders`](https://github.com/gaia-hazlab/gaia-data-downloaders) and
[`precip-stac`](https://github.com/gaia-hazlab/precip-stac).

**Reference.** Rain gauges, matched to the product grid cell.

**Metrics.** Bias and RMSE at daily and hourly accumulation; probability of detection and
critical success index above the 95th and 99th percentile of gauge rainfall; and error in the
upper quantiles of the distribution.

(rainfall-r2)=
## Benchmark 2: ACE2 downscaled to Stage IV

**What is compared.** ACE2 AI weather forecasts, downscaled to Stage IV resolution by a learned
model, against two baselines: bilinear interpolation of ACE2, and quantile mapping.

**Reference.** Stage IV analyses over the forecast window.

**Metrics.** Continuous ranked probability score (CRPS) if the downscaling is probabilistic;
fractions skill score (FSS) at extreme thresholds and several neighbourhood sizes; error in the
upper quantiles; and the power spectrum, to show whether the downscaled field has small-scale
structure or only a smoothed one.

## What this track needs next

Against [the nine rules](#the-nine-rules) on the hub page:

- **Publish the first numbers** for both benchmarks, with their baselines (R4, R5).
- **Fix the event list before scoring.** The atmospheric-river events used for evaluation are
  named before any product is scored, and none of them is in the training window of the
  downscaling model (R2, R6).
- **Archive the gauge matches and the event list** with a DOI (R7).
- **Stamp each row** with product version, period and, for the downscaling model, compute cost
  (R9).
