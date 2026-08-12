# Review: Impact and evaluation officer auditing the measurement system

**Reviewed:** 2026-08-12 · **Scope:** landing page; `/book/` and its nav; `/book/how-we-work`, `/organization`, `/decisions`, `/licensing`, `/faq`; `/dashboard.html`, `/funding.html`; attempted `/metrics-observatory/`, `/latest.json`, `/metrics.html`; the `gaia-hazlab` GitHub organisation repository listing · **Time spent:** 40 minutes of a 45-minute budget

*I am a simulated reviewer, not a real one. I am a persona constructed to approximate how a
funder's evaluation officer would read this project. Everything below is a hypothesis about a
real reader, not evidence about one. Treat it accordingly.*

## In one paragraph

This project has written one of the better measurement frameworks I have read from a research
group, and has not yet built any of it. `book/how-we-work` commits to thirteen numeric targets
across five years, names an automated collector, states that a missing value reads `n/a` rather
than zero, and sets out a four-step escalation ladder for a missed target — all of which I would
normally spend my review arguing about at the margins. Instead I spent it looking for a single
published number and failing to find one. The nav link labelled "Metrics Observatory (live)"
returns 404. `latest.json`, which the same document says the quarterly newsletter pastes from,
returns 404. `dashboard.html` is a sensor map with no metrics on it at all. So the framework is
currently unfalsifiable: I cannot check the `n/a` rule, I cannot check that shortfalls stay
visible, and I cannot check whether the escalation ladder has ever been climbed. Underneath that,
there is a second problem the framework would still have once it ships — not one of the thirteen
targets has a baseline, and the adoption metrics do not distinguish the project's own use of its
own artefacts from anybody else's. My recommendation to a grants committee today would be: do not
accept this reporting framework as sufficient for a grant agreement yet, but do not impose a
different one either. Ask for a baseline table and one published snapshot, and re-read in ninety
days. I think this one is close.

## Weighted score: 57/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 10 | I got a workable sentence in sixty seconds, through two words I do not know |
| D2 Credibility of claims | 2 | 25 | Every measurement claim on the site is currently uncheckable by a reader |
| D3 Navigation and information scent | 2 | 5 | I came for metrics; the only link labelled "(live)" 404s and "Dashboard" is a map |
| D4 Visual design and accessibility | 3 | 5 | Legible and unremarkable; I did not audit it properly — see below |
| D5 Technical depth and reproducibility | 3 | 5 | Largely outside my competence; scored as adequate on what I could see |
| D6 Governance and openness | 3 | 20 | Unusually good documents, all still marked "proposed", none dated |
| D7 Activity and durability | 3 | 15 | Org clearly alive; the collector the reporting depends on has no owner or repo |
| D8 Relevance to me | 4 | 15 | A published measurement framework with stated failure responses is rare and worth my time |

## The sixty-second test

Written on the landing page before I read anything else, and not revised:

> "This project builds computer models of the Earth that fuse sensor data with AI to monitor and
> forecast soil, landslide, flood and 'liquefaction' hazards, at a university lab."

I would call that a pass. I got the domain and the method. I did not get the word "liquefaction",
and I put it in quotation marks because I was copying a shape, not understanding a term.

## Findings

### 1. The Metrics Observatory, the dashboard and `latest.json` are all 404 or absent — no published metric value exists anywhere on this site — BLOCKER · D2

**Where:** `https://gaia-hazlab.github.io/book/` (nav item), `https://gaia-hazlab.github.io/metrics-observatory/`, `https://gaia-hazlab.github.io/latest.json`, `https://gaia-hazlab.github.io/dashboard.html`

**Saw:** The book navigation renders a link, verbatim: "Metrics Observatory (live)". It resolves
to HTTP 404. `https://gaia-hazlab.github.io/latest.json` returns HTTP 404;
`https://gaia-hazlab.github.io/metrics.html` returns HTTP 404. Meanwhile
`https://gaia-hazlab.github.io/book/how-we-work` states: "Nearly all of these are collected
automatically, weekly, by the Metrics Observatory from the GitHub, Zenodo, Hugging Face,
container-registry and Slack APIs"; "The **public dashboard** updates weekly whether or not
anyone is watching"; and "The **quarterly newsletter** to the announce list pastes its numbers
directly from `latest.json`." `https://gaia-hazlab.github.io/dashboard.html` contains no
occurrence of the word "metric" and displays only a sensor map — "Loading the GAIA CRESST
catalog…".

