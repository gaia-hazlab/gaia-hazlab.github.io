---
title: "Thunderstorms: thunderquake detection"
short_title: Thunderstorms
description: Evaluating seismoacoustic detectors of thunder-induced ground motion by how many lightning strikes they add to open lightning catalogs.
---

:::{note}
**In progress, board not yet published.** The thunderstorm track of [HazEvalHub](hazevalhub).
The project runs at [gaia-hazlab.github.io/thunderquakes](https://gaia-hazlab.github.io/thunderquakes/)
from [`gaia-hazlab/thunderquakes`](https://github.com/gaia-hazlab/thunderquakes) (MIT). Its
benchmark page will follow the layout of the
[QuakeScope picker benchmarks](https://seisscoped.org/QuakeScope/benchmark_summary.html) and be
embedded here when it exists.
:::

## What is being detected

Thunder couples into the ground near the strike. A seismometer records it as a broadband
(about 1 to 20 Hz), emergent signal lasting 10 to 30 seconds per clap; a co-located infrasound
microphone records the air-coupled arrival a few seconds later. That seismoacoustic delay is
the main discriminator against earthquakes, explosions and other surface events. Lightning
networks miss strikes in remote terrain and at high latitude, so a detector that recovers them
fills catalog gaps where those gaps are largest.

## What is compared

| Entry | Input |
|---|---|
| STA/LTA detector | Seismic only; the trivial baseline |
| Model A | Spectrogram CNN, seismic only; deployable on any station |
| Model B | Model A plus an infrasound branch; stations with a co-located `BDF` channel only |

Regions in order: Oklahoma, then the Pacific Northwest, then Alaska. Labels for training are the
PNWML analyst `thunder` class against `earthquake`, `explosion`, `surface-event` and `noise`.

## How it is scored

**Reference.** Open lightning catalogs: GOES-GLM, ALDN and WWLLN. All of them miss strikes, so
they are a lower bound on truth, not truth.

**Headline metric: completeness gain.** The number of strikes a detector finds that no catalog
lists, confirmed by the seismoacoustic delay, per station-month. Precision against the catalogs
alone would count every recovered strike as a false alarm and reward the detector that finds the
least.

**The operating point.** Detectors are compared at equal detections emitted per station-day,
not at a shared threshold, as on the picker board.

**Calibration.** Model uncertainty comes from MC-dropout and a small deep ensemble, so each
entry also reports a reliability diagram.

## The board

Not yet published. The plan is a `benchmark_summary` page built from the repository's Quarto
`report` environment, published at `gaia-hazlab.github.io/thunderquakes/benchmark_summary.html`
and embedded on this page.

## What this track needs next

Against [the nine rules](#the-nine-rules) on the hub page:

- **Publish the board**, with the STA/LTA baseline as the first row (R4).
- **A temporally disjoint test period** per region, chosen before training, so a score is not
  measured on storms the model has seen (R2, R6).
- **Archive the test windows and the matched lightning strikes** with a DOI (R7).
- **Stamp each row** with model version, region, period and compute cost (R9).

