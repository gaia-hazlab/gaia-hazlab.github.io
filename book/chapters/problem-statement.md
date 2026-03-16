# Problem Statement

## The Challenge

Landslides triggered by atmospheric rivers, liquefaction amplified by saturated soils, catastrophic runoff after wildfires, severe convective storms intensified by land–atmosphere feedbacks — the most devastating geodisasters arise from **cascading interactions across the ocean, atmosphere, and solid Earth**. The severity of these hazards — landslides, flash floods, earthquake liquefaction, and convective storms — is profoundly shaped by the **soil hydromechanical history** and by **land management practices** that alter the critical zone over time.

Yet our current models struggle to keep pace with these nonlinear cascades. Atmosphere, hydrology, and geomechanics are typically studied and modeled in isolation, leaving critical couplings unresolved. As climate change intensifies extreme weather and shifts precipitation patterns, the gap between what we can predict and what communities need to prepare for continues to grow.

---

## Our Approach

We take a **data-driven and physics-grounded** approach to **monitor**, **characterize**, and **predict** the susceptibility of climate-compounded geodisasters — both in real time and under future weather and climate scenarios.

We leverage:

- **AI and machine learning** for pattern discovery, surrogate modeling, and hazard prediction
- **New sensing technologies** such as Distributed Acoustic Sensing (DAS) for high-resolution subsurface imaging
- **Existing ground-based sensor networks** (seismic, hydrological, meteorological) and **satellite remote sensing** for continuous, multi-scale observation
- **Physical models** grounded in geomechanics, hydrology, and atmospheric science

These capabilities serve three interlinked research goals:

1. **Discovery of missing physics** — Identify the governing processes and couplings (e.g., soil memory effects, ocean–atmosphere teleconnections) that current hazard models neglect.
2. **Real-time hazard prediction** — Monitor and predict the susceptibility to landslides, floods, liquefaction, and severe storms as conditions evolve.
3. **Computational playgrounds for scenario exploration** — Build nowcasting and forecasting frameworks that couple AI-driven weather and climate models with geohazard models to interrogate future climate and hazard scenarios.

---

## Use Cases

We ground our research in real-world coupled natural disasters that validate our methods and drive technological development:

::::{grid} 2
:gutter: 3

:::{grid-item-card} 2025 Western Washington Floods & Landslides
:link: wa-2025-river-floods-sediment-transport
Atmospheric river–driven flooding and landslides across western Washington, linking precipitation extremes, soil saturation history, and sediment transport from mountain to sea.
:::

:::{grid-item-card} 2001–2031 Nisqually Earthquake
:link: wa-2001-2031-nisqually-earthquake
Investigating earthquake-induced ground failure (liquefaction, landslides) and how antecedent soil moisture and hydromechanical state modulate seismic hazard severity.
:::

:::{grid-item-card} 2025 Stehekin Post-fire Debris Flow
:link: wa-2025-stehekin
Post-wildfire debris flow hazard in the Stehekin watershed, where fire-altered soil properties interact with storm precipitation to trigger catastrophic mass movements.
:::

:::{grid-item-card} Convective Thunderstorms
:link: convective-thunderstorms
Severe convective storms and their coupling to land surface conditions, exploring how soil moisture and surface energy fluxes feed back into storm initiation and intensity.
:::

::::

---

## Backbone Technologies

We develop integrated, cloud-native infrastructure to support the full research lifecycle — from data ingestion through hazard evaluation:

- **[DataHub](datahub)** — Multimodal, cloud-native data management for geospatial hazard data spanning seismic, hydrological, meteorological, and remote sensing sources.
- **[ModelHub](modelhub)** — A registry of deep learning and physics-based models for weather forecasting, ground failure prediction, landslide susceptibility, flood hazard, and more.
- **[HazEvalHub](hazevalhub)** — Fair and standardized evaluation frameworks, leaderboards, and benchmarking protocols for hazard prediction models.
- **[Research Software](research-software)** — An ecosystem of open-source tools and agentic pipelines for reproducible, scalable scientific workflows.

---

## Earth System Science Nexus

At the heart of our framework is the **critical zone** — the thin, dynamic layer from bedrock to canopy where rock, soil, water, air, and life interact. The hydromechanical state of the soil governs how water infiltrates to recharge groundwater, evaporates to feed atmospheric moisture, or runs off to drive erosion and flooding. Understanding and monitoring this state — its **memory** of past wetting, drying, and disturbance — is essential for predicting hazard severity under current and future conditions.

We investigate two key nexus domains:

- **[Soil Hydromechanical Memory](soil-memory)** — How antecedent soil conditions control the partitioning of water between infiltration, runoff, and evapotranspiration, and how this modulates geohazard susceptibility.
- **Ocean–Atmosphere Coupling** — How oceanic forcing (e.g., sea surface temperature anomalies, atmospheric rivers) shapes extreme precipitation patterns and cascading terrestrial hazards. *(Coming soon.)*
