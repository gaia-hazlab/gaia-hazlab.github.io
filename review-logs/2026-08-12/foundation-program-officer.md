# Review: Family foundation program officer and donor advisor

**Reviewed:** 2026-08-12 · **Scope:** `https://gaia-hazlab.github.io` (landing), `/book/problem-statement`, `/book/how-we-work`, `/book/faq`, `/people.html`, `/funding.html`, `/dashboard.html`, `/presentations.html`, and the `github.com/gaia-hazlab` organisation profile with its repository list · **Time spent:** 10 minutes

> I am a simulated reviewer, not a real one. I am a persona constructed to catch obvious failures before real readers meet them. Every finding here is a hypothesis about a real program officer, not evidence about one.

## In one paragraph

I came here because a trustee asked me to look, and I was trying to answer one question: if we put a few hundred thousand dollars into this, what changes? I still cannot answer it. The science is real — the problem statement names actual places and actual disasters, which most proposals I read never manage — and the governance writing is better than anything else in my current portfolio. But the two pages a donor needs are the two that failed me. The people page lists no people at all, and the funding page tells me who has already given without telling me what any of it produced, what a private gift could do that the federal award cannot, or how to reach anyone. I fund people, and after ten minutes I do not know a single one of their names. I would not take this to my board yet. I would send one email asking who runs this and what the Paros gift actually bought, and I would look again in three months.

## Weighted score: 66/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 30 | Second paragraph is excellent; the first is jargon, and no human being appears in either |
| D2 Credibility of claims | 3 | 20 | Named events and real award numbers, but no dated outcome anywhere and an empty dashboard |
| D3 Navigation and information scent | 3 | 15 | I found the pages I wanted; nav changes between them and there is no contact route from funding |
| D4 Visual design and accessibility | 4 | 20 | Clean, calm, mobile viewport set on every page, alt text on every logo — this reads fine on my phone |
| D5 Technical depth and reproducibility | 3 | 0 | Not judged. Outside my competence; weighted zero for me |
| D6 Governance and openness | 4 | 5 | Published governance with missed targets included, a decisions register, MIT licence |
| D7 Activity and durability | 4 | 5 | Repositories updated within the last two days; a five-year federal award behind it |
| D8 Relevance to me | 3 | 5 | Right portfolio, wrong language — nothing here is framed around who gets hurt |

## Findings

### 1. The team page has no team on it — BLOCKER · D1
**Where:** `https://gaia-hazlab.github.io/people.html`
**Saw:** Under the heading "Team members", the entire content is one line: "Principal investigators, postdocs, students, and staff driving the project." No names follow. No photographs. The page then moves straight to "Join our team". The only individual named anywhere on the site is "PI Erkan Istanbulluoglu", on the funding page, in a sentence about a different award.
**Why it matters to me:** This is the page I open second, every time, on every project. Family foundations do not fund institutions or platforms — they fund people, and my board will ask me who they are and whether I met them. I said before I started that a team page without faces reads as an org chart. This is not even an org chart, it is an empty room, and there is no other route on the site to find out who these people are. I cannot write a recommendation that says "the team is" and then stop.
**Suggested fix:** Ten to fifteen entries. Photograph, name, one line of what that person actually does on this project, institution. That is an afternoon of work and it is the single highest-value afternoon available on this site.
**Confidence:** high

### 2. Nothing tells me what a private gift would do that the federal award cannot — MAJOR · D1
**Where:** `https://gaia-hazlab.github.io/funding.html`
**Saw:** The page's framing sentence is "GAIA HazLab is built on complementary investments — from the seed that launched the idea, to the federal award now driving it, to the philanthropy and programs that anchor its flagship applications." Every entry below it is retrospective. There is no paragraph about what is unfunded, what is next, or what philanthropy is for here.
**Why it matters to me:** With an NSF award already in hand, my first question at the board table is "why do they need us?" Federal money is slow, restricted, and will not touch some of the most valuable things — travel to talk to county emergency managers, a year of someone's salary at risk, hardware in the ground before an award exists. If that is the answer, say it. If the honest answer is that philanthropy is not needed, say that too and I will close the tab with respect rather than confusion.
**Suggested fix:** One short section on `funding.html` headed something like "What private support makes possible", naming two or three specific things with rough costs, and a named person's email under it. Right now there is no `mailto:`, no contact link, and no donate route anywhere on that page.
**Confidence:** high

### 3. No account of what any previous gift produced — MAJOR · D2
**Where:** `https://gaia-hazlab.github.io/funding.html`
**Saw:** "The Jerome and Linda Paros Geohazard Center supports GAIA's Mount Rainier flagship — integrating dense geophysical and geodetic observation with real-time hazard modeling at one of the Pacific Northwest's highest-risk volcanoes."
**Why it matters to me:** That is a description of scope in the present tense, not an account of a result. How a project treats its last donor is the best available predictor of how it will treat me, and what I am reading is the sentence the Paros Center would have written in its own grant letter, played back. Compare the FFST entry, which does better — "funded the early prototypes, community building, and proof-of-concept that matured into the CSSI project" — that at least tells me a gift turned into something. Even that has no date and no number.
**Suggested fix:** One added sentence per funder, past tense, with a date: what exists now because of that money. "The Paros gift put N instruments on Rainier in 2025; the first N months of data are here." A link is better than an adjective.
**Confidence:** high

