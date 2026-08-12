# Review: CTO of a climate-risk analytics company

**Reviewed:** 2026-08-12 · **Scope:** landing page; `book/` index, `how-we-work`, `organization`, `decisions` (status only), `licensing`, `faq`, `datahub`, `modelhub`, `hazevalhub`; `dashboard.html`; the GitHub organisation profile and, per my own selection logic, `seis-hydro-2-sed`, `landlab-debrisflow`, `fire-debrisflow-ml`, `da-seis-groundfailure`, `landslide-digital-twin`, `geocroissant-hazards`, `gaia-data-downloaders`; licence and `CITATION.cff` coverage enumerated across all 33 org repositories · **Time spent:** 45 minutes (budget spent)

*I am a simulated reviewer, not a real one. This persona is constructed from the project's context and from what people in my role typically need. Every finding here is a hypothesis about a real reader, not evidence about one. Do not cite this as user research.*

## In one paragraph

I came here for post-fire debris-flow and ground-failure layers that are better than what my team can build, and on the science this is exactly the right shop. Then I did what I always do first, which is check the licence on the repository I would actually use, and the evaluation ended there. The five repositories that match my need most closely (`da-seis-groundfailure`, `fire-debrisflow-ml`, `landlab-debrisflow`, `landslide-digital-twin`, `seis-hydro-2-sed`) carry no LICENSE file. Fourteen of thirty-three repositories in the organisation carry none. What makes this frustrating rather than simply disqualifying is that the licensing policy page is one of the better ones I have read from an academic group, and the practice has not caught up with it. Underneath that sit three more of my standing stop conditions: no data provenance or redistribution terms I could hand to counsel, no model performance reported against a baseline anywhere on the site, and no stated domain of validity for any hazard product. I am not opening a conversation this quarter. If a LICENSE file lands on the debris-flow repositories and one worked example reports skill against a statistical baseline, I would put an engineer on the two-day reproduction I described and come back.

## Weighted score: 59/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 4 | 10 | I had the sentence in under sixty seconds; two different taglines cost it the fifth point |
| D2 Credibility of claims | 2 | 15 | A checkable claim about every repository is false, which forces me to discount the uncheckable ones |
| D3 Navigation and information scent | 4 | 10 | Every URL I tried returned 200 and licensing sat where I expected it |
| D4 Visual design and accessibility | 3 | 5 | Adequate on what I saw; largely outside my competence |
| D5 Technical depth and reproducibility | 3 | 25 | Real environment pinning and a reproducibility document, but nothing validated I could verify |
| D6 Governance and openness | 2 | 25 | Excellent written policy, 42% of repositories not complying with it |
| D7 Activity and durability | 4 | 5 | Commits this week, three NSF awards named |
| D8 Relevance to me | 5 | 5 | This is precisely my problem, in my hazards, on my geography |

## Findings

### 1. The repositories I would actually use carry no LICENSE file — BLOCKER · D6

**Where:** https://github.com/gaia-hazlab/landlab-debrisflow · https://github.com/gaia-hazlab/fire-debrisflow-ml · https://github.com/gaia-hazlab/da-seis-groundfailure · https://github.com/gaia-hazlab/landslide-digital-twin · https://github.com/gaia-hazlab/seis-hydro-2-sed

**Saw:** No LICENSE file in the root listing of any of the five, and the About sidebar on each shows no licence designation. The root of `landlab-debrisflow` reads: `.gitignore`, `01_build_erosion_evidence.py` … `README.md`, `environment.yml`, `pyproject.toml`, `run_pipeline_v1.py` — no LICENSE. Enumerated across the organisation, 14 of 33 repositories have no licence: `shred-landlab-prototypes`, `awesome-gaia`, `gaia-data-downloaders`, `seis-hydro-2-sed`, `da-seis-groundfailure`, `fire-debrisflow-ml`, `landlab-debrisflow`, `mt-rainier-smart-sensing`, `landslide-digital-twin`, `gaia-translate-QA`, `landslide-data-prep`, `gaia-slack-digest`, `.github`, `gaia-dot-github`. (Observation. The inference I am *not* drawing is that the team is indifferent to reuse — the licensing page says otherwise.)

