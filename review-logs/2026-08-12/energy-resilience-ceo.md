# Review: CEO of a grid and energy resilience company

**Reviewed:** 2026-08-12 · **Scope:** landing page, `book/pillar-3-forecasting-susceptibility`, `book/problem-statement`, `book/organization`, `book/how-we-work`, `book/decisions`, `book/licensing`, `book/faq`, `people.html`, `funding.html`, `dashboard.html`, the GitHub organisation profile and the `seis-hydro-2-sed` repository · **Time spent:** 10 minutes

> I am a simulated reviewer, not a real one. This persona was constructed to catch obvious failures before real readers meet them. Every finding here is a hypothesis about how a commercial reader would react, not evidence that one did.

## In one paragraph

I came here to find out whether there is a partnership in this for us, and who I would call about it. Sixty seconds in I could tell you roughly what GAIA is — they build models of the Earth that fuse sensor data and AI to watch and forecast landslides, floods and soil failure — and that is better than most university sites manage. What I could not tell you, after ten minutes, is what it does better than what my team already buys, by how much, or who is on the other end of the phone. The "People" page names nobody. The only performance figures on the site are four counts of the project's own size, one of which is the infinity symbol. The forecasting chapter, the one that should carry the single number I care about, gives me "hours/days" and then tells me the rest is still to be written. I would not forward this to my VP of engineering today; there is nothing in it he could act on. I would forward it in a heartbeat if the landing page carried one sentence of the form "we give N hours of additional warning on shallow landslides in western Washington, validated against M events", and a named person under it. The science is plainly in the right place. The site is written for people who already work on it.

## Weighted score: 60/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 30 | I can say what it is; I cannot say what it changes |
| D2 Credibility of claims | 2 | 20 | Real funding, real code, but not one performance number |
| D3 Navigation and information scent | 3 | 15 | Labels are conventional and worked; two of them lead to empty rooms |
| D4 Visual design and accessibility | 4 | 10 | Looks like a company site, not a faculty page — a genuine asset |
| D5 Technical depth and reproducibility | 4 | 5 | Outside my competence, but licence, install steps and an honest maturity warning are visible |
| D6 Governance and openness | 3 | 5 | Permissive licences, decisions of record, all four still "proposed" |
| D7 Activity and durability | 4 | 10 | Commits this week, three NSF awards, 26 repositories |
| D8 Relevance to me | 2 | 5 | My hazards, my geography, nothing addressed to a buyer |

## Findings

### 1. There is no performance number anywhere on the site — BLOCKER · D2

**Where:** https://gaia-hazlab.github.io

**Saw:** The only figures presented on the landing page are "4 — Coupled hazard use cases", "3 — Earth systems linked", "14+ — Researchers & partners", "∞ — Sensors, one platform".

**Why it matters to me:** Every one of those numbers describes the project, not its output. I count staff and use cases to size a vendor, not to justify a hardening spend to a regulator. My rule is that a site with no concrete performance figure anywhere ends my evaluation, and this one triggers it. Lead time, hit rate, false-alarm rate, spatial resolution, anything falsifiable — one number would change my whole reading of this page.

**Suggested fix:** Replace one of the four counters with a real result, even a preliminary one, with its date and the event it was measured against. "12 h median warning, 2025 western Washington event" beats "∞ sensors" by an enormous margin.

**Confidence:** high

### 2. The People page names no people — BLOCKER · D1

**Where:** https://gaia-hazlab.github.io/people.html

**Saw:** Under the heading "People of GAIA HazLab", the section "Team members" contains one line: "Principal investigators, postdocs, students, and staff driving the project." No individual is named anywhere on the page. The only contact route is a `mailto:mdenolle@uw.edu` link.

**Why it matters to me:** I do not partner with institutions, I partner with people. I need to know who leads this, whether they are senior enough to sign anything, and whether they have done this before. A page titled "People" that lists none is worse than no page — it tells me the project has not decided how it presents itself to outsiders. I have an email address with no name attached to it, which means my first message has to open by asking who I am writing to.

