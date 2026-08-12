# Review: CTO of a geospatial AI and foundation-model company

**Reviewed:** 2026-08-12 · **Scope:** landing page; `/book` and the chapters my checks name (hazevalhub, modelhub, datahub, licensing, decisions, organization, how-we-work, faq, problem-statement); the live FrugalMind eval board at `mdenolle.github.io/frugalmind` and its underlying `data/leaderboard.json`; the `gaia-hazlab` GitHub organisation (26 public repositories) and four of them in detail — `gaia-translate-QA`, `catalog`, `gaia-landslides-detect`, `gaia-agentic-ai` · **Time spent:** 45 minutes (budget spent; see "What I could not judge")

*I am a simulated reviewer, not a real one. This persona is constructed from the project's context and from what someone in my role typically needs. Everything below is a hypothesis about a real reader, not evidence about one.*

## The sixty-second test

Written before I read anything else, and not revised:

> "They build digital twins of the Earth by fusing open multimodal data with AI and cloud computing, to monitor and forecast soil, landslides, liquefaction and floods."

That sentence contains no evaluation hub. I came to this site to assess a benchmark, and after sixty seconds on the landing page I did not know one existed. I found HazEvalHub only by opening the book and reading the technology section.

## In one paragraph

There is a real thing here, and it is smaller and more honest than the site around it. The FrugalMind board is a working evaluation with a genuinely good idea in it — cost as a scored axis alongside accuracy — and one of its published numbers checks out exactly against the data file behind the board. But when I went to find out whether a score on this benchmark means anything, the board's own data file told me it might be running smoke tests rather than the real held-out set, the repository holding the scoring code returned 404, and the hazard-side evaluation framework turned out to be a page of empty headings under a heading that says "TBD". Meanwhile the ModelHub documents a Python API that does not exist and asserts in the present tense that every model ships with a model card and is benchmarked against baselines, when no model card and no result is published anywhere. Nothing on this site names persistence or climatology. For my purposes that combination is decisive: I would not put one of our models through this today, and I would not cite a number off this board. I would revisit in six months if the scoring code goes public and the tasks get written down.

## Weighted score: 49/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 10 | Clear what the project is; the evaluation hub is invisible from the front door |
| D2 Credibility of claims | 2 | 20 | Present-tense claims for artifacts that do not exist; one board claim does verify |
| D3 Navigation and information scent | 3 | 5 | Book structure is sane; two links render as raw template variables |
| D4 Visual design and accessibility | 3 | 5 | Legible and unremarkable; largely outside my competence, see below |
| D5 Technical depth and reproducibility | 2 | 25 | Scoring code private, no baselines, no contamination policy, framework TBD |
| D6 Governance and openness | 2 | 20 | Excellent decision *form*, but nothing ratified and the benchmark conflict is unaddressed |
| D7 Activity and durability | 4 | 10 | Pushes within the last two days, board regenerated three weeks ago, three linked NSF awards |
| D8 Relevance to me | 3 | 5 | Right problem; current tasks are agent tasks, not Earth-observation tasks |

## Findings

### 1. The published leaderboard may not be the held-out evaluation, and its own data file says so — BLOCKER · D5

**Where:** https://mdenolle.github.io/frugalmind and https://mdenolle.github.io/frugalmind/data/leaderboard.json

**Saw:** The board tells the reader: "The ranked numbers come from a **hidden** split whose answers are never published — not in git, not on the hub." The JSON file that populates that same board carries, in its `notes` array: "Public leaderboard data may use smoke tests until private golden-set scores are approved for release." The file's `source` field reads `"scripts/demo_dashboard.py --live"`, and every one of the thirty rows carries `"run_file": "demo_dashboard.py --live"`. No row carries a field distinguishing a smoke-test score from a golden-set score.

**Why it matters to me:** This is the one question I came to answer and the site answers it two ways on the same screen. If I cite a number from this board in one of our papers, I cannot state what produced it, and neither can the board. The word "may" is doing catastrophic work — it means every row is of unknown provenance, including the seven scores of exactly 1.000. This is where I stop. Everything below this line I checked for completeness rather than because I was still considering adoption.