**Why it matters to me:** Absent a licence, the default is exclusive copyright to the University of Washington and I have no grant to do anything with the code. This is the one condition that ends my evaluation on its own, before I read a word of the science. It is also the cheapest thing on this entire list to fix, which is what makes it sting: the group has already decided MIT is the default and has simply not written the file.

**Suggested fix:** Add the MIT text with a UW copyright line to those five repositories this week. Then add a CI check, or a scheduled org-wide job, that opens an issue on any repository without a LICENSE — the policy already exists, only the enforcement is missing.

**Confidence:** high

### 2. Data provenance and redistribution terms are not stated in a form I could give counsel — BLOCKER · D6

**Where:** https://gaia-hazlab.github.io/book/datahub · https://github.com/gaia-hazlab/gaia-data-downloaders

**Saw:** The DataHub page identifies providers and links their landing pages, and the only licence-adjacent sentences I found are access notes: "This needs an API key from Synoptic, free for academic use." and "Most station data is public and served over APIs." `gaia-data-downloaders` is thirty-odd notebooks pulling CONUS404, HRRR, PRISM, StageIV, WRF, ECOSTRESS, SNOTEL and USGS gauges, with no LICENSE and no per-source terms file.

**Why it matters to me:** The code being MIT tells me nothing about the data. "Free for academic use" is an explicit exclusion of what I do. If I train on a corpus assembled from those notebooks and ship the result to an insurer, I have inherited every upstream restriction without knowing what they are, and my client audits will find it. Unstated provenance on training or calibration data is a standing stop condition for me.

**Suggested fix:** One table on the DataHub page: source, upstream licence or terms URL, whether redistribution is permitted, whether commercial use is permitted. Ten rows would cover most of it, and the notebooks already name the sources.

**Confidence:** high

### 3. No model performance is reported against a baseline anywhere I could find — BLOCKER · D5

**Where:** https://gaia-hazlab.github.io/book/modelhub · https://gaia-hazlab.github.io/book/hazevalhub

**Saw:** ModelHub states the intent in the present tense: "All models in the ModelHub are benchmarked against: Baseline models (traditional statistical approaches), The best published method for the task, Domain-specific metrics and standards." No benchmark results appear on the page, and no trained model with published weights is linked. HazEvalHub describes hold-out design in some detail ("Geographic hold-out: Testing on different regions", "Temporal hold-out: Testing on future time periods") but its own framework status reads "TBD", and the metrics actually shown are for LLM evaluation — "Is it right?", "What did it cost?", "Is it reproducible?" — not for hazard prediction.

**Why it matters to me:** A hazard model whose skill is not stated relative to a baseline is not a model I can defend to a client's model-risk committee, let alone a regulator. I need one number against one dumb baseline. Describing the validation design without publishing a result reads, to me, as infrastructure that has not yet met data. (Inference, marked as such: it may simply be unpublished.)

**Suggested fix:** Publish one completed evaluation. The Stehekin post-fire debris-flow case looks closest to ready — an AUC or Brier score against a logistic baseline, on a named hold-out, on one page, would move this whole review.

**Confidence:** medium — I timeboxed at 45 minutes and may have missed a results page that is not linked from ModelHub or HazEvalHub. If it exists, the finding becomes a navigation problem instead.

### 4. A README declares "MIT License" on a repository that has no LICENSE file — MAJOR · D6

**Where:** https://github.com/gaia-hazlab/seis-hydro-2-sed

**Saw:** The README carries a section heading "## License" followed by "MIT License". The repository root contains `CITATION.cff`, `Dockerfile`, `REPRODUCIBILITY.md`, `pixi.lock` and much else, but no LICENSE file, and the GitHub API reports the licence as none.

