# Site & Book Remediation Plan

> **What to fix on the website and book, in what order, based on evidence rather than taste.**
> Derived from the ten-persona review round of 2026-08-12
> ([`review-logs/2026-08-12/`](../review-logs/2026-08-12/), synthesis
> [here](../review-logs/2026-08-12/_synthesis.md)): 129 findings, 13 blockers, ten reviewers run
> independently across academia, philanthropy and industry.
>
> This is the **remediation** plan for what exists. The **expansion** plan for Alaska, geodesy
> and SAR is [02-website-evolution.md](02-website-evolution.md) and is not affected by this
> document, except that §2 below should be settled before new pages are written into the same
> structure.

## 1. The finding that organises everything else

The reviewers' scores rank almost perfectly by how much weight each persona puts on
verification. The program officer, who came to read, scored 66. The geospatial AI CTO and the
research software engineer, who came to check whether something could be used, scored 49 and 50.

**The writing is ahead of the artefacts.** Not one of the thirteen blockers concerns design,
prose, navigation, or accessibility. Five concern credibility, three governance, three
reproducibility. The recent plain-voice pass improved the register of a page whose central
sentence the faculty reviewer then named as the one that would be embarrassing in three years —
because the problem with it was never the register. It was the tense.

That reframes the work. This is not a website redesign. It is a campaign to make the claims and
the artefacts agree, and the cheapest direction to close that gap is usually **downward** — say
less, in the right tense — not upward.

## 2. The decision that gates the rest — settled

Four reviewers wanted four different front pages, and the reviews are explicit that adding all
four is the failure mode.

**Decided (2026-08-12): the landing page is for the climate-technology reader** — the CTO and
CEO personas. The other audiences get a visible second door. The technical academic readers all
self-navigated (the RSE went straight to GitHub, the CTOs to the licences, the faculty reviewer
to the claims), so costing them one click is cheap; the industry readers stopped at the front
page and did not recover.

### 2.1 Language constraint

Write the proposition as **extreme weather events and natural disasters**, not as climate
change. The subject matter is unchanged — atmospheric rivers, landslides, liquefaction, floods,
post-fire debris flows — and the framing is chosen to keep the page readable by audiences who
would bounce off climate framing. Applies to the landing page, `funding.html`, and the problem
statement. It does **not** apply to the science chapters, where the literature's own vocabulary
should stand.

### 2.2 What this audience asked for, specifically

Straight from the two industry reviews — this is now the front page's specification:

| Requirement | Raised as |
|---|---|
| One performance number, against a baseline | BLOCKER (both) |
| Named, contactable people | BLOCKER (CEO) |
| Where in the country this works — the landing page never says | MAJOR |
| A lead time, stated as a number rather than "hours/days" | MAJOR |
| Something addressed to a company at all | MAJOR |
| A contact route that is not an unnamed footer mailto | MAJOR |

The CEO's own summary of the failure is the test to design against: the sentence he would
forward to his VP of engineering has a hole where the number goes, so the forward does not
happen. **W3 is therefore a prerequisite for the front page, not a parallel workstream.**

→ Record as `GAIA-D-005 — who the landing page is for`, **status: proposed**, ratified at the
kickoff call (see §5 on why nothing ratifies before then).

## 3. Workstreams

Ordered by blocker weight, not by effort.

### W1 — Make the tense true *(credibility · 8 personas · no blockers resolved without it)*

The largest single category. ModelHub "holds pre-trained weights"; HazEvalHub "holds the
metrics, the validation protocols, and the held-out data"; both document a `gaia_hazlab` Python
API that exists in neither PyPI nor the organisation.

**Scope: every page, not only the hubs.** Four surfaces drew no findings from any of the ten
reviewers — the hazard chapters, `ocean-atmosphere-coupling`, and Pillars 2 and 3 — which means
nobody's path reached them, not that they are clean. A real reader arriving from a search engine
has no such path dependence.

- Sweep every page for present-tense claims about capabilities that do not exist, and move each
  to either a dated future tense with a named owner, or a `draft` admonition.