**Suggested fix:** Add a required per-row field (`split: golden | smoke`) to the scorecard schema and render it as a column on the board. Grey out or hide smoke rows by default. This is a schema change and a filter, not a research project.

**Confidence:** high

---

### 2. The scoring code is not public, so the anti-gaming claim cannot be checked — MAJOR · D6

**Where:** https://gaia-hazlab.github.io/book/hazevalhub/ (link text "source: mdenolle/frugalmind", href `https://github.com/mdenolle/frugalmind`)

**Saw:** The chapter claims scoring is "Deterministic scoring from declarative JSON specs, so results can't be gamed." The linked source repository, `https://github.com/mdenolle/frugalmind`, returns HTTP 404 (checked 2026-08-12); the GitHub API returns `"Not Found"`. The rendered board at `mdenolle.github.io/frugalmind` serves fine, so the Pages site is published from a repository I cannot see.

**Suggested fix:** Make the repository public, or move the scorer into the `gaia-hazlab` organisation under the `gaia-eval` category the organisation chapter already defines. Until then, remove the "can't be gamed" sentence — it is a claim about code nobody can read.

**Why it matters to me:** "Results can't be gamed" is a statement about an implementation. With the implementation private, I am being asked to take the deterministic-scoring property on trust, from the same party that holds the answer keys and publishes models scored by it. That is not a standard I can defend to our research leadership.

**Confidence:** high

---

### 3. No trivial baseline appears anywhere on the site — MAJOR · D5

**Where:** https://gaia-hazlab.github.io/book/hazevalhub/, and by absence across every book chapter I opened

**Saw:** Under the heading "Baseline Models", the entire content is one sentence: "We will provide standard baselines for comparison (e.g., statistical baselines, classic ML models)." Future tense, no named baseline. I then searched the text of every book chapter I had fetched — hazevalhub, modelhub, datahub, licensing, decisions, organization, how-we-work, faq, problem-statement, research-software. The strings "persistence", "climatolog", "nearest neighbo" and "skill score" do not occur on any of them.

**Why it matters to me:** For weather-compounded hazard forecasting, persistence and climatology are the baselines that decide whether a result exists at all. A landslide or flood model that does not beat climatology has not been evaluated, it has been described. Their total absence from an evaluation hub is the single clearest signal to me that the hazard-side evaluation has not yet been designed by someone who has had to defend a forecast skill number.

**Suggested fix:** For each of the two announced tracks, name the mandatory baselines in the task spec — persistence and climatology at minimum, plus a nearest-neighbour or logistic-regression reference for the classification tasks — and require every submission to report against them in the same table.

**Confidence:** high

---

### 4. The benchmark is not separable from the group whose models it scores — MAJOR · D6

**Where:** https://gaia-hazlab.github.io/book/organization/, https://gaia-hazlab.github.io/book/decisions/, https://gaia-hazlab.github.io/book/modelhub/

**Saw:** The organisation chapter lists among "Software we maintain": "the evaluation library behind HazEvalHub, and the research agents." The same organisation publishes ModelHub, "where we register the machine learning and physics-based models that monitor and predict hazards." The entry ladder puts benchmark admission at "Level 3 | Benchmarked | It becomes a task or baseline in the evaluation hub | Maintaining the task and its held-out data" — with no statement of who decides admission, while the far less consequential Level 4 does require "a named maintainer and a numbered decision". The decisions register contains exactly four entries — funding acknowledgment, Slack retention, meeting schedule, and a Google account — and all four read "Status: proposed" with "Date: —". None concerns the evaluation set.

**Why it matters to me:** One group holds the answer keys, writes the scorer, chooses the tasks, and enters models. Every benchmark starts this way and the good ones publish the conflict and constrain it. Nothing here does. (Inference, marked as such: I am not suggesting anyone would act on the conflict — I am saying I cannot tell an outside reader why they should not worry about it.)

**Suggested fix:** Write one numbered decision covering benchmark governance: who admits a task, who holds the held-out answers, and a rule that GAIA-authored models are labelled as such on the board. Even an imperfect published rule beats an unwritten one.