**Why it matters to me:** This is worse for me than silence. Silence I recognise instantly and route around. A bare prose assertion with no licence text and no copyright holder looks settled to a non-lawyer, so it wastes an engineer's week before our counsel rejects it. This was also the repository I most wanted, because it is the one with a `REPRODUCIBILITY.md` and a pinned lockfile.

**Suggested fix:** Add the actual LICENSE file with the copyright line. If the intent is MIT, the README is already correct and only the instrument is missing.

**Confidence:** high

### 5. "Every repository ships a CITATION.cff" is not true, and it is the claim I checked — MAJOR · D2

**Where:** https://gaia-hazlab.github.io/book/faq

**Saw:** Verbatim: "Every repository ships a `CITATION.cff`." I checked all 33 repositories in the organisation. Two have one: `seis-hydro-2-sed` and `geocroissant-hazards`.

**Why it matters to me:** I do not mind a project being early. I mind being told something is universal when a five-minute check says it is 6%. My whole assessment of this site rests on claims I cannot verify from outside, and this was one of the few I could. Getting it wrong makes me reprice every other assertion on the page, including the benchmarking claim in finding 3.

**Suggested fix:** Change the sentence to what is true and aspirational — "Repositories that have reached the point of citation ship a `CITATION.cff`; we are backfilling the rest" — or generate the files. Either is fine. The mismatch is the problem, not the coverage.

**Confidence:** high

### 6. No stated domain of validity or known-limitations statement for any hazard product — MAJOR · D2

**Where:** https://gaia-hazlab.github.io/book/ · https://gaia-hazlab.github.io/book/modelhub

**Saw:** The book front matter offers "A system-science platform for weather-compounded geohazards — bringing AI, data, and physical models together to predict what the atmosphere does to the ground." I found no caveat, no failure mode, and no geographic or regime limit on any page I opened. ModelHub says a model card should cover "Performance metrics and limitations", and no model card is linked.

**Why it matters to me:** Everything visible is trained and demonstrated in Washington State — Nisqually, Stehekin, Mt Rainier, the DREAM network. My book is national. Without a stated domain of validity I have to assume the answer is "the Pacific Northwest, in the conditions observed so far", and I cannot put a layer into a product that does not say where it stops being true.

**Suggested fix:** One paragraph per use case: where it was fit, where it has been tested, where it should not be used yet.

**Confidence:** high

### 7. No releases, no versions, no changelogs — I would not know a model had been retrained — MAJOR · D7

**Where:** https://github.com/gaia-hazlab/seis-hydro-2-sed/releases · https://github.com/gaia-hazlab/gaia-cli · https://github.com/gaia-hazlab/catalog

**Saw:** Zero published releases across every repository I checked, including `seis-hydro-2-sed`, `gaia-cli`, `landlab-debrisflow`, `fire-debrisflow-ml`, `catalog`, `landslide-digital-twin` and the website itself. `seis-hydro-2-sed` has 9 tags and no releases; the rest have neither. No CHANGELOG.md in any of the four I checked.

**Why it matters to me:** If I embed a layer and it silently changes, my client's back-test breaks and I find out from them. I need a version I can pin and a note telling me what moved between versions. Right now the only version identifier available to me is a commit SHA, which tells me nothing about whether the science changed.

**Suggested fix:** Cut a `v0.1.0` release on the two or three repositories anyone might depend on, and add a five-line CHANGELOG. Even "0.1.0 — first tagged state, nothing guaranteed" is more than I have now.

**Confidence:** high

### 8. No machine access — the dashboard is a page and a hope — MAJOR · D5

**Where:** https://gaia-hazlab.github.io/dashboard.html

**Saw:** "Prototype — inline Leaflet map driven by this sidebar, with every layer from the catalog (plus geodetic, coming soon)." Clicking a station "jump[s] to its data-provider landing page". I found no API endpoint, no JSON feed, and no STAC root URL documented on the page. There is a "Catalog source code ↗" link and a "Read the DataHub docs →" link.

