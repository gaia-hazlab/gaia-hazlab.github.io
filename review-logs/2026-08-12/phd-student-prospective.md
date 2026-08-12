# Review: Prospective PhD student choosing a thesis foundation

**Reviewed:** 2026-08-12 · **Scope:** gaia-hazlab.github.io landing page; /book and the chapters problem-statement, research-software, how-we-work, organization, decisions, licensing, faq; people.html, funding.html, dashboard.html, presentations.html; the github.com/gaia-hazlab organisation profile and three repositories I picked myself — landlab-debrisflow, seis-hydro-2-sed, gaia-cli — plus an org-wide check of licence and CITATION.cff presence · **Time spent:** 30 minutes (budget spent; I stopped)

*I am a simulated reviewer, not a real one. I am a persona constructed to catch obvious failures before real readers meet them. Everything below is a hypothesis about how an eight-month-in PhD student would read this site, not evidence about one.*

## My sixty-second sentence

Written before I read anything else, not revised:

> "A University of Washington group that uses AI and cloud data to monitor and predict landslides, floods, liquefaction and soil conditions in Washington State. They say they build 'digital twins of the Earth', and I do not know what that means."

## In one paragraph

I came here because a paper cited a GAIA repository and I wanted to know whether I could put my second and third chapters on top of it. The answer I reached in thirty minutes is: the project is unambiguously alive, there are real graduate students on it whose email addresses I can get, and at least one repository installs three different ways without my emailing anyone. That is more than most lab sites give me, and it is enough that I would send the email. What stopped short of convincing me is everything about ownership. The repository closest to my thesis, `landlab-debrisflow`, has no LICENSE file at all. The flagship science repository, `seis-hydro-2-sed`, says "MIT License" in its README and ships no LICENSE file either. The FAQ told me the co-authorship policy is a numbered decision; the decisions register told me it is not numbered yet and will be settled at a September call whose date is written as `2026-08-__`. For me those are the same question — if I spend two years inside this organisation, do I own what I make and am I an author on it — and the site answers it twice, differently. My next step is to email Michael Hemmett or Manuela Köpfli, not Marine Denolle, and ask what happened the first time they put code into a GAIA repository.

## Weighted score: 62/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 15 | I got a repeatable sentence, but it runs through "digital twin", which is undefined here |
| D2 Credibility of claims | 2 | 10 | Two checkable claims are false, and the demo section contradicts itself in the same paragraph |
| D3 Navigation and information scent | 3 | 15 | Clean nav, findable FAQ and decisions register, but no on-ramp page for an outsider |
| D4 Visual design and accessibility | 3 | 10 | Readable; the roster exists only in JavaScript and one team photo 404s |
| D5 Technical depth and reproducibility | 3 | 25 | Real install paths in two repos, no licence in the one I would actually fork |
| D6 Governance and openness | 3 | 5 | Better written than most labs, but every decision is still "proposed" |
| D7 Activity and durability | 4 | 15 | Pushes yesterday and the day before, 33 repos, 22 org members, three NSF awards |
| D8 Relevance to me | 4 | 5 | Landslides plus machine learning is squarely what this is |

## Findings

### 1. The repository closest to my thesis has no licence — MAJOR · D5
**Where:** https://github.com/gaia-hazlab/landlab-debrisflow
**Saw:** The repository root file listing contains no `LICENSE`, `COPYING`, or `CITATION.cff`. GitHub's own licence detection returns null for it. The README does describe itself as a "Landlab-focused workspace for postfire terrain, ecohydrology, and landslide probability workflows" and gives working setup commands (`conda env create -f environment.yml`).
**Why it matters to me:** This is the one repository in the whole organisation that is about the thing my advisor told me to look into. Unlicensed code is not open code — my university's policy is that I cannot build a dissertation chapter on something with no licence, and I cannot ask a journal to accept a methods section that points at it. I would have to email someone and wait, which is exactly what the site is otherwise good at letting me avoid.
**Not a blocker because:** I would still evaluate the rest of the project, and the fix is one file. But it is the single thing most likely to end my adoption.
**Suggested fix:** Add MIT `LICENSE` and `CITATION.cff` to `landlab-debrisflow`. Across the organisation, 14 of 33 repositories currently have no licence GitHub can detect; the licensing chapter already says what to do, so this is a batch job, not a decision.
**Confidence:** high

