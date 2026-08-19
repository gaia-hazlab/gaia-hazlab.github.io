# Problem Statement

## The Challenge

Landslides triggered by atmospheric rivers, liquefaction amplified by saturated soils, catastrophic runoff after wildfires, severe convective storms intensified by land–atmosphere feedbacks: the worst geodisasters arise from **cascading interactions across the ocean, atmosphere, and solid Earth**. How bad each one gets is set largely by the **soil hydromechanical history** and by the **land management practices** that reshape the critical zone over years and decades.

Our models do not resolve those cascades. Atmosphere, hydrology, and geomechanics are studied and modeled separately, and the couplings between them fall in the gaps. Climate change is intensifying extreme weather and shifting precipitation patterns faster than that fragmented picture can track.

---

## Our Approach

We take a **data-driven and physics-grounded** approach to **monitor**, **characterize**, and **predict** the susceptibility of weather-compounded geodisasters — both in real time and under future weather and climate scenarios.

We build on:

- **AI and machine learning** for pattern discovery, surrogate modeling, and hazard prediction
- **New sensing technologies** such as Distributed Acoustic Sensing (DAS) for high-resolution subsurface imaging
- **Existing ground-based sensor networks** (seismic, hydrological, meteorological) and **satellite remote sensing** for continuous, multi-scale observation
- **Physical models** grounded in geomechanics, hydrology, and atmospheric science

These feed three research goals:

1. **Discovery of missing physics** — Identify the governing processes and couplings (e.g., soil memory effects, ocean–atmosphere teleconnections) that current hazard models neglect.
2. **Real-time hazard prediction** — Monitor and predict the susceptibility to landslides, floods, liquefaction, and severe storms as conditions evolve.
3. **Computational playgrounds for scenario exploration** — Build nowcasting and forecasting frameworks that couple AI-driven weather and climate models with geohazard models to interrogate future climate and hazard scenarios.

---

## Use Cases

We work on four coupled disasters, chosen because each one breaks a different part of the method and forces the infrastructure to catch up:

::::{grid} 2

:::{grid-item-card} 2025 Western Washington Floods & Landslides
:link: https://gaia-hazlab.github.io/seis-hydro-2-sed/
Atmospheric river–driven flooding and landslides across western Washington, linking precipitation extremes, soil saturation history, and sediment transport from mountain to sea.
:::

:::{grid-item-card} 2001–2031 Nisqually Earthquake
Investigating earthquake-induced ground failure (liquefaction, landslides) and how antecedent soil moisture and hydromechanical state modulate seismic hazard severity.
:::

:::{grid-item-card} 2025 Stehekin Post-fire Debris Flow
Post-wildfire debris flow hazard in the Stehekin watershed, where fire-altered soil properties interact with storm precipitation to trigger catastrophic mass movements.
:::

:::{grid-item-card} Convective Thunderstorms
Severe convective storms and their coupling to land surface conditions, exploring how soil moisture and surface energy fluxes feed back into storm initiation and intensity.
:::

::::

---

## Platform

We build the cloud-native infrastructure that carries a project from data ingestion through hazard evaluation:

- **[DataHub](datahub)** — Multimodal, cloud-native data management for geospatial hazard data spanning seismic, hydrological, meteorological, and remote sensing sources.
- **[ModelHub](modelhub)** — A registry of deep learning and physics-based models for weather forecasting, ground failure prediction, landslide susceptibility, flood hazard, and more.
- **[HazEvalHub](hazevalhub)** — Fair and standardized evaluation frameworks, leaderboards, and benchmarking protocols for hazard prediction models.
- **[Research Software](research-software)** — An ecosystem of open-source tools and agentic pipelines for reproducible, scalable scientific workflows.

---

## Earth System Science Nexus

Our subject is the **critical zone**: the thin layer from bedrock to canopy where rock, soil, water, air, and life interact. The hydromechanical state of the soil decides how water partitions — infiltrating to recharge groundwater, evaporating back to the atmosphere, or running off to drive erosion and flooding. That state carries a **memory** of past wetting, drying, and disturbance, and without tracking it you cannot say how severe the next event will be.

We work on two nexus domains:

- **[Soil Hydromechanical Memory](soil-memory)** — How antecedent soil conditions control the partitioning of water between infiltration, runoff, and evapotranspiration, and how this modulates geohazard susceptibility.
- **Ocean–Atmosphere Coupling** — How oceanic forcing (e.g., sea surface temperature anomalies, atmospheric rivers) shapes extreme precipitation patterns and cascading terrestrial hazards. *(Coming soon.)*
