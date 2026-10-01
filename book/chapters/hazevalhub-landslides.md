---
title: "Landslides: evaluation tasks"
short_title: Landslides
description: Evaluation tasks for AI models in landslide research, from classifying the seismic signals of slope failures to mapping failure probability. Each task has its own page with its test data, metrics and leaderboard.
---

The landslide track of [HazEvalHub](hazevalhub). Each task fixes a test set and a set of
metrics, and ranks models on them. Two tasks score data processing, the detection and labelling
of the seismic signals that slope failures produce. One scores modeling, the prediction of where
slopes fail. Test sets come from published work and will be revised; each task page names the
version it uses.

| Task | What the model does | Test data | Entries |
|---|---|---|---:|
| [L1 Seismic event classification](hazevalhub-landslides-classification) | Labels a trace as earthquake, explosion, surface event or noise | 8,000 PNW traces from the common test set of [@kharita2026] | 7 |
| [L2 Continuous detection](hazevalhub-landslides-detection) | Finds and labels surface events in continuous data at Mount Rainier, 2010 to 2025 | 3,970 PNSN surface events and explosions | 1 |
| [L3 Susceptibility mapping](hazevalhub-landslides-susceptibility) | Maps failure probability before the 2025 Stehekin debris flows | Mapped failures from the 2025 events | 0 |

## Adding a model

Open an issue or pull request on
[`gaia-hazlab/gaia-hazlab.github.io`](https://github.com/gaia-hazlab/gaia-hazlab.github.io)
with a link to the code and commit, the training data used, the predictions in the format the
task page asks for, and the parameter count and processing time with the hardware. There is no
public scorer yet, so current rows come from published papers or the authors' own runs, as each
row's source says.

## References