**Why it matters to me:** I consume things on a schedule or I do not consume them. A human-clickable map is a demonstration, not an interface, and I will not build a scraper against a research group's HTML. The organisation clearly has STAC catalogs — I can see `precip-stac`, `prism-stac`, `solus-stac`, `landlab-stac` in the repository list — but the dashboard, which is where a reader like me lands, never gives me a catalog URL to point a client at.

**Suggested fix:** Put the STAC root URL on the dashboard page, above the fold, in plain text. That one line converts this from a demo into something I can evaluate.

**Confidence:** medium — the DataHub docs may expose an endpoint I did not reach inside the budget. See finding 11.

### 9. Commercial use is unaddressed, and silence is a risk I have to price — MAJOR · D6

**Where:** https://gaia-hazlab.github.io/book/organization · https://gaia-hazlab.github.io/book/licensing · https://gaia-hazlab.github.io/book/faq

**Saw:** The organization page describes escalating levels of commitment to external software — "Each is a larger commitment by us than the one before, so each is agreed rather than assumed" — and level 0 "needs nobody's permission beyond a pull request". It is entirely about what GAIA adopts *inward*. I found no sentence anywhere about a company using GAIA's output, no industry-engagement route, and no named contact for one. The FAQ discusses meeting access and co-authorship norms for collaborators, not commercial reuse.

**Why it matters to me:** MIT settles the legal question and leaves the relationship question open. When my name appears in a client deck next to a UW project that never invited commercial use, I want to have asked first. Unaddressed is not the same as unwelcome, but I have to treat it as a risk until someone writes a sentence.

**Suggested fix:** Two sentences on the licensing page: whether commercial use is welcomed, and an email address for it.

**Confidence:** high

### 10. Twenty of thirty-three repositories are tagged as unstable, and the tag is easy to miss — MINOR · D7

**Where:** https://gaia-hazlab.github.io/book/faq · https://github.com/gaia-hazlab

**Saw:** "Repositories tagged `gaia-incubating` change shape without warning, so check the tag before building something on top." I counted 20 of 33 repositories carrying an incubating topic.

**Why it matters to me:** I respect the honesty here and I want to say so. But the practical reading is that two thirds of the organisation is explicitly not build-on-able, and I only learned the rule because I happened to open the FAQ. On the organisation page the topic is a small grey pill I would have scrolled past.

**Suggested fix:** Say it once on the organisation profile README, not only in the FAQ, and consider stating the converse — which repositories are *not* incubating, since that is the shorter and more useful list.

**Confidence:** high

### 11. I ran out of patience before I found the DataHub integration guide — MINOR · D3

**Where:** https://gaia-hazlab.github.io/book/datahub-integration-guide

**Saw:** The DataHub page points onward to a "DataHub Integration Guide". The URL resolves (HTTP 200), so this is not a broken link. I simply reached the end of my 45 minutes with three stop conditions already triggered and did not open it, and I am recording that rather than pretending otherwise.

**Why it matters to me:** The material that would have answered findings 2 and 8 may well live one click past where I stopped. That is worth knowing: the answers a commercial evaluator needs are apparently on the third page, and I am a second-page reader. Whatever is in that guide about endpoints and data terms should be surfaced on `datahub` and `dashboard.html` themselves.

**Suggested fix:** Promote the licence table and any endpoint URLs from the integration guide up onto the DataHub and dashboard pages.

**Confidence:** high

### 12. A shell-quoting accident is committed to a repository root — POLISH · D5

**Where:** https://github.com/gaia-hazlab/landlab-debrisflow

**Saw:** The root file listing contains an entry literally named `lide notebook"`, alongside a separate `notebook` directory. It looks like an unterminated quote in a `mkdir` or `mv` that got committed.

**Why it matters to me:** Nothing, functionally. But I read repository hygiene as a proxy for review discipline, and this is the sort of thing a pull-request template catches. Minor evidence about process on a repository I was already unable to license. Noting that this is partly a matter of taste.

**Suggested fix:** `git rm` it, and require review on main.

**Confidence:** high

## What worked