**Confidence:** high

---

### 5. Dataset licensing never addresses training or commercial use — MAJOR · D6

**Where:** https://gaia-hazlab.github.io/book/licensing/

**Saw:** The page opens with an admonition: "Status. Proposed, awaiting a numbered decision in the decisions register. Until it is ratified, individual repositories may not yet match what is described here." The licence table gives "Curated data products we generate | CC BY 4.0, with upstream terms restated" and "Data we merely redistribute | upstream terms, restated". The word "commercial" occurs on the page exactly twice, both times inside the AI-assisted-code section pointing at the "Anthropic Commercial Terms" — never about GAIA's own data. There is no sentence anywhere about training a machine-learning model on these datasets.

**Why it matters to me:** I need this stated, not inferred. CC BY 4.0 would permit what I want, but "upstream terms, restated" describes a policy for restating terms rather than the terms themselves, and the DataHub chapter does not carry per-dataset licence rows. So for any given dataset I would have to run the upstream provenance myself before our lawyers would let it near a training corpus. That cost, multiplied across a catalogue, is why we walk away from datasets that are probably fine.

**Suggested fix:** Add one sentence to the licensing page — "GAIA-generated data products under CC BY 4.0 may be used to train machine-learning models, including commercially, with attribution" — and add a licence column to the per-hazard data inventories.

**Confidence:** high

---

### 6. A third of the organisation's repositories carry no licence, including an evaluation-dataset repository — MAJOR · D6

**Where:** https://github.com/gaia-hazlab (26 public repositories, enumerated via the GitHub API on 2026-08-12)

**Saw:** Nine repositories report no licence at all: `seis-hydro-2-sed`, `.github`, `gaia-data-downloaders`, `awesome-gaia`, `landlab-debrisflow`, `gaia-translate-QA`, `mt-rainier-smart-sensing`, `da-seis-groundfailure`, `shred-landlab-prototypes`. One more, `geocroissant-hazards`, reports `NOASSERTION`. `gaia-translate-QA` is described as "repository to build evaluation data set for the aia translateor" and contains a directory named `eval_dataset` — an evaluation dataset with no licence. Separately, `usgs-gauge-utils` is GPL-3.0, in an organisation whose own policy says of copyleft: "Avoid for anything meant to be a library; never vendor into MIT".

**Why it matters to me:** No licence means no permission, so these are unusable to me regardless of quality — and the one I would most want, an eval dataset, is among them. The licensing page pre-announces this gap, which I credit, but a warning that repositories may not match the policy does not make the repositories usable.

**Suggested fix:** Add a LICENSE to the nine, starting with `gaia-translate-QA` and `gaia-data-downloaders`. Add a CI check that fails the org dashboard when a public repository lacks one.

**Confidence:** high

---

### 7. ModelHub documents a Python API that does not exist — MAJOR · D2

**Where:** https://gaia-hazlab.github.io/book/modelhub/

**Saw:** Four code blocks presented as usage, without any "planned" or "illustrative" marker. For example: `from gaia_hazlab.models import FloodDetectionModel` followed by `model = FloodDetectionModel.from_pretrained('flood-v1.0')`; and `from gaia_hazlab.serving import ModelServer` / `server = ModelServer(model='flood-detection-v1.0')` / `server.start(port=8000)`. There is no `gaia-hazlab` or `gaia_hazlab` package on PyPI (both return 404, checked 2026-08-12), and no repository in the organisation provides that import path.

**Why it matters to me:** My evaluation of a project's honesty is largely a count of how many of its concrete-looking statements survive being checked. This one fails in about ninety seconds — the time to try `pip install`. Once I find one API documented into existence, I re-read every other present-tense sentence on the site as aspirational, which is what happened for findings 8 and 9 below.

**Suggested fix:** Either mark the blocks "planned API, not yet released", or delete them. The rest of the chapter — the named models with named leads — is the credible part and is undermined by sitting next to these.

**Confidence:** high

---

### 8. Model cards and benchmark results are asserted in the present tense; none is published — MAJOR · D2