**Why it matters to me:** This is where I stop. Not because a page is broken — pages break — but
because the entire measurement system on this site is currently a description of a measurement
system. Three separate load-bearing artefacts are named in the present tense and none of them
exist at a URL a reader can reach. I cannot audit an instrument I cannot open. Worse, the label
says "(live)", which is a claim about the current state of the world, and it is not true today.
Everything else in this review is conditional on this being fixed. (Inference, marked as such: I
believe this is a shipping gap rather than a deception, because the site carries a banner reading
"This is a new website, code examples are non-functional placeholders!" — but the banner does not
cover a nav link that says "live".)

**Suggested fix:** Two hours of work, in this order. (a) Publish `latest.json` and one static
HTML page at `/metrics-observatory/` containing the thirteen committed metrics with every value
as `n/a` and a visible "as of 2026-08-12 — collection not yet running" stamp. An honest page of
`n/a` is a stronger signal than no page. (b) Until that exists, retitle the nav link from
"Metrics Observatory (live)" to "Metrics Observatory (planned)".

**Confidence:** high

### 2. Not one of the thirteen targets has a baseline — MAJOR · D2

**Where:** `https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** Both target tables run "Y1 | Y2 | Y3 | Y4 | Y5" with no starting-value column. For
example: "M3 unique institutions | 20 | 30 | 50 | 100 | 100" and "M2 container pulls + dataset
downloads (annual) | 500 | 2K | 5K | 10K | 20K". The framing above them reads: "These numbers are
commitments from the funded proposal, not aspirations, and we report against them publicly."

**Why it matters to me:** A target without a baseline is a wish. I cannot tell whether "20 unique
institutions in Y1" represents twenty new institutions or the eighteen already in the
collaboration plus two, and those are very different projects. This is the single most common way
a well-intentioned metrics table becomes uninterpretable by year three — nobody records where it
started, and by the time anyone asks, the answer is reconstructed from memory. The fix costs an
afternoon now and is impossible later.

**Suggested fix:** Add a "Y0 (2026-08)" column to both tables, filled in this month, with `n/a`
where genuinely unmeasured. Freeze it in the decisions register so it cannot drift.

**Confidence:** high

### 3. The adoption metrics do not exclude the project's own use of its own artefacts — MAJOR · D2

**Where:** `https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** "M2 container pulls + dataset downloads (annual) | 500 | 2K | 5K | 10K | 20K" and "M2
derived agents (`IsDerivedFrom`) | 2 | 8 | 29 | 50 | 100". Nothing on the page states that pulls
originating from the project's own CI, its own team, or its own hackweek attendees are excluded.

**Why it matters to me:** Self-pulls of one's own container are not adoption. A CI pipeline that
builds nightly across five repositories pulls a base image more than 500 times in a year without
a single outside user ever hearing of the project — and the Y1 target is 500. Similarly,
`IsDerivedFrom` is a relation the project itself can assert; two derived agents in Y1 is met by
the team forking its own agent twice. I am not saying anyone would do this deliberately. I am
saying the metric cannot tell the difference, which means in three years neither can I, and
neither can the programme officer reading the annual report.

**Suggested fix:** Add one sentence per metric defining the exclusion — "pulls from GAIA-owned CI
runners and GAIA institutional IP ranges are excluded and reported separately" — and report the
excluded count alongside, not instead. For `IsDerivedFrom`, distinguish "derived by a GAIA
institution" from "derived elsewhere" as two rows.

**Confidence:** high

### 4. The FAQ answers a question about a dashboard state no reader can observe — MAJOR · D2

**Where:** `https://gaia-hazlab.github.io/book/faq`

**Saw:** Question: "Why is the dashboard showing numbers below target?" Answer: "Because hiding
them would make the rest of the dashboard worthless. Figures below target stay visible, and the
escalation path for each is written down."

**Why it matters to me:** This is written in the present tense about a dashboard that shows no
numbers at all. Read against finding 1, it describes a candour the site does not currently
demonstrate. I want to be precise about my objection: the sentiment is exactly right, and it is
the reason I scored D8 at 4. But an FAQ entry defending a shortfall that is not on display reads,
to me, as the project claiming credit for an honesty test it has not yet sat. If everything is
green because nothing is published, that is the same information vacuum as everything being green
because the targets were soft.

**Suggested fix:** Reword to future or conditional tense until the dashboard is live — "When the
dashboard shows numbers below target, they will stay visible" — or, better, ship finding 1 and
leave this answer exactly as it is.

**Confidence:** high

### 5. The Observatory has no repository, no named owner, and no visible code — MAJOR · D7