**The licensing page is better than most of what I read from industry.** "Choose the least restrictive licence that still requires attribution" is a defensible policy stated in one line, and the page goes on to handle GPL contamination correctly — that pulling GPL code into an MIT repository forces the combined work to GPL is exactly the trap that costs companies like mine real money, and I have seen commercial teams get it wrong. The section on AI-assisted code, that it is licensed like any other code and that AI vendors are never listed as copyright holders, is a question my own counsel is still arguing about. If the practice matched this page I would have had a very different review.

**The vocabulary is clean.** I went in expecting to flag `thrust`, `focal node`, `broader impacts`, `senior personnel` and `level-3 benchmarked` as jargon I do not know. None of them appear on any page I opened. The landing page told me what this does in one sentence I could repeat to my board, and it did it in sixty seconds: "We build digital twins of the Earth — fusing open, multimodal data with AI and cloud computing, all grounded in physical models — to monitor and forecast soil, landslides, liquefaction, and floods." That is a real achievement and I would protect it.

**`seis-hydro-2-sed` shows me what reproducibility looks like when someone means it.** A `Dockerfile`, a `pixi.lock`, an `environment.yml`, a `REPRODUCIBILITY.md`, a `CITATION.cff` and a `paper/` directory in one repository is the setup I would want my own team to ship. This is the repository I would have put an engineer on for the two-day reproduction. It is the licence, and only the licence, standing between us.

**Nothing 404'd.** I checked fifteen URLs across the site and every one returned 200. For a project this young that is unusual, and it meant my time went into judging content rather than chasing dead links.

## What I could not judge

- **Whether the science is right.** I am not a geomorphologist or a seismologist. I can tell you a model has no baseline; I cannot tell you whether its physics is sound.
- **Accessibility in any rigorous sense.** I did not test keyboard reach, contrast ratios, alt text or screen-reader behaviour, and I did not view the site on a phone. My D4 score of 3 is a placeholder, not an assessment, and should be overridden by any reviewer who actually tested it.
- **Whether the Leaflet dashboard renders correctly**, since I read these pages as text. My finding about machine access stands regardless of how it looks.
- **The decisions register.** It returns 200 and the FAQ says it "provides the reasoning behind all governance choices", but I did not read it inside the budget. Governance-of-record is a strength I may be under-crediting.
- **The `geocroissant-hazards` licence status.** GitHub reports it as unrecognised, though the LICENSE file itself plainly reads "This work is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0)." That is a GitHub detection artefact rather than a licensing problem, and I have not counted it against the project. Adding the SPDX identifier line would fix the display.

## My signature question

**Could our legal team clear this for commercial use today, from what is published?**

No — not for the components I actually want, and the blocker is documentation rather than intent.

| Component | Cleared today? | What would settle it |
|---|---|---|
| `landlab-debrisflow`, `fire-debrisflow-ml`, `da-seis-groundfailure`, `landslide-digital-twin` | **No** | A LICENSE file in each repository root |
| `seis-hydro-2-sed` | **No** | A LICENSE file; the README's "MIT License" is an assertion, not a grant |
| `gaia-cli`, `catalog`, the STAC catalogs, `thunderquakes`, `gwl-space-time-smooth` | **Yes**, for the code | Already MIT — nothing further needed for the source itself |
| `gaia-agentic-ai` | **Yes** | BSD-3-Clause, fine for us |
| `usgs-gauge-utils` | **Yes but never linked into our stack** | GPL-3.0, and the repository is marked obsolete anyway |
| `geocroissant-hazards` vocabulary | **Yes** | CC BY 4.0 in the file; add the SPDX line so tooling sees it |
| Any dataset staged by `gaia-data-downloaders` | **Unknowable** | A per-source terms table on `book/datahub` |
| Any trained model or hazard layer | **Unknowable** | A model card with training-data provenance, a baseline comparison, and a domain of validity |

The one-sentence version: the code I do not need is cleared, the code I do need has no licence, and the data and models underneath both are unknowable from outside — so the answer today is no, and roughly a week of file-writing would change it to yes.
