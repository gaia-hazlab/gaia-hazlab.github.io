---
title: "Tutorial 4: Evaluating agent runs"
short_title: 4. Evaluating agent runs
description: Score a set of agent runs on the three HazEvalHub questions, is it right, what did it cost, is it reproducible, and compare an open-weight model with a private one on the same task.
---

(tutorial-evaluating-agent-runs)=

:::{note}
**Status.** Stub. Objectives, prerequisites, exercise and self-check are drafted; the
code cells are empty and carry a comment saying what belongs in each. To be completed
with UW eScience. Compute needs are tracked in
[compute requirements](../compute-requirements.md). Companion to the
[lecture](../agents-intro.md), segments 34 to 45, and to the
[HazEvalHub](../../../chapters/hazevalhub.md) chapter.
:::

## Learning objectives

After this tutorial a participant can:

1. Write a task specification with a checkable ground truth and a declarative scoring
   rule, in the style the FrugalMind prototype uses for HazEvalHub.
2. Capture the trajectory of an agent run (prompts, model turns, tool calls, tool
   results, token counts) in a form that can be scored and re-read.
3. Score a batch of runs on outcome, cost, and reproducibility, and present the three
   together rather than the first alone.
4. Compare two models, one open-weight and run locally, one private and reached by API,
   on the same task with the same skill, and read the result as skill lift.
5. Say what a Reproducibility Statement for an agent-assisted result would have to
   contain [@denolle2026three].

## Prerequisites

- [Tutorial 2](02-writing-your-first-skill.md): the acknowledgement skill, which is the
  task under evaluation here.
- [Tutorial 1](01-anatomy-of-an-agent.md): one captured transcript, and the code from
  its steps 4 to 6.
- The [HazEvalHub](../../../chapters/hazevalhub.md) chapter, for the three questions and
  the cost-versus-performance board.
- TODO: access to one open-weight model served locally (the HazEvalHub prototype used
  7 to 8 billion parameter models) and one private model by API. Hardware and key
  handling are in [compute requirements](../compute-requirements.md).
- A second harness for the local model. A skill is a Claude Code construct, and Claude
  Code drives the vendor's models, so the open-weight condition runs on a different loop
  (TODO: which; the HazEvalHub prototype has one). "Same task, same skill" then means the
  skill body pasted into that harness's system prompt, and the comparison is across two
  harnesses as well as two models. Record that in the scorecard.
- TODO: the scoring specification format. The FrugalMind prototype uses declarative JSON
  specs; confirm whether the course adopts that format directly or a simplified one.

## Estimated duration

Two hours, estimated as: twenty minutes on the task specification, forty running the
batch, forty scoring and plotting, twenty on the reproducibility statement. TODO: revise
after the first run with eScience.

## Worked exercise

The task is deliberately small so that the evaluation, not the task, is the object of
study: insert the agreed NSF acknowledgement into a page. Ground truth is a string
comparison against the governance page. The interesting quantities are how often each
model gets it exactly right, at what cost, and whether the same prompt gives the same
result twice.

### Step 1. Write the task specification

```json
// Belongs here: the task spec. Fields: task id, the prompt, the input file, the file
// the ground truth is read from, the scoring rule (exact match of the inserted
// paragraph; partial credit rules if any), and the fields to record per run (model,
// skill on or off, tokens in, tokens out, wall time, exit reason).
```

### Step 2. Capture trajectories

```bash
# Belongs here: a loop that runs the task N times per condition (two models, skill on
# and off, so four conditions), each as a bounded headless run with structured output,
# and stores each trajectory under a run id. TODO: N. Record the model version string
# and the skill file's git hash with each run.
```

### Step 3. Score outcome

```python
# Belongs here: code that reads each run's output file, applies the scoring rule from
# step 1, and writes a scorecard row per run: run id, condition, score, exit reason.
```

### Step 4. Score cost

```python
# Belongs here: code that reads tokens in and out from each trajectory and converts to
# a cost using a price table that the participant fills in from the vendor's current
# page (do not embed prices in the code). For the local model, record wall time and
# the hardware used instead. Add the cost column to the scorecard.
```

### Step 5. Score reproducibility

```python
# Belongs here: code that groups runs by condition and reports, per condition, the
# fraction of runs with the identical inserted paragraph, and the number of distinct
# outputs observed. Add both to the scorecard.
```

Four things make that fraction less than one: the next token is sampled and the API used
here exposes no seed; batched inference on shared accelerators is generally not
bit-reproducible (TODO: cite); a model name can point at new weights, so log the model ID
with every run; and the page, the repository and the web the agent touched can differ
between runs, which only the trajectory records.

### Step 6. Plot the board

```python
# Belongs here: a cost-versus-score scatter in the style of the HazEvalHub board: each
# model plotted twice, skill off (hollow) and skill on (filled), joined by a line
# whose length is the skill lift. One point per condition, error bars from the N runs.
```

Read the plot against the prototype's early result: small local models reach parity with
cloud models on configuration tasks once given domain skills. Does the acknowledgement
task behave like a configuration task? Would a numerical task?

### Step 7. Write the Reproducibility Statement

For one run of your choice, write the paragraph a paper would need: which model and
version, which skill at which commit, which prompt, which harness and version, the run
id and where its trajectory is stored, the cost, and what a reader would need to do to
reproduce it. Compare it to a Data Availability statement in a paper you have written.

```markdown
<!-- Belongs here: the participant's Reproducibility Statement for one run. -->
```

## Check yourself

1. Which of the three questions (right, cost, reproducible) did the private model win
   on, and which did the open-weight model win on? Was the answer the same with the
   skill on and off?
2. Two runs in the same condition gave different outputs. Name three things that could
   differ between them and which of the three your trajectory capture would reveal.
3. A model scores perfectly at ten times the cost of another that scores nearly
   perfectly. Which would you ship in a GAIA agent, and what would change your answer?
4. What in your Reproducibility Statement could not be written from the trajectory
   alone? Where would it have to come from?
5. The scoring rule was an exact string match. Name a GAIA task from the HazEvalHub
   chapter for which no such rule exists, and say what would replace it.
