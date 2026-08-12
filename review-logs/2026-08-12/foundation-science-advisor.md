# Review: Foundation science advisor doing technical diligence

**Reviewed:** 2026-08-12 · **Scope:** landing page; `book/` problem-statement, datahub, modelhub, hazevalhub, modelhub-landslide, pillar-1-soil-reanalysis; governance chapters how-we-work, organization, decisions, licensing, faq; people.html, funding.html, dashboard.html; the `gaia-hazlab` GitHub organisation and all 26 repositories via the API, with `seis-hydro-2-sed`, `da-seis-groundfailure` and `gaia-agentic-ai` opened directly · **Time spent:** 35 minutes (5 over budget; I say where below)

*I am a simulated reviewer, not a real one. This persona is constructed from the project's
funding context and from what people in my role typically need. Nothing here is user research.
Every finding is a hypothesis about a real reader, not evidence about one.*

## In one paragraph

I came close to ending this evaluation twice and did not, and the reason I did not is the most
important thing I have to say. My stopping rule is "no stated technical risk anywhere" — and for
the first twenty minutes I believed I had met it. The front door, the problem statement, and the
three platform chapters a reader is actually pointed at state no assumption, no caveat, and no
condition under which the approach fails. Then I opened two chapters that nothing on the landing
page links to, and found a section literally titled "Two observational modalities (with honest
limitations)", a table separating what the model *solves* from what it *assumes*, and a paragraph
admitting that the project's own soil data currently lives at "personal absolute paths like
`/mnt/c/Users/.../Downloads/...`". That is the writing of a team that knows exactly what could
sink it. It is three clicks from anywhere a funder would land. So my conclusion is not that this
is the wrong bet — it is that the site is selling the part of the project I would not fund
(a platform whose registries are empty) and hiding the part I would (a specific, falsifiable,
self-critical claim about soil hydromechanical memory). What I would do next: recommend a small
exploratory grant, 12 months, one named milestone — a demonstration that the soil reanalysis
product improves landslide-probability skill over the ERA5-Land baseline the team's own
comparison table already names — and make the money conditional on that comparison being
published whichever way it comes out.

## Weighted score: 61/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 4 | 15 | My sixty-second sentence matched their own framing almost word for word |
| D2 Credibility of claims | 3 | 30 | Deep chapters are exemplary; front-facing platform claims outrun what exists |
| D3 Navigation and information scent | 2 | 5 | The best evidence on the site is unreachable from the front door |
| D4 Visual design and accessibility | 3 | 5 | Clean and legible; two pages ship unrendered template variables |
| D5 Technical depth and reproducibility | 3 | 15 | Real equations and parameters; no runnable path, and no licence on key repos |
| D6 Governance and openness | 3 | 10 | Decisions register is better than most, but ratifies nothing and records no science |
| D7 Activity and durability | 3 | 15 | Plainly alive and funded for five years; no external adoption yet |
| D8 Relevance to me | 2 | 5 | There is no ask on this site, and nothing philanthropy is uniquely positioned to buy |

## Findings

No blockers. I checked my stopping conditions and none of them held once I had read the
whole site — see finding 2 for the one that nearly did. I am not inflating anything to
get attention; the order below is the order I would work in.