- Where a claim needs a person to confirm whether the thing exists, mark it **"in progress"**
  and add the item to [`kickoff-agenda.md`](kickoff-agenda.md) rather than guessing. "In
  progress" with an owner is honest; a present-tense claim awaiting verification is not.
- The `gaia_hazlab` code examples either become real or become clearly labelled as illustrative
  design sketches. The site-wide banner is not a substitute — two reviewers read it as
  discrediting the pages they would otherwise have trusted most.
- Retire the banner once the pages no longer need it.

Owner: Website lead. **Do not delegate this to a proofreading pass** — each sentence needs
someone who knows whether the thing exists. That is why the "in progress" escape hatch exists.

### W2 — Licences and citation *(governance · 8 personas · resolves blockers 1, 2, 3)*

Verified 2026-08-12: 9 of 26 public repositories carry no LICENSE file, 14 of 33 including
private, while several READMEs and the site footer assert MIT. The climate-risk CTO's estimate
was that about a week of file-writing flips his answer from "cannot clear this" to "can".

**Delivery mechanism: one pull request per repository, not a direct push.** Each PR adds
`LICENSE` and `CITATION.cff` together and tags the repository owner as reviewer. Owners choose
their own licence and confirm their citation metadata; nobody has a licence chosen for them by
someone else. The PR body states the project rule, links the
[licensing page](../book/governance/licensing.md), and says what happens if the PR is not
actioned.

Target repositories (unlicensed and public): `.github`, `awesome-gaia`,
`da-seis-groundfailure`, `gaia-data-downloaders`, `gaia-translate-QA`, `landlab-debrisflow`,
`mt-rainier-smart-sensing`, `seis-hydro-2-sed`, `shred-landlab-prototypes`.

The `CITATION.cff` PRs also go to repositories that already have a licence but no citation file
— 31 of 33 repositories lack one, and the FAQ currently claims all of them have it.

Also in this workstream:

- Resolve the one copyleft repository against the project's own stated rule, or amend the rule.
- Fix [`faq.md:42`](../book/governance/faq.md) — it claims every repository ships a
  `CITATION.cff`; two of 33 do. Correct the sentence **now**, independently of the PR campaign,
  and let it become true later. Three reviewers checked this claim; one noted it was the only
  claim he chose to verify.

Owner: CI infra lead opens the PRs; each repository owner reviews their own.

### W2b — Data licensing: propagate, do not author *(replaces the earlier data-terms item)*

We do not write a GAIA data licence. The position to state on the DataHub page is narrower and
more defensible:

1. **GAIA uses open-access data only.** That is the acquisition rule, not a disclaimer.
2. **Upstream data licences and terms propagate through the workflow** and are carried in each
   product's provenance record, alongside the source, sensor, resolution and uncertainty fields
   the [DataHub Integration Guide](../book/chapters/datahub-integration-guide.md) already
   specifies.
3. A derived product therefore inherits and names its upstream terms rather than being
   relicensed by us.

This answers the climate-risk CTO's second blocker — he needed redistribution terms he could
hand to counsel — without the project taking on a licensing role it should not hold. It also
retires the "free for academic use" line, which was a Synoptic API-key condition being read as
a statement about GAIA's data.

**Engineering consequence:** the provenance record needs a licence field, and it needs to be
populated at ingestion rather than backfilled. Fold into the Integration Guide's provenance
standard.

Owner: DataHub lead.

### W3 — Publish one number *(credibility · 5 personas · resolves blockers 4, 5, 6)*

No performance figure exists anywhere on the site. The CEO stopped over it; both CTOs asked for
a trivial baseline and found none; the evaluation officer found no baseline against any of the
thirteen committed targets.

- Pick **one** model with a result and publish it against a named baseline, with the date, the
  data split, and the metric. One honest number outranks a benchmarking framework described in
  the abstract.
- Give every published metric a baseline value and a measurement date.
- Exclude the project's own use from adoption metrics, or state that it is included. The
  evaluation officer's signature answer was that all thirteen targets can currently be hit using
  only the project's own people and artefacts.

Owner: Metrics lead + the model owner for whichever result goes first.

