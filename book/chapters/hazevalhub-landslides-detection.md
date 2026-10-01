---
title: "L2: continuous detection at Mount Rainier"
short_title: L2 Detection
description: Landslide track task L2. Models detect and label surface events and explosions in fifteen years of continuous data around Mount Rainier, scored against the PNSN catalog.
---

Task L2 of the [landslide track](hazevalhub-landslides). The model runs over continuous
waveforms from stations within 50 km of the Mount Rainier summit, 2010 to 2025, and returns a
catalog of network events, each with a start time and a class.

## Test data

PNSN events labelled surface event (`su`) or explosion (`px`), 2010 to April 2026, for which at
least half of the reporting stations lie within 50 km of the summit: 3,269 surface events and
701 explosions. A PNSN event counts as found if the model's catalog has an event starting within
60 s of the PNSN origin time.

## Metrics

| Metric | Definition |
|---|---|
| su recall | Share of PNSN surface events found. Ranking metric |
| px recall | Share of PNSN explosions found |
| su label, px label | Share of found PNSN events that the model gave the PNSN class |
| Not in PNSN | Model detections with no PNSN match |
| Precision | Not scored: PNSN does not list every surface event, so unmatched detections are unlabelled |

## Leaderboard

```{include} includes/landslides-detection.md
```

The QuakeXNet catalog can be explored on its
[interactive map](https://akashkharita.github.io/pnw_seismic_event_detection/data/enveloc_dashboard.html).

## Limits

- QuakeXNet was trained on data curated from PNSN, the source of the reference labels.
- There is no baseline row. An STA/LTA detector over the same stations and years would give one.
- 2026 is partial: the PNSN list runs to 22 April 2026, and the copy of the model catalog in
  the repository's diagnostic notebook ends on 11 March.
