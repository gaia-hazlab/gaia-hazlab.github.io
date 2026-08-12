# Kickoff call — agenda queue

> **Where items go when they need a human decision.** Anything the site or a plan marks
> "in progress" because it needs a person rather than a task lands here, so the kickoff call has
> a real agenda instead of a status round.
>
> This lives in `project_coordination/` rather than a Google Doc because
> [`GAIA-D-002`](../book/governance/decisions.md) makes GitHub the durable system of record and
> Slack the ephemeral one — an agenda that produces decisions of record belongs on the durable
> side. Mirror it to Google for the meeting if that is easier to read in the room; the copy here
> is the one that counts.

**Kickoff date:** *to be fixed — two decisions in the register carry `2026-08-__` placeholders
that this date fills.*

## How to use this

Add an item when a plan needs a decision you cannot make alone. Each item names what is being
decided, who needs to be in the room, and what is blocked until it settles. After the call, the
decision goes to [`decisions.md`](../book/governance/decisions.md) as a numbered entry and comes
off this list.

Nothing in the decisions register ratifies before this call. That is correct and deliberate — see
[08 §W8](08-site-remediation-plan.md).

---

## A. Ratifications

The register has four standing decisions plus one new, all `proposed`. Seven of ten reviewers
noted that nothing has ever been ratified and discounted the governance writing because of it.

| # | Decision | Notes |
|---|---|---|
| GAIA-D-001 | Funding acknowledgment text and mechanics | The faculty reviewer found the front page violates it |
| GAIA-D-002 | System of record: Slack ephemeral, GitHub durable | — |
| GAIA-D-003 | Meeting schedule and the sunset rule | Fill the placeholder date |
| GAIA-D-004 | Project Google identity | — |
| **GAIA-D-005** | **Who the landing page is for** | New. Climate tech, framed as extreme weather and natural disasters ([08 §2](08-site-remediation-plan.md)) |

Also pending and unnumbered: co-authorship policy, openness/recording policy. The FAQ currently
describes the authorship policy as a numbered decision; the register says it is not yet numbered.
One of them is wrong and a reviewer caught it.

## B. Decisions needed

### B1. Commercial use — resolve the wording *(blocks W2)*

"No commercial use yet, but everything open source" cannot both be true: permissive licences
grant commercial use irrevocably. [08 §8.1](08-site-remediation-plan.md) proposes wording that
says we neither seek nor restrict it. **Confirm that reading, or accept that withholding
commercial rights means relicensing every repository and dropping the open-source claim.**

Needs: Lead PI. Blocks: the licensing page rewrite, and the climate-risk CTO's blocker.

### B2. Who owns HazEvalHub *(blocks W9 / all of [09](09-hazevalhub-ctf-plan.md))*

The role is "CI / eval leads" and unfilled. This is the project's largest claim-versus-artefact
gap and the source of two review blockers.

### B3. Labelling campaign — people and time *(critical path for HazEvalHub v0.5)*

The temporally-disjoint test set needs at least two independent annotators per event plus
adjudication. This is the long pole in the entire eval plan. Is there student time?

### B4. External entry before publishing a GAIA result?

AI2 and the Kutz group are named collaborators. One external submission at launch is worth more
than three internal ones.

### B5. Year-six holder

No institutional answer yet; the working assumption is a future research centre. The question is
whether to publish that as an open question — [08 §8.2](08-site-remediation-plan.md) argues yes,
because DOI archiving makes artefacts survive regardless of who ends up holding them.

---

*Resolved before the call, kept for the record:*

- ~~*SeisSCOPED reuse permission*~~ — `SeisSCOPED/community-metrics` now carries MIT
  (`LICENSE.md`, confirmed 2026-08-12). W5 is unblocked; retain the upstream copyright notice
  when vendoring.
- ~~*Custody of the QuakeXNet hidden labels*~~ — handled inside the eval team, not a kickoff
  item. The separability principle still stands ([09 §2.1](09-hazevalhub-ctf-plan.md)).

## C. Facts only a person holds

These block the W1 sweep. Each is a page that currently claims something in the present tense
where nobody outside the team can tell whether it is true. Marked "in progress" on the site until
answered.

| Question | Page |
|---|---|
| Does any part of the `gaia_hazlab` Python API exist? | ModelHub, HazEvalHub |
| Which models have a result that could be published against a baseline? | ModelHub, front page |
| What is the real lead time for the landslide nowcast? Currently "hours/days" in a draft | Pillar 3, front page |
| Which repositories are genuinely maintained versus parked? | Research Software |
| Where in the country does this work, as a sentence for the landing page? | Front page |
| What should the landing-page counters count, if not "∞ Sensors"? | Front page |

The second and third gate the front page — the industry reviewers' blocker was the absence of a
number, and the CEO's test is whether a sentence can be forwarded to a VP of engineering without
a hole in it.

## D. Standing

- Review the persona round: [`review-logs/2026-08-12/_synthesis.md`](../review-logs/2026-08-12/_synthesis.md).
  129 findings, 13 blockers, none about design.
- Agree when to re-run the ten personas ([08 §7](08-site-remediation-plan.md)). The number to
  watch is the 17-point spread between reviewers who read and reviewers who verify, not the mean.
