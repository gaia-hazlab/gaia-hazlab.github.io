# Pillar 3 — Forecasting Hazard Susceptibility

:::{note}
**Draft / scaffold.** Pillar 3 of the [Digital Twin Framework](digital-twin-overview).
Section headings define the intended structure; content to be added from the three-pillar
write-up.
:::

## Scientific framing

The forecast couples the [nowcast](pillar-2-nowcasting-susceptibility) with **weather
nowcast/forecast and climate scenarios** to project hazard susceptibility into the future —
from hours/days (operational warning) to seasonal and climate-scenario timescales
(scenario exploration). This is the "computational playground" of the
[problem statement](problem-statement).

## State variables & observables

- inputs: forecast forcing (precipitation, temperature, atmospheric rivers), evolving soil
  state, scenario parameters;
- outputs: time-evolving per-hazard susceptibility with forecast uncertainty and lead time.

## Data & forcing

*(Link to [DataHub](datahub) and weather/climate products: AR index, ACE2, Clima-X,
downscaling. See [Ocean–Atmosphere Coupling](ocean-atmosphere-coupling).)*

## Models

*(Link to [ModelHub](modelhub): coupled weather→hazard model chains, surrogates / reduced-
order models for fast scenario sweeps, downscaling.)*

## Evaluation & metrics

*(Link to [HazEvalHub](hazevalhub): skill vs. persistence/climatology baselines, ROC /
precision-recall at decision thresholds, cost-loss / value metrics, lead-time vs. skill.)*

## Open questions & roadmap

- Propagating uncertainty from weather forecast through hazard models.
- Climate-scenario design for actionable, decision-relevant projections.

## References