**Where:** `https://github.com/orgs/gaia-hazlab/repositories` and
`https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** The organisation lists 26 repositories. None is named for or described as a metrics
collector, an observatory, or a reporting pipeline; the closest, "catalog", is described as "data
catalog + web map". The governance page nonetheless says "the Observatory snapshot is archived
with a DOI each August" and assigns it a weekly duty. No named person or role is attached to it
anywhere I looked, including `https://gaia-hazlab.github.io/book/organization`, which explicitly
requires "a named maintainer and a numbered decision" for repositories entering the organisation.

**Why it matters to me:** Five-year projects lose people. The question I always ask is what
happens to the reporting when the person who built the collector leaves, and here I cannot even
establish that a person built one. The project has stated the right rule — named maintainer,
numbered decision — and has not applied it to the one component the entire public accountability
story rests on. (Observation: no such repository is listed. Inference: the collector is not yet
written.)

**Suggested fix:** Create the repository even if it is empty, put a named maintainer in its
README, and register it as a numbered decision. That is a fifteen-minute action that converts a
promise into an object with an owner.

**Confidence:** medium — I searched the public organisation listing; a private repository would
not appear to me, and if one exists the finding is weaker but the reader's problem is identical.

### 6. The landing-page counters are undefined, unrelated to the committed metrics, and one of them is not a number — MAJOR · D1, D2

**Where:** `https://gaia-hazlab.github.io`

**Saw:** Four figures displayed prominently: "4 Coupled hazard use cases", "3 Earth systems
linked", "14+ Researchers & partners", "∞ Sensors, one platform".

**Why it matters to me:** This is the first quantitative thing a reader meets, and none of it
connects to the thirteen numbers the project is actually accountable for. I cannot tell who is
inside "14+" — funded staff, co-authors, anyone on a mailing list? — and the "+" means the number
can only ever go up. "∞" is not a measurement; it is a decoration in the position where a
measurement goes. The governance page says "We count few things… We do not add flattering ones",
and then the front door shows four flattering ones. That contradiction is the kind of thing I am
paid to notice, and it undercuts the credibility of the disciplined table three clicks deeper,
which deserved better.

**Suggested fix:** Either define each counter in a footnote with its instrument and date, or
replace all four with two real ones from the committed set once the Observatory ships. Drop the
"∞" regardless.

**Confidence:** high

### 7. Every governance decision is "proposed" and undated; the escalation ladder has never been climbed — MAJOR · D6

**Where:** `https://gaia-hazlab.github.io/book/decisions`, `https://gaia-hazlab.github.io/book/licensing`, `https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** All four decision records — "Funding acknowledgment text and mechanics", "System of
record: Slack ephemeral, GitHub durable", "Meeting schedule and the sunset rule", "Project Google
identity" — carry status "proposed" and a date of "—". The licensing page carries: "Status.
Proposed, awaiting a numbered decision in the decisions register. Until it is ratified,
individual repositories may not yet match what is described here." The governance page is
"Version 0.1, drafted August 2026". The organisation page says its tagging taxonomy is "Proposed
— not yet ratified".

**Why it matters to me:** A ladder nobody has climbed is untested. The escalation table is the
best part of this framework — "The accountable lead either names a corrective action with a date,
or explicitly accepts the shortfall and says why. Both outcomes are recorded; silence is not an
option" is a sentence I would quote to other grantees. But I have no evidence any of it has run
once, and I have learned to discount unexercised process heavily. The undated records compound
it: I cannot tell whether this register is two weeks old or stalled for six months, which is
precisely the distinction I need. I will also note in the project's favour that "proposed" is
displayed rather than hidden, which is more than most projects manage.

**Suggested fix:** Put a date on every decision record, proposed or not — proposal date and
ratification date as separate columns. Then ratify at least one, so the register demonstrates a
full lifecycle. Once the Observatory ships, run the monthly step once against a deliberately
`n/a` metric and publish the record.

**Confidence:** high

### 8. "Skill-adoption gain" has no instrument, no denominator and no response-rate floor, and its target path falls in Y4 — MINOR · D2

**Where:** `https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** "M4 skill-adoption gain (post − pre) | +20% | +25% | +40% | +35% | +40%" and "Two —
disciplines represented and skill-adoption gain — come from surveys and are entered by a human."

