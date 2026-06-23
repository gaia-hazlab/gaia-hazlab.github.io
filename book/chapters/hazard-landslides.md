# Landslides

:::{note}
**Draft / scaffold.** Hazard target of the [Digital Twin Framework](digital-twin-overview).
This page covers the two **rainfall- and groundwater-driven** landslide types — **shallow**
and **deep-seated** — which share Landlab machinery and differ mainly in depth, triggering, and
hydrology. The wildfire-conditioned [post-fire debris flow](hazard-postfire-debris-flows) is a
special case on its own page. Modeling detail is in
[Pillar 2 — Nowcasting Hazard Susceptibility](pillar-2-nowcasting-susceptibility).
:::

Landsliding spans a continuum of failure depths and timescales [@hungr2014]. The GAIA digital
twin predicts a **probability of failure** $P_f$ for two end-members that bracket the core
hazard; neither takes burn severity as an input.

## 1. Process & triggering mechanisms

| | **Shallow landslides** | **Deep-seated landslides** |
|---|---|---|
| Trigger | Storm **infiltration** raising transient pore pressure | **Groundwater recharge** raising the water table / hydraulic head |
| Mechanism | Loss of suction and effective stress in the soil mantle [@iverson2000; @lu2008] | Sustained elevated head reduces effective stress on a deep surface |
| Timescale | Hours–days (event-driven) | Seasonal–multiyear (memory-rich) |
| Key state variable | Vadose-zone saturation $S_w$ | Water-table depth $d_{wt}$ / head $h$ |
| Antecedent control | Soil-moisture history [@guzzetti2008] | Long-memory groundwater ([soil-memory](soil-memory)) |

Both inherit their state from [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis):
shallow failures respond to the **saturation** field, deep failures to the **water-table**
field.

## 2. Characteristics

| | **Shallow** | **Deep-seated** |
|---|---|---|
| Failure depth | ~0.5–3 m (soil mantle) | meters–tens of meters |
| Failure surface | soil–bedrock interface | deep rupture in rock/regolith |
| Typical motion | rapid, often mobilizing to flows | slow creep, episodic acceleration |
| Observables | rainfall I–D thresholds, soil moisture, seismic/geotech | surface displacement (InSAR/GNSS), piezometric head, seismicity |
| Validation label | rainfall-triggered inventories; optical/SAR detection | displacement time series (InSAR/GNSS) |

## 3. Implementation in Landlab

Both use the **same** Landlab engine — the infinite-slope factor of safety solved
probabilistically by the `LandslideProbability` component (Monte Carlo over uncertain
parameters → $P_f = \Pr(FS<1)$; full equations in
[Pillar 2 §2.3](pillar-2-nowcasting-susceptibility)) [@strauch2018]. They differ in the
**hydrology closure** that sets the relative wetness entering the factor of safety:

| | **Shallow** | **Deep-seated** |
|---|---|---|
| Wetness driver | steady-state topographic wetness from recharge & transmissivity [@beven1979; @montgomery1994] | water-table / hydraulic-head field from the soil reanalysis |
| Soil column depth $D$ | thin (soil mantle) | thick (to the deep surface) |
| Dominant uncertain parameters | recharge $R$, transmissivity $T$, root + soil cohesion | head $h$, deep strength, transmissivity at depth |
| Burn severity input | **No** | **No** |
| Validation labels | optical/SAR landslide masks [@mondini2021; @handwerger2022] | InSAR/GNSS displacement [@mondini2021] |

This shared-engine design is exactly why the two live on one page: the difference is a swapped
hydrology closure and parameter set, not a different model.

## Data — what we ingest

The full, traceable catalog — every raw product, every deterministically derived layer, and
every model output, with sources/APIs, access sensitivity, spatial/temporal resolution, and
limitations — lives in the **[Landslide Data Inventory](datahub-landslide-inventory)** under the
[DataHub](datahub). In brief, the core (non-post-fire) model ingests:

