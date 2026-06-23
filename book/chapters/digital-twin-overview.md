# The GAIA Geohazard Digital Twin

:::{note}
**Draft / scaffold.** This page anchors the three-pillar architecture. Section headings
define the intended structure; content is being filled in (see `DOCS_ROADMAP.md`).
:::

## What is a geohazard digital twin?

A digital twin of the critical zone is a continuously updated, physically consistent model
of the land surface and shallow subsurface that lets us **monitor**, **nowcast**, and
**forecast** the susceptibility of geohazards — landslides, liquefaction / ground failures,
and floods. It blends real-time observations, physics-based and surrogate models, and
weather/climate forcing into a single decision-relevant system.

## The three pillars

::::{grid} 1 1 3 3
:gutter: 3

:::{grid-item-card} Pillar 1 — Soil Reanalysis Product
:link: pillar-1-soil-reanalysis
The real-time state of soils and subsurface water content (soil moisture, water-table
depth, hydromechanical properties), blended with recent geology and climatology.
:::

:::{grid-item-card} Pillar 2 — Nowcasting Hazard Susceptibility
:link: pillar-2-nowcasting-susceptibility
Given today's soil state and current forcing, estimate the likelihood and severity of each
hazard *now*.
:::

:::{grid-item-card} Pillar 3 — Forecasting Hazard Susceptibility
:link: pillar-3-forecasting-susceptibility
Couple the nowcast with weather nowcast/forecast and climate scenarios to project hazard
susceptibility into the future.
:::

::::

## How the pillars map to the GAIA platforms

The pillars are the **workflow spine**; they are implemented on the existing GAIA
infrastructure:

- **[DataHub](datahub)** stages the multi-agency, multimodal observations that feed Pillar 1.
- **[ModelHub](modelhub)** hosts the state-estimation, susceptibility, and surrogate models
  that drive Pillars 2 and 3.
- **[HazEvalHub](hazevalhub)** defines the metrics and leaderboards that make each pillar's
  output trustworthy and actionable.

The pillars predict the **[Hazards](hazard-shallow-landslides)** targets and rest on the
**[Earth System Science](soil-memory)** that governs water and stress in the critical zone.

## Shared state-variable notation

*(To be filled — define the variables that flow between pillars, e.g. soil moisture
$\theta(x,t)$, water-table depth $d_{wt}(x,t)$, saturation $S_w$, effective stress, and the
hazard susceptibility indices, consistent with [soil-memory](soil-memory).)*

## Open questions & roadmap

- How do we keep the reanalysis, nowcast, and forecast physically consistent across pillars?
- What is the right interface (data contract) between pillars?
- See `DOCS_ROADMAP.md` for phased plan and owners.

## References