### W4 — Put people on the people page *(clarity · 5 personas · resolves blockers 7, 8)*

Verified: `people.html` returns 1,005 characters of visible text with JavaScript off and
contains no personal name. The roster is injected client-side, so it is invisible to a reader
without JS, to a crawler, and to anyone reading a cached copy.

- Server-render the roster at build time, or inline it as static HTML. This is the single
  highest-leverage hour on the list: it clears two blockers raised from opposite ends.
- **Sort alphabetically.** No ranking by seniority — the order should not encode hierarchy.
- **Add "CSSI co-PI" to the title of each co-PI.** The award structure is currently invisible on
  the page, and the faculty reviewer separately noted the front page cannot count its own team.
- Name at least one contactable person who is not a PI. The PhD student's entire conversion
  path is emailing a graduate student, and he could not find one.
- Fix the 404 team photograph and the 404 favicon.

Owner: Website lead.

### W5 — Metrics Observatory: MVP by refactoring SeisSCOPED *(5 personas · resolves blocker 6)*

`https://gaia-hazlab.github.io/metrics-observatory/` returns 404 and is linked from the book's
own table of contents at [`myst.yml:65`](../myst.yml). The governance pages rest on public
accountability against thirteen metrics; no metric value is published anywhere.

**Decided: build the MVP by refactoring [`SeisSCOPED/community-metrics`](https://github.com/SeisSCOPED/community-metrics)**
rather than designing from scratch. It already carries the shape we need — a `metrics/`
collection layer, a `dashboard/`, `scripts/`, and a static `index.html` that publishes to Pages,
which fits the constraint in [02 §6](02-website-evolution.md) that the surface stay static and
consume generated JSON.

Reuse is cleared: `SeisSCOPED/community-metrics` carries **MIT** (`LICENSE.md`, confirmed
2026-08-12). Retain the upstream copyright notice when vendoring — that is MIT's one obligation,
and getting it wrong on the repository we hold up as a licensing example would be avoidable.

Sequence:

1. Fork or vendor into `gaia-hazlab/metrics-observatory`, licensed per our own rule, upstream
   notice retained and SeisSCOPED credited in the README.
2. Repoint collection at the GAIA org, and map its metric set onto the D1–D5 / M1–M4 definitions
   in [04-metrics-observatory.md](04-metrics-observatory.md).
3. Publish with **baselines and measurement dates from the first commit**. The evaluation
   officer's finding was that not one of thirteen targets has a baseline — shipping the MVP
   without them reproduces the defect in a new place.
4. Until it is live, the ToC link comes out. A removed link is more credible than a 404.

Owner: Metrics lead.

### W6 — Durability *(governance · 3 personas · resolves blockers 12, 13)*

- Tag releases. Nothing in the organisation has a version, so adoption means pinning commit
  hashes indefinitely.
- Give data products a citable version and a DOI. They are currently served off
  `refs/heads/main` with no tags.
- Move data products out of per-user namespaces (`s3://cresst/{user}/`).
- Name the institution that holds the artefacts in year six. The national-lab scientist's
  summary of the current answer was "some files, and nobody."

Owner: DataHub lead + Lead PI for the institutional commitment.

### W7 — Navigation: surface what is already good *(3 personas · blocked on §2)*

The reviewers who found `pillar-1-soil-reanalysis`, `modelhub-landslide` and the DataHub
Integration Guide called them the project's strongest evidence. The reviewers who did not find
them could not reach them from the front page. The science advisor's version is the costly one:
*the only pages that state technical risk are invisible from the front door*.

Separately, four surfaces drew **no findings from any of the ten reviewers** — the hazard
chapters, `ocean-atmosphere-coupling`, and Pillars 2 and 3. Nobody's path reached them.

Owner: Website lead, after `GAIA-D-005`.

### W8 — Governance: say why nothing is ratified *(7 personas · no blockers, high credibility cost)*

Every decision reads "proposed"; two carry the unfilled placeholder `2026-08-__`. Seven
reviewers praised the governance writing as better than comparable projects and then discounted
it because it has never been used.

**The kickoff has not happened, so everything correctly stays `proposed`.** The reviewers were
not wrong to notice, but they inferred neglect where the real cause is sequence. The fix is
therefore to make the sequence legible rather than to ratify anything early:

- Add one line at the top of the decisions register: nothing ratifies before the kickoff call,
  and here is its date. An unratified register with a stated ratification date reads as a
  project waiting for its meeting; an unratified register with no date reads as an abandoned
  one. That is the entire difference, and it costs a sentence.
- Fill the two `2026-08-__` placeholders with the real kickoff date as soon as it is fixed. A
  placeholder date shipped to a public site was raised by four reviewers.
- `GAIA-D-005` (front page audience) joins the register as `proposed` and ratifies with the rest.
- A technical decision should join the register too — the science advisor read its absence as a
  sign the register is a governance artefact rather than a working instrument. The data-licence
  position in W2b is the natural first one.

Owner: Lead PI + Coordinator. Ratification is a kickoff agenda item, not a task.

### W9 — Stand up HazEvalHub *(2 blockers · the largest single credibility gap)*

HazEvalHub is described on the site as holding metrics, validation protocols and held-out data.
It has no repository. The faculty reviewer made this his blocker and named its central sentence
as the one that would be embarrassing in three years; the geospatial AI CTO made the published
leaderboard his, because the board cannot say whether a row came from the hidden set.

This is too large to be a bullet in a remediation plan, and W1 can only make the page honest —
it cannot make the hub exist. Full design and phasing:
**[09-hazevalhub-ctf-plan.md](09-hazevalhub-ctf-plan.md)**.

Until v0.5 lands, the HazEvalHub chapter says "in progress" with a date and an owner.

Owner: CI / eval leads.

## 4. The "in progress" convention

Applies across every workstream. Where a fix needs a human decision or a fact only a team member
holds, the page says **"in progress"** with an owner and a date, and the underlying question goes
to [`kickoff-agenda.md`](kickoff-agenda.md).

This is deliberately not a backlog. The synthesis guide's closing warning is that turning
findings into an issue tracker means they get worked in severity order and the actual decisions
never settle. The agenda file is where the decisions go; the issue tracker is for the work that
follows them.

## 5. Sequencing

### Day one — about two hours, clears items from twenty-nine findings

None of these requires a decision or a meeting.

| Fix | Workstream |
|---|---|
| Correct the `CITATION.cff` sentence in the FAQ | W2 |
| Fill the two `2026-08-__` placeholder dates | W8 |
| Replace or drop "∞ Sensors" | W1 |
| Gloss "digital twin" in one sentence on the landing page | W1 |
| Fix the 404 favicon and 404 team photo | W4 |
| Link the DataHub Integration Guide from the DataHub page | W7 |
| Remove `/metrics-observatory/` from the ToC until it exists | W5 |
| Add the "nothing ratifies before kickoff" line to the decisions register | W8 |

### Week one

- W4 in full — server-render the roster alphabetically, add co-PI titles, name a non-PI contact.
- W2 — open the `LICENSE` + `CITATION.cff` PRs and tag each repository owner.
- W2b — write the open-access-only + licence-propagation position onto the DataHub page.
- W1 begins its full-site sweep, starting with ModelHub, HazEvalHub and Research Software.
- W5 — fork `community-metrics` into the org. Reuse is already cleared under MIT.

### Month one

- W3 — one published number against one baseline. **Gates the front page.**
- W9 — HazEvalHub v0.5 seed tasks scoped ([09](09-hazevalhub-ctf-plan.md) §5).
- W5 — Observatory MVP refactored from SeisSCOPED, baselines and dates from the first commit.
- Kickoff call: ratify the register, including `GAIA-D-005`. W7 unblocks.

### Quarter

- W6 durability: releases, DOIs, and the year-six holder question (see §8).
- W9 — HazEvalHub v0.5 live with one hazard task and one agent task.
- W1 sweep complete across all pages.
- Re-run the ten personas and compare (§7).

## 6. What not to do

- **Do not redesign.** No blocker concerns design, typography, navigation quality or
  accessibility. The prose was independently praised by the reviewers most hostile to everything
  else. Sanding the writing will not move any score that matters.
- **Do not add four front pages.** See §2. The reviews specifically warn about this.
- **Do not delete the draft admonitions.** Three reviewers noticed them favourably. The
  scaffolding is honestly labelled; it is the claims *around* the scaffolding that are not.
- **Do not treat the FrugalMind board as a liability to hide.** It is simultaneously the most
  advanced artefact on the site and the least defensible as published. Publishing the scorer and
  stamping each row with the split that produced it converts it into the strongest evidence the
  project has.

## 7. How we will know it worked

Re-run the same ten personas against the same rubric once W1–W5 have landed, and file the round
in [`review-logs/`](../review-logs/) alongside this one. The comparison to watch is not the
average — it is **the spread between the reading personas and the verifying personas**. Today
that gap is 17 points (66 to 49). Closing it is the actual goal; raising the mean without
closing it would mean the writing got better again.

Do not edit the 2026-08-12 logs to reflect fixes. File the next round.

## 8. Decisions taken, 2026-08-12

The five open questions from the first draft are settled. Recorded here; they enter the
decisions register as `proposed` and ratify at kickoff with everything else.

| # | Question | Decision |
|---|---|---|
| 1 | Front page audience | **Climate technology**, framed as extreme weather and natural disasters (§2) |
| 2 | The Observatory | **MVP it**, by refactoring SeisSCOPED `community-metrics` (W5) |
| 3 | Commercial use | **Not pursued yet.** Everything ships open source — see the caveat below |
| 4 | Year-six holder | **No institutional answer yet.** Working assumption: Marine, in a future research centre (an FRO or equivalent) |
| 5 | Scope of the W1 sweep | **Every page** (W1) |

### 8.1 One thing to resolve before the licensing page changes

Decision 3 needs a sharper form of words than "no commercial use but open source", because those
two halves conflict. A permissive open-source licence — MIT, BSD-3, Apache-2.0, all of which the
project already uses and [03 §1.2](03-ai-tools-and-evals.md) mandates for containers —
**grants commercial use to anyone**, irrevocably. A licence that withholds it (CC-BY-NC, or a
custom non-commercial clause) is not open source under the OSI definition and would fail the
FAIR and openness commitments the governance pages make.

The reading that fits everything else in the project:

> GAIA is not pursuing commercial partnerships or paid licensing at this stage. Code and
> documentation ship under permissive open-source licences, which do permit commercial reuse by
> third parties. We neither seek nor restrict it.

This answers the climate-risk CTO's blocker honestly — his objection was to *silence*, not to
permission — and it costs nothing, because MIT already grants what he was asking about.

If the intent is genuinely to **withhold** commercial rights, that is a different and much larger
decision: it changes the licence on every repository, contradicts the current footer, and should
be its own entry in the register rather than a line on the licensing page. **Confirm which before
W2 writes anything.**

### 8.2 Year-six holder — how to write it

Decision 4 is an honest "not yet", and the plan's position is that publishing the question beats
implying an answer. Suggested wording for the durability section:

> Long-term stewardship of GAIA artefacts beyond the award is **in progress**. The current
> intent is that the software, data products and evaluation infrastructure move to a dedicated
> research centre; the institutional home is not yet settled. Until it is, all artefacts are
> archived to Zenodo with DOIs so that they outlive any single repository or namespace.

The second sentence is the one that matters to the national-lab scientist, and it is true today
if W6 lands. His finding was not that the holder is unknown — it is that *nothing would survive*,
which DOI archiving fixes independently of who ends up holding it.

## 9. Related

- [09-hazevalhub-ctf-plan.md](09-hazevalhub-ctf-plan.md) — the HazEvalHub design (W9)
- [kickoff-agenda.md](kickoff-agenda.md) — items this plan sends to the kickoff call
- [review-logs/2026-08-12/](../review-logs/2026-08-12/) — the evidence
- [02-website-evolution.md](02-website-evolution.md) — the expansion plan, unaffected by this one
