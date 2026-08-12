# Review: Senior faculty reading as a panel reviewer would

**Reviewed:** 2026-08-12 · **Scope:** landing page; `/book` and the problem statement, DataHub, ModelHub, HazEvalHub, GaiaAgent, how-we-work, organisation, decisions, licensing and FAQ chapters; `/people.html`, `/funding.html`, `/dashboard.html`, `/presentations.html`; the `gaia-hazlab` GitHub organisation and the `seis-hydro-2-sed`, `gaia-cli`, `gaia-agentic-ai`, `catalog` and `gaia-skills` repositories · **Time spent:** 30 minutes

*I am a simulated reviewer, not a real one. These findings are hypotheses about how a panel member would read this site, not evidence about one. Treat them accordingly.*

## In one paragraph

I came to this site to answer three questions: is the claim supported, is it novel against what already exists, and will this team do what it says. I can answer the first and third better than most infrastructure projects I review. The sixty-second test passed cleanly — I wrote down "builds digital twins of the Earth by fusing open multimodal data with AI and cloud computing, grounded in physics, to monitor and forecast soil, landslides, liquefaction and floods," and nothing I read afterwards contradicted it. The governance material is the best I have seen from a project at this stage; a decisions register that records rejected alternatives and a metrics table weighted toward adoption rather than activity are exactly what I ask for and almost never get. But I could not answer the second question at all. Across every page I opened, this project never says how it differs from the infrastructure that already exists in its domain — no EarthScope, no Pangeo, no NASA Earthdata, no DesignSafe, no Planetary Computer, not even to say why they are insufficient. A panel will ask that in the first ten minutes and the site gives me nothing to answer with. Alongside that, the platform is described in a present tense the underlying pages do not support: HazEvalHub "holds" metrics and held-out data on one line and is "developing two tracks" on the next. My recommendation would be to fix the tense and write the novelty paragraph before the site visit, in that order. Everything else here is detail.

## Weighted score: 65/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 4 | 15 | I wrote the right sentence in sixty seconds and never had to revise it |
| D2 Credibility of claims | 2 | 30 | No falsifiable hypothesis, no novelty comparison, present tense outrunning the artifacts |
| D3 Navigation and information scent | 4 | 5 | Landing page to book to repository worked every time I tried it |
| D4 Visual design and accessibility | 3 | 5 | Looks professional; I am not competent to audit contrast or keyboard reach |
| D5 Technical depth and reproducibility | 3 | 10 | Real code in real repositories, but the flagship prototype's source is unreachable |
| D6 Governance and openness | 4 | 15 | Genuinely strong, and undercut by its own unratified state |
| D7 Activity and durability | 4 | 15 | Commits from two days ago, three linked awards, one worrying namespace |
| D8 Relevance to me | 4 | 5 | Coupled hazards across the critical zone is a real gap and they name it well |

Weighted total: (4×15 + 2×30 + 4×5 + 3×5 + 3×10 + 4×15 + 4×15 + 4×5) / 5 = **65/100**.

## Findings

### 1. No acknowledgement of any adjacent effort, anywhere on the site — BLOCKER · D2
**Where:** https://gaia-hazlab.github.io/book/datahub/ (and every other page I opened)
**Saw:** The DataHub chapter's statement of scope reads in full: "We are working on access first: getting data streams from several agencies into one place for our Washington State projects." I searched the text of the landing page, the problem statement, DataHub, ModelHub, HazEvalHub, GaiaAgent, how-we-work, organisation, decisions, licensing and the FAQ for the names of comparable infrastructure. EarthScope appears three times, always as a *partner institution* holding award OAC-2608511, never as a system to compare against. Pangeo, NASA Earthdata, Google Earth Engine, Microsoft Planetary Computer, OpenTopography, DesignSafe and Destination Earth appear zero times. No page contains the words "unlike", "differs from", "compared to", or "prior art".
**Why it matters to me:** This is the question a panel asks first and the one I would be assigned to write on. "Cloud-native multimodal data access with a catalog and a Python client" describes at least four things that already exist and have staff. I am not saying GAIA duplicates them — I am saying the site gives me no way to argue that it does not, and that silence reads one of two ways: either the team does not know the landscape, or it is hoping I do not. Both are fatal at panel. This is the finding that stops my evaluation: I cannot write a novelty paragraph from this material.
**Suggested fix:** One page, `book/related-work`, six paragraphs. Name the four or five closest systems, say in one sentence each what they do well, and say what GAIA does that they do not. The honest answer is probably "none of them couple atmospheric forcing to geomechanical state, and none of them evaluate agents on cost" — that is a good answer and it is currently nowhere on the site.
**Confidence:** high

