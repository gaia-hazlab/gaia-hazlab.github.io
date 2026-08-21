# Liquefaction & Ground Failure

:::{note}
Hazard target of the [Digital Twin Framework](digital-twin-overview). Science framing is in
[Pillar 2 §3](pillar-2-nowcasting-susceptibility); the model itself is on the
[Liquefaction Model](modelhub-liquefaction) page; layer-by-layer data in the
[Data Inventory](datahub-inventory).
:::

## Scientific framing

Earthquake shaking can drive saturated, loose granular soils to lose strength and behave as a
fluid, producing settlement, lateral spreading, and surface ejecta. The trigger is seismic, but
susceptibility is set by the ground itself — how loose it is, how deep the water table sits, and
what the deposit is made of.

That split is what makes liquefaction a coupling problem for GAIA rather than a purely seismic
one. Shaking comes from the earthquake side; saturation comes from the same
[Pillar 1](pillar-1-soil-reanalysis) hydromechanical state the landslide models use. A wetter
season, a drought, or a rising sea level changes the hazard without changing the earthquake.

## State variables & observables

| | |
|---|---|
| **Demand** | PGA and magnitude from a ShakeMap or a hazard model |
| **Capacity** | soil density and typology, inferred from geospatial proxies or measured by CPT |
| **Gate** | water-table depth — only saturated soil liquefies |
| **Output** | manifestation severity (LPI, LPI$_{ISH}$, LSN) and the probability of ground failure |

Water-table depth is the dominant control and the one that varies in time.

## Data — what we ingest

Cone penetration tests are the backbone: ~37,000 of them, compiled globally, are what the GAIA
model is trained against and what anchors its predictions where they exist
[@sanger2024cptna; @rasanen2024cpt]. Around them sit geospatial proxies for soil thickness,
saturation, and typology — terrain and hydrologic derivatives, modeled groundwater, $V_{s30}$,
surface geology — plus ground motion from USGS ShakeMaps. Sources, resolutions, and caveats are
in the [Data Inventory](datahub-inventory).

## Models

GAIA uses the mechanics-informed geospatial surrogate of [@sanger2025jgge], which predicts what a
CPT-based geotechnical analysis would say at locations with no CPT, and updates those predictions
with subsurface data where it exists. Full treatment on the
[Liquefaction Model](modelhub-liquefaction) page.

## Evaluation & metrics

Scored against observed liquefaction from past earthquakes using Brier score and calibration
curves; the 2001 Nisqually record [@rasanen2023] is the regional target. Definitions in
[HazEvalHub](hazevalhub).

## Connection to use cases

Central to the [2001–2031 Nisqually earthquake](wa-2001-2031-nisqually-earthquake) use case, and
to Cascadia scenario planning.

## Open questions & roadmap

- Make the **water table a live model input** rather than a static training value — the step that
  turns a static hazard map into a twin that responds to season, drought, and sea-level rise.

## References
