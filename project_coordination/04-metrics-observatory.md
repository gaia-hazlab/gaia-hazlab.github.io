# Metrics Observatory

> The automated impact-tracking system for GAIA. Extends the SCOPED open-source
> dashboard ([seisSCOPED/community-metrics](https://github.com/seisSCOPED/community-metrics))
> to collect, version, and report **delivery (D1–D5)** and **usage (M1–M4)** metrics.
> Computed **weekly** by a GitHub Action, rendered on GitHub Pages
> ([../dashboard.html](../dashboard.html)), and **DOI-archived annually**.
>
> **Principle:** every metric has an **automated source**. If a number needs a human to
> type it, redesign the pipeline or mark it clearly as manual.

## 1. Architecture

```
┌ scheduled Action (weekly) ─────────────────────────────────────────────┐
│  scripts/metrics/collect_*.py                                           │
│    GitHub API · Zenodo API · Hugging Face API · container registry ·    │
│    Google Form/Sheets export · Slack export · OpenAlex/CrossRef/Scholar │
│                       ↓ normalize → data/metrics/latest.json            │
│           append → data/metrics/history/YYYY-Www.json (versioned)       │
└──────────────────────────┬──────────────────────────────────────────────┘
                           ↓
        dashboard.html reads latest.json  →  GitHub Pages
                           ↓ (annual)
        tag + Zenodo release → DOI-archived snapshot
```

- **Single JSON contract:** collectors write `data/metrics/latest.json`; the dashboard
  only ever reads that file — so the front-end works on static Pages with no backend.
- **History:** each run appends a dated snapshot for trend lines and reproducibility.
- **Composite score:** a normalized composite across M2–M4 (alongside individual
  metrics) to spot **under-engaged domains** → triggers targeted outreach/tutorials.

## 2. Delivery metrics (D1–D5) — supply side

Targets from the Delivery Mechanism plan (Table 1). Cumulative unless noted.

| ID | Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Source (automation) |
|---|---|---|---|---|---|---|---|
| D1 | CI-template repos passing tests | 3 | 6 | 10 | 14 | 18 | GitHub API (Actions status) |
| D2 | Container images in registry | 3 | 8 | 15 | 25 | 35 | Registry logs / GHCR API |
| D3 | DOI-archived datasets | 5 | 10 | 20 | 50 | 100 | Zenodo API |
| D4 | Versioned model cards | 1 | 5 | 8 | 12 | 15 | Hugging Face API |
| D5 | JupyterBooks + hackweeks (per year) | 1+1 | 2+1 | 3+1 | 4+2 | 5+2 | Repos + Calendar |

## 3. Usage metrics (M1–M4) — impact side

Four tiers: **M1** delivery (= the D-table, supply), **M2** reuse/productivity,
**M3** breadth/multiplicity, **M4** transformation of research practice.

| Tier | Metric | Y1 | Y2 | Y3 | Y4 | Y5 | Source (automation) |
|---|---|---|---|---|---|---|---|
| M2 | Container pulls + dataset downloads (annual) | 500 | 2K | 5K | 10K | 20K | Registry + Zenodo API |
| M2 | Derived agents via `IsDerivedFrom` (cum.) | 2 | 8 | 29 | 50 | 100 | Zenodo metadata API |
| M2 | Research publications using GAIA (cum.) | 0 | 3 | 10 | 20 | 30 | Provenance YAML + Scholar |
| M3 | Unique institutions | 20 | 30 | 50 | 100 | 100 | Slack + registration forms |
| M3 | Disciplines represented | 3 | 4 | 5 | 6 | 7 | Self-report tags |
| M4 | Agent modes used in publications | >2 | >2 | >3 | >3 | >4 | Provenance YAML |
| M4 | Modalities per study (median) | >2 | >3 | >3 | >4 | >5 | Provenance YAML |
| M4 | Skill-adoption gain (post−pre, %) | +20 | +25 | +40 | +35 | +40 | Pre/post surveys |

**M4 note:** the CSSI expansions directly move these — geodesy + SAR raise *modalities
per study*; the agent registry + CTF raise *agent modes*. The Observatory is how we show
that the expansion worked.

## 4. Collectors (target: one module per source)

> **Current scaffold:** a single file, [`../scripts/metrics/collect.py`](../scripts/metrics/collect.py),
> implements the GitHub-only path (real D1; M3 an explicit `null` stub) and writes both
> `latest.json` and the weekly `history/` snapshot. The per-source modules below are the
> **target decomposition** — split `collect.py` into them as each source is wired. They do
> not all exist yet; don't go looking for `collect_zenodo.py` until D3 work starts.

| Module (target) | Reads | Emits | Auth |
|---|---|---|---|
| `collect_github.py` | Org repos, Actions status, PRs, forks, contributors, unique institutions (email domains) | D1, M2(sw), M3 | `GITHUB_TOKEN` |
| `collect_zenodo.py` | GAIA community records, downloads, `IsDerivedFrom` graph | D3, M2 | `ZENODO_TOKEN` |
| `collect_huggingface.py` | Model cards, versions, usage | D4, M2 | `HF_TOKEN` |
| `collect_registry.py` | Container images + pull counts (GHCR) | D2, M2 | `GITHUB_TOKEN` |
| `collect_scholarly.py` | OpenAlex/CrossRef/Scholar citations of GAIA tools | M2, M4 | public / key |
| `collect_provenance.py` | Provenance YAMLs across repos → modalities, agent modes | M4 | `GITHUB_TOKEN` |
| `collect_surveys.py` | Google Form/Sheets export → skill gain, disciplines | M3, M4 | service acct |
| `collect_calendar.py` | Google Calendar → seminars/hackweeks/events | D5 | service acct |

All normalize to the shared schema in §5 and are called by the weekly Action
([05 runbook §5](05-automation-runbook.md)). Start with the **no-auth / GitHub-only**
collectors in kickoff; add Google/Zenodo/HF as tokens land.

## 5. Data contract (`data/metrics/latest.json`)

```json
{
  "generated_utc": "2026-01-15T06:00:00Z",
  "project_year": 1,
  "delivery": {
    "D1_ci_templates": {"value": 3, "target": 3, "source": "github"},
    "D2_containers":   {"value": 1, "target": 3, "source": "ghcr"}
  },
  "usage": {
    "M2_pulls_downloads":     {"value": 120,  "target": 500, "source": "registry+zenodo"},
    "M2_derived_agents":      {"value": 0,    "target": 2,   "source": "zenodo"},
    "M3_unique_institutions": {"value": 14,   "target": 20,  "source": "github+slack"},
    "M4_modalities_median":   {"value": 2,    "target": ">2", "source": "provenance"}
  },
  "composite": {"score": 0.42, "under_engaged": ["geodesy", "floods"]},
  "eval": {
    "source": "frugalmind", "board_url": "https://mdenolle.github.io/frugalmind",
    "suite": "dvv_processing", "suite_label": "CodaMeter (dv/v processing)",
    "best": {"model_id": "llama3.1:8b", "score": 1.0, "cost_usd": 0.0},
    "cheapest_at_top_score": {"model_id": "llama3.1:8b", "cost_usd": 0.0},
    "max_skill_lift": {"model_id": "claude-haiku-4-5", "score_none": 0.19, "score_full": 1.0, "lift": 0.81},
    "toy_suites_excluded": ["synthetic_stalta"]
  }
}
```

### 5.1 The `eval` block — HazEvalHub scorecard (M4)

Pulled by `collect_frugalmind()` from the live [FrugalMind board](https://mdenolle.github.io/frugalmind)
(public Pages JSON, no auth). **Only the `dvv_processing` suite — "CodaMeter" (dv/v from
coda waves) — is treated as a real GAIA eval right now;** every other suite on the board
(e.g. `synthetic_stalta`) is a toy example and is listed under `toy_suites_excluded`, not
scored. As suites are promoted, add them to `REAL_EVAL_SUITES` in
[`../scripts/metrics/collect.py`](../scripts/metrics/collect.py). This is the concrete
first slice of the FrugalMind→HazEvalHub migration in
[03 §3.0](03-ai-tools-and-evals.md); it carries the **frugality/cost axis** into the
Observatory (best score, cheapest model reaching it, largest skill lift).

`target` carries the year's goal so the dashboard can render progress bars and flag
misses without extra logic.

## 6. Dashboard

The dashboard has **two surfaces on one page** ([`../dashboard.html`](../dashboard.html)),
switchable by tab. Both are static and GitHub-Pages friendly (no backend).

- **Impact tab (metrics):** fetches `data/metrics/latest.json` and renders D/M panels +
  trend sparklines from `history/`. Show **target vs actual** and the **composite +
  under-engaged domains** prominently — that's the feedback loop that drives outreach.
- **Data Catalog tab (inventory):** fetches `data/catalog/summary.json` +
  `catalog.geojson` and renders a map (SAR tracks, seismic/infrasound stations, GNSS
  sites by use) with count tiles. Full design in
  [06-data-catalog.md §5](06-data-catalog.md).
- Design all charts/maps per the **dataviz** conventions (accessible categorical
  palette, consistent light/dark).

## 6b. Data Catalog collectors (separate from impact metrics)

The observational inventory (SAR/seismic/infrasound/GNSS) has its own collectors and its
own scheduled Action, kept separate from the impact-metrics collectors so a slow FDSN/ASF
query never delays the weekly impact run. Collectors live in
[`../scripts/catalog/`](../scripts/catalog/) and are specified in
[06-data-catalog.md §4](06-data-catalog.md); they emit `data/catalog/*.csv`,
`catalog.geojson`, and `summary.json` for the dashboard's Data Catalog tab.

## 7. Annual DOI archive

Once per year: tag the metrics history, cut a **Zenodo release** (GAIA community) so the
impact record is itself a citable, FAIR artifact — and counts toward D3.

## 8. Kickoff checklist

- [ ] `scripts/metrics/` scaffolded with `collect_github.py` producing real numbers.
- [ ] `data/metrics/latest.json` written by the gated weekly Action (workflow_dispatch first).
- [ ] Dashboard reads and renders `latest.json`.
- [ ] Add Zenodo/HF/Google collectors as tokens are provisioned.
- [ ] Schedule the annual Zenodo archive for end of each project year.