**Where:** https://gaia-hazlab.github.io/book/modelhub/

**Saw:** "Each model ships with a model card covering: Model description and intended use; Training data and preprocessing steps; Performance metrics and limitations; Ethical considerations and biases; Citation and attribution." And: "All models in the ModelHub are benchmarked against: Baseline models (traditional statistical approaches); The best published method for the task; Domain-specific metrics and standards." The chapter then lists roughly fifteen models across hazard, flood and landslide sections. I could not find a single model card or a single benchmark number for any of them, on that page or linked from it. The citation template is itself a placeholder: "GAIA HazLab Team. (2024). [Model Name]. GAIA HazLab ModelHub."

**Why it matters to me:** Model cards with training data and failure modes are check six on my list and the thing I would need before putting any of these near a product. "Ships with" describes a state of affairs. The true statement is "will ship with", and the difference is the whole question.

**Suggested fix:** Publish one real model card — the Mt. Rainier surface-event detector is the obvious candidate since a catalogue already exists — and change the present-tense sentences to future tense until the rest follow.

**Confidence:** high

---

### 9. Pretraining contamination is never mentioned — MAJOR · D5

**Where:** https://gaia-hazlab.github.io/book/hazevalhub/, and by absence across all book chapters checked

**Saw:** The strings "contaminat" and "leakage" do not appear on any book chapter I fetched. The nearest statement is on the eval prototype: "Validation splits are public; test splits are hidden to prevent memorization."

**Why it matters to me:** Hiding a test split protects against a model being fine-tuned on it. It does nothing about the case that actually bites us: the evaluation is built from Sentinel scenes, USGS catalogues and ObsPy documentation, and a frontier model has already read all of it during pretraining. On the agent tasks named here — "ObsPy function usage", "STA/LTA code generation" — this is not a theoretical risk, it is the most likely explanation for a high score. An evaluation hub that has not written a paragraph about this has not yet met its main adversary.

**Suggested fix:** One paragraph in the chapter stating the position, plus a cheap concrete measure: hold back a portion of tasks built from data published after a stated cutoff, and report those scores separately.

**Confidence:** high

---

### 10. The submission path is a broken template placeholder — MAJOR · D3

**Where:** https://gaia-hazlab.github.io/book/modelhub/ and https://gaia-hazlab.github.io/book/hazevalhub/

**Saw:** ModelHub, under "Contributing Models", renders the literal text: `Follow our [model contribution guidelines]({{ github_org_url }}/{{ book_repo }}/blob/main/CONTRIBUTING.md)`. HazEvalHub, under "Resources", renders: `[Metrics API Reference]({{ github_org_url }}/{{ book_repo }}/wiki/metrics-api)`. Both are unrendered template variables published as page text, not links.

**Why it matters to me:** This is check seven on my list — could an outside team submit a model, and what does it cost them. The answer on the ModelHub side is that the instructions do not resolve. The board's own page does better (it describes pinning agents by commit SHA and publishing validation splits to Hugging Face or Zenodo with DOIs), but the book chapter a reader lands on first is a dead end.

**Suggested fix:** Fix the two template variables, and add a link from the ModelHub contribution section to the board's submission description so there is one path rather than two half-paths.

**Confidence:** high

---

### 11. The hazard evaluation framework is a skeleton of empty headings — MINOR · D5

**Where:** https://gaia-hazlab.github.io/book/hazevalhub/

**Saw:** A heading reading "Evaluation Framework (TBD)", followed by ten headings with no body text beneath them: "Evaluation Metrics", "Validation Protocols", "Cross-Validation", "Performance Comparison", "Uncertainty Quantification", "Probabilistic Evaluation", "Case Studies", "Quality Assurance", "Operational Evaluation", "Real-time Monitoring". The subsections that do carry text are lists of category names, for example "Geographic hold-out: Testing on different regions".

**Why it matters to me:** Minor only because the "(TBD)" is honest — I was not misled, and I would rather see an admitted gap than a filled-in one. But it means check four, whether a task is specified tightly enough for someone who did not design it to reproduce it, has no answer yet on the hazard side.