**Suggested fix:** Four to six named people with a one-line role each, institution, and a photo. The PI first, with a direct email. This is an afternoon of work and it is the single highest-value fix on the site.

**Confidence:** high

### 3. The lead time — the one number that decides whether you are useful to us — is a range in a draft chapter — MAJOR · D2

**Where:** https://gaia-hazlab.github.io/book/pillar-3-forecasting-susceptibility

**Saw:** "The forecast couples the nowcast with weather nowcast/forecast and climate scenarios to project hazard susceptibility into the future — from hours/days (operational warning) to seasonal and climate-scenario timescales (scenario exploration)." The page then presents itself as draft scaffolding, with sections marked as content still to be added, and gives no skill score or validation result.

**Why it matters to me:** "Hours/days" spans a factor of fifty, and the difference between six hours and three days is the difference between a work order and a press release. This is the page I was sent to for the number that determines whether the work is operationally useful to us, and it does not have one. I do not object to the answer being early — I object to not being told what it currently is.

**Suggested fix:** State the current achieved lead time for one hazard at one site, with the caveat attached. "Today: 6–18 h on shallow landslides at the Stehekin site, unvalidated" is a usable sentence. A range with no anchor is not.

**Confidence:** high

### 4. The landing page never says where in the country this works — MAJOR · D1

**Where:** https://gaia-hazlab.github.io and https://gaia-hazlab.github.io/book/problem-statement

**Saw:** The landing page names no place. The geography appears only after clicking into the book, where the problem statement names "2025 Western Washington Floods & Landslides", "2001–2031 Nisqually Earthquake" and "2025 Stehekin Post-fire Debris Flow" in the "Stehekin watershed".

**Why it matters to me:** The first thing I do with any hazard product is ask whether it covers my customers' service territory. Western Washington is a real, checkable answer and it is a good one — atmospheric river country with transmission corridors through unstable ground is exactly our problem. Burying it two clicks deep costs you readers who close the tab assuming it is generic. Nowhere did I find a statement of what it would take to extend this to a different region, which is the second question I would have asked.

**Suggested fix:** Put "Currently: western Washington — Stehekin, Nisqually, Puget lowlands" on the first screen, and add one paragraph on portability: what is site-specific, what is not, what new region requires.

**Confidence:** high

### 5. Nothing on this site is addressed to a company — MAJOR · D8

**Where:** https://gaia-hazlab.github.io/book/faq and https://gaia-hazlab.github.io/book/organization and https://gaia-hazlab.github.io/book/how-we-work

**Saw:** The FAQ sections cover "Taking part", "Citing and acknowledging", "How the project runs" and "Documents and tooling" — tool listings, acknowledgment wording, co-authorship, meeting access, Slack privacy. The collaboration is described as three academic institutions: University of Washington, University of Alaska Fairbanks, and the EarthScope Consortium. No industry partner, commercial user, or external service arrangement is mentioned on any page I opened.

**Why it matters to me:** The FAQ answers the questions the project has, not the questions its readers have. Mine are: has anyone outside a university used this, what happened, and would we be the first? I could not answer any of them. Being the experiment is not automatically a no — but I need to know that is what I am being offered, and right now the site does not acknowledge the question exists. *(Inference: that no industry precedent is stated does not prove none exists.)*

**Suggested fix:** One FAQ entry — "Can a company use this?" — answering licence, support expectations, and whether you want commercial partners. Three sentences. If the honest answer is "we have not done this yet and would like to", say that.

**Confidence:** medium

### 6. The contact route is an unnamed email in the footer — MAJOR · D3

**Where:** https://gaia-hazlab.github.io