### 1. The three platform pillars are described in the present tense and two of them are empty — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/book/modelhub/ and https://gaia-hazlab.github.io/book/hazevalhub/
**Saw:** ModelHub — "The ModelHub is where we register the machine learning and physics-based
models that monitor and predict hazards. It holds pre-trained weights, the training pipelines
that produced them, and the tooling to build new hazard models on top." The page then shows
working-looking code: `from gaia_hazlab.models import FloodDetectionModel` and
`model = FloodDetectionModel.from_pretrained('flood-v1.0')`. There is no `gaia_hazlab` package
on PyPI (both `gaia-hazlab` and `gaia_hazlab` return 404 from the JSON API) and no such
repository among the 26 in the organisation. The citation block reads "GAIA HazLab Team. (2024).
[Model Name]." — an unfilled placeholder with the wrong year. HazEvalHub has nine section
headings ("Evaluation Metrics", "Performance Comparison", "Case Studies", "Probabilistic
Evaluation") with no text under them at all, under a parent heading that says "Evaluation
Framework (TBD)".
**Why it matters to me:** I read "It holds pre-trained weights" as a statement about today. When
I go looking and find a template, I stop trusting the tense on every other page, including the
pages that turned out to deserve it. This is the single cheapest way this project loses a funder,
and it costs the team nothing real — the underlying work is genuinely early, and saying so would
not diminish it.
**Suggested fix:** Put the tense right. "The ModelHub *will be* where we register…" plus a short
"Available today" list (the Landlab landslide implementation, QuakeXNet, the FrugalMind board)
and a dated "Not yet built" list. Delete the fabricated import examples or mark them clearly as a
proposed API. Two hours of work.
**Confidence:** high

### 2. The only pages that state technical risk are invisible from the front door — MAJOR · D3, D2
**Where:** https://gaia-hazlab.github.io/book/pillar-1-soil-reanalysis/ and
https://gaia-hazlab.github.io/book/modelhub-landslide/ — neither is linked from
https://gaia-hazlab.github.io (whose only book links are datahub, modelhub, hazevalhub,
research-software, gaia-agent, soil-memory, hazard-landslides,
hazard-liquefaction-ground-failure)
**Saw:** Pillar 1, §3.3, "Two observational modalities (with honest limitations)": "*Clouds and
snow.* Optical imagery is cloud-contaminated (Sentinel de-clouding helps) and loses contrast over
snow — limiting usefulness exactly when winter hazards peak." And: "a downscaled 9 km
soil-moisture pixel … still has a 9–25 km support, and these artifacts leak into downstream
products … unless explicitly tracked." The landslide chapter: "What the model does **not** do: it
does not solve transient 3-D groundwater flow, does not mobilize or route the failed mass
(runout), and does not by itself ingest a forecast." And a table column headed "What it
*assumes*": "planar slope-parallel failure; steady-state wetness; parameters independent across
draws."
**Why it matters to me:** This is the material I do diligence for, and it is the material that
would have ended my evaluation by its absence. A reader on my budget who stops at the platform
chapters concludes the team has not identified its own weak points. The opposite is true. The
information architecture is actively working against the project's best asset.
**Suggested fix:** Add one link from the landing page and from the problem statement, labelled
something like "What we assume, and where it breaks". Promote the "solved vs assumed" table and
the §3.3 limitations to a short standalone page. This is a navigation fix, not a writing one —
the writing already exists.
**Confidence:** high

### 3. Five years of output counts are scheduled; the science has no date on it anywhere — MAJOR · D2, D7
**Where:** https://gaia-hazlab.github.io/book/how-we-work
**Saw:** A year-by-year table of deliverables — CI-template repos 3 (Y1) → 18 (Y5), container
images 3 → 35, DOI-archived datasets 5 → 100, versioned model cards 1 → 15 — and adoption targets
"from 500 annual container pulls/downloads (Y1) to 20K (Y5)". Nowhere on the site is there a date
attached to the scientific claim: that tracking soil hydromechanical memory measurably improves
hazard prediction.
**Why it matters to me:** Counting repositories is not evidence that the load-bearing idea works.
A project can hit every one of these numbers and have learned nothing about whether soil memory
predicts anything. Check six of my process asks whether the hardest thing is scheduled first or
last; here it is not scheduled at all, which is worse than last, because nothing forces the
reckoning.
**Suggested fix:** Add one row to that table with a year and a metric — for example, "Y2: soil
reanalysis product beats ERA5-Land baseline on landslide-probability skill for the 2025 western
Washington events, published either way." One row changes what this project is accountable for.
**Confidence:** high

### 4. The site claims MIT throughout; a fifth of the repositories carry no licence at all — MAJOR · D6
**Where:** https://gaia-hazlab.github.io (footer) and https://github.com/gaia-hazlab
**Saw:** Footer, every page: "© 2026 GAIA HazLab · University of Washington · Licensed under the
MIT License." The licensing chapter: "Choose the least restrictive licence that still requires
attribution." Against that, 12 of the 26 repositories return no licence from the GitHub API, and
`https://raw.githubusercontent.com/gaia-hazlab/<repo>/main/LICENSE` returns 404 for
`seis-hydro-2-sed`, `da-seis-groundfailure`, `mt-rainier-smart-sensing`, `landlab-debrisflow`
and `gaia-data-downloaders`. `seis-hydro-2-sed` is the repository behind the landing page's
"See it live" call to action. Separately, `usgs-gauge-utils` is GPL-3.0 inside an organisation
whose own licensing page says "Never embed copyleft (GPL/AGPL) code into MIT repositories."
**Why it matters to me:** *Observation:* those repositories have no LICENSE file. *Inference,
marked as such:* the openness here is partly decorative — asserted at the footer, not yet
enforced at the artifact. Unlicensed code is not open code; I cannot legally fork the very
demo the site invites me to look at.
**Suggested fix:** Add LICENSE to the twelve, or state on the licensing page which repositories
are deliberately unlicensed and why. The licensing chapter itself notes it is "currently proposed
and awaiting formal ratification" — ratify it and the cleanup follows.
**Confidence:** high