**Suggested fix:** Collapse the empty headings into a single short "Not yet written" note. Ten empty headings read as abandonment; one honest sentence reads as a plan.

**Confidence:** high

---

### 12. The evaluation is very small, and the board does not say so — MINOR · D5

**Where:** https://mdenolle.github.io/frugalmind/data/leaderboard.json

**Saw:** Thirty rows covering five distinct models across three suites, with `n_total` of 12 (`lit_rag`), 20 (`codameter`) and 11 (`synthetic_stalta`). Seven rows score exactly 1.000, all on the 12-item and 20-item suites.

**Why it matters to me:** A perfect score on twelve items tells me almost nothing — the confidence interval swallows the ranking. This does not make the board wrong, it makes the ordering unstable, and the page presents ranks 1 through 30 without an error bar or an item count in view. Ranking is the format's implicit claim to precision it does not have.

**Suggested fix:** Show `n` next to every score on the board and add a confidence interval to the scatter. The data are already in the JSON; this is a rendering change.

**Confidence:** medium — I am reading item counts from the data file, and per finding 1 these may be smoke-test sizes rather than golden-set sizes.

---

### 13. The headline result omits that domain skills made most local models worse — MINOR · D2

**Where:** https://gaia-hazlab.github.io/book/hazevalhub/ compared against https://mdenolle.github.io/frugalmind/data/leaderboard.json

**Saw:** The chapter summarises: "Free local 7B models (qwen2.5:7b, llama3.1:8b) reach perfect scores on configuration tasks once given domain skills — but fail at numerical code generation, where only cloud models succeed (~0.56 base, rising to 0.76 with skills)." In the data, on `synthetic_stalta`, the skill lowered three of four local models against their own generic-agent condition: qwen2.5:7b 0.200 to 0.109, llama3.1:8b 0.191 to 0.100, olmo2:7b 0.191 to 0.109. Only deepseek-r1:7b improved, 0.009 to 0.045.

**Why it matters to me:** "Fail at numerical code generation" is true but softer than what the data show, which is that the intervention was actively harmful on that suite. The chapter's next sentence does concede the effect is uneven, so this is a matter of emphasis rather than a misstatement — but a negative result is the most interesting thing on this board and it is currently buried in a JSON file.

**Suggested fix:** State the regression directly in the chapter. It is the most credible sentence available to you.

**Confidence:** high

---

### 14. "thrust" is used as a unit of organisation without ever being defined — MINOR · D1

**Where:** https://gaia-hazlab.github.io/book/how-we-work/, https://gaia-hazlab.github.io/book/faq/, https://gaia-hazlab.github.io/book/decisions/

**Saw:** "Monthly, thrust sync | Figures below target are agenda item one." And: "Levels 0–3 are handled by the relevant thrust lead through the normal pull-request process." And, in GAIA-D-003: "Monthly cycle: thrust sync in week 3 (where decisions of record are taken)".

**Why it matters to me:** I do not know this word. It appears to name a subdivision of the project with a lead and a budget, but I am guessing, and the guess matters because "the relevant thrust lead" is who I would have to reach to get a task admitted to the benchmark. Flagging rather than assuming, per my own limits.

**Suggested fix:** Define it once in the FAQ, or replace it with a word an outside collaborator already owns.

**Confidence:** high

---

### 15. The flagship detector repository ships no data and no weights, under a different model name than the site uses — POLISH · D5

**Where:** https://gaia-hazlab.github.io/book/modelhub/ and https://github.com/gaia-hazlab/gaia-landslides-detect

**Saw:** The chapter says: "The QuakeXNet detector + ENVELOC location produce a 15-year Mt. Rainier surface-event catalog and interactive map". The repository README instead advertises "QuakeScope model support with pre-trained weights". Its `data/` directory contains only `raw/`, `processed/` and a `.gitkeep`; no weights are present. The repository does carry a LICENSE, CONTRIBUTING.md, tests and a `train.py`, which is better structured than most in the organisation.

