# Review: Family foundation program officer and donor advisor

**Reviewed:** 2026-08-10 · **Scope:** homepage, `/book/problem-statement`, `/funding.html`,
`/dashboard.html`, `/people.html`, `/book/licensing`, attempted `/book/how-we-work` ·
**Time spent:** 10 minutes

*Simulated persona review. Not a real program officer — see [`../shared/method.md`](../shared/method.md).*

## In one paragraph

A trustee asked me to look, so I looked, and I got further than I expected — but not to a
place where I could brief a board. The first screen tells me the science is coupled; it does
not tell me who gets hurt. The opening sentence contains three phrases I would have to define
aloud before a trustee could follow me, and "digital twin" is the first thing I meet. Deeper
in, on the problem page and the flood demo, the site suddenly gets good: there is a December
2025 atmospheric-river flood on Mount Rainier's glacial rivers, and the phrase "Orting–Puyallup
lahar corridor" is the only moment in ten minutes when I pictured a town with people in it.
That sentence should be on the homepage. On the money question I am left empty-handed: the
funding page is a clear, honest list of who paid, but it never says what a private gift buys
that a federal grant cannot, there is no giving contact, and — the thing I was sent to check —
the Paros Center gift is described as supporting a "flagship" without one line of what that
support has produced. The people page has no names and no faces, which for a family board is a
real problem: families give to people. Right now I would not take this to committee. I would
take a call, because the Rainier flood story is genuinely fundable if someone will tell it in
English.

## Weighted score: 51/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 2 | 30 | Opening sentence is jargon-first; nobody is harmed in it. Strong plain material exists but sits three clicks down. |
| D2 Credibility of claims | 3 | 20 | Real named events, real awards, honest about what is unfinished — but no consequence figures and repeated "coming soon". |
| D3 Navigation | 3 | 15 | Nav is clean and Funding is where I expected it; `/book/how-we-work` 404s and `people.html` is empty. |
| D4 Visual design and accessibility | 2 | 20 | Not one photograph of a person or a place. Institutional logos and animations only. |
| D5 Technical depth | 3 | 0 | Not mine to judge; weight zero. |
| D6 Governance | 3 | 5 | Licensing page exists and opens in plain language. |
| D7 Activity and durability | 3 | 5 | 2026 copyright and a Dec-2025 case study, but a "relaunched / placeholders" banner at the top. |
| D8 Relevance | 4 | 5 | Squarely in an environment and resilience portfolio. |

## Findings

### 1. The Paros gift is acknowledged but nothing is said about what it produced — MAJOR · D2

**Where:** `/funding.html`
**Saw:** "The Jerome and Linda Paros Geohazard Center supports GAIA's Mount Rainier flagship —
integrating dense geophysical and geodetic observation with real-time hazard modeling at one
of the Pacific Northwest's highest-risk volcanoes."
**Why it matters to me:** This is the single sentence I was sent to find, and it describes
intent, not result. It tells me what the money is *for*, never what it *did* — no instruments
in the ground, no first detection, no student, no paper, no month when something worked. I read
this as a preview of how my own foundation would be written up in three years. Better than a
logo wall, but only just.
**Suggested fix:** Three or four sentences under the Paros heading: what the gift bought (how
many instruments, where on the mountain, installed when), what it has produced so far (one
concrete result, dated), one sentence on what it enables next.
**Confidence:** high

### 2. No statement of what philanthropy can do that federal money cannot — MAJOR · D1

**Where:** `/funding.html`
**Saw:** "GAIA HazLab is built on complementary investments — from the seed that launched the
idea, to the federal award now driving it, to the philanthropy and programs that anchor its
flagship applications."
**Why it matters to me:** This is the whole reason I opened the page. "Anchor its flagship
applications" is a category, not a case. No giving instructions, no named contact, no sense of
what a few hundred thousand dollars would change. The genuinely useful signal is elsewhere —
the seed fund "funded the early prototypes, community building, and proof-of-concept that
matured into the CSSI project" — which *is* the argument for private money, and it is never
made explicitly.
**Suggested fix:** A short section headed "What private support makes possible": two or three
specific things federal awards will not fund fast — instruments in a new watershed, a year of
a student's time, keeping the live map running between grants — each with a rough cost. Add a
named person and an email.
**Confidence:** high