### 5. The counterfactual is never stated at project level, though the team clearly knows it — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/book/datahub and https://gaia-hazlab.github.io/book/organization
**Saw:** DataHub's contribution is described as "a small Python client that wraps the existing API
tools and stages the datasets each research group needs" over data the page itself says is
"public and served over APIs" by IRIS and Synoptic. The organization chapter names SCOPED as
methodological precedent but no coordination relationship with EarthScope, USGS, NASA, NOAA or
NHERI — while people.html lists a co-PI at EarthScope Consortium (David Mencin, "Geodesy (GNSS),
data services") and two senior personnel at the Alaska Satellite Facility.
**Why it matters to me:** My second question is always what happens if the project does not exist.
For the platform, the answer looks like "EarthScope, ASF, Synoptic and Landlab continue, and
someone writes the staging client anyway." The genuinely additional part is the coupling — and
the one page that argues this well is Pillar 1 §4, "State of the art — and the gap GAIA fills",
with a comparison table naming ERA5-Land, GLDAS and NLDAS-2 and what each cannot do for Pacific
Northwest hazards. That argument belongs on the front page, not in a chapter nothing links to.
**Suggested fix:** Move the Pillar 1 §4 table, or a three-line version of it, into the problem
statement. Add one sentence to the organization chapter saying what GAIA does that EarthScope and
ASF — its own partners — do not.
**Confidence:** medium (I may have missed a coordination statement elsewhere in the book)

### 6. Liquefaction is a headline capability resting on one graduate student — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/people.html (rendered from
https://gaia-hazlab.github.io/data/team.json) against https://gaia-hazlab.github.io
**Saw:** The landing page names three research areas, one of them "Liquefaction – How saturated
soils lose strength under shaking", and the problem statement names "2001–2031 Nisqually
Earthquake" as one of four use cases, on "earthquake-induced ground failure (liquefaction,
landslides)". Of the 24 people listed, exactly one gives geotechnical engineering as their
expertise: "Morgan Sanger | Graduate Student | Civil and Environmental Engineering | geo:
Geotechnical Engineering". ModelHub names the same person as lead on "Ground Failure Modeling:
Surrogate model to predict liquefaction and ground failure potential index (lead Morgan Sanger)".
By comparison, roughly eight people list seismology or seismic imaging.
**Why it matters to me:** Check five of my process is to name the thinnest human coverage against
a promised capability, and this is it, unambiguously. A PhD student is not a durability plan for
a quarter of the science, and students graduate inside a five-year award. Pillar 1 also notes
that `da-seis-groundfailure` "has no soil inputs wired yet", which is consistent with the
staffing.
**Suggested fix:** Either name a geotechnical faculty collaborator or senior personnel, or
demote liquefaction on the landing page from a headline area to a stated stretch goal. Both are
honest; the current pairing is not.
**Confidence:** high

### 7. The accountability dashboard the governance pages promise does not exist — MAJOR · D6
**Where:** https://gaia-hazlab.github.io/dashboard.html, against
https://gaia-hazlab.github.io/book/faq
**Saw:** The FAQ answers a question titled, in effect, "Why does the dashboard show below-target
numbers?" with "Hiding them would undermine the dashboard's credibility. Below-target figures
remain visible with documented escalation paths." How-we-work describes weekly "Observatory
updates" and a "metrics dashboard". What is at `/dashboard.html` is a Leaflet sensor map —
"Loading the GAIA CRESST catalog…", layers, basemaps, station links — with no metric, no target,
and no number from the D1–D5 table on it. I found no metrics page: `/metrics.html`,
`/observatory.html`, `/book/metrics/`, `/book/observatory/` and `/book/dashboard/` all 404.
**Why it matters to me:** Willingness to publish your own misses is the strongest openness signal
a project can send, and this project has written the promise down twice. Right now the promise
has no artifact behind it, and the word "dashboard" points at something else entirely. Of every
finding here this is the one where the gap between stated culture and shipped reality is widest.
**Suggested fix:** Publish the D1–D5 table with current values, even if every value is zero in
Y1 — zeros dated 2026-08 are more persuasive than an absent page. Give it a distinct URL and
rename the map to `/map.html` so the two do not collide.
**Confidence:** high

### 8. There is no ask, and nothing shaped to what philanthropy can uniquely buy — MAJOR · D8
**Where:** https://gaia-hazlab.github.io/funding.html
**Saw:** Funders, awards ("collaborative awards OAC-2608509, 2608510, and 2608511"), a standard
acknowledgment block, and the note that FFST seed money "supported the early prototypes,
community building, and proof-of-concept that matured into the CSSI project." No amounts, no
durations, no gap, no request.
**Why it matters to me:** Check eight of my process asks whether the ask is shaped to what federal
money cannot do — speed, risk, and people between grants. Here there is no ask at all, so I have
nothing to take to a board. This is a missed opportunity rather than a flaw: that one sentence
about FFST is the strongest philanthropic argument on the site, because it is a documented case
of small early philanthropy converting into a multi-institution federal award. The site states
it as a credit line instead of as evidence.
**Suggested fix:** Add a short section naming two or three things the CSSI award cannot fund — a
bridge for a postdoc between grants, a rapid-response deployment after an unscheduled event, a
negative result nobody will fund — with an indicative figure against each. Lead it with the FFST
conversion story.
**Confidence:** high

### 9. The decisions register is well built, ratifies nothing, and contains no technical decision — MINOR · D6
**Where:** https://gaia-hazlab.github.io/book/decisions
**Saw:** Four records — GAIA-D-001 funding acknowledgment, D-002 system of record, D-003 meeting
schedule, D-004 Google identity — each with "Rejected:", "Obligates:" and "Open:" fields. All
four are marked proposed, and the dates render as "—" against a kickoff logged as "2026-08-__".
The licensing chapter says its own guidelines are "awaiting formal ratification through the
decisions register." How-we-work states "Nothing counts as decided until it has a number."
**Why it matters to me:** The structure is genuinely better than most projects I look at — the
"Rejected" field is the part almost everyone omits, and D-002's admission that "role attribution
is not anonymity where one person holds each role" is exactly the kind of inconvenient fact I
look for. But every entry is administrative. Nothing about data format, model architecture,
evaluation protocol, or licence has entered the register, so the machinery has not yet touched
the science it exists to record. It does not change my recommendation; it does mean I cannot yet
score the openness as structural.
**Suggested fix:** Ratify the four with real dates, and add one technical decision — the STAC/Zarr
choice, or the two-soil-vocabulary conflict Pillar 1 already describes, which is a decision
waiting to be written down.
**Confidence:** high

### 10. A live chapter links to a repository that does not exist — MINOR · D5
**Where:** https://gaia-hazlab.github.io/book/pillar-1-soil-reanalysis/
**Saw:** "Two soil vocabularies run in parallel (SOLUS100 at 100 m vs POLARIS at 30 m in
[`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin))".
`https://github.com/gaia-hazlab/landslide-digital-twin` returns 404, and no repository of that
name is among the 26 in the organisation.
**Why it matters to me:** Small, but it is on the one page whose credibility I am relying on
most. A dead link in the middle of the most careful chapter on the site is the kind of thing that
makes a reviewer re-check everything else on it, which is what I did.
**Suggested fix:** Point it at the right repository or drop the link and keep the sentence.
**Confidence:** high

### 11. Unrendered template variables and a stale placeholder year — POLISH · D4
**Where:** https://gaia-hazlab.github.io/book/modelhub/ and https://gaia-hazlab.github.io/book/hazevalhub/
**Saw:** Both pages render `{{ github_org_url }}` and `{{ book_repo }}` literally — for example
"[model contribution guidelines]({{ github_org_url }}/{{ book_repo }}/blob/main/CONTRIBUTING.md)".
ModelHub's citation template reads "GAIA HazLab Team. (2024)." on a 2026 project.
**Why it matters to me:** Cosmetic on its own. It matters only because it lands on the same two
pages as finding 1, and the combination reads as pages nobody has looked at recently.
**Suggested fix:** Fix the substitution or hard-code the URLs; update the year.
**Confidence:** high

## What worked

**The FrugalMind eval board is the best thing on this site, and it publishes a negative result.**
At https://gaia-hazlab.github.io/book/hazevalhub/ : "Free local 7B models (`qwen2.5:7b`,
`llama3.1:8b`) reach perfect scores on configuration tasks once given domain skills — but fail at
numerical code generation, where only cloud models succeed (~0.56 base, rising to 0.76 with
skills)." Numbers, a named failure, and a live board at https://mdenolle.github.io/frugalmind
that resolves. Treating cost as "a first-class axis, not an afterthought" is a genuinely
distinctive design choice. Protect this.

**The landslide chapter separates what is solved from what is assumed, in a table.** At
https://gaia-hazlab.github.io/book/modelhub-landslide/ : a column headed "What it *assumes*"
reading "planar slope-parallel failure; steady-state wetness; parameters independent across
draws", alongside "so a reviewer knows where the physics is real and where it" is not. I would
point other projects at this table as a model. It is the strongest single artifact I found.

**The project publishes its own mess.** Pillar 1 states that soil data currently sits at
"personal absolute paths like `/mnt/c/Users/.../Downloads/...` … with no shared mechanism" and
that `da-seis-groundfailure` "has no soil inputs wired yet". Very few projects put that on their
public site. It is the clearest evidence I have that the openness is not purely decorative,
and it is the reason finding 4 is a major and not a blocker.

**The sixty-second test passed.** What I wrote after one minute on the landing page — "they build
digital twins of the Earth, fusing open multimodal data with AI, cloud computing and physical
models, to monitor and forecast weather-driven soil, landslide, liquefaction and flood hazards" —
is close to a paraphrase of their own sentence. Most projects I review fail this badly.

## What I could not judge

- **Whether the science is right.** I left the bench a decade ago. I can tell that the
  infinite-slope factor-of-safety formulation and the Monte Carlo probability-of-failure
  treatment are stated precisely enough to be checked; I cannot check them. That needs the
  faculty-reviewer persona or a real geomorphologist.
- **Whether the soil reanalysis product is achievable at the stated resolution.** Pillar 1's
  comparison table asserts that ERA5-Land at ~9 km is "too coarse for ridge–valley gradients."
  Whether GAIA can get meaningfully finer with the modalities listed is the whole bet, and I
  cannot evaluate it from a table.
- **Code quality, container correctness, CI health.** I did not open a workflow file and would
  not know what I was looking at. A research software engineer should.
- **Whether the collaboration is real.** Twenty-four people across UW, UAF, ASF and EarthScope
  looks strong on paper. Whether the Alaska half and the Washington half actually work together,
  or run as two projects under one award, is not visible from a website and is the thing I would
  most want to test in a site visit.
- **What I ran out of patience before finding.** I went five minutes over my thirty-minute budget
  and spent the overrun confirming that the deep chapters really do state their assumptions,
  because that determined whether I stopped. That means I never opened `gaia-agentic-ai`,
  `gaia-skills` or the GaiaAgent chapter — and "AI-driven" is the first phrase in the project's
  own name. A reader with a stricter budget than mine would have formed a view of this project's
  AI work without ever seeing it.

## My signature question

*What is the single assumption on which everything else rests, and what evidence exists that it
holds? If the site does not name it, name it for them.*

The assumption is this: **that the hydromechanical state of the soil — not just its moisture, but
its strength — can be estimated continuously, at hillslope resolution, from sensors that already
exist, and that knowing it improves hazard prediction enough to matter.** Everything else is
downstream. If soil state is recoverable at that resolution, the coupling across atmosphere,
hydrology and geomechanics becomes tractable and the four use cases are variations on one method.
If it is not, GAIA is a competent data-staging layer over infrastructure that already exists, and
the counterfactual swallows it.

The site does name this, but only in one chapter that nothing links to. Pillar 1 states the
positive case — that geophysical networks are "a modality absent from every comparable product",
specifically time-lapse seismic velocity dv/v "which responds to pore pressure and saturation",
which is the mechanism by which strength rather than wetness becomes observable. That is the real
idea, and it is a good one. The evidence that it holds is, so far, citations to prior literature
rather than a GAIA result: no page shows dv/v-derived soil state improving a hazard prediction
against a baseline. The team has also written down, honestly, the conditions under which the
satellite half of the observing system degrades — clouds and snow, "limiting usefulness exactly
when winter hazards peak", which is when Pacific Northwest landslides happen.

So: the assumption is identified, its failure mode is identified, and it is not yet tested. That
is a perfectly good place for a project two years in to be. It is a bad place for a website to
hide. My recommendation is a small exploratory grant with exactly one milestone at twelve months
— the soil reanalysis product versus the ERA5-Land baseline on landslide probability for the 2025
western Washington events, published whichever way it comes out — because that is the assumption
everything else rests on, and because the team has already shown, in the FrugalMind result, that
it will publish a number that does not flatter it.
