---
title: "Landslides: detection, modeling and the Stehekin validation"
short_title: Landslides
description: Evaluating QuakeXNet surface-event detection and classification, and Landlab failure-probability modeling validated against the 2025 Stehekin post-fire debris flows.
---

:::{note}
**In progress, no scores published yet.** The landslide track of [HazEvalHub](hazevalhub),
hosted here until it has a board of its own. This page fixes what will be compared and how it
will be scored, in the same form as the
[QuakeScope picker benchmarks](https://seisscoped.org/QuakeScope/benchmark_summary.html). The
science behind each half is on [Landslides](hazard-landslides) and in
[Pillar 2 §2](pillar-2-nowcasting-susceptibility).
:::

## Why two halves

A landslide claim has two parts that fail differently. A detector says an event happened, when
and roughly where. A model says how likely failure was, cell by cell, before anything moved.
The detector is scored against labelled waveforms; the model is scored against failures it never
saw, and some of those failures are the detector's output. Scoring the two separately keeps an
error in one from being credited to the other.

## Part 1: detection and classification (QuakeXNet)

**What is compared.** QuakeXNet against the other machine-learning classifiers in
[@kharita2026], trained and tested on roughly 200,000 waveforms from an AI-curated regional
dataset [@ni2023], with an STA/LTA detector as the trivial baseline.

**Reference labels.** Analyst classes (earthquake, explosion, surface event, noise) from the
PNSN and ESEC catalogs [@kharita2025quakexnet].

**Headline metric.** Probability of detection (POD), false-alarm ratio (FAR) and critical
success index (CSI) per class, with the surface-event class reported first because it is the one
a landslide study uses.

**The operating point.** As on the picker board, a shared probability threshold is not a fair
comparison. Each classifier is swept across its thresholds and compared at equal detections
emitted per station-day, so a permissive model cannot win by emitting more events.

**The catalog it produces.** The fifteen-year (2010–2025) Mount Rainier catalog, located with
ENVELOC:

:::{iframe} https://akashkharita.github.io/pnw_seismic_event_detection/data/enveloc_dashboard.html
:width: 100%
QuakeXNet · Mt. Rainier ENVELOC-located surface-event catalog, Akash Kharita. The catalog is
under review and its class labels are still changing.
:::

## Part 2: modeling and validation (Landlab, Stehekin 2025)

**What is compared.** Failure probability $P_f$ from Landlab's `LandslideProbability`
component [@strauch2018], run through the
[`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) MMP workflow with the
burn-severity layer switched on, against two baselines: a slope-only susceptibility map, and the
same model with burn severity switched off.

**Validation case.** The 2025 post-fire debris flows at Stehekin, Washington. Independent labels,
none of which enter the model:

| Label | Source |
|---|---|
| Event timing and approximate location | Seismic detections from [`gaia-stehekin-postfire-debrisflows`](https://github.com/gaia-hazlab/gaia-stehekin-postfire-debrisflows) |
| Mapped failure extent | Post-event DEM or lidar differencing [@bernard2021] |
| Regional failures | Sentinel-1 SAR detections [@mondini2021; @handwerger2022] |

**Headline metrics.** ROC and precision-recall curves for $P_f$ against mapped failures; Brier
score and a reliability diagram, because a probability that is never calibrated is a ranking;
spatial intersection over union (IoU) at the threshold a user would act on; and lead time from
the forcing that crossed that threshold to the first seismic detection.

Stehekin is a **validation case, not a held-out test set**. The workflow was configured for
these events, so a good score here shows the model can describe them, not that it generalises.

## What this track needs next

Against [the nine rules](#the-nine-rules) on the hub page:

- **Publish the first numbers** for both halves, with the baselines alongside (R4, R5).
- **A second, untouched debris-flow event** chosen before the model is run on it, so Stehekin
  stops doing double duty as tuning and test (R2, R6).
- **Archive the label sets with a DOI** and a datasheet: the classifier test split, the
  Stehekin masks and the seismic detections (R7).
- **A scorer anyone can run** on a submitted $P_f$ raster or detection list (R3).
- **Separation.** GAIA builds the detector, the model and this page (R8). The first mitigation is
  to invite an outside susceptibility model onto the Stehekin case.

## References
