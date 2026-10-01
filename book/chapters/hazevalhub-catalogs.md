---
title: "Earthquakes: phase pickers (QuakeScope)"
short_title: Earthquakes
description: The earthquake track of HazEvalHub. Deep-learning phase pickers scored against analyst picks on the QuakeScope board, maintained by SeisSCOPED.
---

:::{note}
The board runs at
[seisscoped.org/QuakeScope](https://seisscoped.org/QuakeScope/benchmark_summary.html) from
[`SeisSCOPED/QuakeScope`](https://github.com/SeisSCOPED/QuakeScope) (MIT). SeisSCOPED maintains
it, not GAIA. QuakeScope is a picker benchmark and is unrelated to QuakeXNet, the classifier on
the [landslides leaderboard](hazevalhub-landslides).
:::

| Task | What the model does | Ranked by | Entries |
|---|---|---|---:|
| Phase picking | Picks P and S arrivals in continuous waveforms | Recall of analyst picks within 0.5 s, per phase | 4 sets of weights: `quakescope2026`, `jma_wc`, `original`, `instance` |

## Test sets

| Study | Reference picks |
|---|---|
| US sequences | ComCat events with SCEDC and NCEDC analyst picks |
| Global sequences | GeoNet, INGV and NOA bulletin picks |
| Ridgecrest aftershocks | SCEDC analyst picks, 30-minute window |
| Ocean bottom | iasp91 predicted arrivals and analyst picks |
| Western reproduction | Campaign data re-picked through FDSN |

## Board

:::{iframe} https://seisscoped.org/QuakeScope/benchmark_summary.html
:width: 100%
QuakeScope picker benchmarks: recall for four sets of model weights across five studies.
:::

The board also plots recall against the number of picks each model emits, because pickers with
the same probability threshold can emit very different numbers of picks.

## Limits

- All reference picks come from public bulletins, so a model may have trained on them.
- There is no STA/LTA baseline row.
- The test sets are not archived with a DOI, so results can shift when bulletins are revised.
- Throughput per station-day is not reported.