**Why it matters to me:** Polish, because I would expect weights to live on a model hub rather than in git. But two names for what I think is one model is the kind of thing that costs a downstream user an afternoon, and the empty data directories mean I cannot reproduce the catalogue from this repository alone.

**Suggested fix:** Reconcile the name in one place or the other, and add a line to the README saying where the weights and the 15-year catalogue actually live.

**Confidence:** medium — I did not read the source, so QuakeXNet and QuakeScope may genuinely be two different things.

## What worked

**Cost is scored as a first-class axis.** From https://gaia-hazlab.github.io/book/hazevalhub/: "What did it cost? | Token/dollar cost — cost is a first-class axis, not an afterthought". The board renders this as a cost-versus-performance scatter where "each model appears twice — *without* domain skills (hollow marker) and *with* them (filled) — joined by a line showing the skill lift." Almost every public benchmark I deal with reports accuracy and ignores what the accuracy cost, which is exactly backwards for anyone deciding what to deploy. This design is better than what we use internally and I would say so in public. Protect it.

**A specific published number survived checking.** The chapter claims cloud models reach "~0.56 base, rising to 0.76 with skills" on numerical code generation. The data file gives claude-haiku-4-5 at 0.559 under `generic-coding-agent` and 0.758 under `stalta-detection+skill-v0.3`. The claim is falsifiable, I falsified against it, and it held. That is rarer than it should be and it is the main reason I finished the review rather than closing the tab at finding 1.

**The decisions register is well designed.** From https://gaia-hazlab.github.io/book/decisions/: "Nothing counts as decided until it has a number here. If it lives only in a Doc, a Slack thread, or someone's memory of a call, it is still a proposal." And: "Entries are never edited after they go active — to change a decision, write a new entry that supersedes the old one." Each entry carries a "Rejected:" field naming the alternatives. I would point our own engineering leadership at this format. The problem is not the instrument, it is that all four entries still read "proposed" — and the register would be the right place to fix findings 4 and 5.

**The licensing page is honest about the limits of its own authority.** "Most inputs — USGS gauge records, ASF products, NASA holdings — are federal and already public domain or carry their own terms. We cannot relicense them; stamping a GAIA licence on a repackaged federal dataset asserts a right we do not have." Most projects at this stage quietly stamp the whole catalogue with one licence. Getting this right early is worth more than it looks.

## What I could not judge

- **Whether the hidden golden sets exist and are well constructed.** By design I cannot see them, and per finding 2 the repository that would hold their construction code is not public. This is the single largest gap in my assessment and it is unresolvable from outside.
- **Visual design and accessibility in any depth.** I scored D4 at 3 on the basis that pages were legible and loaded quickly on desktop. I did not test a phone viewport, keyboard reach, contrast ratios or alt text, and I am not the right reviewer for it. Treat that score as a placeholder rather than a judgement.
- **The hazard science itself.** Whether the Landlab landslide implementation, the liquefaction surrogate or the wavefield reconstruction models are any good is outside my competence entirely. I assessed how they are evaluated and documented, not whether they are right.
- **The word "thrust".** Flagged in finding 14 rather than assumed. I do not know how much of the governance structure I misread as a result.
- **Whether the 11–20 item suites reflect real golden-set sizes.** Finding 1 makes every count in that file ambiguous.
- **What I ran out of time for.** My 45 minutes went on the eval board, the licensing chain and the repository licence sweep. I never opened `/dashboard.html`, `/presentations.html` or `/people.html` beyond confirming they return 200, and I did not read the `research-software` chapter, which may well answer some of finding 10. I also did not look for a CONTRIBUTING or a governance file at the organisation root. A more patient reader would have found more; a less patient one would have stopped at finding 1, which is where the actual decision got made.

## My signature question

**Would a result on this benchmark be worth citing in a paper of ours?**

No — not today, because the board cannot tell me whether a given number came from the hidden golden set or from a smoke test, and the code that produced it is in a repository I cannot open. The single change that would most improve the answer: publish the scorer and the task specifications, and stamp every leaderboard row with the split that produced it. Do that and I will run one of our models through it and publish the result, including if it embarrasses us.