### 4. The dashboard, offered as the main call to action, showed me nothing — MAJOR · D2
**Where:** `https://gaia-hazlab.github.io/dashboard.html`
**Saw:** The landing page's primary buttons are "Explore the Dashboard" and "See it live". The dashboard page itself carries "Loading the GAIA CRESST catalog…", labels itself "Prototype — inline Leaflet map", and describes geodetic data as "coming soon". I saw no data, no timestamps, no counts, no results.
**Why it matters to me:** This is the one place on the site where I could have seen the project doing what it said rather than planning to, and it is also the destination the landing page pushes hardest. I want to open something on my phone in front of a trustee and have it show a real hillside with real numbers on it. Instead the loudest button on the site leads to a page that says it is a prototype. I cannot tell whether it is broken or simply unfinished, and from where I sit that distinction does not help.
**Suggested fix:** Either put a small number of live counts at the top of the page that render without waiting on the catalog — stations reporting, days of data, last update time — or retitle the button honestly ("See the prototype map"). An overpromising button is worse than a modest one.
**Confidence:** high

### 5. A public deck framing this science as a financial instrument sits alongside the ask for philanthropy — MAJOR · D8
**Where:** `https://gaia-hazlab.github.io/presentations.html`
**Saw:** The first listed presentation is "Priced by Physics", dated July 2026, 34 slides, described as covering "high-resolution hazard science as a financial instrument—from catastrophe insurance to groundwater markets".
**Why it matters to me:** I am not against earned revenue and I would not hold this against them privately. But my board will find this page, and the question I will be asked is whether we are subsidising the research-and-development phase of something that will later be sold to insurers. That is a legitimate question and it deserves a stated answer on the site rather than an inference from a slide deck title. **This is my inference, not an observation** — the deck may say something entirely different, and I did not open it.
**Suggested fix:** One line on the funding page stating the intent: what stays open and free, what if anything is intended to be commercialised, and who benefits. Projects that say this out loud are easier to fund, not harder.
**Confidence:** medium

### 6. The first sentence I read is the one I understand least — MAJOR · D1
**Where:** `https://gaia-hazlab.github.io`
**Saw:** Headline: "Smart sensing of the living Earth". First body sentence: "We build digital twins of the Earth — fusing open, multimodal data with AI and cloud computing, all grounded in physical models — to monitor and forecast soil, landslides, liquefaction, and floods." The phrase "digital twin" appears six times on the landing page. "Agentic" appears twice, "STAC" twice, "assimilation", "reanalysis", "surrogate" and "multimodal" once each. None is glossed.
**Why it matters to me:** I could not read that opening aloud to a trustee without stopping twice. And it is a real shame, because the *second* paragraph is one of the best openings I have read this year — "The most devastating disasters are coupled. Landslides from atmospheric rivers, liquefaction in saturated soils, debris flows after wildfire, storms fed by the land surface." That is plain, vivid and true. It is sitting in second place behind the sentence that loses me.
**Suggested fix:** Swap them. Lead with the coupled-disasters paragraph, and keep the digital-twin sentence for the About page where a reader has already decided to care.
**Confidence:** high

### 7. Nobody is harmed in this story — MAJOR · D1
**Where:** `https://gaia-hazlab.github.io` and `https://gaia-hazlab.github.io/book/problem-statement`
**Saw:** The problem statement's account of the failure is "Our models do not resolve those cascades. Atmosphere, hydrology, and geomechanics are studied and modeled separately, and the couplings between them fall in the gaps." The landing page sections are "What we sense", "The platform", "How it all connects", "Bringing partners back", "The team".
**Why it matters to me:** Every actor in this story is a model or a dataset. There are no communities, no emergency managers, no homeowners, no county planner deciding whether to close a road at two in the morning. The stated problem is a gap between disciplines, which is a problem for scientists. My board funds harm reduction; they will want to know who gets a warning they do not currently get, and how much earlier. That person does not appear anywhere I looked.
**Suggested fix:** One sentence naming the decision-maker and the decision, on the landing page. "When an atmospheric river is forecast, a county emergency manager has to decide which roads to close, and today has almost nothing to go on." That costs one line and changes the whole register.
**Confidence:** high

### 8. Navigation changes from page to page — MINOR · D3
**Where:** `https://gaia-hazlab.github.io/funding.html` compared with `https://gaia-hazlab.github.io` and `/people.html`
**Saw:** The landing page nav reads "About, Science, Demos, Technology, Dashboard, Presentations, People, Funding, Docs". The people page nav drops "Demos". The funding page nav drops both "Demos" and "Presentations", reading "About, Science, Technology, Dashboard, People, Funding, Docs".
**Why it matters to me:** Small, but I noticed it because I went looking for the talks after the funding page and the link had vanished. It reads as hand-maintained pages drifting apart, which is a proxy for other things drifting.
**Suggested fix:** One shared nav include across all four top-level pages.
**Confidence:** high