- **Terrain** — a DEM (USGS 3DEP / OpenTopography) → `topographic__elevation`, `slope`,
  contributing area.
- **Static soil properties** — SOLUS100 (100 m) or POLARIS (30 m) → thickness, density,
  friction angle, cohesion bounds, $K_{sat}$/transmissivity, porosity, field capacity, wilting
  point.
- **Vegetation** — NLCD landcover → `vegetation__plant_functional_type` (LAI, root cohesion).
- **Forcing** — observed PRISM precipitation/temperature (hindcast/daily) and Earth2Studio
  AI-weather precipitation (forecast).
- **Reanalysis state** — the saturation (shallow) and water-table (deep) fields from
  [Pillar 1](pillar-1-soil-reanalysis).
- **Calibration targets** — SMAP soil moisture, ERA5 SWE, and mapped landslide inventories.

No **burn severity** — that layer is specific to
[post-fire debris flows](hazard-postfire-debris-flows). See the
[inventory](datahub-landslide-inventory) for sources, sensitivity, resolution, and the models
behind each derived product.

## Models

The full model documentation — physics equations, the data→Landlab pipeline, what is solved vs
assumed, watershed/single-drainage constraints, Landlab limits for digital twins, Earth2Studio
interoperability, and evaluation — is on the
**[Landslide Model — Landlab Implementation](modelhub-landslide)** page in the
[ModelHub](modelhub). The implementation lives in
[`gaia-hazlab/landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow); see also
[Pillar 2 §2.5](pillar-2-nowcasting-susceptibility).

(landslide-detection)=
## Detection & monitoring

Susceptibility is the *forecast* side; GAIA also **detects landslides as they happen**. Rapid
mass movements — debris flows, rockfalls, icefalls, lahars — radiate seismic and infrasound
energy, so a continuously running detector can catalog events in near-real time, independent of
the revisit gaps that limit optical/SAR mapping.

In the Mt. Rainier region this is done with **QuakeXNet**, a deep-learning detector run on
continuous waveforms from seismic stations within ~50 km of the volcano: per-station detections
are aggregated to network-level events, located with **ENVELOC**, and validated against the PNSN
and ESEC catalogs — yielding a 15-year (2010–2025) catalog of ≈128,500 located events
(≈115,000 surface events plus explosions) [@kharita2025quakexnet]. The trained model is
distributed through the SeisBench ecosystem; multi-sensor extensions (infrasound, tilt, DAS) and
other PNW sites are in progress (see [ModelHub](modelhub)). The catalog is currently **under
review, with ongoing refinement of the event-classification model**, so event counts and class
labels will continue to evolve.

These detections close the loop with the model in two ways: they provide **validation labels**
for the modeled probability of failure $P_f$ — event presence, time, and location (see
[model §8](modelhub-landslide) and [HazEvalHub](hazevalhub)) — and they are a **real-time
monitoring** stream alongside the nowcast.

Explore the located catalog on the interactive map (full project:
[pnw_seismic_event_detection](https://akashkharita.github.io/pnw_seismic_event_detection/)):

:::{iframe} https://akashkharita.github.io/pnw_seismic_event_detection/data/enveloc_dashboard.html
:width: 100%
QuakeXNet · Mt. Rainier ENVELOC-located surface-event catalog — Akash Kharita (dashboard
currently renders the ENVELOC-located subset; the full catalog spans 2010–2025)
:::

## Evaluation & metrics

*(Link to [HazEvalHub](hazevalhub): probabilistic calibration (Brier, reliability) of $P_f$,
spatial agreement (IoU) against detection masks and the seismic [detection](#landslide-detection)
catalog, and — for deep-seated — displacement-rate skill and early-warning lead time.)*

## Connection to use cases

Shallow failures feature in the
[2025 Western Washington floods & landslides](wa-2025-river-floods-sediment-transport).

## Open questions & roadmap

- Quantify how prior uncertainty in static soil layers propagates to $P_f$ for each type.
- A unified hydrology closure spanning the shallow (vadose) and deep (water-table) regimes.

## References