### 2. HazEvalHub is described in the present tense as holding things it does not hold — BLOCKER · D2
**Where:** https://gaia-hazlab.github.io/book/hazevalhub/
**Saw:** Two consecutive paragraphs. First: "The HazEvalHub is where hazard models get scored. It holds the metrics, the validation protocols, and the held-out data that decide whether a prediction is good enough to act on." Immediately after: "We are developing two tracks for evaluating model performance". The landing page card is present tense with no status marker at all: "HazEvalHub — Benchmarks and skill scores to validate hazard forecasts against what actually happened." There is no `hazevalhub` repository in the GitHub organisation, and no `modelhub` repository either, though the ModelHub page opens "The ModelHub is where we register the machine learning and physics-based models that monitor and predict hazards. It holds pre-trained weights, the training pipelines that produced them, and the tooling to build new hazard models on top."
**Why it matters to me:** A capability asserted in the present tense that does not yet exist is the single fastest way to lose me, and it costs the project the credit it has actually earned. Two of the six platform components on the front page have no repository behind them. I want to stress that the underlying work is not vapour — the ModelHub page names real models with named leads, and the QuakeXNet detector and the fifteen-year Rainier catalog are concrete. The problem is purely that "holds" and "is where we register" describe a registry that is not there, so I now have to re-examine every other present-tense sentence on the site rather than reading them in good faith.
**Suggested fix:** Change "holds" to "will hold" in both overviews, and put a one-word status badge — *planned* / *prototype* / *available* — on each of the six platform cards on the landing page. The demo section already does this well; copy that pattern upward.
**Confidence:** high

### 3. The central claim is a research agenda, not a falsifiable hypothesis, and no test is named — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/book/problem-statement/
**Saw:** The strongest claim on the page is diagnostic rather than predictive: "Our models do not resolve those cascades. Atmosphere, hydrology, and geomechanics are studied and modeled separately, and the couplings between them fall in the gaps." The approach that follows is "We take a data-driven and physics-grounded approach to monitor, characterize, and predict the susceptibility of weather-compounded geodisasters", and the three goals include "Discovery of missing physics — Identify the governing processes and couplings (e.g., soil memory effects, ocean–atmosphere teleconnections) that current hazard models neglect." No quantitative target, baseline, skill score, or decision threshold appears anywhere on the page.
**Why it matters to me:** I asked my standing question — what would have to be true for this claim to be false — and I could not construct the answer. "Integrating data and models" is not a claim, and "discover missing physics" cannot fail. The project clearly *has* a falsifiable version of this: the soil-memory thesis says antecedent hydromechanical state carries predictive information that current models discard, which is testable as a skill improvement over a memoryless baseline on a named event set. That sentence is not on the page.
**Suggested fix:** Add three sentences to the problem statement in the form "We predict that X. If Y, we are wrong." One for soil memory, one for the seismic-discharge inversion, one for the liquefaction surrogate. Name the baseline each is measured against.
**Confidence:** high

