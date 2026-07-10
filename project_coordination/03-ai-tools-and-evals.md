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

### 3.3 CTF phasing

- **v0 (Y1):** one task (e.g. landslide nowcast POD/FAR/CSI), one hidden test set, one
  baseline, leaderboard stub on Pages.
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