**Saw:** A single `mailto:mdenolle@uw.edu` link on the landing page, below the fold in the footer alongside "© 2026 GAIA HazLab · University of Washington · Licensed under the MIT License." The two calls to action above the fold are "Explore the Dashboard" and "▶ See it live", neither of which leads to a person.

**Why it matters to me:** A raw email is better than a contact form, so this does not quite end my visit — but it took me longer than a minute to be sure that was the only route, and I still do not know whose inbox it is. Counting clicks from landing to a meaningful contact: two, and the destination is a page with no names on it. The two things I most wanted, a value number and a person, are the two things not on the first screen.

**Suggested fix:** Add a named contact line to the landing page near the calls to action — name, role, email. Not a form.

**Confidence:** high

### 7. The decisions of record shipped with a placeholder date — MAJOR · D2

**Where:** https://gaia-hazlab.github.io/book/decisions

**Saw:** Four decisions, GAIA-D-001 through GAIA-D-004. GAIA-D-001 shows "**Date:** — · **Status:** proposed" and records "Decided at: kickoff call, 2026-08-__", with the day left as an unfilled placeholder. All four are "proposed".

**Why it matters to me:** I am not technical enough to review code, but I know what an unfilled template field looks like, and I read it as a page published before it was finished. On a page whose whole purpose is to show that decisions are recorded and dated, a blank date does the opposite of its job. It also makes me wonder how much else on this site is scaffolding I have not spotted.

**Suggested fix:** Fill the date or delete the field. If nothing has been ratified yet, label the page "Proposed decisions — none ratified as of 2026-08" so the status is deliberate rather than accidental.

**Confidence:** high

### 8. The headline is poetry and the proposition is three lines down — MINOR · D1

**Where:** https://gaia-hazlab.github.io

**Saw:** "Smart sensing of the living Earth", then "Predictive understanding of weather-compounded geohazards.", then "We build digital twins of the Earth — fusing open, multimodal data with AI and cloud computing, all grounded in physical models — to monitor and forecast soil, landslides, liquefaction, and floods."

**Why it matters to me:** The third line is the good one and it is doing all the work. The first tells me nothing and the second is an abstract noun phrase. If I had bounced after five seconds instead of sixty I would have left with nothing. *(This is partly taste — reasonable people like an evocative headline, and I am not one of them.)*

**Suggested fix:** Promote the third sentence, cut it to its first fifteen words, and demote "Smart sensing of the living Earth" to a strapline.

**Confidence:** medium

### 9. The primary call to action leads to a prototype — MINOR · D2

**Where:** https://gaia-hazlab.github.io/dashboard.html

**Saw:** The page describes itself as "Prototype — inline Leaflet map", shows "Loading the GAIA CRESST catalog…", and states that the catalog will carry "every layer from the catalog (plus geodetic, coming soon)". No sensor values or measurements are displayed. Coverage is given as "Washington State regions of interest".

**Why it matters to me:** "Explore the Dashboard" is the first button on the site, so this is where a lot of readers land first. I am glad it says "prototype" rather than pretending — that honesty is worth something. But sending your best-positioned button to a page with no numbers on it wastes the click. I would rather the button said "Explore the dashboard (prototype)" and I arrived with the right expectation.

**Suggested fix:** Label the state on the button, and put one real measured value on the dashboard even if it is a single station.

**Confidence:** medium

### 10. Words I do not know, used without explanation — MINOR · D1

**Where:** https://gaia-hazlab.github.io/book/pillar-3-forecasting-susceptibility and https://gaia-hazlab.github.io/funding.html

**Saw:** On the forecasting chapter: "nowcast", "assimilation", "uncertainty propagation", "reduced-order models", "ROC / precision-recall", "climatology baselines". On the funding page: "Cyberinfrastructure for Sustained Scientific Innovation (CSSI)", "physics-aware geophysical data assimilation".

