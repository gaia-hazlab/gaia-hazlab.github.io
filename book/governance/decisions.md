---
title: Decisions of record
short_title: Decisions
description: Every GAIA decision that constrains later choices, with its reasoning and the alternatives rejected. Numbers are permanent; entries are superseded, never edited.
---

NSF awards OAC-2608509, OAC-2608510 and OAC-2608511 (University of Washington, University
of Alaska Fairbanks, EarthScope Consortium). This file is the project's memory of **what
was decided and why**.

Rules:

- Nothing counts as decided until it has a number here. If it lives only in a Doc,
  a Slack thread, or someone's memory of a call, it is still a proposal.
- Numbers are permanent and never reused. Entries are **never edited after they go
  `active`** — to change a decision, write a new entry that supersedes the old one and
  set the old entry's status to `superseded by GAIA-D-nnn`. The history stays honest.
- Keep entries short. Decision, why, what was rejected, what it obligates. The long
  version belongs in the linked discussion, not here.
- Where a decision produces a document (the [charter](./how-we-work.md), a policy page), this file records
  *that it was ratified* and links to it. It does not duplicate its text.

**Status vocabulary:** `proposed` (drafted, not yet decided) · `active` (in force) ·
`superseded by GAIA-D-nnn` · `withdrawn` (dropped without replacement).

**To add an entry:** copy the template at the bottom, take the next number, add a row to
the index, open a PR. Decisions taken in a meeting are logged by whoever ran it, within
one working day.

---

## Index

