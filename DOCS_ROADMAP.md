# GAIA Digital-Twin Documentation Roadmap

> Planning document for the science/technology write-up that organizes GAIA HazLab
> around **building geohazard digital twins**. This file is *meta* — it is not part of
> the published book (not in `myst.yml`). It tracks structure, ownership, and status so
> the documentation can grow into citable, publication-grade material.

## 1. Vision

Our goal is to **predict, in real time, the susceptibility of geohazards in the critical
zone** — landslides, liquefaction / ground failures, and floods — and to project that
susceptibility into the future under weather and climate scenarios. The documentation is
organized around a **three-pillar digital-twin architecture**:

1. **Soil Reanalysis Product (Pillar 1)** — the real-time state of soils and subsurface
   water content, blended with recent geology/climatology. A soil "reanalysis" in the
   sense of atmospheric reanalysis: a continuously updated, physically consistent estimate
   of state variables (soil moisture, water-table depth, hydromechanical properties).
2. **Nowcasting Hazard Susceptibility (Pillar 2)** — given today's soil state plus current
   forcing, estimate the likelihood and severity of each hazard *now* (shallow/deep
   landslides, debris flows, earthquake liquefaction/ground failure, floods).
3. **Forecasting Hazard Susceptibility (Pillar 3)** — couple the nowcast with weather
   nowcast/forecast and climate scenarios to project hazard susceptibility into the future.

These pillars are the **workflow spine**. They cut across the existing GAIA platforms —
**DataHub** (ingestion/staging), **ModelHub** (susceptibility & surrogate models), and
**HazEvalHub** (evaluation & metrics) — and they predict the **hazard targets** documented
in the Hazards section. The Earth System Science section supplies the underpinning physics.

```
            ┌─────────────── DIGITAL TWIN FRAMEWORK (workflow spine) ──────────────┐
            │  Pillar 1: Soil Reanalysis → Pillar 2: Nowcast → Pillar 3: Forecast   │
            └───────┬───────────────────────┬───────────────────────┬──────────────┘
                    │ physics                │ targets               │ infrastructure
        ┌───────────▼──────────┐  ┌──────────▼─────────┐  ┌──────────▼───────────┐
        │ Earth System Science │  │      Hazards       │  │      Technology      │
        │ soil memory, fluxes, │  │ landslides, debris │  │ DataHub / ModelHub / │
        │ groundwater, O–A     │  │ flows, liquefac-   │  │ HazEvalHub /         │
        │ coupling             │  │ tion, floods       │  │ research software    │
        └──────────────────────┘  └────────────────────┘  └──────────────────────┘
```

## 2. Information architecture

The book is built with **MyST-MD**. The published table of contents lives in
[`myst.yml`](myst.yml) (the `book/_config.yml` is a legacy Jupyter Book config and is *not*
the active ToC). **Any new page must be registered in `myst.yml`.**

Target structure (✅ = registered in `myst.yml`):

| Part | Page | File | Status |
|---|---|---|---|
| _top_ | Intro | `book/intro.md` | existing |
| _top_ | Problem Statement | `book/chapters/problem-statement.md` | existing |
| **Digital Twin Framework** | Overview | `book/chapters/digital-twin-overview.md` | ✅ stub |
| | Pillar 1 — Soil Reanalysis Product | `book/chapters/pillar-1-soil-reanalysis.md` | ✅ stub |
| | Pillar 2 — Nowcasting Hazard Susceptibility | `book/chapters/pillar-2-nowcasting-susceptibility.md` | ✅ stub |
| | Pillar 3 — Forecasting Hazard Susceptibility | `book/chapters/pillar-3-forecasting-susceptibility.md` | ✅ stub |
| **Earth System Science** | Soil Hydromechanical Memory | `book/chapters/soil-memory.md` | existing |
| | Soil Reanalysis Science (water fluxes, land-surface modeling) | `book/chapters/soil-reanalysis-science.md` | ✅ stub |
| | Groundwater & Soil Moisture (resource management) | `book/chapters/groundwater-soil-moisture.md` | ✅ stub |
| | Ocean–Atmosphere Coupling | `book/chapters/ocean-atmosphere-coupling.md` | ✅ stub |
| **Hazards** | Shallow Landslides | `book/chapters/hazard-shallow-landslides.md` | ✅ stub |
| | Deep-Seated Landslides | `book/chapters/hazard-deep-seated-landslides.md` | ✅ stub |
| | Debris Flows | `book/chapters/hazard-debris-flows.md` | ✅ stub |
| | Liquefaction & Ground Failure | `book/chapters/hazard-liquefaction-ground-failure.md` | ✅ stub |
| | Floods | `book/chapters/hazard-floods.md` | ✅ stub |
| **Technology** | DataHub / ModelHub / HazEvalHub / Translator / Research Software | `book/chapters/*` | existing |
| **Use Cases** | Nisqually / Stehekin / River floods / Convective storms | `book/chapters/*` | existing |
| _top_ | Project Organization | `book/chapters/project-organization.md` | existing |