### 4. The front page violates the project's own funding-acknowledgement decision — MAJOR · D6
**Where:** https://gaia-hazlab.github.io (footer) versus https://gaia-hazlab.github.io/book/decisions/
**Saw:** The landing page states: "This material is based upon work supported by the U.S. National Science Foundation under Grant No. OAC‑2608509 (GAIA‑CSSI), the Fund for Future Science and Technology (FFST), and the Jerome and Linda Paros Geohazard Center." Singular "Grant No.", one award. GAIA-D-001 says the opposite, and says why: "All GAIA outputs carry one canonical acknowledgment, citing all three linked awards regardless of the author's institution", with rejected alternative "citing only the author's own institutional award — it fragments the citation string the metrics search on, and under-credits the partners." The decision's obligations explicitly include a "copy-paste block on the website". `/funding.html` gets it right, listing "OAC‑2608509, 2608510, and 2608511".
**Why it matters to me:** Observation: the front page cites one award; the register requires three. Inference, and I mark it as inference: at a site visit I would ask the UAF and EarthScope co-PIs whether they feel like partners or subawardees, because the most-read page of the collaboration credits only Seattle. This is also self-defeating on the project's own terms — M4 tracks acknowledgement strings through CrossRef, so the front page is degrading a metric the team says it will report against.
**Suggested fix:** Paste the canonical block from GAIA-D-001 into the landing page footer. One edit.
**Confidence:** high

### 5. Every decision of record is unratified, and two carry unfilled placeholder dates — MAJOR · D6
**Where:** https://gaia-hazlab.github.io/book/decisions/
**Saw:** The index lists four entries — "001 Funding acknowledgment text and mechanics | proposed | —", "002 System of record | proposed | —", "003 Meeting schedule and the sunset rule | proposed | —", "004 Project Google identity | proposed | —". Every status is `proposed` and every date is an em dash. Each entry header reads "Date: — · Decided at: kickoff call, 2026-08-__ · Status: proposed", with the literal characters `2026-08-__` published live. The page's own first rule states: "Nothing counts as decided until it has a number here."
**Why it matters to me:** By the register's own standard, this project has made zero decisions. That is defensible three weeks into an award and I would not hold it against the team — what I hold against it is publishing a fill-in-the-blank date to the open web. It tells me the page went up before the kickoff call it describes, which makes me wonder how much else on this site describes a meeting that has not happened yet. The register is genuinely good work; that is exactly why the placeholder undermines it.
**Suggested fix:** Replace `2026-08-__` with the real date or with "scheduled", and add one line under the index saying "No decision is yet ratified; the first four go to the September project-wide call." State the state you are in rather than looking like you forgot.
**Confidence:** high