### 2. "Every repository ships a CITATION.cff" is false — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/book/faq
**Saw:** "Yes. If a GAIA tool or dataset materially shaped your result, cite its DOI. Every repository ships a `CITATION.cff`. Citing software matters because infrastructure work is often under-represented in the citation record, and citing it is how that record stays accurate."
**Why it matters to me:** I checked all 33 repositories in the organisation. Two have a `CITATION.cff` — `seis-hydro-2-sed` and `geocroissant-hazards`. The claim is specific, dated by nothing, and checkable in about ninety seconds, and it does not hold. Once I catch one claim like that, I start treating the rest of the site as marketing, including the parts I cannot check.
**Suggested fix:** Either add the files or change the sentence to describe the target rather than the state — "every repository at level 2 and above ships a `CITATION.cff`; we are backfilling the rest." A dated statement of intent costs nothing and survives being checked.
**Confidence:** high

### 3. The FAQ and the decisions register disagree about whether the authorship policy exists — MAJOR · D2 / D6
**Where:** https://gaia-hazlab.github.io/book/faq and https://gaia-hazlab.github.io/book/decisions
**Saw:** FAQ: "The authorship policy is a numbered decision; see the decisions register." Decisions register: "Pending, not yet numbered — co-authorship policy and the openness/recording policy go to a comment window after the kickoff and are numbered when they ratify at the September project-wide call."
**Why it matters to me:** This is the question. Whether students go on software and dataset author lists or into acknowledgments is the difference between a chapter and a favour. The FAQ sent me to the register to find the answer, and the register told me the answer does not exist yet. That is worse than saying nothing, because I spent two of my thirty minutes finding out.
**Suggested fix:** Change the FAQ line to "The authorship policy is pending; it is expected to be numbered at the September 2026 project-wide call — see the decisions register." Then it is honest and it still points somewhere useful.
**Confidence:** high

### 4. Nothing about student credit on software or datasets in "How we work" — MAJOR · D6
**Where:** https://gaia-hazlab.github.io/book/how-we-work
**Saw:** The section headings are "The collaboration", "1. What we are accountable for", "2. Why we measure", "3. What happens when a target is missed", "4. What we record, and why", "5. What is public, and what is not", "6. What we do with all of it", "7. Agents, and the rule that makes the claim checkable", "8. Changing any of this". None of them is about authorship or credit. The page does say "over five years, postdocs and students cycle through while the PI is the only continuous thread."
**Why it matters to me:** I went to this page specifically to find out whether students appear as authors on software and data, and it is not there. And the one sentence that mentions students frames us as the part of the system that churns. That is honest about the staffing problem and it is not reassuring about whose name ends up on the artifacts.
**Suggested fix:** Add a short numbered section to "How we work" — even three sentences — on who is listed as an author of a repository, a dataset, and a release, and link it from the FAQ.
**Confidence:** high

### 5. Every promised capability is undated and has no named owner — MAJOR · D7
**Where:** https://gaia-hazlab.github.io (demos section) and https://gaia-hazlab.github.io/book/decisions
**Saw:** On the landing page: "Live demo coming soon", "Interactive, real-time slope-failure forecasting — currently in build. Check back soon for the live panel.", "In compilation", "live panel coming soon", "preview in preparation". On the decisions page, every one of the four entries is marked "proposed", and GAIA-D-001 reads "Date: — · Decided at: kickoff call, 2026-08-__ · Status: proposed".
**Why it matters to me:** This is my signature question in one screenshot. `2026-08-__` is a literal unfilled blank on a live page. I cannot plan four years against "soon". I am not asking for a guarantee — I am asking for one name and one month per promise so that in six months I can tell whether the project keeps its word.
**Suggested fix:** Put an owner and a target month on each "coming soon" panel, and fill in or remove the `2026-08-__` blank. Missing a stated date is survivable; having no date at all is what I cannot evaluate.
**Confidence:** high