## 3. Page template (every pillar & hazard page)

To keep pages convertible into manuscripts, each pillar and hazard page follows the same
spine:

1. **Scientific framing** — the process and why it matters for prediction.
2. **State variables & observables** — what we estimate; what we measure (with notation,
   following the [soil-memory](book/chapters/soil-memory.md) page's style).
3. **Data** — what we ingest, linked to **DataHub**.
4. **Models** — methods/surrogates, linked to **ModelHub**.
5. **Evaluation & metrics** — how we score skill and actionability, linked to **HazEvalHub**.
6. **Open questions & roadmap** — research gaps, planned work, owners.
7. **References** — `[@key]` citations resolved from [`book/references.bib`](book/references.bib).

## 4. Cross-cutting workstreams

### 4.1 Citations (publication-readiness)
- `book/references.bib` is the single bibliography; `myst.yml` registers it via
  `project.bibliography`. Cite with `[@key]`.
- **Action:** verify the DOIs marked `TODO` in `references.bib` before any page is treated
  as publication-ready. Do not ship fabricated DOIs.
- The [soil-memory](book/chapters/soil-memory.md) page is the worked example of the citation
  pattern.

### 4.2 Evaluation & metrics (the flagged "next" priority)
The [HazEvalHub](book/chapters/hazevalhub.md) page currently stubs metrics in comments. The
priority is to define **hazard-relevant, actionable metrics** for digital-twin insight, not
just generic ML scores. Target metric families per hazard, to be developed with AI2 and the
AI Institute for Dynamical Systems Common Task Framework:

- **State (Pillar 1):** RMSE/bias vs. wells, soil-moisture sensors, ET products; temporal
  correlation of storm response; physical-consistency checks (hydrostatic, mass balance).
- **Nowcast (Pillar 2):** event-based detection (POD, FAR, CSI), spatial agreement
  (IoU/Dice for mapped failures), probabilistic calibration (Brier, reliability), lead-time
  to alert.
- **Forecast (Pillar 3):** skill vs. persistence/climatology baselines, ROC/precision-recall
  at decision thresholds, value/utility metrics (cost-loss), forecast lead time vs. skill.
- **Actionability:** decision-relevant thresholds, false-alarm cost, warning lead time —
  metrics that translate to operational and community value.

### 4.3 Conventions
- File naming: `pillar-N-*.md`, `hazard-*.md`, kebab-case.
- Cross-links use the page basename, e.g. `[DataHub](datahub)`.
- Math: `dollarmath` is enabled; follow soil-memory's LaTeX conventions.
- Cards/grids: `sphinx-design` / `{grid}` directives (see problem-statement.md).
- Keep the "draft" admonition at the top of a stub until the page has real content.

## 5. Phased plan

**Phase 0 — Scaffolding (this change).** Roadmap, ToC restructure, `references.bib`,
templated stubs. ✅

**Phase 1 — The spine.** Fill `digital-twin-overview.md` and the three pillar pages with the
content from the three-pillar write-up. Establish state-variable notation shared across
pillars. Seed `references.bib`.

**Phase 2 — Earth System Science.** Expand soil-reanalysis science (water fluxes,
land-surface modeling) and groundwater/soil-moisture; connect to existing soil-memory.

**Phase 3 — Hazards.** One page per hazard, each ending in metrics + references. Cross-link
to use cases (e.g., liquefaction ↔ Nisqually, debris flows ↔ Stehekin).

**Phase 4 — Evaluation platform.** Replace HazEvalHub stubs with the metric definitions from
§4.2; define leaderboards and the hidden-test common-task framework.

**Phase 5 — Publication.** Verify all DOIs, harmonize notation, and split pages into
manuscript drafts.

## 6. Suggested page leads (confirm)

Inferred from current ModelHub/ESS attributions — confirm and adjust:

- **Soil reanalysis / dv/v → state:** Marine Denolle, Manuela Köpfli
- **Liquefaction & ground failure:** Morgan Sanger, Yiyu Ni
- **Earthquake wavefields:** Yiyu Ni
- **Landslide detection / susceptibility:** Akash Kharita, Scott Henderson (+ AI2)
- **Weather nowcast/forecast (AR, Clima-X):** Richard Zhuang, Brandon Kerns, Aditya Grover
- **Convective storms / heatwaves:** Alexandra Anderson-Frey, Greg Hakim
- **Floods:** _to assign_
- **Evaluation & metrics:** _to assign_ (with Nathan Kutz / Kaggle / AI2)
