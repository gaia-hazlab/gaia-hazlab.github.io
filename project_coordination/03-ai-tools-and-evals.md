# AI Tools & Evaluation

> Plan for the agentic layer of GAIA: the **research-agent registry**, shared
> **CI-template repos** and **containers**, and the **HazEvalHub Common-Task Framework
> (CTF)** with a rigorous evaluation harness. This is where "more AI tools + evals"
> becomes concrete and measurable.
>
> Everything here is **FAIR and provenance-first**: agents, models, and datasets carry
> DOIs/SWHIDs, RO-Crate metadata, and a companion provenance YAML so reuse and
> derivation are automatically traceable ([04 metrics](04-metrics-observatory.md)).

## 1. The agentic stack (what we ship)

The GAIA GitHub org plays four roles; the AI layer sits on top:

1. **Discovery hub** — tagged registry of established community software (MTUQ,
   SeisBench, NoisePy, ObsPy, PyShred, LLMoxie, RioXarray, ISCE3, MintPy, …).
2. **Container registry** — composable Dockerfiles (model: `seisscoped/container`).
3. **CI-template repos** — full-stack research-workflow templates with tests.
4. **Research-agent repos** — the agents themselves, each with an eval + provenance.

### 1.1 Agent taxonomy

| Agent class | Job | Example |
|---|---|---|
| **RSE agent** | Research-software engineering: scaffold repos, write tests, containerize, FAIR-ify | existing eScience/Paros-supported agent |
| **Data-interrogation agents** | Query DataHub, build AI-ready cubes (Zarr/Parquet), QC | geodesy/SAR ingestion agent |
| **Modeling/surrogate agents** | Train/evaluate surrogates, emit model cards | landslide, liquefaction, InSAR surrogates |
| **Coordination agents** | Draft meeting summaries, weekly-status digests, metrics narratives | the "coordinator" role assist ([01 §2](01-project-coordination.md)) |
| **Translator agent** | Natural-language → workflow across hubs | `gaia-translator` |

### 1.2 Shared conventions (ratify in kickoff)

- **Repo layout & docs:** one template; tests required; README sets contribution rules.
- **Containers:** composable, versioned, CI-tested; permissive license (**MIT / BSD-3**).
- **Provenance:** every publication/agent ships a **provenance YAML** (software stack,
  datasets, agents used) + **RO-Crate**; derived products tag
  `relatedIdentifier: IsDerivedFrom` in Zenodo → enables M2 derived-agent counts.
- **Model cards:** Hugging Face, versioned, archived on Zenodo, linked to a GitHub repo
  that ships loaders + evaluators + training workflow.

## 2. CI-template repos (D1)

Launch the org + first **3 template repos** in Y1 (D1 target: 3→6→10→14→18 cum.).
Each template = a research workflow that passes tests in CI and is copy-to-start:

- `gaia-template-datacube` — ingest → Zarr/Parquet + RO-Crate + tests.
- `gaia-template-surrogate` — train → model card → HF publish → evaluator hooks.
- `gaia-template-agent` — a research agent with an eval harness + provenance YAML.

The **D1 metric** ("CI-template repos passing tests") is collected automatically from
the GitHub API ([04](04-metrics-observatory.md)); a template only counts when its CI is
green — evaluation is baked into delivery.

## 3. HazEvalHub — Common-Task Framework (CTF)

The flagged "next" priority (DOCS_ROADMAP §4.2). Build **hazard-relevant, actionable**
metrics, not generic ML scores. Developed with **AI2, Nathan Kutz / AI Institute for
Dynamical Systems, Kaggle-style** hosting.

### 3.0 First prototype — FrugalMind EvalHub (live)

