# Website & Book Evolution

> Structural plan for growing the GAIA site/book to cover the CSSI expansions:
> **Alaska** (new region), **geodesy**, and **SAR/InSAR processing**. Keeps the
> three-pillar digital-twin spine intact while adding a **region** axis and two new
> **modality** entries.
>
> Science-facing detail for pages lives in [../DOCS_ROADMAP.md](../DOCS_ROADMAP.md);
> this doc is the **information-architecture (IA) and delivery** plan.

## 1. Current structure (baseline)

The book is MyST-MD; the ToC is [`../myst.yml`](../myst.yml) (the legacy
`book/_config.yml` is inactive). Current top-level parts:

```
Intro · Problem Statement
Digital Twin Framework  (overview + Pillars 1–3)
Earth System Science    (soil reanalysis, soil memory, groundwater, ocean–atmosphere)
Hazards                 (landslides, post-fire debris flows, liquefaction, floods)
DataHub · ModelHub · HazEvalHub
GAIA Agent (translator, agentic, research-software)
Use Cases (Nisqually, Stehekin, river floods, convective storms)
Project Organization
```

Two front-end surfaces sit outside the book: [`../index.html`](../index.html) (splash)
and [`../dashboard.html`](../dashboard.html) (metrics/status). The site deploys via
`.github/workflows/deploy.yml` (`pixi run build-ci` → uploads `website/`).

## 2. The IA problem

The CSSI adds a **third organizing axis**. Today content is organized by **pillar** ×
**hazard**. We now add **region** (Cascadia/WA, **Alaska**) and **modality**
(seismic, hydrology, weather + **geodesy**, **SAR/InSAR**). If we bolt regions onto
hazards we get combinatorial sprawl. Chosen approach:

- **Modalities** are documented once under a new **"Observation & Processing"** part
  (geodesy, SAR/InSAR) and *cross-linked* from hazards/pillars — not duplicated.
- **Regions** become a lightweight **"Regions" landing part** plus tags/use-cases, so
  Alaska is discoverable without cloning every hazard page.

## 3. Proposed structure (target)

New/changed parts marked ⬤. Detailed page templates follow the DOCS_ROADMAP §3 spine.

```
Intro · Problem Statement
Digital Twin Framework            (unchanged spine)
Earth System Science              (unchanged)
⬤ Observation & Processing        ← NEW PART (modalities)
    - Seismic wavefields (existing content, relocated/linked)
    - ⬤ Geodesy (GNSS/GPS): overview, data, products
    - ⬤ SAR / InSAR: SAR processing, InSAR time series, deformation products
Hazards                           (add geodesy/SAR cross-links + Alaska tags)
⬤ Regions                         ← NEW PART
    - Cascadia / Washington (existing use-cases regrouped)
    - ⬤ Alaska: tectonic + cryo-hydro setting, hazards, data availability
DataHub · ModelHub · HazEvalHub   (add geodesy/SAR inventory + surrogate rows)
GAIA Agent (…)
Use Cases                         (existing + ⬤ Alaska use case stub)
Project Organization
```

### 3.1 New pages (kebab-case, per DOCS_ROADMAP conventions)

| Part | Page | File | Lead role |
|---|---|---|---|
| Observation & Processing | Overview | `book/chapters/obs-processing-overview.md` | Website + CI lead |
| " | Geodesy (GNSS) | `book/chapters/geodesy-gnss.md` | Geodesy RC lead |
| " | SAR / InSAR processing | `book/chapters/sar-insar-processing.md` | SAR RC lead |
| " | InSAR deformation products | `book/chapters/insar-deformation-products.md` | SAR RC lead |
| Regions | Overview | `book/chapters/regions-overview.md` | Website lead |
| " | Alaska | `book/chapters/region-alaska.md` | Alaska lead |
| DataHub | Geodesy & SAR inventory | `book/chapters/datahub-geodesy-sar-inventory.md` | DataHub lead |
| ModelHub | InSAR/geodesy surrogates | `book/chapters/modelhub-insar.md` | ModelHub lead |
| Use Cases | Alaska use case (stub) | `book/chapters/ak-<event>.md` | Alaska lead |

Each ships first as a **`draft` admonition stub** registered in `myst.yml` so the site
builds green immediately; content fills in per the phase roadmap.

### 3.2 Proposed `myst.yml` ToC delta

Add after the **Earth System Science** block and before **Hazards**:

