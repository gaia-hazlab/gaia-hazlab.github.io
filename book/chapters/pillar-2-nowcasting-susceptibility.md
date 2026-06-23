# Pillar 2 — Nowcasting Hazard Susceptibility

:::{note}
**Draft / scaffold.** Pillar 2 of the [Digital Twin Framework](digital-twin-overview).
Section headings define the intended structure; content to be added from the three-pillar
write-up.
:::

## Scientific framing

Given the real-time soil state from [Pillar 1](pillar-1-soil-reanalysis) and current
forcing, the nowcast estimates the **likelihood and severity of each hazard now** — shallow
and deep landslides, debris flows, earthquake liquefaction / ground failure, and floods. It
turns state into actionable susceptibility.

## State variables & observables

- inputs: soil state ($S_w$, $d_{wt}$, effective stress), current precipitation/streamflow,
  recent seismicity, triggering conditions;
- outputs: per-hazard susceptibility / probability and severity index, with uncertainty.

## Data — what we ingest

*(Link to [DataHub](datahub): real-time sensor streams and the Pillar 1 reanalysis product.)*

## Models

*(Link to [ModelHub](modelhub): susceptibility mapping, triggering models, ground-failure
surrogates, detection from multi-sensor geophysical networks. Link each to the relevant
[Hazards](hazard-shallow-landslides) page.)*

## Evaluation & metrics

*(Link to [HazEvalHub](hazevalhub): event-based detection — POD, FAR, CSI; spatial agreement
— IoU/Dice; probabilistic calibration — Brier, reliability; alert lead time.)*

## Open questions & roadmap

- How to fuse heterogeneous, non-co-located sensors into a coherent nowcast?
- Cascading/compound hazards: nowcasting interactions, not just single hazards.

## References
