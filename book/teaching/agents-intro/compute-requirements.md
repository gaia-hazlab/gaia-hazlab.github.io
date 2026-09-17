---
title: Compute requirements for the agents tutorials
short_title: Compute requirements
description: Working document for the conversation with UW eScience on what each tutorial needs in API access, key management, environments, hardware, session length and per-participant cost. Every quantity is a TODO.
---

(agents-intro-compute-requirements)=

:::{note}
**Status.** Working document, opened 17 September 2026, for the conversation with UW
eScience about backend compute for the four [agents tutorials](tutorials/01-anatomy-of-an-agent.md).
No quantity on this page has been estimated; every one is a **TODO** to be filled from a
vendor price page, a measured run, or an eScience answer. Once filled, the cost rows
become budget figures. Decide before merging whether those rows stay on the public site
or move to the private coordination assets, as `project_coordination/README.md` requires
for budget material.
:::

## What is being asked of eScience

Four hands-on tutorials, each between one and two hours, each needing every participant
to run a coding agent against a real repository, and one tutorial also needing
a locally served open-weight model. The lecture that precedes them needs nothing beyond
a projector and one working session on the presenter's machine.

The questions for eScience, in the order they block us:

1. Can participants get a model API key or a hosted session without each one signing up
   with a vendor? Who holds the account, and how are spend caps set?
2. Is there a shared JupyterHub, a container platform, or per-participant cloud
   instances that can run the harness with a shell and git, at the size of the cohort?
3. For tutorial 4, is there a GPU node, or a CPU node large enough, to serve one
   open-weight model of the class the HazEvalHub prototype used, for the cohort at once?
4. What did the 17 June workshop use, and what did it cost? The event page
   [@escience2026codingagents] asked participants to bring a laptop with Chrome and a
   GitHub account, which suggests a browser-based environment; TODO confirm.

## Per-tutorial requirements

Every cell that is a quantity is TODO. Cells that are choices are marked as such.

### Tutorial 1. Anatomy of an agent

| Requirement | Value | Source when filled |
|---|---|---|
| Harness | TODO: choice (Claude Code is what the lecture uses) | course decision |
| Model | TODO: name and version string | course decision |
| API access | TODO: per-participant key, shared key behind a proxy, or hosted session | eScience |
| Key management | TODO: how issued, how revoked, expiry | eScience |
| Environment | TODO: choice (pixi as this repo uses, or a container) | course decision |
| CPU per participant | TODO | measured |
| Memory per participant | TODO | measured |
| GPU | none expected; TODO confirm | measured |
| Disk per participant | TODO (repository clone plus transcripts) | measured |
| Session length | TODO (estimated 90 min in the stub; confirm after a dry run) | dry run |
| Tokens per participant | TODO (one bounded session plus three short runs in step 7) | dry run |
| Cost per participant | TODO | tokens times vendor price on the day |
| Network | outbound to the model API; GitHub | course decision |

### Tutorial 2. Writing your first skill

| Requirement | Value | Source when filled |
|---|---|---|
| Harness and model | same as tutorial 1; TODO confirm | course decision |
| API access and keys | same as tutorial 1; TODO confirm | eScience |
| Environment | same as tutorial 1 plus git write access to a participant branch | course decision |
| CPU, memory, disk | TODO | measured |
| GPU | none expected; TODO confirm | measured |
| Session length | TODO (estimated 60 min in the stub) | dry run |
| Tokens per participant | TODO (roughly six short sessions: steps 4, 5, 6 and the second skill) | dry run |
| Cost per participant | TODO | tokens times vendor price on the day |
| Repository | TODO: choice (own fork of this repository, or a course repository) | course decision |

### Tutorial 3. Subagents and orchestration

| Requirement | Value | Source when filled |
|---|---|---|
| Harness and model | same as tutorial 1; TODO confirm | course decision |
| API access and keys | same as tutorial 1, plus a credential for the MCP server; TODO | eScience |
| MCP server | TODO: choice (GitHub server or web search), install method, credential scope | course decision |
| GitHub | a scratch repository per participant or per pair with issue-creation rights; TODO | course decision |
| Environment | same as tutorial 1 plus the MCP server runtime; TODO | course decision |
| CPU, memory, disk | TODO (two subagents in parallel per participant) | measured |
| GPU | none expected; TODO confirm | measured |
| Session length | TODO (estimated 120 min in the stub) | dry run |
| Tokens per participant | TODO (two subagent runs plus orchestrator plus two gated runs) | dry run |
| Cost per participant | TODO | tokens times vendor price on the day |
| Concurrency | TODO: subagents per participant times cohort size, against the API rate limit | eScience and vendor |

### Tutorial 4. Evaluating agent runs

| Requirement | Value | Source when filled |
|---|---|---|
| Private model | same as tutorial 1; TODO confirm | course decision |
| Open-weight model | TODO: name, parameter count, serving software | course decision |
| Serving hardware | TODO: GPU type and count, or CPU node size, to serve the cohort concurrently | eScience |
| Serving location | TODO: shared node, per-participant instance, or presenter-only | eScience |
| Runs per participant | TODO: N per condition times four conditions | course decision |
| Tokens per participant | TODO | dry run |
| Wall time per local run | TODO | measured on the chosen hardware |
| Cost per participant, private model | TODO | tokens times vendor price on the day |
| Cost per participant, local model | TODO | node time times rate, if charged |
| Storage for trajectories | TODO per participant, and where they live afterwards | eScience |
| Session length | TODO (estimated 120 min in the stub) | dry run |
| Price table | TODO: fetched from the vendor page on the day; not embedded in code | vendor |

## Cross-cutting

| Topic | Question | Owner |
|---|---|---|
| Spend cap | TODO: a hard cap per key or per account, and who gets the alert | eScience |
| Kill switch | TODO: how a runaway headless run is stopped when the presenter is not at the participant's machine | course decision |
| Data governance | TODO: what participants may paste into a private model; whether the course repository contains anything that must not leave UW | course decision |
| Retention | TODO: whether transcripts and trajectories are kept after the course, where, and who may read them | eScience |
| Accounts | GitHub account per participant (as in the eScience workshop); TODO whether a vendor account is also needed | course decision |
| Cohort size | TODO | course decision |
| Dry run | TODO: date of a full dry run of all four tutorials on the chosen platform, which fills most of the measured cells above | course decision |