### 3. The first screen is written for scientists, not for the people at risk — MAJOR · D1

**Where:** homepage
**Saw:** "We build digital twins of the Earth — fusing open, multimodal data with AI and cloud
computing, all grounded in physical models — to monitor and forecast soil, landslides,
liquefaction, and floods."
**Why it matters to me:** In sixty seconds I need to know who is harmed and what you do about
it. This tells me what you build and what it is made of. "Digital twin" is on my list of words
I do not have; "multimodal data" and "liquefaction" I would also have to explain. There is no
person in this sentence — no town, no family, no emergency manager.
**Suggested fix:** Lead with the harm. "Rain-soaked hillsides collapse. Rivers rise faster than
the gauges can see. We put sensors on Mount Rainier and use them to give the towns downstream
more warning." Technology in the second paragraph.
**Confidence:** high

### 4. No photographs of people, and the people page is empty — MAJOR · D4

**Where:** `/people.html`
**Saw:** "People of GAIA HazLab" · "Geoscientists, engineers, and AI builders working across
seismology, hydrology, geotechnics, and machine learning."
**Why it matters to me:** No names, no roles, no faces — a category description under a heading
that promises people. The homepage counts "14+ Researchers & partners" and invites me to "Meet
the full team", and then the team is not there. Family boards give to people they can picture.
**Suggested fix:** Photographs and one-line bios, principal investigator first, with a sentence
on why she works on this. If the roster loads dynamically, make sure it renders without
scripts.
**Confidence:** medium — read through text extraction, so images and script-loaded content may
not have reached me; but no names came through either, which a text fetch would normally show.

### 5. `/book/how-we-work` returns 404 — MINOR · D3

**Where:** `/book/how-we-work`
**Saw:** "The page returned a 404 client error"
**Why it matters to me:** Small in itself. It matters because "how we work" is exactly the page
a funder wants — who decides, who is accountable, how a community gets involved — and it is
missing while the licensing page beside it works.
**Suggested fix:** Publish it or remove the path.
**Confidence:** high

### 6. The strongest, most human sentence on the site is buried in a demo — MINOR · D1

**Where:** homepage
**Saw:** "During the December-2025 atmospheric-river floods on Mt. Rainier's glacial rivers, a
seismic network estimated river discharge in the long reaches *between* sparse stream gauges,
while a Stage IV precipitation mosaic tracked the rainfall driving the floods — the forcing and
the response, side by side, toward earlier flood awareness in the Orting–Puyallup lahar
corridor."
**Why it matters to me:** The only place in ten minutes with a dated event, a named place and a
stated benefit to somebody. Still overwritten, but Orting is a town and "earlier flood
awareness" is a consequence. This is the case for support, and it is halfway down the homepage
inside a technical demo.
**Suggested fix:** Promote a plain-English version to the top, with a photograph of the valley
and a number: how many people live in that corridor, and how many extra minutes of warning you
are aiming for.
**Confidence:** high

### 7. Hard to tell what exists today from what is hoped for — MINOR · D7

**Where:** homepage
**Saw:** "📢 Newly relaunched — code examples are placeholders while we rebuild." · "Live demo
coming soon" · "In compilation" · "live panel coming soon"
**Why it matters to me:** I respect the honesty and do not penalise a project for being
mid-build. But I am assessing whether a gift changes something real, and four "coming soon"
markers plus a placeholder banner make that hard to judge. A trustee will ask exactly this.
**Suggested fix:** One line near the top separating what runs now from what is in build, with
dates. "The sensor map is live. The landslide forecast goes live in spring 2027."
**Confidence:** high

### 8. The dashboard shows coverage, not progress — MINOR · D2

