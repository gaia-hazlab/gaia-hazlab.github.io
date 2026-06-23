# Post-Fire Debris Flows

:::{note}
**Draft / scaffold.** Hazard target of the [Digital Twin Framework](digital-twin-overview).
A **special, wildfire-conditioned case of landslides** — distinct from the rainfall- and
groundwater-driven [shallow and deep-seated landslides](hazard-landslides), which do **not**
take burn severity as an input.
:::

## Scientific framing

Post-fire debris flows are fast, destructive mixtures of water and sediment initiated on
**recently burned** steep terrain when short-duration, high-intensity rainfall mobilizes loose
material. Wildfire is the conditioning factor: it removes protective vegetation, induces soil
**water repellency (hydrophobicity)**, and lowers root cohesion, so that storms far smaller
than ordinary landslide-triggering events can generate a flow. This makes them a **special
case of landsliding** in which **burn severity** (e.g. dNBR) and fire-altered soil properties
are first-order inputs — the feature that separates this hazard from the core GAIA
shallow/deep landslide susceptibility, which is rainfall- and groundwater-driven and carries
no fire term.

## State variables & observables

*(Burn severity / dNBR, soil water repellency, short-duration rainfall intensity thresholds,
sediment supply; seismic/infrasound detection, post-event DEM/lidar differencing for
run-out and volume.)*

## Data — what we ingest

*(Link to [DataHub](datahub): burn severity (MTBS/BAER), high-resolution rainfall, terrain,
and the soil layers of [Pillar 1](pillar-1-soil-reanalysis). This is the one landslide hazard
whose data stack requires a wildfire layer.)*

## Models

*(Link to [ModelHub](modelhub): the Landlab `LandslideProbability` workflow run with
fire-reduced cohesion and burn severity (see
[Pillar 2 §2.5](pillar-2-nowcasting-susceptibility)), rainfall intensity–duration thresholds,
run-out modeling, and multi-sensor detection.)*

## Evaluation & metrics

*(Link to [HazEvalHub](hazevalhub): triggering detection, run-out extent agreement, warning
lead time.)*

## Connection to use cases

The driving use case is the [2025 Stehekin post-fire debris flow](wa-2025-stehekin); the
modeling pipeline lives in
[`gaia-hazlab/landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow).

## Open questions & roadmap

## References
