---
title: "Tutorial 3: Subagents and orchestration"
short_title: 3. Subagents and orchestration
description: Split one task across subagents with separate context windows, connect an external tool server through MCP, and merge the results under a permission gate.
---

(tutorial-subagents-and-orchestration)=

:::{note}
**Status.** Stub. Objectives, prerequisites, exercise and self-check are drafted; the
code cells are empty and carry a comment saying what belongs in each. To be completed
with UW eScience. Compute needs are tracked in
[compute requirements](../compute-requirements.md). Companion to the
[lecture](../lecture.md), segments 6 to 14 and 33 to 40.
:::

## Learning objectives

After this tutorial a participant can:

1. Say when a task should be split across subagents and when it should not, in terms of
   context-window isolation, parallelism, and the cost of the merge.
2. Define a subagent in the layout this repository uses (`.claude/agents/`), with its own
   instructions and tool allow-list.
3. Run several subagents on independent inputs and merge their reports without losing
   provenance of which subagent said what.
4. Connect one external tool server through the Model Context Protocol (MCP) and explain
   what the agent gains and what new party it now trusts.
5. Put a permission gate between the orchestrator and any outward-facing action, and
   show it working.

## Prerequisites

- [Tutorial 1](01-anatomy-of-an-agent.md) and [Tutorial 2](02-writing-your-first-skill.md).
- The ten persona reviewers in `.claude/agents/gaia-review-*.md` and one dated example
  of their output under `review-logs/`.
- A GitHub account with permission to open issues on a scratch repository. TODO: decide
  whether participants use their own forks or a course repository.
- The harness's *permission mode*: the setting that decides which tool calls run without
  asking, which pause for a yes, and which are refused. Step 6 depends on it.
- TODO: which MCP server the exercise will use (a GitHub server is the natural choice
  for this repository; a web-search server is the alternative), how it is installed, and
  what credentials it needs. See [compute requirements](../compute-requirements.md).

## Estimated duration

Two hours, estimated as: twenty minutes reading a persona agent, forty on the fan-out
and merge, forty on MCP, twenty on the permission gate and discussion. TODO: revise after
the first run with eScience.

## Worked exercise

The exercise uses the persona review machinery this repository already runs. Two
reviewers read the same page in isolation, an orchestrator merges their findings, and
the merged result is turned into a GitHub issue through an MCP server, behind a
permission prompt.

### Step 1. Read a subagent definition

Open one file under `.claude/agents/`, for example the PhD-student persona. Note the
front matter (name, description, tools allowed), the instructions, and where the output
is to be filed. Compare it to a skill from tutorial 2: the subagent has its own tool
list and its own context; the skill has neither.

### Step 2. Define a scratch subagent

Write a new agent file that reviews a single book page for one thing only: claims that
carry no source. Keep the tools to read and search; no write, no shell.

```markdown
<!-- Belongs here: the new agent file under .claude/agents/, front matter with name,
     description, and the read-only tool list, then the instructions and the output
     format (a Markdown list of claim, line number, and what source would settle it). -->
```

### Step 3. Fan out

Run the scratch subagent and one existing persona on the same page, in parallel, from an
orchestrating session.

```bash
# Belongs here: the orchestrator invocation that launches both subagents on
# book/chapters/gaia-agentic.md (a short, draft page with empty sections), waits, and
# collects both reports. Note: the persona files send reviewers to the live site; for
# this exercise the invocation must override that with the single page. Capture each
# subagent's report to its own file with the subagent's name in the filename.
```

### Step 4. Merge without losing provenance

```python
# Belongs here: code that reads the two report files and produces one merged list of
# findings, each tagged with the subagent it came from, de-duplicated where both
# reviewers flagged the same line. Print the merged list and the counts per source.
# Also: keep only the fields the report format defines (claim, line, source); drop or
# quarantine any free text, especially sentences addressed to "you" or to the
# orchestrator. A subagent's report re-enters the parent as a tool result, which is
# the injection path step 7 asks about.
```

Look at the merged list. Did the orchestrator's own context window need either report in
full, or only the merged list? That difference is the argument for subagents.

### Step 5. Connect an MCP server

```json
// Belongs here: the harness configuration block that registers one MCP server (TODO:
// which one) with its command, arguments, and the environment variable that carries
// its credential. The credential itself must not appear in this file.
```

```bash
# Belongs here: the command that lists the tools the server advertises, so participants
# can see the name, description, and argument schema of each. Count how many tool
# descriptions were added to the context.
```

### Step 6. Gate the outward-facing action

Ask the orchestrator to open one GitHub issue on the scratch repository containing the
merged findings. The harness must ask before the issue is created.

```bash
# Belongs here: the orchestrator run with the permission mode set so that any tool
# call that creates or modifies something on GitHub prompts. Capture the prompt text
# and the participant's answer. Run once answering no, once answering yes. Verify with
# the GitHub CLI that exactly one issue exists afterwards.
```

### Step 7. Remove the gate and think about it

Do not run this step. Read the configuration that would remove the gate, and write down
what the orchestrator could then do with the credential from step 5 if a subagent's
report contained an instruction addressed to the orchestrator. This is the injection
problem, and the merge in step 4 is where it enters.

## Check yourself

1. Give one task where subagents cost more than they save. What is the cost that
   dominates?
2. What comes back from a subagent to its parent, and what does not? Why does that make
   the subagent's output format part of its definition?
3. After step 5, how many tool descriptions did the MCP server add to the context? Where
   in the window do they sit, and are they paid for on every turn?
4. In step 6, what exactly did the permission prompt show you? Was it enough to decide?
5. In step 7, name the sentence in a subagent report that would be most dangerous to the
   orchestrator, and say what in the merge step should strip or quarantine it.
