---
title: How GAIA works
short_title: How we work
description: Governance, measurement and openness for the GAIA collaboration. Public by design.
---

Most research projects keep their governance internal. We publish ours, for three reasons.
It makes our openness claim checkable rather than rhetorical. It is reusable — any project
running distributed cyberinfrastructure faces these same questions, and we would rather
hand over an answer than have everyone reinvent one. And a project willing to publish the
numbers it is missing has more credibility than one that publishes only its wins.

:::{note} Status
Version 0.1, drafted August 2026. Sections marked *proposed* are open for comment and are
ratified through the [decisions register](./decisions.md). Once ratified, the version here
is canonical.
:::

## The collaboration

GAIA — Geophysical AI-driven Integration & Assimilation — is a collaboration of the
**University of Washington**, the **University of Alaska Fairbanks** and the **EarthScope
Consortium**, supported by three linked NSF awards: **OAC-2608509, OAC-2608510 and
OAC-2608511**. Earlier and continuing support comes from the Fund for Future Science and
Technology and the Jerome and Linda Paros Geohazard Center.

### Acknowledgement — the agreed wording

Use this verbatim. All three award numbers are cited by every partner regardless of
institution: these are linked collaborative awards, not a prime with subawards, so no one
cites only their own.

> This material is based upon work supported by the U.S. National Science Foundation under
> Grant Nos. OAC-2608509, OAC-2608510 and OAC-2608511. Any opinions, findings, and
> conclusions or recommendations expressed in this material are those of the author(s) and
> do not necessarily reflect the views of the National Science Foundation.

Where the seed work or the Paros Center contributed, append: *"…, the Fund for Future
Science and Technology, and the Jerome and Linda Paros Geohazard Center."*

## 1. What we are accountable for

We told NSF what GAIA would produce and how adoption would be measured. Those numbers are
not aspirational language in a funded proposal; they are the scoreboard, and they are public.

**Delivery — what we ship** (cumulative unless noted)

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| D1 CI-template repos passing tests | 3 | 6 | 10 | 14 | 18 |
| D2 container images in the registry | 3 | 8 | 15 | 25 | 35 |
| D3 DOI-archived datasets | 5 | 10 | 20 | 50 | 100 |
| D4 versioned model cards | 1 | 5 | 8 | 12 | 15 |
| D5 JupyterBooks + hackweeks (per year) | 1+1 | 2+1 | 3+1 | 4+2 | 5+2 |

**Adoption — whether anyone uses it**

| | Y1 | Y2 | Y3 | Y4 | Y5 |
|---|---|---|---|---|---|
| M2 container pulls + dataset downloads (annual) | 500 | 2K | 5K | 10K | 20K |
| M2 derived agents (`IsDerivedFrom`) | 2 | 8 | 29 | 50 | 100 |
| M2 publications using GAIA | 0 | 3 | 10 | 20 | 30 |
| M3 unique institutions | 20 | 30 | 50 | 100 | 100 |
| M3 disciplines represented | 3 | 4 | 5 | 6 | 7 |
| M4 agent modes used in publications | >2 | >2 | >3 | >3 | >4 |
| M4 modalities per study (median) | >2 | >3 | >3 | >4 | >5 |
| M4 skill-adoption gain (post − pre) | +20% | +25% | +40% | +35% | +40% |

Nearly all of these are collected automatically, weekly, by the Metrics Observatory from
the GitHub, Zenodo, Hugging Face, container-registry and Slack APIs. Two — disciplines
represented and skill-adoption gain — come from surveys and are entered by a human. Every
value is published with its source.

## 2. Why we measure

Not for compliance. If the only purpose were the annual report we would collect these
numbers once a year, in April, under duress, and they would tell us nothing we could act on.

We measure weekly because the numbers are a steering instrument. Adoption metrics in
particular are the only honest signal that infrastructure is working: software that nobody
installs, datasets nobody downloads, and evaluation harnesses nobody submits to are
indistinguishable from software that does not exist. Counting them monthly rather than
annually is the difference between correcting course in Y2 and discovering the problem in
the final report.

Three rules keep the measurement honest.

**A metric that cannot be collected reads `n/a`, never zero.** A missing source and a real
zero mean completely different things, and conflating them is how dashboards start lying.

**Figures below target stay visible.** The dashboard shows what we are behind on, publicly,
in the same table as what we have met. This is the part most projects quietly omit, and it
is the part that makes the rest believable.

**We count few things.** Every metric above is one we committed to. We do not add
flattering ones.

## 3. What happens when a target is missed

A metric with no response attached is decoration. Ours escalate on a fixed ladder, so being
behind triggers something specific rather than a vague sense of unease.

| When | What happens |
|---|---|
| **Weekly** | The Observatory updates. Nobody acts. Data collection is not management. |
| **Monthly**, thrust sync | Figures below target are agenda item one. The accountable lead either names a corrective action with a date, or explicitly accepts the shortfall and says why. Both outcomes are recorded; silence is not an option. |
| **Quarterly**, PI coordination | Anything still behind after a quarter escalates. Three legitimate responses: reallocate effort, revise the target, or raise it with the programme officer. |
| **Annually**, NSF report | We report what happened, including what we missed and what we did about it. |

