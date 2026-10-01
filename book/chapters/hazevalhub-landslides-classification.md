---
title: "L1: seismic event classification"
short_title: L1 Classification
description: Landslide track task L1. Models label three-component seismic traces as earthquake, explosion, surface event or noise, scored on the common test set of Kharita et al. (2026).
---

Task L1 of the [landslide track](hazevalhub-landslides). The model receives a three-component
waveform window from one station and returns one of four classes: earthquake, explosion, surface
event, noise. Surface events include rockfalls, debris flows and avalanches.

## Test data

The common test set of [@kharita2026]: 8,000 traces, 2,000 per class, from the curated Pacific
Northwest dataset [@ni2023], with extra surface-event recordings from nearby stations. No event
in the test set appears in the training or validation data. The set is public.

## Metrics

| Metric | Definition |
|---|---|
| F1 | Harmonic mean of precision and recall, as reported in Table 1 of [@kharita2026]. Ranking metric |
| Accuracy | Share of the 8,000 traces given the correct class |
| Params | Trainable parameters |
| MB | Memory used by the model |
| s/day | Seconds to process one day of 100 Hz data at one station |

## Leaderboard

```{include} includes/landslides-classification.md
```

## Limits

- A model trained on the full curated dataset may have seen the test traces. Entries must state
  their training data.
- The test trace IDs are not yet published as a separate file, so outside models cannot yet be
  scored on exactly these traces.

## References
