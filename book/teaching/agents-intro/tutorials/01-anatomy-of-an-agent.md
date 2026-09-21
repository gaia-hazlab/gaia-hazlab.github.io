---
title: "Tutorial 1: Anatomy of an agent"
short_title: 1. Anatomy of an agent
description: Run one agent session end to end, capture its transcript, and label every step of the loop, every tool call, and every token spent on context.
---

(tutorial-anatomy-of-an-agent)=

:::{note}
**Status.** Stub. Objectives, prerequisites, exercise and self-check are drafted; the
code cells are empty and carry a comment saying what belongs in each. To be completed
with UW eScience. Compute needs are tracked in
[compute requirements](../compute-requirements.md). Companion to the
[lecture](../agents-101.md), segments 0 to 14.
:::

## Learning objectives

After this tutorial a participant can:

1. State what a language model does with a prompt, and what an agent harness adds.
2. Identify the four stages of the agent loop (gather context, act, verify, repeat) in a
   real transcript, and mark where each stage begins.
3. Read a repository's context file and say which lines change the agent's behaviour and
   which are dead weight.
4. Account for the context window of one session: how many tokens went to the system
   prompt, the context file, tool descriptions, the conversation, and tool results.
5. Stop a run deliberately, and explain the three ways a run ends.

## Prerequisites

- A GitHub account and a laptop with a terminal. This matches the eScience workshop's
  stated prerequisites [@escience2026codingagents]; no AI or machine-learning background
  is assumed.
- Git, and a clone of this repository or of the exercise repository (TODO: decide which).
- Access to a coding agent. The *harness* is the program that calls the model in a loop,
  parses its tool calls, checks permissions and runs them; Claude Code is the one used in
  the lecture. TODO: which harness and model the course uses, and how participants obtain
  a key or a session; see [compute requirements](../compute-requirements.md).
- The harness's *permission mode*: the setting that says which tool calls run without
  asking, which pause for a yes, and which are refused. Know where it is set before
  step 3.
- The [lecture](../agents-101.md), or its first fourteen minutes.

## Estimated duration

Ninety minutes, estimated as: fifteen minutes of setup, forty-five of exercise, thirty of
annotation and discussion. TODO: revise after the first run with eScience.

## Worked exercise

The exercise runs one bounded agent session on a small, real task in this repository,
captures everything the agent did, and then dissects the capture.

### Step 1. Confirm the environment

```bash
# Belongs here: the commands that confirm the harness is installed, the model is
# reachable, and the key or session is valid. Print the harness version. Print the
# model name the harness will use. Do not print the key.
```

### Step 2. Read the context file before the agent does

Open `AGENTS.md` and `CLAUDE.md` at the repository root. For each line, write one of
three labels in the margin: *changes behaviour*, *could be found by reading the code*,
or *not needed for this task*. Keep the sheet; you will compare it to what the agent
actually used.

### Step 3. Run one bounded session

The task: the repository's spellcheck fails on a scratch page; fix it and show that the
check passes. Before the session, the instructor adds one page under `book/teaching/`
with a single misspelling (not committed; a committed misspelling fails CI). The task is
chosen because it needs a gather (run `pixi run spellcheck`, read the page), an act (edit
one word) and a real verify (rerun the check, exit 0), and because the pass condition is
the repository's own tool rather than the model's opinion. Watch whether the agent
changes more than one word; that is the minimal-change rule from the lecture.

```bash
# Belongs here: the headless invocation of the harness with the task above as the
# prompt, a turn limit, and structured output captured to a file. The exact flags
# depend on the harness version chosen for the course; leave a comment naming them.
```

```bash
# Belongs here: the same task run interactively, so participants can watch each tool
# call appear and see the permission prompt for any gated action. Note which mode
# you use for the rest of the tutorial and why.
```

### Step 4. Capture the transcript

```python
# Belongs here: code that loads the captured transcript (structured output from step 3,
# or the harness's own session log) into a list of events, one per prompt, model
# turn, tool call, or tool result. Print the count of each event type.
```

### Step 5. Label the loop

```python
# Belongs here: code that walks the event list and tags each tool call as
# gather-context (read, list, search), act (write, edit, run), or verify (re-read,
# test, diff). Print the sequence as a single line of tags so the loop is visible.
```

Compare the sequence to the figure in the lecture. Where does the first *verify* appear?
Did the agent rerun the spellcheck on its own, or only because the task said "show me it
passes"? Try the task once more without that clause and compare the tag sequences.

### Step 6. Account for the window

```python
# Belongs here: code that sums tokens (or characters as a proxy) by the categories the
# captured transcript exposes: participant prompts, model text, tool calls, tool results,
# and per-turn token counts if the harness reports them. The system prompt and the
# tool descriptions are usually not in the transcript; say so in the table rather than
# estimating them. Mark which single tool result was the largest.
```

Return to the sheet from step 2. Which lines of the context file appear to have mattered?
Which tool result was the largest, and would a subagent have contained it? Which
categories could you not measure at all, and why does that matter for the cost column in
tutorial 4?

### Step 7. End a run three ways

```bash
# Belongs here: three short invocations. One that ends because the model reports
# completion. One that ends because the turn limit is reached (set it too low on
# purpose). One that a participant interrupts by hand. Capture the exit status and
# the last event of each.
```

## Check yourself

1. In your own words, what is the difference between a prompt and an agent run? One
   sentence each.
2. Point to the line in the transcript where the agent first *acted* rather than
   *gathered*. What tool was it?
3. Of the categories you could measure, which took the most tokens? Which categories
   could you not measure, and where do they sit in the loop on the lecture's code slide?
4. Name one line in `AGENTS.md` that you would delete, and say what would go wrong
   without one line you would keep.
5. Of the three ways the run ended, which would you rely on for a run nobody watches,
   and why is it not the first one?