### 9. The presentations page is thin and half of it is unattributed — MINOR · D7
**Where:** `https://gaia-hazlab.github.io/presentations.html`
**Saw:** Two entries. "Priced by Physics", attributed to "GAIA Hazard Lab", July 2026. "Data assimilation, simplified", with no speaker, no venue and no date.
**Why it matters to me:** I use talk lists as a cheap activity signal — who is out in the world saying this, and to whom. Two entries, one undated and with no named speaker, tells me almost nothing. The repository list on GitHub told me far more about whether this project is alive.
**Suggested fix:** Add venue, date and named speaker to every entry, and backfill conference talks from the past year. If they have not given any, that is worth knowing too.
**Confidence:** high

### 10. A date range on the problem statement reads as a typo — POLISH · D2
**Where:** `https://gaia-hazlab.github.io/book/problem-statement`
**Saw:** A use case titled "2001–2031 Nisqually Earthquake".
**Why it matters to me:** I know very little geology, but I do know an earthquake happens on a day, not over thirty years. If it means a study window, it does not say so. Small errors on a page I cannot check make me wonder about the pages I *really* cannot check.
**Suggested fix:** "Nisqually earthquake (2001), with a 2001–2031 study window" or whatever the intended meaning is.
**Confidence:** medium

## What worked

**The use cases are real places with real dates.** `book/problem-statement` gives me "2025 Western Washington Floods & Landslides" — "Atmospheric river–driven flooding and landslides across western Washington, linking precipitation extremes, soil saturation history, and sediment transport from mountain to sea" — and "2025 Stehekin Post-fire Debris Flow", described as sitting "in the Stehekin watershed, where fire-altered soil properties interact with storm precipitation to trigger catastrophic mass movements." Named place, named cause, named consequence. Most proposals I read never get past "the region". This is the material I would build the whole landing page from.

**The governance writing is the best I have seen in this portfolio.** `book/how-we-work` opens with "Most research projects keep their governance internal. GAIA publishes theirs for three reasons", and includes "publishing the targets we have not met, next to those we have, keeps the record honest." The FAQ answers "Why is the dashboard showing numbers below target?" with "Because hiding them would make the rest of the dashboard worthless." I would quote that line to other grantees. I did not open the decisions register itself, so I am judging the promise rather than the practice.

**It reads well on a phone.** Every page I checked carries `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, every sponsor logo carries real alt text rather than a filename, and the type and colour are calm and legible. I read this between meetings on a phone and never had to pinch to zoom. This is a matter of taste in part, but the accessibility basics are not — those are done properly.

**The project is visibly alive.** The GitHub organisation shows repositories updated on 10 and 11 August 2026, two days before I looked, across nine or ten projects with human descriptions like "turn river discharge and seismic power to predict dynamic bedload transport". Combined with a multi-award federal grant, I have no doubt this exists in three years.

## What I could not judge

- Whether any of the science is correct, novel, or better than what already exists. I have a policy background. I would need an external reviewer and I have said so to my board before.
- Whether the software actually runs, whether the models are validated, or whether the repositories contain what their descriptions claim. Explicitly outside my competence and weighted zero for me.
- Whether the Paros Center is satisfied with how it has been treated. I am inferring from a web page. The right move is to ask them, and I would.
- What "Priced by Physics" actually argues. I read the one-line description on the presentations page and did not open the deck.
- Whether the empty people page is an authoring gap or a page that failed to render for me. Either way it is what a reader gets, so I have recorded it as what I saw.
- Contrast ratios and keyboard reach, properly measured. I formed an impression; I did not test.

## My signature question

*Count the sentences I would have to translate for a trustee. Quote the worst three verbatim, and rewrite each in plain words.*

**Thirteen**, across the landing page, the funding page and the problem statement. Roughly one sentence in four on the landing page. The three worst:

**1.** "We build digital twins of the Earth — fusing open, multimodal data with AI and cloud computing, all grounded in physical models — to monitor and forecast soil, landslides, liquefaction, and floods." (`https://gaia-hazlab.github.io`)

> *We build a working computer copy of a real landscape, fed by live sensors, weather records and satellite data, so we can watch a hillside or a floodplain change and give warning before it fails.*

**2.** "Explore memory effects in the critical zone with soil reanalysis products and event catalogs." (`https://gaia-hazlab.github.io`, "What we sense")

> *Soil remembers. Ground already soaked by last month's rain fails faster in this month's storm, and we track that history so a forecast knows what state the hillside was in before the rain started.*

**3.** "It develops open, agentic cyberinfrastructure for real-time, physics-aware geophysical data assimilation and multi-hazard prediction across Cascadia and Alaska." (`https://gaia-hazlab.github.io/funding.html`)

> *We are building free, shared software that takes sensor readings as they arrive, checks them against the physics of how ground and water actually behave, and turns them into live hazard warnings for the Pacific Northwest and Alaska.*

Six of my thirteen are the phrase "digital twin" alone. If one change were made to this site, it would be to gloss that phrase once, in the first sentence it appears, in eight words.