### 6. The one working prototype on the site has an unreachable source repository, in a personal namespace — MAJOR · D5
**Where:** https://gaia-hazlab.github.io/book/hazevalhub/
**Saw:** "FrugalMind EvalHub is the first working prototype of HazEvalHub." The page links "▶ Open the live eval board · source: mdenolle/frugalmind". The board itself loads (https://mdenolle.github.io/frugalmind returns 200). The source link, https://github.com/mdenolle/frugalmind, returns **404** — private or absent. The same section claims "Is it reproducible? Deterministic scoring from declarative JSON specs, so results can't be gamed", and reports results I would want to check: "Free local 7B models (qwen2.5:7b, llama3.1:8b) reach perfect scores on configuration tasks once given domain skills — but fail at numerical code generation, where only cloud models succeed (~0.56 base, rising to 0.76 with skills)."
**Why it matters to me:** This is the strongest single piece of evidence on the site — real numbers, cost as a first-class axis, hidden test splits. It is also the one I cannot verify, because the repository behind a page that advertises non-gameable determinism does not open. Separately, and this is the durability point: the flagship prototype of a five-year, three-institution award lives under an individual's GitHub account, not the organisation's. Observation. The inference I would voice at panel is that if that person moves, the demo moves with them.
**Suggested fix:** Make the repository public or remove the source link, and transfer it to `gaia-hazlab/` with a redirect. If it must stay private for now, say why on the page.
**Confidence:** high

### 7. The repository behind the front page's flagship demo has no licence, under a footer claiming MIT — MAJOR · D6
**Where:** https://gaia-hazlab.github.io ("Read the WA-2025 flood & sediment study" → https://github.com/gaia-hazlab/seis-hydro-2-sed)
**Saw:** The landing page footer reads "© 2026 GAIA HazLab · University of Washington · Licensed under the MIT License." The GitHub API reports `seis-hydro-2-sed` has `license: null`. It is the organisation's most-starred repository (2), its most recently pushed (2026-08-10), and the destination of the only "read the study" link in the demos section. Four other repositories I checked are licensed — `gaia-cli` MIT, `catalog` MIT, `gaia-skills` MIT, `gaia-agentic-ai` BSD-3-Clause.
**Why it matters to me:** Observation: no LICENSE file. Inference, marked as such: nobody has run a licence sweep across the organisation, and the mixed MIT/BSD-3 split suggests per-repository improvisation rather than the policy the licensing chapter implies. For a project whose adoption metrics depend on other people installing and deriving from its code, an unlicensed flagship is a legal reason for exactly those people not to.
**Suggested fix:** Add the licence file. Then add a CI check across the organisation that fails a repository without one — the project already has CI-template repos as a delivery target, so put it in the template.
**Confidence:** high

### 8. Two promised areas have nobody senior attached — MAJOR · D7
**Where:** https://gaia-hazlab.github.io/people.html (roster served from https://gaia-hazlab.github.io/data/team.json)
**Saw:** Twenty-four people, well distributed across UW, UAF and EarthScope. Liquefaction is one of three headline areas on the landing page ("Liquefaction — How saturated soils lose strength under shaking") and one of four use cases in the problem statement. The only person on the roster whose listed work is geotechnical is "Morgan Sanger | Graduate Student | Civil and Environmental Engineering, University of Washington", who is also named on the ModelHub page as "lead" for "Ground Failure Modeling : Surrogate model to predict liquefaction and ground failure potential index". Separately, the problem statement names "Ocean–Atmosphere Coupling" as one of two nexus domains, describing "How oceanic forcing (e.g., sea surface temperature anomalies, atmospheric rivers) shapes extreme precipitation patterns" — no oceanographer appears on the roster; the nearest are atmospheric scientists.
**Why it matters to me:** The panel question is always which promised area has nobody attached to it, and here I can name two. A graduate student leading the surrogate model for one of four flagship use cases is a single point of failure on a five-year award — when they graduate in year three, liquefaction leaves with them. The ocean domain is at least honestly flagged "(Coming soon.)" in the text, which I credit, but a nexus domain with no personnel is a scope claim the team cannot currently meet.
**Suggested fix:** Name a senior geotechnical collaborator, even unfunded, and either staff the ocean domain or demote it from a named nexus domain to a stated future direction.
**Confidence:** medium — I am reading staffing from a roster, and unfunded collaborators may exist who are not listed.

### 9. A carefully built metrics table contains no measure of anyone trained — MAJOR · D7
**Where:** https://gaia-hazlab.github.io/book/how-we-work/
**Saw:** The delivery table lists five rows — CI-template repos, container images, DOI-archived datasets, versioned model cards, and "D5 JupyterBooks + hackweeks (per year) | 1+1 | 2+1 | 3+1 | 4+2 | 5+2". The adoption table lists container pulls, derived agents, publications, "M3 unique institutions", "M3 disciplines represented", agent modes, modalities, and "M4 skill-adoption gain (post − pre)". No row counts students supported, degrees completed, hackweek participants, postdocs mentored, or anyone trained. The page's own framing is "We told NSF what GAIA would produce and how adoption would be measured. These numbers are commitments from the funded proposal, not aspirations".
**Why it matters to me:** Hackweeks are counted as events delivered, not as people trained — one is activity by the team, the other is the outcome NSF asks about. This project has eight students and postdocs on its roster and a genuine claim to make about workforce, and the metrics table is the one place a reviewer looks for it. I note the asymmetry: the team was disciplined enough to weight its software metrics toward external adoption and then applied none of that discipline to people.
**Suggested fix:** Add two rows — hackweek participants from outside the three institutions, and students supported who complete a GAIA-based thesis chapter. Both are already collectable.
**Confidence:** high

### 10. The front page cannot count its own team — MINOR · D2
**Where:** https://gaia-hazlab.github.io
**Saw:** The statistics band reads "14+ / Researchers & partners". The roster that the same site serves to `/people.html` contains twenty-four people.
**Why it matters to me:** Trivial in itself, and I would not raise it if finding 1 were fixed. But a panel reviewer checks the cheapest verifiable number on the page first, precisely because it predicts the care taken over the expensive ones. Understating by ten is a stale hand-maintained figure sitting next to a machine-readable file that already has the answer.
**Suggested fix:** Compute it from `data/team.json` at build time.
**Confidence:** high

### 11. "∞ Sensors, one platform" — MINOR · D2
**Where:** https://gaia-hazlab.github.io
**Saw:** The fourth statistic in the band is the infinity symbol, labelled "Sensors, one platform". The three beside it are real and checkable: "4 Coupled hazard use cases", "3 Earth systems linked", "14+ Researchers & partners".
**Why it matters to me:** It is the only unfalsifiable number on the page and it sits in a row of falsifiable ones, which weakens them by association. The project runs actual instruments and could put the actual count there. Matter of taste in part — some readers find it charming — but I am telling you how it reads to a panel.
**Suggested fix:** Use the station count from the CRESST catalog, which the dashboard already knows.
**Confidence:** medium — partly a matter of taste, and I say so.

### 12. Small errors on pages that carry technical weight — POLISH · D2
**Where:** https://gaia-hazlab.github.io/book/problem-statement/ and https://gaia-hazlab.github.io/book/modelhub/
**Saw:** A use case titled "2001–2031 Nisqually Earthquake" — the Nisqually earthquake was 2001, and the intended sense of the range is not recoverable from the text, which describes "earthquake-induced ground failure (liquefaction, landslides) and how antecedent soil moisture and hydromechanical state modulate seismic hazard severity". On ModelHub: "coupling ACE2 with Amtmospheric River Index". The landing page also carries a standing banner: "📢 Newly relaunched — code examples are placeholders while we rebuild. Welcome back, partners."
**Why it matters to me:** The date range on a named historical event is the kind of thing I circle, because I cannot tell whether it is a typo or a scenario definition I failed to understand. The banner I actually approve of as honesty — I mention it only because "code examples are placeholders" sitting above six present-tense platform cards is the whole tension in finding 2, stated by the team itself.
**Suggested fix:** Fix both typos. Keep the banner until the examples are real, then remove it.
**Confidence:** high

## What worked

**The governance chapter is the best thing on this site and better than most funded projects manage in year three.** https://gaia-hazlab.github.io/book/how-we-work/ commits to a five-year table of numbers, then states the escalation ladder for missing them: "The accountable lead either names a corrective action with a date, or explicitly accepts the shortfall and says why. Both outcomes are recorded; silence is not an option." I would point another PI at this page.

**The metrics are weighted toward adoption, which is the opposite of what I usually find.** "Adoption metrics matter most here: software nobody installs, datasets nobody downloads, and evaluation harnesses nobody submits to are not serving the community, however complete they look." The team also pre-committed against gaming: "We count few things. Every metric above is one we committed to. We do not add flattering ones." My standing complaint about vanity metrics does not apply here, and I want that on the record.

**The decisions register records rejected alternatives, not just outcomes.** GAIA-D-002 rejects "buying Slack Pro (recurring cost, and preserves the wrong artifact) · moving all status into GitHub Discussions (loses the low-friction chat people actually use)". A register without rejected alternatives records outcomes; this one records decisions. GAIA-D-001 even flags its own uncertainty — "EarthScope's (2608511) is inferred by elimination and should be confirmed against their award notice" — which is the sort of thing most teams quietly leave out.

**The demo section labels its own vapour.** "Live demo coming soon", "In compilation", "live panel coming soon", "currently in build". This is exactly the visual distinction between delivered and aspirational that I check for, done well. It makes the unlabelled platform cards in finding 2 more puzzling rather than less — the team clearly knows how to do this.

**The organisation is demonstrably alive.** Twenty-six repositories, the most recent pushed two days before I looked, spanning STAC catalogs, a data-staging CLI, Landlab debris-flow models and agent evaluation sets. Whatever else is true, someone is working.

## What I could not judge

- **Accessibility.** I noted that the site looks professional on both viewports, but I am not competent to assess contrast ratios, keyboard traversal, alt text or screen-reader behaviour, and I did not test them. D4's score of 3 is a placeholder, not an assessment.
- **Whether the science is right.** I did not evaluate the seismic-discharge inversion, the liquefaction surrogate, or the ACE2 coupling on their merits. My concern throughout is whether claims are supported and dated, not whether the physics holds.
- **The dashboard's substance.** https://gaia-hazlab.github.io/dashboard.html renders client-side and I read its shell, not its contents. The same is true of `/people.html`, where I recovered the roster from `data/team.json` instead — if that fetch fails for a reader, the page is empty, and I did not test that failure mode.
- **What the proposal actually promised.** Several claims here are traceable to a funded proposal I have not read. Where the site says a number is a commitment, I took that at face value.
- **The private record.** Meeting notes and the `gaia-hazlab/notes` repository are internal by design. I have no way to check that the published decisions match what was decided, and I am not suggesting they do not.

## What I ran out of patience before finding

I never opened `/presentations.html` beyond confirming it returns 200, and I did not read the licensing chapter closely enough to say whether the mixed MIT/BSD-3 licensing in finding 7 contradicts a stated policy or merely lacks one. I spent that time on the novelty question instead, and came up empty.

## My signature question

*Which sentence on this site would be embarrassing in three years?*

This one, from https://gaia-hazlab.github.io/book/hazevalhub/: **"It holds the metrics, the validation protocols, and the held-out data that decide whether a prediction is good enough to act on."** — because HazEvalHub has no repository in the organisation, the next paragraph concedes "We are developing two tracks", and the only working evaluation board is in a personal namespace with a 404 for a source link. In three years this sentence will either be true, in which case nobody remembers it was written early, or it will not, in which case it is the sentence a reviewer quotes back.

The full list of present-tense claims about things that do not yet demonstrably exist, quoted exactly:

- "It holds the metrics, the validation protocols, and the held-out data that decide whether a prediction is good enough to act on." (`/book/hazevalhub/`)
- "The ModelHub is where we register the machine learning and physics-based models that monitor and predict hazards. It holds pre-trained weights, the training pipelines that produced them, and the tooling to build new hazard models on top." (`/book/modelhub/`)
- "HazEvalHub — Benchmarks and skill scores to validate hazard forecasts against what actually happened." (landing page card, no status marker)
- "ModelHub — Physics-informed and surrogate ML models for hazard prediction and pattern discovery." (landing page card, no status marker)
- "DataHub — Streamlined access to precipitation, streamflow, seismic, and DAS data across Washington State." (landing page card — the chapter it links to says "We are working on access first" and "two products in progress")
- "GaiaAgent — The agentic-AI layer — a cross-disciplinary translator, agentic data downloaders, and research-software agents." (landing page card — the four repositories it names do exist, so this is the weakest instance and may need only a status badge)
- "We build digital twins of the Earth" (landing page hero — the landslide digital twin is labelled "currently in build" further down the same page)
- "An interactive map of every colocated sensor and event in our regions of interest." (landing page — "every" is the load-bearing word and I could not verify it)

None of these is dishonest. All of them are the kind of sentence that is written in month one and quoted in year four.