```yaml
    - title: Observation & Processing
      children:
        - file: book/chapters/obs-processing-overview.md
        - file: book/chapters/geodesy-gnss.md
        - file: book/chapters/sar-insar-processing.md
          children:
            - file: book/chapters/insar-deformation-products.md
```

Add after **Hazards** (or before Use Cases):

```yaml
    - title: Regions
      children:
        - file: book/chapters/regions-overview.md
        - file: book/chapters/region-alaska.md
```

Extend existing hubs (children lists):

```yaml
    - file: book/chapters/datahub.md
      children:
        - file: book/chapters/datahub-integration-guide.md
        - file: book/chapters/datahub-inventory.md
        - file: book/chapters/datahub-geodesy-sar-inventory.md   # NEW
    - file: book/chapters/modelhub.md
      children:
        - file: book/chapters/modelhub-landslide.md
        - file: book/chapters/modelhub-liquefaction.md
        - file: book/chapters/modelhub-insar.md                  # NEW
```

Land this as **one tracked PR** (`docs/website-ia-cssi-expansion`) with all stubs, so
reviewers see the whole IA at once and the build stays green.

## 4. SAR/InSAR processing integration (technical)

SAR is the heaviest new modality (large data, real processing pipelines). Plan:

- **Software discovery hub (D1):** register **ISCE3**, and where relevant `MintPy`,
  `hyp3-sdk`/**ASF HyP3**, `dolphin`, `RAiDER`, `snaphu`, `RioXarray` in the GAIA org
  with metadata tags. ASF is a named partner — use HyP3 for on-demand processing.
- **Container (D2):** a composable InSAR Dockerfile (ISCE3 + MintPy stack) modeled on
  `seisscoped/container`; opens with the Y2 registry.
- **AI-ready data (D3):** InSAR time-series and deformation as **Zarr/TileDB**
  (Xarray-compatible) with YAML + RO-Crate metadata; event catalogs as Parquet.
- **Surrogate model (D4):** deformation/velocity surrogates on Hugging Face with model
  cards; loaders + evaluators in a linked GitHub repo.
- **Cross-hazard tie-ins:** InSAR deformation → deep-seated landslide creep and
  liquefaction/subsidence; GNSS → strain/loading context. Cross-link from the relevant
  hazard pages rather than duplicating.

## 5. Alaska region integration

- `region-alaska.md`: tectonic + cryo-hydrologic setting, priority hazards
  (subduction/crustal earthquakes, landslides/RSLs, glacial/permafrost processes,
  floods/GLOFs), and **data availability** (AEC seismic, ASF SAR, GNSS/EarthScope).
- Partner alignment: **ASF** (SAR/HyP3), **AEC** (Alaska Earthquake Center), EarthScope.
- Seed **one Alaska use case** to mirror the Cascadia use-cases and validate the
  region+modality cross-linking pattern end-to-end.

## 6. Front-end (splash + dashboard)

- [`../index.html`](../index.html): add Alaska/geodesy/SAR to the scope narrative and
  region map; add ASF/AEC to funders/partners logos as appropriate.
- [`../dashboard.html`](../dashboard.html): becomes the **Metrics Observatory** surface
  ([04](04-metrics-observatory.md)) — auto-fed panels for D1–D5 / M1–M4. Keep it a
  static page consuming a generated JSON so it works on GitHub Pages.
- Add an **events page** fed by the Google Calendar (coordination §5).

## 7. Delivery & sequencing

| When | Milestone |
|---|---|
| Y1 Q1 | IA PR merged; all stubs registered; build green (kickoff Day 45–90). |
| Y1 | Geodesy + SAR overview pages have real content; Alaska region page seeded. |
| Y2 | InSAR container in registry; DataHub geodesy/SAR inventory populated; Alaska use case. |
| Y3 | InSAR surrogate model card; deformation products DOI-archived; cross-hazard links complete. |
| Y4–Y5 | Publication-grade region + modality pages; tutorials for 4-year-college audiences. |

## 8. Guardrails

- Every new page **registered in `myst.yml`** (unregistered pages don't publish).
- Keep the **draft admonition** until a page has real content.
- Run `pixi run build-ci` (and optionally spellcheck/linkcheck) locally before PR.
- Big SAR artifacts never go in-repo — they live on Zenodo/HF/registry and are *linked*
  (respects the <1 GB GitHub / <50 GB Zenodo / containerized-large policy).
