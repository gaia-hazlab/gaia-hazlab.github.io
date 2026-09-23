---
title: Seismic event catalog workflows — the QuakeScope benchmarks
short_title: Catalog workflows
description: Benchmarking the phase pickers and workflows that turn continuous seismic data into event catalogs, against analyst arrivals across five study regions.
---

:::{note}
**Live, hosted externally — and being reworked.** The catalog-workflow track of
[HazEvalHub](hazevalhub); see also [agent evaluations](hazevalhub-agents). The benchmarks run at
[seisscoped.org/QuakeScope](https://seisscoped.org/QuakeScope/) from
[`SeisSCOPED/QuakeScope`](https://github.com/SeisSCOPED/QuakeScope) (MIT), maintained by
SeisSCOPED. The catalogs this track evaluates feed
[Landslides → Detection](hazard-landslides) and [ModelHub](modelhub).
:::

## Why catalog workflows need their own evaluation

A phase picker is one stage. What a hazard user consumes is the catalog that a whole workflow
emits — detection, phase picking, association, location, magnitude — and an improvement at one
stage can be undone at the next. Scoring the picker in isolation measures a component; scoring
the workflow measures the product.

The distinction matters concretely for GAIA. The fifteen-year Mount Rainier surface-event
catalog is produced by running a classifier over a continuous archive and locating what it finds
[@kharita2025quakexnet], and the choice of classifier was itself settled by a comparison of
machine-learning methods on roughly 200,000 waveforms from an AI-curated regional dataset
[@kharita2026; @ni2023]. Every one of those stages has its own failure mode, and only the
catalog at the end is what a landslide study actually uses.

:::{important}
**QuakeScope and QuakeXNet are different things.** QuakeScope is SeisSCOPED's benchmarking
framework for seismic phase pickers, described on this page. QuakeXNet is the GAIA event
classifier documented under [Landslides → Detection](hazard-landslides) and in
[@kharita2026]. An outside reviewer has already conflated the two; the names are unfortunately
close.
:::

## The picker benchmarks

QuakeScope compares sets of model weights against reference arrivals across five study regions,
consolidating five benchmark notebooks into one report.

:::{iframe} https://seisscoped.org/QuakeScope/benchmark_summary.html
:width: 100%
QuakeScope picker benchmarks — recall for four sets of model weights across five benchmark
studies
:::

Full report at
[seisscoped.org/QuakeScope/benchmark_summary.html](https://seisscoped.org/QuakeScope/benchmark_summary.html);
project at [seisscoped.org/QuakeScope](https://seisscoped.org/QuakeScope/); source at
[github.com/SeisSCOPED/QuakeScope](https://github.com/SeisSCOPED/QuakeScope).

## What is compared

Four sets of model weights — `quakescope2026`, `jma_wc`, `original` and `instance` — against
five sets of reference arrivals:

| Study | Reference arrivals |
|---|---|
| US sequences | ComCat events with SCEDC and NCEDC analyst arrivals, manual picks only |
| Global sequences | GeoNet, INGV and NOA bulletins, manual picks |
| Ridgecrest aftershocks | SCEDC analyst picks in a 30-minute window |
| Ocean bottom | iasp91 predicted arrivals plus analyst picks from several sources |
| Western reproduction | Campaign data re-picked through FDSN |

The headline metric is recall — the fraction of reference picks recovered within 0.5 seconds —
reported per phase for P and S.

## A threshold is not an operating point

This is the transferable idea on the page, and it generalises well beyond phase picking.

Two models that both emit a probability do not emit the same probability. A confidence of 0.3
from one picker and 0.3 from another can correspond to completely different pick budgets, so
comparing recall at a shared threshold silently compares one model being permissive against
another being conservative. The model that emits more picks recovers more reference arrivals,
and has not necessarily done anything better.

The comparison that holds is recall against **picks emitted**: sweep the threshold, plot the
curve, and read off what each model recovers at equal budget. Any benchmark whose leaderboard
reports a single number at a fixed threshold is making this mistake, and most do.

## What this track needs next

Against [the nine rules](#the-nine-rules) on the hub page:

- **No frozen task specification** (R1). The benchmarks are a report, not an open task others can
  submit to.
- **Nothing is hidden** (R2). Every study runs against public bulletins, so the benchmark cannot
  distinguish generalisation from familiarity with a well-studied sequence.
- **No trivial baseline** (R4). An STA/LTA detector published alongside would give the recall
  numbers a floor.
- **Splits are not DOI-archived with a datasheet** (R7), so a result here is not reproducible
  after the underlying bulletins change.
- **No per-row cost** (R9). Picker throughput is a real operational constraint at archive scale
  and is currently invisible.

One rule this track already passes that the agent track does not: **the benchmark is maintained
by SeisSCOPED, not by GAIA** (R8). We are scored here rather than scoring ourselves, which is the
separability the agent board has to engineer deliberately.

The GAIA-specific next step is a temporally disjoint Mount Rainier test set — events drawn from
after the training window of the models it scores, newly labelled — which turns this from a
report into a benchmark a result could be cited from.

## References