The quarterly step matters most. A target that is unreachable because the world changed
should be renegotiated openly and early, not quietly missed for four years and explained in
a final report.

:::{important}
Revising a target is legitimate. Leaving it unexamined is not.
:::

## 4. What we record, and why

Three kinds of record, each solving a specific failure.

**Decisions of record.** Every decision that constrains future choices gets a permanent
number (`GAIA-D-001`, …) in the [decisions register](./decisions.md), with its reasoning and
the alternatives rejected. Entries are never edited once active; a decision that changes is
superseded by a new numbered entry, and the old one stays visible.

*The failure this prevents:* eighteen months from now someone asks why we chose one format
over another. Without a record, either the debate reruns from scratch with people who were
not there, or someone senior answers from memory — and memory is often wrong. With it, the
newcomer reads the reasoning and can make a real argument that it has gone stale. Nothing
counts as decided until it has a number.

**Meeting notes.** Recorded with an AI notetaker, cleaned, attributed by role rather than
name except for shout-outs, and filed as Markdown in a private repository.

*The failure this prevents:* over five years, postdocs and students cycle through while the
PI is the only continuous thread. A project where all context lives in one person's head
makes that person both a bottleneck and a single point of failure.

**A weekly digest of Slack.** An agent reads an allowlisted set of channels and drafts a
topic-organised summary attributed by role; a team member corrects it, numbers any
decisions, and merges. Merging is the approval, and the approver is named on the digest.
Anyone can react `:offrecord:` to remove a message — and, on a thread parent, the whole
thread — before anything reads it. No explanation is asked for. Channels covering personnel,
budget, and general chat are never read.

*The failure this prevents:* Slack's free tier hides history past ninety days, which would
silently destroy the working record. Digesting weekly means the window never binds.

:::{warning} A limitation we state rather than hide
Role-level attribution is not anonymity in a team where one person holds each role. The real
protections are the off-record marker, summarising at the level of topic rather than who
said what, and human review before anything is published. We do not claim more than that.
:::

## 5. What is public, and what is not

**Public from day one:** the coordination repository, the roadmap, open issues, decision
records, cleaned meeting notes, the metrics dashboard including whatever is behind target,
and this document.

**Public and prepared:** a monthly *GAIA Open Update* — roughly twenty minutes, on YouTube.
Two five-minute lightning talks rotating through the whole team including PIs (one slide,
one result, one ask, with negative results explicitly welcome), one demo, and the month's
metric. Recording is opt-in per speaker.

**Internal:** working meetings, recorded only to the private notes repository. Personnel and
budget discussions are permanently off the record.

We do not livestream working meetings, and the reasoning is worth stating plainly because it
looks like a retreat from openness. Public recording suppresses the half-formed idea, the "I
don't understand this," and the negative result — which are exactly the conversations a
research project runs on. People stop thinking aloud and start performing, and the real
discussion migrates to private messages where nothing is preserved at all. That is a bad
trade for a modest signal. Openness belongs in artifacts and in curated video, not in
surveillance of the working day. Publishing a dashboard with a missed target on it is a
stronger claim than any raw recording, and it costs nothing but nerve.

## 6. What we do with all of it

The metrics and records feed five outputs, four of which are public.

The **monthly project-wide update** opens with the dashboard. The **quarterly newsletter**
to the announce list pastes its numbers directly from `latest.json`. The **annual NSF
report** is compiled by the Lead PI from decision records and auto-pulled metrics, and the
Observatory snapshot is archived with a DOI each August. The **public dashboard** updates
weekly whether or not anyone is watching.

And once a year we intend to publish an account of running the project this way —
DOI-archived, describing what the coordination agents did, where they failed, and what the
measurement actually changed about our decisions. Nobody in geoscience cyberinfrastructure
has written that paper, the data is a by-product of what we already collect, and it is the
most direct evidence we can offer for the claim that agentic project management is more than
a slogan.

## 7. Agents, and the rule that makes the claim checkable

GAIA uses agents to run GAIA: drafting meeting notes, digesting status, narrating metrics,
triaging issues. The governing rule is that **agents draft, humans approve, and the approval
is visible.** Every agent-generated artifact carries a footer naming the model, the date, and
the person who signed off.

Without that footer, any claim about agentic project management is unfalsifiable. With it, a
reader can check. We also intend to score our own coordination agents in the same evaluation
harness we use for scientific agents — on accuracy, cost, and reproducibility — because a
project asserting that this approach works should be willing to publish how well it actually
works, including where it does not.

Nothing outward-facing ships without a named human approver, and no agent output containing a
citation or DOI is published without that reference being checked.

## 8. Changing any of this

This document is ratified by the team and amended the same way anything else changes: a
proposal, a comment window, and a numbered decision that supersedes what came before. The
current version and its full history are in the
[repository](https://github.com/gaia-hazlab/gaia-hazlab.github.io/tree/main/book/governance).

Related pages: [the organisation and how work joins it](./organization.md) ·
[decisions of record](./decisions.md) · [FAQ](./faq.md).

*Want to reuse this for your own project? Please do — open an issue and tell us what needed
changing. We would rather it be copied than admired.*