| # | Decision | Status | Date |
|---|---|---|---|
| [001](#gaia-d-001) | Funding acknowledgment text and mechanics | proposed | — |
| [002](#gaia-d-002) | System of record: Slack ephemeral, GitHub durable | proposed | — |
| [003](#gaia-d-003) | Meeting schedule and the sunset rule | proposed | — |
| [004](#gaia-d-004) | Project Google identity | proposed | — |

Pending, not yet numbered — co-authorship policy and the openness/recording policy go to
a comment window after the kickoff and are numbered when they ratify at the September
project-wide call.

---

(gaia-d-001)=
## GAIA-D-001 — Funding acknowledgment

**Date:** — · **Decided at:** kickoff call, 2026-08-__ · **Status:** proposed

All GAIA outputs carry one canonical acknowledgment, citing **all three** linked awards
regardless of the author's institution:

> This material is based upon work supported by the U.S. National Science Foundation
> under Grant Nos. OAC-2608509, OAC-2608510 and OAC-2608511. Any opinions, findings, and
> conclusions or recommendations expressed in this material are those of the author(s)
> and do not necessarily reflect the views of the National Science Foundation.

Where the seed work or the Paros Center contributed, the FFST and Jerome and Linda Paros
Geohazard Center sentence is appended.

**Why:** GAIA is three linked collaborative awards — UW, UAF and EarthScope each hold
their own — not a prime with subawards, so no partner's award number is the "main" one.
Acknowledgment is also a tracked metric (M4, via CrossRef/OpenAlex): if it takes more
than a few seconds, the metric under-reports real usage and the annual report understates
the project. One canonical block removes the friction and stops people composing their own.

**Rejected:** citing only the author's own institutional award — it fragments the citation
string the metrics search on, and under-credits the partners.

**Obligates:** `CITATION.cff` in every repo · all three award numbers as required fields
in the provenance YAML schema · copy-paste block on the website.

**Open:** which number belongs to which institution is confirmed for UW (2608509) and
UAF (2608510); EarthScope's (2608511) is inferred by elimination and should be confirmed
against their award notice before it appears in any per-institution table.

**Discussion:** [kickoff briefs, Brief 1](https://docs.google.com/document/d/1kcy5L6VTg18lKTgfBw58_ofBKRu4YMuC6mEI7Q1Nq-8/edit)

---

(gaia-d-002)=
## GAIA-D-002 — System of record (Slack and GitHub)

**Date:** — · **Decided at:** kickoff call, 2026-08-__ · **Status:** proposed

Slack is ephemeral working memory; GitHub is the durable record. A weekly agent drafts a
role-attributed digest from an allowlist of channels; a human corrects it, numbers any
decisions, and merges — **merging is the approval**. An `:offrecord:` reaction removes a
message before anything reads it, and on a thread parent removes the whole thread, with
no explanation asked. `#general`, `#random`, and anything touching personnel or budget
are never digested. Redacted verbatim source is retained in the private
`gaia-hazlab/notes` repo. We do not purchase Slack Pro.

**Why:** the free tier hides history past 90 days, which would silently destroy the
`#weekly-status` archive the coordination plan depends on. Digesting weekly means the
window never binds. A verbatim Slack archive is also mostly a liability — searchable,
quotable, full of half-formed thinking never meant as a position — whereas a curated
role-level digest is an asset.

**Rejected:** buying Slack Pro (recurring cost, and preserves the wrong artifact) ·
moving all status into GitHub Discussions (loses the low-friction chat people
actually use).

**Named limitation, stated to the team:** role attribution is not anonymity where one
person holds each role. The real protections are the off-record valve, topic-level
summarising, and human review before merge. We do not claim more than that.

**Obligates:** private `gaia-hazlab/notes` repo · internal Slack app (never distributed,
or it drops to the 1 req/min tier) · `:offrecord:` emoji created and the rule in every
digested channel topic.

**Open:** final channel allowlist · who reviews the Monday PR (proposal: rotate among leads).

**Review:** 6-week pilot, reviewed at the October project-wide call.

**Discussion:** [kickoff briefs, Brief 2](https://docs.google.com/document/d/1kcy5L6VTg18lKTgfBw58_ofBKRu4YMuC6mEI7Q1Nq-8/edit)

---

(gaia-d-003)=
## GAIA-D-003 — Meeting schedule

**Date:** — · **Decided at:** kickoff call, 2026-08-__ · **Status:** proposed

Monthly cycle: thrust sync in week 3 (where decisions of record are taken), project-wide
update in week 4, PI coordination in week 1 capped at 30 minutes. Optional: a
student/postdoc forum owned by a postdoc rather than a PI, and biweekly office hours.
Async status in `#weekly-status` weekly for anyone above 25% FTE, monthly otherwise.

**Sunset rule:** any standing meeting that produces no decision or artifact for three
consecutive months is cut at the next review.

**Why:** the management plan's five-meeting monthly cycle is more standing meetings than
a four-institution team across three time zones sustains; the usual failure is quiet
decay around month four. Naming two load-bearing meetings and writing the sunset rule now
makes cancelling later an act of hygiene rather than an admission of failure. The forum
is postdoc-owned because PI-run forums become seminars where nobody admits confusion.

**Rejected:** keeping all five as mandatory.

**Obligates:** first thrust sync scheduled within two weeks of kickoff · slots chosen to
work in AKDT, PT and MT · a named coordinator for the first rotation.

**Discussion:** [kickoff briefs, Brief 3](https://docs.google.com/document/d/1kcy5L6VTg18lKTgfBw58_ofBKRu4YMuC6mEI7Q1Nq-8/edit)

---

(gaia-d-004)=
## GAIA-D-004 — Project Google identity

**Date:** — · **Decided at:** kickoff call, 2026-08-__ · **Status:** proposed

The project Google identity is **`gaia.hazlab@gmail.com`**. Coordination docs referencing
`gaia.ci@gmail.com` are updated to match, and that address is parked with a forward if it
exists. Credentials live in a password manager shared by the Lead PI and one other
person, never in git.

**Why:** two identities split the Calendar, the shared Sheet, and Drive ownership within
a semester. `gaia.hazlab@` already owns the intake form and the Drive folder the team has
touched, so switching would orphan live artifacts and force a re-send.

**Rejected:** `gaia.ci@gmail.com` — cleaner name, but nothing behind it yet.

**Obligates:** docs PR within a week · Calendar and Drive ownership confirmed on
`gaia.hazlab@` · credential handoff recorded off git.

**Discussion:** [kickoff briefs, Brief 4](https://docs.google.com/document/d/1kcy5L6VTg18lKTgfBw58_ofBKRu4YMuC6mEI7Q1Nq-8/edit)

---

## Template

```markdown
## GAIA-D-nnn — Short title

**Date:** YYYY-MM-DD · **Decided at:** <meeting> · **Status:** active

What was decided, in two or three sentences, in the present tense.

**Why:** the reasoning someone will need in two years when they ask why.
**Rejected:** the alternatives considered, and briefly why not.
**Obligates:** concrete follow-up work this decision creates.
**Open:** anything deliberately left unanswered.
**Discussion:** link to the Doc, issue, or notes entry.
```
