---
title: Ocean–Atmosphere Coupling
short_title: Ocean–Atmosphere
description: How oceanic forcing — SST anomalies, the MJO, and atmospheric rivers — shapes extreme precipitation and the cascading terrestrial hazards it triggers.
---

:::{note}
**In development.** Earth System Science page supplying forcing to
[Pillar 3 — Forecasting](pillar-3-forecasting-susceptibility). Sections marked with
*(outline)* are scaffolds awaiting content.
:::

**Lead: Shuyi Chen** (UW Atmospheric Sciences), whose work on the connection between the
Madden–Julian Oscillation and atmospheric rivers anchors this thread.

## Why this sits in a geohazards project

The most damaging events in our [use cases](problem-statement) do not begin in the ground.
An atmospheric river makes landfall, days of rain saturate a hillslope whose strength was
already set by its wetting history, and the failure that follows is recorded as a landslide
or a flood. Treating the atmospheric forcing as an external boundary condition — something
handed to us by a weather product — throws away most of the predictability.

The claim this page tests is narrower and more useful: **if the ocean sets up the
atmospheric river days to weeks in advance, then the lead time on a geohazard forecast is
not limited by the hillslope.** It is limited by how far upstream in the coupled system we
are willing to look.

## The MJO → atmospheric river link *(lead thread)*

The Madden–Julian Oscillation is the dominant mode of intraseasonal tropical variability,
and its eastward-propagating convective envelope modulates where and when atmospheric rivers
form and make landfall on the west coast of North America. That modulation operates on the
two-to-six-week horizon — the gap between weather forecasting and seasonal prediction, and
precisely the horizon on which emergency managers can still act.

*(outline — to be developed with Shuyi Chen: MJO phase compositing against AR landfall
frequency and intensity; which phases favour Pacific Northwest versus California landfall;
how far the skill extends; what the coupled ocean state contributes beyond the atmospheric
signal alone.)*

## Atmospheric rivers and extreme precipitation *(outline)*

AR dynamics, detection and tracking; integrated vapour transport as the working variable;
landfall geometry against terrain. Links to the weather products catalogued in
[ModelHub](modelhub) — AR index, ACE2, Clima-X.

## Teleconnections and climate modes *(outline)*

SST anomalies, ENSO and other modes; what each contributes to seasonal predictability of
extreme precipitation, and where those signals are and are not separable from the MJO.

## Handoff to the hazard pillars

This page produces one thing the rest of the project consumes: **precipitation forcing with
an honest uncertainty and a stated lead time.** Pillar 1 uses it to drive soil-moisture
reanalysis; Pillar 3 uses it to extend the forecast horizon beyond what hillslope state
alone supports. The interface, not the meteorology, is what has to be specified first.

*(outline — the forcing contract: variables, resolution, ensemble treatment, and how lead
time is reported alongside skill.)*

## Data and models *(outline)*

See [DataHub](datahub) for the observational and reanalysis holdings, and
[ModelHub](modelhub) for the AI weather models under evaluation.

## Evaluation *(outline)*

Skill against persistence and climatology at each lead time, following the metric families
in [HazEvalHub](hazevalhub). A forecast that beats climatology at two weeks is worth more to
this project than one that beats it at two days.

## Open questions

- How much of the AR landfall signal is recoverable from the MJO phase alone, and how much
  requires the coupled ocean state?
- Do AI weather models inherit MJO skill, or do they degrade at exactly the intraseasonal
  range where this thread is useful?
- What is the shortest defensible lead time at which a coupled ocean–atmosphere signal
  changes a hillslope forecast?

## References

*(to be added)*