**<https://mdenolle.github.io/frugalmind>** — repo
[`mdenolle/frugalmind`](https://github.com/mdenolle/frugalmind). This is the **working v0
of HazEvalHub**: a live eval board for scientific AI agents in geoscience. It already
demonstrates the pattern the CTF generalizes, so it is the thing to point at, extend, and
migrate — not to rebuild.

What it establishes (and HazEvalHub inherits):

- **Three questions per submission** — *Is it right?* (accuracy vs ground truth), *What
  did it cost?* (tokens/$), *Is it reproducible?* (deterministic scoring). **Cost is a
  first-class axis** — an evaluation dimension the CTF metric tables (§3.2) do not yet
  carry, and should.
- **Cost-vs-performance leaderboard** — each model plotted twice, without domain skills
  (hollow) and with them (filled), joined by a line showing **skill lift**. Upper-left
  (high skill, low cost) wins. Hover for model version/weights/metrics; export CSV/PNG.
- **Declarative JSON scoring specs, not scoring code** — reproducible and hard to game.
  This is the `gaia-eval` scorecard contract (§4) in embryo.
- **Public validation splits + hidden test splits** — the anti-memorization design §3.1
  calls for, already running.
- **Task taxonomy** — document-based (lit review, RAG QA, multimodal), software-agent
  (write a detector, run a pipeline, produce data), research-workflow (orchestration,
  trajectory scoring). Concrete benchmarks: *dv/v* parameter choice, STA/LTA code
  generation, ObsPy function usage.
- **A real result worth publishing:** free local 7B models (`qwen2.5:7b`, `llama3.1:8b`)
  hit perfect scores on *configuration* tasks once given domain skills, but fail at
  *numerical code generation*, where only cloud models succeed (~0.56 base → 0.76 with
  skills). That "skills lift small models onto frontier parity for some task classes"
  finding is the frugality thesis, and it maps directly to M4 (transformation of research
  practice).

**Migration path into HazEvalHub:**

| Step | Action |
|---|---|
| Now | Link the live board from the [HazEvalHub chapter](../book/chapters/hazevalhub.md) + book ToC; cite it as the EvalHub prototype. |
| Y1 | Move the repo under the **`gaia-hazlab`** org (or mirror it); adopt its JSON scoring spec as the `gaia-eval` scorecard schema (§4). |
| Y1 | Add the **cost axis** (tokens/$ per submission) to the CTF metric families in §3.2 — it is currently missing. |
| Y1–Y2 | Extend the task taxonomy from *agent* tasks to the **pillar × hazard** grid (§3.1); keep the agent tasks as the "research-workflow" track. |
| Y2 | Feed the board's scorecards into the Metrics Observatory (M2/M4) and DOI-archive the splits (D3) + model cards (D4). |

### 3.1 Design

- **Tasks** map to the three pillars: *state* (Pillar 1), *nowcast* (Pillar 2),
  *forecast* (Pillar 3), per hazard.
- **Hidden test sets** — public train/val; held-out test for the leaderboard (Kaggle
  pattern). Prevents overfitting and makes adoption measurable.
- **Baselines** — persistence/climatology for forecast; simple GLM/logistic for
  susceptibility — so skill is always relative.
- **Leaderboards** rendered on GitHub Pages; submissions are containerized workflows
  (reproducible, provenance-tagged).

### 3.2 Metric families (from DOCS_ROADMAP §4.2)

| Pillar | Metrics |
|---|---|
| State (P1) | RMSE/bias vs wells, soil-moisture sensors, ET; storm-response temporal correlation; physical-consistency (mass balance, hydrostatic) |
| Nowcast (P2) | POD / FAR / CSI; IoU/Dice for mapped failures; Brier + reliability; lead-time-to-alert |
| Forecast (P3) | Skill vs persistence/climatology; ROC / PR at decision thresholds; cost–loss value; lead time vs skill |
| Actionability | Decision thresholds; false-alarm cost; warning lead time |
| **Frugality** (from §3.0) | **Tokens / $ per submission; skill-per-dollar; skill lift from domain skills (with − without)** — the FrugalMind cost axis, applied to every task |

### 3.3 CTF phasing

- **v0 (now, live):** **[FrugalMind EvalHub](https://mdenolle.github.io/frugalmind)** —
  agent tasks (dv/v config, STA/LTA codegen, ObsPy usage), hidden splits, cost-vs-skill
  board. Already running; see §3.0.
- **v0.5 (Y1):** add the first *hazard* task (landslide nowcast POD/FAR/CSI) with one
  hidden test set + one baseline, on the same board — proving the board generalizes from
  agent tasks to pillar tasks.
- **v1 (Y2):** add liquefaction + a state task; containerized submissions; auto-scoring
  Action.
- **v2 (Y3):** full pillar × hazard grid; SAR/geodesy tasks (InSAR deformation → creep);
  public leaderboards drive M2/M4.
- **v3 (Y4–Y5):** hackathon-driven tasks; community-contributed benchmarks; DOI-archived
  datasets (D3 → 100 cum.) and model cards (D4 → 15 cum.).

## 4. Evaluation harness (engineering)

A shared `gaia-eval` library so every model/agent is scored the same way:

- **Interface:** a model/agent implements `predict(inputs) -> outputs`; the harness runs
  it in its container against a task's hidden set and emits a scorecard JSON.
- **Scorecard:** metric values + provenance (model card version, data DOIs, container
  digest) → feeds the Metrics Observatory (M1/M2/M4).
- **Regression gate:** template repos run the harness in CI; a PR that lowers skill
  fails — evaluation is continuous, not a one-off.
- **Agent evals:** beyond task skill, track **agent modes** (literature synthesis, code
  generation, data interrogation, best-practice prompting) and **modalities combined**
  per study — these are M4 transformation metrics, read from provenance YAML.

## 5. Agent-assisted coordination (dogfooding)

Use our own agents to run the project — the most credible adoption story:

- **Meeting-notes agent:** Zoom transcript → cleaned/anonymized MD summary
  (accomplishments, decisions, action items, issue links) → private `notes` repo.
- **Weekly-status digest agent:** `#weekly-status` posts → monthly Discussion summary.
- **Metrics-narrative agent:** turns the Observatory's numbers into the NSF-report prose
  ([templates/nsf-annual-report-entry.md](templates/nsf-annual-report-entry.md)).
- **Triage agent:** labels/routes new issues by thrust (mirrors the Gmail routing).

These run as scheduled Actions ([05 runbook](05-automation-runbook.md)); each keeps a
provenance trail so "agents used in coordination" is itself a tracked M4 signal.

## 6. Guardrails

- Human-in-the-loop for anything outward-facing (reports, partner comms): agents draft,
  a role approves.
- No fabricated DOIs or citations (DOCS_ROADMAP §4.1); provenance must be real.
- Keep secrets (LLM API keys, tokens) in GitHub Secrets, never in repo
  ([05 runbook §1](05-automation-runbook.md)).