### 6. The demo section calls itself real time on the same screen as "coming soon" — MAJOR · D2
**Where:** https://gaia-hazlab.github.io
**Saw:** "Each demo is a working slice of the GAIA stack applied to a real, coupled-hazard use case — real events, real sensors, real time." Directly below it, the second demo card reads "Live demo coming soon" and "Shallow-landslide digital twin — Interactive, real-time slope-failure forecasting — currently in build."
**Why it matters to me:** One of the two demos is real and one is a picture of a plan, and the sentence above them says both are real. My persona's stopping rule is "documentation that describes a system that does not exist yet, without saying so." They do say so, three lines later, which is why I did not stop. But the header sentence is doing the opposite work from the cards under it.
**Suggested fix:** Move "real events, real sensors, real time" onto the WA-2025 card, where it is true, and let the landslide card say what it is: in build.
**Confidence:** high

### 7. There is no way in for someone without an invitation — MAJOR · D3
**Where:** https://gaia-hazlab.github.io/people.html, https://gaia-hazlab.github.io/book/organization, https://gaia-hazlab.github.io/book/faq
**Saw:** The people page's "Join our team" block says "We are always looking for talented, curious people who want to work at the intersection of geoscience, physics, and AI", and its only contact is a "Get in touch" button pointing at `mailto:mdenolle@uw.edu`. I searched the landing page, "How we work", "The organisation", the FAQ and "Research software" for "good first issue", "getting started", "onboarding" and "office hours" and found zero hits on all four. "hackweek" appears once, in "How we work", not as an event I could attend.
**Why it matters to me:** Every route in goes through the PI. I am not going to cold-email a PI at another university to ask whether her software works — that is a conversation I would have to be somebody to start. What I want is a `good first issue` label, or a tutorial notebook with a "start here" at the top, or a monthly open call with a date on it. The FAQ does say the monthly project-wide update is open to unsupported collaborators, which is exactly the right thing, but I found it on page four of the book rather than next to "Join our team".
**Suggested fix:** Put the "you can join the monthly update" line on `people.html` next to the join block, with the date and the joining link, and add a `good-first-issue` label to two repositories.
**Confidence:** medium — this is partly about my own reluctance to email a PI, which another student might not share.

### 8. The flagship science repository claims MIT in prose and ships no LICENSE file — MAJOR · D5 / D6
**Where:** https://github.com/gaia-hazlab/seis-hydro-2-sed
**Saw:** The README contains a "## License" heading followed by "MIT License". The repository root file listing contains `CITATION.cff` but no `LICENSE`, and GitHub's licence detection returns null. Meanwhile https://gaia-hazlab.github.io/book/licensing states that new repositories "should include `LICENSE` files created via GitHub's template picker and maintain consistent declarations in `CITATION.cff` files and READMEs."
**Why it matters to me:** This is the repository the book's own table of contents links to as a use case, and it is the one whose install instructions actually work. A licence named only in a README is the kind of thing my department's research-computing person tells me not to rely on. The project has written down the right rule on its own licensing page and has not applied it to its most visible repository.
**Suggested fix:** Add the `LICENSE` file. It is a two-minute fix on the repository that most readers will land on first.
**Confidence:** high

