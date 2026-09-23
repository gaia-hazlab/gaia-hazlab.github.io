---
title: Agent evaluations — the Repère board
short_title: Agent evaluations
description: Repère EvalHub scores AI agents doing geoscience work on accuracy, cost and reproducibility. The running board for HazEvalHub's agent track.
---

:::{note}
**Live, hosted externally.** The agent track of [HazEvalHub](hazevalhub); see also
[seismic event catalog workflows](hazevalhub-catalogs). The board runs at
[mdenolle.github.io/repere](https://mdenolle.github.io/repere/) from
[`mdenolle/repere`](https://github.com/mdenolle/repere) (MIT), a personal namespace rather than
`gaia-hazlab`. Moving it into the organisation is open work.
:::

## What the board scores

An agent that gets the right answer at ten times the cost of another agent has not won. Repère
scores every submission on three questions at once, and treats the second as a first-class axis
rather than an operational footnote.

| Question | What it measures |
|---|---|
| Is it right? | Accuracy against ground truth for the task |
| What did it cost? | Tokens and dollars spent reaching the answer |
| Is it reproducible? | Whether the same submission scores the same way twice |

The third question is why submissions are pinned rather than described. An agent is a moving
target — its model, its prompt, its tool definitions and its skills all drift — so a score
without a pin is a measurement of something that no longer exists.

## The board

Cost runs along the horizontal axis and performance up the vertical, so the upper left is where
a reader should look. Each model appears twice: a hollow marker for the run without domain
skills, a filled marker for the run with them, joined by a line whose length is the skill lift.

:::{iframe} https://mdenolle.github.io/repere/
:width: 100%
Repère EvalHub — cost against performance; hollow markers are runs without domain skills, filled
markers with them, and the connecting line is the skill lift
:::

Full board at [mdenolle.github.io/repere](https://mdenolle.github.io/repere/); source at
[github.com/mdenolle/repere](https://github.com/mdenolle/repere).

## Task categories

**Document-based tasks.** Reading and reasoning over literature: review, critique, translation
between subfield vocabularies, and interpretation of figures. These are the tasks where a
plausible wrong answer is most expensive, because it is hardest to spot.

**Software-agent tasks.** The agent drives scientific software rather than describing it —
writing a detector, running a processing pipeline, producing a data product. Concrete benchmarks
include choosing *dv/v* parameters, generating STA/LTA code, and correct ObsPy usage.

**Research-workflow tasks.** An orchestrator coordinating sub-agents and their dependencies,
scored on the trajectory as well as the answer. This is the category closest to how the project
actually intends to use agents, and the least mature.

## How a submission is pinned

- The agent is pinned by **commit SHA**, in whatever repository it already lives in. Nothing is
  vendored into the eval harness.
- Skills are versioned by **semantic-version git tag**, so a skill lift can be attributed to a
  specific revision.
- Public **validation splits** are published to Hugging Face or Zenodo with a DOI.
- **Test splits are held server-side** and the answers are never published.

## What the board shows, and what it does not yet

Read against [the nine rules](#the-nine-rules) on the hub page:

- **The evaluation's size is not stated on the board** (R2, R9). A reader cannot tell how many
  items a score is computed over, which bounds how much any gap between two models means.
- **Rows are not stamped with the split that produced them** (R2). Hidden splits exist, but the
  board does not distinguish a hidden-set result from a development run.
- **The scorer is not yet public** (R3). Until it is, the claim that scoring is deterministic and
  hard to game cannot be checked by anyone outside the project.
- **No trivial baseline is published** (R4). Without a floor, a score has no scale.
- **GAIA builds both the agents and the board** (R8). This is the rule this track fails hardest.
  The declared mitigations are to mark which entries are ours, to separate the person holding
  test answers from the person submitting, and to invite an external entry before publishing a
  GAIA result.

Stating these here rather than on the hub is deliberate. Anyone who follows the card to this
page meets the limits before they meet a number.

## Early results

Free local models in the 7-billion-parameter range reach perfect scores on configuration tasks
once given domain skills, and fail at numerical code generation, where only cloud models
succeed. Skill lift is large for some task classes and absent for others.

The result worth reporting alongside that one is negative: **on some task classes, domain skills
made local models worse.** A board that can only detect improvement is not measuring anything.
The number of items behind each of these figures is not published on the board, so treat them as
directional until it is.
