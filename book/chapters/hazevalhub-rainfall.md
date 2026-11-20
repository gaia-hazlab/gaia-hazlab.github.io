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
## Benchmark 1: rainfall datasets, Skagit River basin

There is no model to train here. Each row is a published gridded precipitation product, and
the score is how well it reproduces observed storm totals. The comparison is led by Nicoleta
Cristea and is from a manuscript in preparation; no scores are posted until its authors release
them.

**What is compared.** Six products in three classes.

| Product | Class | Grid | Time step | Built from the reference stations |
|---|---|---|---|---|
| PRISM | Station interpolation | 4 km | Daily | Yes |
| Daymet V4 | Station interpolation | 1 km | Daily | Yes |
| gridMET | PRISM climatology blended with NLDAS-2 reanalysis | 4 km | Daily | Through PRISM |
| CONUS404 | WRF downscaling of ERA5 | 4 km | Hourly | No |
| UCLA WUS-D3 | WRF downscaling of ERA5 | 9 km | Hourly | No |
| PNNL-WRF | WRF downscaling of ERA-Interim | 6 km | Hourly | No |

**Events.** Twelve storms in the Skagit River basin, Washington: the six atmospheric-river
events (category 4 or 5 on the [CW3E AR scale](https://cw3e.ucsd.edu/)) and the six
non-atmospheric-river events with the highest peak discharge at USGS gauge 12189500, Skagit
River near Mount Vernon. Each is scored over seven days, from two days before the event date
to five days after. The event dates will be listed here when the list is archived.

**Two tables, one ranked.**

*R1a, station validation (ranked).* Reference: SNOTEL and meteorological stations in the basin,
matched to the product grid cell. Ranked by mean absolute error in the seven-day event total.

| Rank | Product | Abs. error, 7-day total (mm) | Bias, AR events (mm) | Bias, non-AR events (mm) | Stations | Source |
|---:|---|---:|---:|---:|---:|---|
| | *No entries yet* | | | | | |

*R1b, agreement with PRISM (not ranked).* Reference: PRISM. This table measures the spread
between products. It is not a ranking, because PRISM is itself one of the products.

| Product | Abs. difference, basin-mean 7-day total (mm) | Median bias, 3-day totals above 100 mm (mm) | Bias in 99th-percentile daily precipitation (mm/day) | Source |
|---|---:|---:|---:|---|
| | *No entries yet* | | | |

**Limits.**

- PRISM and Daymet are interpolated from stations that include the reference stations, and
  gridMET takes its spatial pattern from PRISM. Their rows in R1a are not independent tests.
  The last column of the product table marks this.
- High-elevation windward slopes have few stations, and gauges under-catch snow and
  wind-driven rain. Station error is not yet estimated.
- Storm totals, not peak hours. Three of the six products are daily, so this benchmark does not
  yet score the hourly intensities described above. Only the WRF products can be scored hourly.
- One basin. A product's rank here does not carry to other terrain.

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

- **Publish the first numbers** for both benchmarks, with their baselines (R4, R5). For
  Benchmark 1 this needs the per-station event totals and the authors' release.
- **Archive the event list and the station matches** with a DOI. Benchmark 1 has its twelve
  events; none of them may fall in the training window of the downscaling model in Benchmark 2
  (R2, R6, R7).
- **Score stations that no product ingests.** Withheld or independent gauges would make the
  PRISM, Daymet and gridMET rows of R1a a fair test (R6).
- **Stamp each row** with product version, period and, for the downscaling model, compute cost
  (R9).