### 9. The team roster exists only in JavaScript, and one member's photo 404s — MINOR · D4
**Where:** https://gaia-hazlab.github.io/people.html
**Saw:** The served HTML contains the heading "Team members" and the line "Principal investigators, postdocs, students, and staff driving the project." followed by an empty container. The roster is injected by `js/team-loader.js`, which does `fetch('data/team.json')`. That file loads and contains 24 people, including four PhD students in Earth and Space Sciences with `@uw.edu` addresses. One entry, Hunter Jimenez, has `"photo": "/images/team/XX"` — which returns 404 — and no email.
**Why it matters to me:** With JavaScript on, this page answers my most important question well: there are students, several of them, at my career stage, and I can email them. That is the thing that would make me convert. But it is invisible to anything that does not run scripts, and one card renders as a broken image with no contact. **Observation:** the file 404s. **Inference, marked as such:** a reader on a bad connection or a locked-down browser sees a team page with no team, which reads much worse than it is.
**Suggested fix:** Replace `/images/team/XX` with a real photo or a neutral placeholder, add Hunter Jimenez's email, and consider baking the roster into the HTML at build time so it survives without JavaScript.
**Confidence:** high

### 10. Words I do not know, used without definition and with no glossary — MINOR · D1
**Where:** https://gaia-hazlab.github.io and https://gaia-hazlab.github.io/book/problem-statement
**Saw:** The landing page uses "digital twin" or "digital twins" six times, starting in the hero — "We build digital twins of the Earth" — and never defines it. Across the pages I opened I also counted `reanalysis` (landing page, DataHub), `FAIR` (problem statement, "How we work", HazEvalHub, decisions), `surrogate model` (problem statement, ModelHub, people page), `cyberinfrastructure` (funding page, "How we work"), `STAC`, `provenance`, `held-out` and `thrust`. A search for "glossary" across the landing page, "How we work", "The organisation", the FAQ and "Research software" returns nothing.
**Why it matters to me:** I have used ObsPy and xarray and I can write Python. I still do not know what a digital twin is in a way I could defend at a committee meeting, and the hero sentence — the one sentence I would repeat to my advisor — is built on it. My persona is instructed to flag these rather than quietly understand them, and I am flagging them: the site is written for people who already work in this area.
**Suggested fix:** One glossary page in the book, twelve entries, one sentence each, linked from the footer. Or, cheaper: put a five-word gloss in the hero — "digital twins (live, physics-based simulations of a real place)".
**Confidence:** high — that the words are undefined. Low on whether that would actually cost the project readers.

### 11. "Research software" is a catalogue of other people's tools — MINOR · D5
**Where:** https://gaia-hazlab.github.io/book/research-software
**Saw:** The chapter's entries include ObsPy, "Conda & Mamba" ("Description: Package and environment management"), containerisation platforms ("Use Cases: Reproducible computing environments, HPC deployment"), and foundation models for Earth observation. Its forward-looking items include "Tutorial notebooks for the common workflows" and "FrugalMind EvalHub (live prototype)". The landing page card for the same chapter promises "Open packages for data I/O, AI/ML, visualization, and reproducible hazard workflows."
**Why it matters to me:** I clicked "Browse software →" expecting to find the GAIA packages I would `pip install`. I found a reading list, most of which I already use. The organisation page is honest that curated external tools are "explicitly *not* a maintenance promise", which is the right framing — but the landing page card does not say that, so the click was wasted.
**Suggested fix:** Split the chapter, or retitle the landing card "Software we use and software we maintain", and put the three GAIA packages that actually install at the top.
**Confidence:** medium

### 12. Two numbers on the landing page are not numbers — POLISH · D2
**Where:** https://gaia-hazlab.github.io
**Saw:** The statistics strip reads "4 / Coupled hazard use cases · 3 / Earth systems linked · 14+ / Researchers & partners · ∞ / Sensors, one platform". The roster at `data/team.json` lists 24 people.
**Why it matters to me:** "∞" is not a count of anything, and "14+" undersells a team the site's own data file says is 24. Small thing, and I would not act on it, but it sits next to claims I did check and did not believe.
**Suggested fix:** Say 24, and replace ∞ with the number of stations on the dashboard.
**Confidence:** high