**Why it matters to me:** This is a hand-entered self-report with the most degrees of freedom of
any metric here, and the least definition. Percentage of what, measured with which instrument,
among how many respondents, and what happens if six people out of sixty reply? A pre/post gain
computed over self-selected hackweek completers will clear +20% essentially by construction. The
Y3-to-Y4 drop from +40% to +35% is also unexplained; either it encodes a real expectation about
scaling or it is a typo, and I cannot tell which, which is itself the problem.

**Suggested fix:** Name the instrument, state the denominator, and set a minimum response rate
below which the value publishes as `n/a` rather than as a number. Add one clause explaining the
Y4 dip or correct it.

**Confidence:** medium — I am inferring the survey design from its absence.

### 9. Two targets are flat between Y4 and Y5 — MINOR · D2

**Where:** `https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** "M3 unique institutions | 20 | 30 | 50 | 100 | 100".

**Why it matters to me:** A cumulative metric with an identical Y4 and Y5 target means the final
year of the award requires zero additional institutions. That may be deliberate — a plateau after
a push is a defensible model — but as written it reads like a table that ran out of ambition, and
in year five it will be trivially met. I would want one sentence of intent.

**Suggested fix:** Either raise Y5 or add a footnote saying the plateau is intentional and why.

**Confidence:** high on the observation, low on whether it matters.

### 10. Two words on the landing page mean nothing to me — MINOR · D8

**Where:** `https://gaia-hazlab.github.io`

**Saw:** "to monitor and forecast soil, landslides, liquefaction, and floods" in the tagline, and
"reanalysis" elsewhere on the same page.

**Why it matters to me:** I do not know either word, and I am flagging that rather than quietly
looking them up, because a funder's evaluation staff is exactly the audience that will not look
them up. Three of the four items in that list are things I can picture. The fourth is a word I
copied into my sixty-second sentence in quotation marks. It is a small tax, and it lands on the
first sentence a reader meets.

**Suggested fix:** A four-word gloss in parentheses on first use — "liquefaction (ground turning
to slurry in a quake)". The deeper chapters can assume whatever they like.

**Confidence:** high, and this one is by definition about me rather than about the site.

### 11. Eleven of twenty-six repositories show no licence, on a project whose licensing page says the rule is settled — MINOR · D6

**Where:** `https://github.com/orgs/gaia-hazlab/repositories`, `https://gaia-hazlab.github.io/book/licensing`

**Saw:** Repositories with no licence shown in the organisation listing include "seis-hydro-2-sed",
"geocroissant-hazards", "gaia-data-downloaders", "landlab-debrisflow", "mt-rainier-smart-sensing"
and "da-seis-groundfailure". The licensing page states the principle "Choose the least
restrictive licence that still requires attribution" and, to its credit, "Until it is ratified,
individual repositories may not yet match what is described here."

**Why it matters to me:** The governance page lists among things "Public from day one: the
coordination repository, the roadmap, open issues…". Public and reusable are different things,
and an unlicensed public repository is legally not reusable. I cannot judge the code, but I can
count LICENSE files, and eleven gaps is a compliance item I would raise at a first review. The
project has already stated the caveat honestly, which is why this is minor rather than major.

**Suggested fix:** A single pass adding LICENSE files to the eleven, or an explicit note on the
licensing page listing which repositories are knowingly unlicensed and why.

**Confidence:** high on the count as displayed; medium on whether a LICENSE file exists but is
not surfaced in the listing.

### 12. The word "dashboard" means two different things on this site — POLISH · D3

**Where:** `https://gaia-hazlab.github.io/dashboard.html` and `https://gaia-hazlab.github.io/book/how-we-work`

**Saw:** The nav item "Dashboard" leads to a page whose content is "The GAIA sensing map" and "See
every sensor on one living map". The governance page uses "the metrics dashboard including
whatever is behind target" to mean something else entirely.

**Why it matters to me:** It cost me a few minutes of my forty. I clicked "Dashboard" expecting
metrics, got a map, and had to work out that the thing I wanted lived at a third URL that turned
out not to exist. Minor on its own; it compounds finding 1.

**Suggested fix:** Rename the map page "Sensing map" and reserve "Dashboard" for the metrics.

**Confidence:** high

## What worked

**The escalation ladder is the best thing on this site, and I would cite it elsewhere.**
`https://gaia-hazlab.github.io/book/how-we-work`: "Weekly | The Observatory updates. Nobody acts.
Data collection is not management." and "A target that is unreachable because the world changed
should be renegotiated openly and early, not quietly missed for four years and explained in a
final report." Most grantees have no stated response to a missed target at all. Having one, with
named timeframes and an accountable lead who must either act or explicitly accept the shortfall,
is unusual. Protect this wording.