**Why it matters to me:** I run a company that sells hazard services to utilities and I do not know what "assimilation" or "cyberinfrastructure" mean in your sense. That is a fact about your audience, not a gap in me — my VP of engineering might follow these, but he only opens the link if I forward it, and I forward what I understand. "Nowcast" I can guess from context, which is not the same as knowing.

**Suggested fix:** A one-line gloss on first use in each chapter, or a short glossary linked from the book's front page. "Assimilation: continuously correcting a physical model with incoming sensor data" costs one sentence.

**Confidence:** high

### 11. "∞ Sensors, one platform" — POLISH · D2

**Where:** https://gaia-hazlab.github.io

**Saw:** The fourth statistic in the landing page counter row is the infinity symbol, labelled "Sensors, one platform".

**Why it matters to me:** Sitting in a row with three real counts, this reads as a number that was not available. It is a small thing and it does not change my decision, but it is in the most quantitative-looking element on the page, which is precisely where I am looking for something I can trust.

**Suggested fix:** Use the actual count of ingested stations or streams. If it varies, "1,200+ stations ingested daily" is both true and more impressive than infinity.

**Confidence:** medium

## What worked

**The site does not look like an academic project page.** The typography, the UW purple palette, the hero treatment and the structure of the landing page are closer to a company site than to the faculty pages I usually get sent. That matters more than the team probably thinks: it is the reason I gave this ten minutes instead of thirty seconds. Protect it.

**The funding is exactly what a regulator would accept.** https://gaia-hazlab.github.io/funding.html names "OAC‑2608509, 2608510, and 2608511" under the NSF "Cyberinfrastructure for Sustained Scientific Innovation (CSSI)" programme, plus the Fund for Future Science & Technology and the "Jerome & Linda Paros Geohazard Center". Three federal award numbers and named institutions are citable in a rate filing. This is the strongest credibility asset on the site and it is on a page nobody will reach — consider a line of it on the landing page.

**The project is visibly alive.** https://github.com/gaia-hazlab shows 26 repositories with commits dated within the last two days at the time of this review, and the multi-year NSF awards give me a reason to think it exists in three years. Most things I get sent went quiet eighteen months ago.

**The code is honest about its own maturity.** https://github.com/gaia-hazlab/seis-hydro-2-sed carries an MIT licence, three installation routes, and the warning "The interface may change without warning. Ask before building on this — an issue is how something moves from incubating to stable." I cannot judge the code, but I can judge that sentence, and it is the kind of thing that makes me trust the rest. The `gaia-stable · gaia-incubating · gaia-archived` taxonomy on https://gaia-hazlab.github.io/book/organization is a good idea. It is invisible on the public site — pull it forward.

## What I could not judge

- Whether any of the code is correct, well-engineered, or performant. I am not technical enough and did not try.
- Whether the science is right. I cannot assess whether coupling atmospheric, hydrologic and solid-Earth models is the correct approach or whether the physics is sound.
- Accessibility in any rigorous sense — contrast ratios, keyboard reach, screen-reader behaviour, alt text. I looked at the site and it read cleanly to me, which is not the same as testing it.
- Mobile rendering. I reviewed at desktop width and did not confirm phone behaviour.
- Whether the "14+ Researchers & partners" figure is accurate, since no partners are named anywhere I looked.
- I ran out of patience before opening `/presentations.html`, `/book/graph/gaia-knowledge-graph.html`, and the hazard-specific chapters on landslides and liquefaction. Those may well contain the number I said was missing. If they do, it is in the wrong place — I spent my whole budget and never reached them.

## My signature question

*In one sentence a utility executive would understand: what does this change, and by how much?*

I cannot answer it from this site, and that is my headline finding: GAIA can tell me what it studies, where it is funded from and that it is genuinely active, but not one page tells me what decision gets better or by what margin, so the sentence I would have to write to my VP of engineering — "they give you N more hours on landslide risk in your corridors" — has a hole in it where the number goes, and without that number the forward does not happen.