### 13. The favicon 404s from a typo — POLISH · D4
**Where:** https://gaia-hazlab.github.io
**Saw:** `<link rel="icon" type="image/png" href="book/img/img/gaia-hazalab-logo.png">` — the path doubles `img/`, the filename reads "hazalab" rather than "hazlab", and the URL returns 404. It was the only broken internal link I found in a sweep of the landing page's links.
**Why it matters to me:** It does not change anything for me. I note it because one broken link out of the whole landing page is a genuinely good result and it should be zero.
**Suggested fix:** Fix the path and the spelling.
**Confidence:** high

## What worked

**There are real students, and I can email them.** `data/team.json`, rendered on https://gaia-hazlab.github.io/people.html, lists Michael Hemmett, Yiyu Ni, Akash Kharita and Manuela Köpfli as PhD students in Earth and Space Sciences with working `@uw.edu` addresses, plus Morgan Sanger in Civil and Environmental Engineering and Derek Yao as an undergraduate. My persona's hardest stopping rule is "every named person is faculty", and this project clears it. This is the thing that made me not walk away, and it is the thing to protect.

**One repository installs three ways without my emailing anyone.** https://github.com/gaia-hazlab/seis-hydro-2-sed gives pixi (`pixi install` then `pixi shell`), conda (`conda env create -f environment.yml`) and pip (`pip install -e .`), has 90 commits, ships a `CITATION.cff`, and labels itself "Incubating" with a warning that interfaces may change without notice. The warning is as valuable as the install instructions — it tells me what I am signing up for.

**The banner tells me the site is under construction before I ask.** https://gaia-hazlab.github.io opens with "📢 Newly relaunched — code examples are placeholders while we rebuild. Welcome back, partners." I would rather be told this in the first two seconds than discover it in the twentieth minute. It is why several of my findings above are majors rather than blockers.

**The FAQ answers outsider questions rather than insider ones.** https://gaia-hazlab.github.io/book/faq includes "Can I join project meetings if I'm unfunded and external?" and "Does GAIA accept external pull requests?", and answers both concretely, including what is closed. Most lab sites do not have a page that imagines someone like me reading it.

**The organisation is not dormant.** Across 33 repositories, pushes landed on 2026-08-11 and 2026-08-10, and fourteen repositories have been pushed to within the last three months. 22 accounts are org members. Whatever else is unfinished, nobody has walked away from this.

## What I could not judge

- Whether the science is right. I have been in a PhD for eight months and this spans seismology, hydrology, geotechnics and atmospheric science. I cannot assess the soil-memory argument.
- Whether the containers are correctly built or pinned. I have never built a container. The organisation page discusses "a lean image and a teaching image" and pinned dependencies; I have no way to check any of it.
- Accessibility in any rigorous sense. I did not test keyboard navigation, screen-reader order, or contrast ratios with a tool. My D4 score is a lay impression and should be read as one.
- Whether the dashboard map actually works. I read its text, not its behaviour — "an inline Leaflet map driven by this sidebar" could be excellent or could be an empty basemap, and I did not load it interactively.
- Whether the students listed would answer an email, or what they would say. That is the whole point of my next step and it is not something the site can tell me.
- Whether the agentic-AI parts do what they claim. "agents draft, humans approve, and the approval is visible" is a governance sentence I can read but not verify.

## My signature question

**Will this still be maintained when I defend?**

Probably yes — three NSF CSSI awards, 33 repositories, and commits landing the day before I looked are as strong a signal of life as an outsider can get — but the site itself does not let me answer it, because the award end date is published nowhere, every decision in the register is still "proposed", one of them dates itself `2026-08-__`, and every forward-looking claim on the landing page ("coming soon", "currently in build", "in compilation", "preview in preparation") carries neither a month nor a name.
