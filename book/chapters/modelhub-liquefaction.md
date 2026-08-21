# Liquefaction Model — Mechanics-Informed Geospatial Surrogate

:::{note}
**The model-side companion to the liquefaction digital twin.** ModelHub home for the geospatial
liquefaction model (GLM) of Sanger, Geyin & Maurer [@sanger2025jgge], with a Pacific Northwest
demonstration in [@sanger2026geoai].

Science framing in [Pillar 2 §3](pillar-2-nowcasting-susceptibility); inputs and outputs in the
[Data Inventory](datahub-inventory).
:::

## 1. The idea

Practice-standard liquefaction assessments need in-situ measurements. Geospatial models don't, but they buy
that coverage by regressing liquefaction *observations* on proxy variables — and there are only a
handful of well-mapped earthquakes per decade to learn from.

This model changes the target. Instead of learning "did the ground liquefy here," it learns
**what a CPT-based triggering analysis would have said here**. Training targets come from running
the Idriss & Boulanger procedure [@idrissboulanger2008] on ~37,000 cone penetration tests across
48 U.S. states and 19 countries; geospatial variables sampled at those same sites are the
features. The mechanics live in the target, so the model inherits them rather than having to
relearn them from sparse case histories — and the training set is orders of magnitude larger than
any liquefaction inventory, because a CPT site doesn't need to have experienced an earthquake to
be useful. The approach builds on [@geyin2022]; the critique motivating it is [@maurersanger2023].

## 2. What it produces

The published product is a set of precomputed ~90 m rasters of two
parameters, $A$ and $B$, that describe a site's liquefaction response across *all* levels of
shaking:

$$
MI(PGA_M) =
\begin{cases}
0, & PGA_M < 0.1\,g \\[6pt]
A\,\tan^{-1}\!\left[\,B\left(PGA_M - \dfrac{A/100}{B}\right)^{2}\right], & PGA_M \ge 0.1\,g
\end{cases}
$$

where $MI$ is a manifestation index — $LPI$ [@iwasaki1978], $LPI_{ISH}$ [@maurer2015], or $LSN$
[@vanballegooy2014] — and $PGA_M$ is magnitude-scaled PGA. Roughly, $A$ sets how severe the
response gets and $B$ sets how quickly it gets there.

Because $A$ and $B$ are **event-independent**, the expensive work is already done: ~1.3 billion
locations, >1 TB of geospatial input, HPC on DesignSafe and UW Hyak. At run time a user supplies
a ShakeMap and evaluates the equation above — arithmetic, no ML inference, no HPC. Manifestation
indices then convert to a probability of ground failure through fragility functions
[@geyin2020fragility], kept separate so they can be swapped as they are revised.

Two model domains ship: **global** (37 predictors) and **New Zealand** (43), each with $A$/$B$
for all three indices. Coverage is continuous except where predictions were deliberately
suppressed — slopes above 5°, water, ice, permafrost. Full package sizes are 33 GB global and
85 MB for New Zealand; one index over one continent is ~1.5 GB.

## 3. Updating with subsurface data

Where the subsurface has actually been measured, the model should defer to it. $A$ and $B$ are
updated by regression kriging [@hengl2007]: the ML prediction supplies the regression term, and
the interpolated ML *residual* — known exactly at CPT sites, decaying to zero within ~1.2 km —
supplies the correction. Predictions are scaled up or down toward what the geotechnical data
says.

Each product ships with a **variance classification map** grading how much of the local
prediction variance the ML model still owns, from *no geotechnical influence* to *major*. A user
can see, per pixel, whether they are looking at a geotechnical answer or a geospatial one.
Anyone holding proprietary or municipal CPT data can re-krige against the published rasters
without retraining.

## 4. How well it works

Skill is scored by Brier score against the operational benchmark, Rashidian & Baise
[@rashidian2020], with significance from bootstrap confidence intervals, KS tests, and Cohen's
$d$.

| Test | RB20 | Best ML |
|---|---|---|
| **Unseen events** — 2019 Ridgecrest, 2019 Puerto Rico, 2023 Türkiye; no CPTs in training there | 0.393 | **0.128** |
| **332 global case histories** [@rateria2024], before → after updating | 0.299 | 0.228 → **0.209** |
| **Canterbury**, 16,836 observations [@geyin2021canterbury] | 0.204 | **0.127** |

Two results worth stating plainly. **Updating helps** — measurably, and exactly where subsurface
data exists. And **regionalization mostly didn't**: New Zealand has abundant CPTs and
high-quality national geology, groundwater, and $V_{s30}$ layers, and its bespoke model still
only matched the global one. If a region-specific model can't clearly win there, the case for
building them elsewhere is weak.

## 5. Where GAIA takes it

**Groundwater depth is the model's single most influential predictor — and it is currently
frozen at its training value.** Making it a run-time variable, supplied alongside shaking the way
$PGA_M$ already is, is the main line of future work [@sanger2025jgge] and the direct interface to
the rest of GAIA: the water table from [Pillar 1](pillar-1-soil-reanalysis) and the
[groundwater modeling](groundwater-soil-moisture), and with it the route by which seasonal
change, drought, and sea-level rise modulate liquefaction hazard. It requires retraining with
groundwater held out, not a new input slot.

Then, the model can be used in a probabilistic hazard framework, where shaking is a random variable
and the water table is a random variable, and the output is a probability distribution of
manifestation severity and ground failure. That is the liquefaction digital twin, and it is
what the [2001–2031 Nisqually earthquake](wa-2001-2031-nisqually-earthquake) use case is built to demonstrate.

## 6. Products & repositories

Published on DesignSafe: global model maps [@sanger2024global], New Zealand model maps
[@sanger2024nz], and an example implementation — a Jupyter notebook and Matlab script that take a
USGS ShakeMap URL and return geotiffs of the selected index and the probability of ground failure
[@sanger2024scripts]. Supporting CPT databases: North America [@sanger2024cptna] and Cascadia
[@rasanen2024cpt].

Repositories: [`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) ·


## Related

- [Pillar 2 — Nowcasting Hazard Susceptibility](pillar-2-nowcasting-susceptibility) — science
  framing · [Liquefaction & Ground Failure](hazard-liquefaction-ground-failure) — hazard page.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) ·
  [Groundwater & Soil Moisture](groundwater-soil-moisture) — the water table this model would
  consume once §6 is built.
- [Data Inventory](datahub-inventory) · [Landslide Model](modelhub-landslide) ·
  [HazEvalHub](hazevalhub).

## References
