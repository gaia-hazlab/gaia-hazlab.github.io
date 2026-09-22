---
title: "Tutorial 2: Writing your first skill"
short_title: 2. Your first skill
description: Package one procedure the group repeats into a skill, make it trigger on its own, test it, and version it in the repository.
---

(tutorial-writing-your-first-skill)=

:::{note}
**Status.** Stub. Objectives, prerequisites, exercise and self-check are drafted; the
code cells are empty and carry a comment saying what belongs in each. To be completed
with UW eScience. Compute needs are tracked in
[compute requirements](../compute-requirements.md). Companion to the
[lecture](../agents-intro.md), the writing-your-own segment.
:::

## Learning objectives

After this tutorial a participant can:

1. Describe the parts of a skill (a folder, a `SKILL.md` with name and description in the
   front matter, instructions below, optional reference files) and say what the harness
   reads at startup versus on use.
2. Write a description that makes the skill trigger on the right requests and not on
   others.
3. Write instructions that read their facts from a source of truth rather than embedding
   them.
4. Test a skill by invoking it by name and by letting it trigger unprompted, and tell the
   two results apart.
5. Commit a skill to a repository in the layout this project uses (`.claude/skills/`) with
   a line in the skills README.

## Prerequisites

- [Tutorial 1](01-anatomy-of-an-agent.md), or the equivalent: a working harness and one
  captured session.
- A clone of this repository on a branch of your own.
- The skill format as this repository documents it, in `.claude/skills/README.md`, and
  the existing `plain-voice` skill as a reference implementation.
- Read access to the page whose content the skill will use:
  [How we work](../../../governance/how-we-work.md), acknowledgement section.

## Estimated duration

Sixty minutes, estimated as: ten minutes reading the existing skill, thirty writing and
testing, twenty on the second skill and discussion. TODO: revise after the first run
with eScience.

## Worked exercise

The skill built here is the one from the lecture: insert the agreed NSF acknowledgement
wording, verbatim, wherever a page or document needs a funding statement. It is small,
its correctness is checkable by string comparison, and the rule it enforces is already
written down in the governance page and in `AGENTS.md`.

### Step 1. Read a skill that already works

Open `.claude/skills/plain-voice/SKILL.md`. Note the front matter fields, the length of
the description, and how the body is organised. Note what it does not contain: no code,
no tool definitions, no model settings.

### Step 2. Write the description first

The description is the only part of the skill that is in the model's window before the
skill is used, and it is there on every call, fired or not. The harness does not match
it; the model reads it and decides. Draft it in one or two sentences that name the task
in the words a colleague would use: acknowledgement, funding statement, NSF award, grant
numbers. Longer descriptions with more trigger phrases fire more reliably and cost more
per call; `plain-voice` in this repository was trimmed from about 150 words to about 60
for exactly that reason, and its body stayed at about 2300.

```markdown
<!-- Belongs here: the SKILL.md front matter. name: nsf-acknowledgement.
     description: the one- or two-sentence trigger text drafted above. -->
```

### Step 3. Write the instructions

Three instructions, imperative and specific. Read the wording from
`book/governance/how-we-work.md` at the time of use, so there is one source of truth.
Insert it verbatim, all three award numbers included. If the seed grant or the Paros
Center contributed, append the second sentence from the same page.

```markdown
<!-- Belongs here: the SKILL.md body. Three numbered instructions as above, plus one
     line saying what the skill must never do (paraphrase the wording, omit an award,
     invent an award number). -->
```

### Step 4. Test by name

```bash
# Belongs here: a fresh session that invokes the skill by name against a scratch copy
# of book/chapters/mt-rainier.md, then a diff of the result against the original.
# Then a string comparison of the inserted paragraph against the governance page.
```

### Step 5. Test unprompted

```bash
# Belongs here: a fresh session that asks, without naming the skill, to "add a
# funding acknowledgement" to the same scratch page. Capture whether the skill loaded:
# in the transcript it appears as a tool call that reads the SKILL.md body, and the
# harness usually prints the skill name when it loads. If it did not, edit the
# description and repeat. Keep each description you tried.
```

### Step 6. Break it on purpose

On your own branch, change one award number in `book/governance/how-we-work.md` itself
(the skill reads that path, so a scratch copy would change nothing) and run the skill
again. Does the skill insert the changed wording or the original? It should insert
whatever the page says, because the page is the source of truth. If it inserted the
original, the wording leaked into the skill body; fix that. Then revert the page.

### Step 7. Version it

```bash
# Belongs here: git commands to add the skill folder and a one-line entry in
# .claude/skills/README.md on your branch, with a commit message that discloses agent
# assistance per CONTRIBUTING.md.
```

### Step 8. A second skill of your own

Choose one procedure your group repeats and that has a written rule somewhere: a data
citation format, a figure-caption convention, a check that a notebook clears its outputs.
Repeat steps 2 to 5. Bring the description that triggered and the ones that did not to
the discussion.

```markdown
<!-- Belongs here: the participant's second SKILL.md. -->
```

## Check yourself

1. What does the harness read from a skill at startup, and what does it read only when
   the skill is used? Why does that make description length matter more than body length?
2. Your skill reads the acknowledgement from a page instead of storing it. Name one
   thing that becomes possible because of that and one thing that becomes riskier.
3. Give one request that should trigger the skill and one that should not, and check
   your description against both.
4. A skill and a subagent can both encapsulate a procedure. What is the difference in
   where each runs, and when would you choose the subagent?
5. What would a test for this skill look like if it had to run in CI without a model?
   (Hint: the skill's output is a paragraph and the source of truth is a page; a test
   needs no model to compare two strings.)