**The `n/a` rule is correct and rarely written down.** "A metric that cannot be collected reads
`n/a`, never zero. A missing source and a real zero mean different things, and conflating them
makes a dashboard misleading." I have argued this point with grantees for years. Someone here
already knew it.

**One target is honestly set to zero.** "M2 publications using GAIA | 0 | 3 | 10 | 20 | 30". A Y1
target of zero is a small act of courage in a table someone will read as a scorecard, and it is
evidence the tables were built from a real plan rather than from optimism.

**Stated limitations rather than glossed ones.** "Role-level attribution is not anonymity in a
team where one person holds each role… We do not claim more than that." And the site-wide banner:
"This is a new website, code examples are non-functional placeholders!" A project that flags its
own weak points is one whose numbers I am more inclined to believe, once there are numbers.

**"We count few things."** Thirteen metrics for a five-year award is restraint. I see forty-metric
frameworks routinely and they measure nothing.

## What I could not judge

- Whether the science is any good. Out of scope by design, and out of my competence entirely.
- The technical terms `dv/v`, `InSAR`, `surrogate model` — I did not encounter the first three in
  what I opened, and `reanalysis` I encountered and did not understand. Where a page depends on
  them, I have no view.
- Accessibility. I scored D4 at 3 as a placeholder. I did not test contrast, keyboard reach, alt
  text or a phone-width viewport, and my score should not be read as a pass. A real audit is
  needed and I am not it.
- Whether the 26 repositories contain working code. I read the listing metadata only.
- Whether a private metrics repository exists. I searched public listings.
- Whether the escalation ladder has been exercised internally without a public record. I can only
  see what is published, and nothing published shows it running.
- What I ran out of patience before finding: I never located a single dated, published metric
  value. I spent roughly half my budget looking. If one exists somewhere I did not reach, its
  discoverability is the finding.

## My signature question

**For every published metric: name the cheapest way to hit the target without doing the
underlying work, and say whether anything currently prevents it.**

Nothing currently prevents any of them, because nothing is currently published or collected.
That is the honest one-line answer. Taking the thirteen committed targets as they will be
collected:

| Metric | Cheapest way to hit it without the work | Prevented today? |
|---|---|---|
| D1 CI-template repos passing tests | Add a trivial passing test to three existing repos | No — "passing tests" is undefined; no coverage or substance floor |
| D2 container images in the registry | Push three tagged rebuilds of one image | No — "images" is not qualified as distinct or functional |
| D3 DOI-archived datasets | Split one dataset into five Zenodo deposits | No — no minimum size, distinctness or reuse condition stated |
| D4 versioned model cards | Write one card, bump the version | No — "versioned" invites exactly this |
| D5 JupyterBooks + hackweeks | Publish a thin book; hold a one-day internal hackweek | No — no attendance, external-participation or content floor |
| M2 container pulls + downloads | Let CI pull the base image nightly | No — self-pulls are not excluded (finding 3) |
| M2 derived agents (`IsDerivedFrom`) | The team asserts the relation on its own forks | No — the project controls the assertion |
| M2 publications using GAIA | Team's own papers cite the platform | No — no "external author" condition |
| M3 unique institutions | Count every co-author affiliation and hackweek registrant | No — "unique institutions" has no engagement threshold |
| M3 disciplines represented | Self-classify the existing team more finely | No — hand-entered, no taxonomy named |
| M4 agent modes in publications | Team's own papers exercise three modes | No — no external-authorship condition |
| M4 modalities per study (median) | Add a thin extra modality to each study | No — no materiality condition on a modality |
| M4 skill-adoption gain | Survey only enthusiastic hackweek completers | No — no denominator, instrument or response floor (finding 8) |

The pattern is the same in every row: the project can move all thirteen numbers using only its
own people and its own artefacts. The framework's honesty rules govern *how values are displayed*
— `n/a` versus zero, shortfalls visible — and none of them govern *who counts*. That is the gap I
would close first, and it is closed with about a paragraph of definition per metric, not with a
new system.

The counterweight I want to record fairly: a team that intended to game these numbers would not
have written the escalation ladder, would not have set a Y1 publication target of zero, and would
not have published the `n/a` rule. My finding is that the framework is currently gameable, not
that anyone is gaming it.

---

*Simulated review, generated 2026-08-12 against the live site. Findings are hypotheses about a
real reader of this type, not observations of one. Every quotation was taken from the URL cited
on the date above; the site is under active development and these may not reproduce later.*