**Where:** `/dashboard.html`
**Saw:** "Every colocated sensor, image, and event across our Washington State regions of
interest." · "Prototype"
**Why it matters to me:** I came looking for evidence of progress. A map of instruments is
evidence of installation — no last-updated date, no counts, nothing that changes between my
visit and the next. I could not tell a board what moved this year.
**Suggested fix:** A visible last-updated timestamp and three or four running numbers a
non-specialist can read: stations live, events captured, warnings issued or hindcast.
**Confidence:** high

## What worked

- **The funding page is honest and well organised.** Four funders, each with a heading, a role
  and a sentence — seed money, federal core, a wildfire programme with a named PI, and the
  philanthropic flagship. Nobody is reduced to a logo. "GAIA started as a seed effort supported
  by the Fund for Future Science and Technology (FFST) through UW CRESST, which funded the
  early prototypes, community building, and proof-of-concept that matured into the CSSI
  project" is a genuinely good sentence about what early money achieves.
- **The problem statement names real things**: "2025 Western Washington Floods & Landslides",
  "2025 Stehekin Post-fire Debris Flow", the Nisqually earthquake. More than most sites give me.
- **The licensing page opens in a voice I can follow**: "Everything GAIA publishes is meant to
  be reusable — a condition of the awards, and the reason for building shared infrastructure
  rather than one-off scripts." Whoever wrote that should be given the homepage.
- **Navigation is short and predictable**, and Funding is top-level. I found it without hunting.

## What I could not judge

- **Type size, contrast and phone layout.** I read through text extraction and could not
  inspect the rendered page, so D4 is scored on the absence of human imagery rather than on
  typography. Someone should check it on a small screen.
- **Whether the people page has photographs that did not reach me.** See finding 4.
- **The interactive map and the knowledge graph.** "Hue is the category, brightness the
  subcategory; hover a node to trace its chain" tells me the graph is for someone who already
  knows the system.
- **Any consequence figures.** No death toll, damage cost, population at risk or evacuation
  anywhere. That is the number my board asks for first.

## My signature question

**Sentences I would have to translate for a trustee: 11 across the pages I opened, containing
at least 9 occurrences of words I do not have** — digital twin (twice), reanalysis, surrogate,
agentic (twice), cyberinfrastructure (twice), assimilation (twice), hydromechanical. Add
"multimodal", "liquefaction", "critical zone", "Stage IV precipitation mosaic", "quantitative
precipitation estimates", "physics-informed", "colocated" and "lahar", none of which a family
board will know.

The worst three, verbatim, with rewrites:

**1.** homepage — *"We build digital twins of the Earth — fusing open, multimodal data with AI
and cloud computing, all grounded in physical models — to monitor and forecast soil,
landslides, liquefaction, and floods."*
> "We put sensors on mountains and in rivers, and use computers to turn what they hear into a
> warning — before a hillside slides or a river floods."

**2.** `/funding.html` — *"It develops open, agentic cyberinfrastructure for real-time,
physics-aware geophysical data assimilation and multi-hazard prediction across Cascadia and
Alaska."*
> "It builds free, shared tools that pull in live measurements from across the Pacific
> Northwest and Alaska and turn them into forecasts of floods, landslides and ground failure —
> tools any researcher or agency can use."

**3.** `/book/problem-statement` — *"The severity of these hazards — landslides, flash floods,
earthquake liquefaction, and convective storms — is profoundly shaped by the soil
hydromechanical history and by land management practices"*
> "How bad these disasters get depends on two things we can actually measure: how wet the
> ground already was, and how the land has been used — logged, burned, built on."

Honourable mentions I would also have to translate: *"Exploring memory effects in the critical
zone with soil reanalysis products and event catalogs"*, *"Physics-informed and surrogate ML
models for hazard prediction and pattern discovery"*, and *"The agentic-AI layer — a
cross-disciplinary translator, agentic data downloaders, and research-software agents."* That
last is a sentence about a translator that itself needs translating.

**Where I land:** I would ask for a call. Not because the site convinced me — it did not — but
because the Rainier flood work, the Paros Center's presence and the Orting corridor add up to
something a family board could understand if a human being spent thirty minutes explaining it.
I would go into that call asking two questions: what did the Paros gift actually produce, and
what would three hundred thousand dollars buy that NSF will not pay for.
