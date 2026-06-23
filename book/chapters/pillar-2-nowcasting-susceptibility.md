# Pillar 2 — Nowcasting Hazard Susceptibility

:::{note}
**Actively developed (landslide track).** Pillar 2 of the
[Digital Twin Framework](digital-twin-overview). It consumes the real-time state from
[Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) and turns it into hazard
likelihood *now*. The **landslide** track below is the most mature; the **liquefaction**
track (§3) is scoped but scheduled for a later pass. References have Crossref/arXiv-verified
DOIs.
:::

## 1. From state to susceptibility

Given the soil state from Pillar 1 (saturation $S_w$, water-table depth $d_{wt}$, effective
stress, strength) and current forcing, the nowcast estimates the **likelihood and severity**
of each hazard at the present time. "Susceptibility" here is a *probability of failure*, not a
binary map — the quantity that downstream warning and the [forecast](pillar-3-forecasting-susceptibility)
build on. Two hazard tracks are in scope:

- **(a) Landslides** — advanced; modeled with [Landlab](modelhub) (§2).
- **(b) Liquefaction & ground failure** — scoped, next pass (§3).

## 2. Landslides

### 2.1 Three types, three physics

Following the Varnes classification update [@hungr2014], we treat three distinct failure
processes that share data but **not** governing physics — each will become its own subpage:

| Type | Failure surface | Dominant control | Burn severity input? | Hazard page |
|---|---|---|---|---|
| **Shallow landslides** | ~0.5–3 m (soil mantle) | storm infiltration → pore pressure → loss of suction | **No** | [landslides](hazard-landslides) |
| **Deep-seated landslides** | meters–tens of m | groundwater / hydraulic head on seasonal–multiyear scales | **No** | [landslides](hazard-landslides) |
| **Post-fire debris flows** | mobilized channel/colluvium | high-intensity rainfall on **recently burned**, fire-altered terrain | **Yes** | [post-fire debris flows](hazard-postfire-debris-flows) |

The core GAIA digital-twin landslide products — **shallow** and **deep-seated** susceptibility —
are rainfall- and groundwater-driven and **do not take burn severity as an input**. Post-fire
debris flows are a **special, wildfire-conditioned case** of landsliding: only that track adds
a burn-severity layer and fire-reduced cohesion. The current modeling effort targets
**shallow-landslide probability**; the same Landlab framework extends to the others by swapping
the hydrology and stability closures (and, for post-fire debris flows, adding the fire terms).

### 2.2 Modeling with Landlab

[**Landlab**](https://landlab.csdms.io) is an open-source Python toolkit for building
two-dimensional numerical models of Earth-surface processes [@hobley2017; @barnhart2020]. Its
defining feature — **the one that matters most for us** — is **component-based model coupling
on a shared grid**: a library of interoperable *components* (flow routing, snowpack,
ecohydrology, slope stability) that each read and write named fields (`topographic__elevation`,
`soil__saturated_hydraulic_conductivity`, …) on one common raster grid. This lets us **chain a
full hillslope hydrology-to-stability pipeline** instead of stitching together disconnected
models — the intermediate fields (e.g. soil moisture) are explicit, inspectable, and
*validatable* (§2.6).

The landslide engine is Landlab's **`LandslideProbability` component** [@strauch2018], a
probabilistic infinite-slope model driven by a topographically-controlled wetness index.

### 2.3 The physics (the equations we solve)

**Infinite-slope factor of safety.** On a planar failure surface at slope angle $\theta$, the
factor of safety is the ratio of resisting to driving stress. In the dimensionless form used
by the Landlab component [@strauch2018]:

$$
FS = \frac{\tilde C}{\sin\theta\cos\theta}
   + \left(1 - w\,\frac{\rho_w}{\rho_s}\right)\frac{\tan\phi}{\tan\theta},
$$

where $\tilde C = (C_r + C_s)/(\rho_s g D)$ is the combined root + soil cohesion normalized by
the saturated soil weight, $D$ is soil depth, $\phi$ the internal friction angle, $\rho_s,
\rho_w$ soil and water densities, and $w\in[0,1]$ is the **relative wetness** (saturated
fraction of the soil column). Failure is expected when $FS<1$.

**Relative wetness (the topographic control).** Following steady-state shallow subsurface flow
[@beven1979; @montgomery1994], wetness rises with recharge and contributing area and falls with
transmissivity and slope:

$$
w = \min\!\left(\frac{R}{T}\,\frac{a}{b}\,\frac{1}{\sin\theta},\; 1\right),
$$

with recharge $R$, soil transmissivity $T$, specific contributing area $a/b$ (upslope area per
unit contour width, from flow routing), and slope $\theta$. This is the SHALSTAB/SINMAP family
of models [@montgomery1994; @pack1998]; the unsaturated extension via suction stress is given
by [@lu2008; @iverson2000].

**From factor of safety to probability.** The inputs $R$, $T$, $\tilde C$, $\phi$ are uncertain.
The component draws them from distributions and runs a **Monte Carlo** ensemble, yielding a
distribution of $FS$. The nowcast susceptibility is the **probability of failure**

$$
P_f = \Pr(FS < 1),
$$

i.e. the fraction of the ensemble that fails — a continuous 0–1 field, not a yes/no map.

### 2.4 Data clarity: raw vs. static vs. dynamic vs. derived vs. label

The most common source of confusion in this pipeline is conflating *what is measured*, *what
is computed*, *what is predicted*, and *what is used to check the prediction*. They are
different objects with different uncertainty and different roles:

```
RAW INPUTS ──► DERIVED / INTERMEDIATE FIELDS ──► PREDICTION ──► checked against ──► LABELS
(measured)     (computed by the model)            (P_f)                             (independent truth)
```

- **Raw inputs** are measured/observed and ingested via [DataHub](datahub) (Pillar 1).
- **Static** inputs do not change over a run; **dynamic** inputs are time-varying forcing.
- **Derived / intermediate fields** are *computed by the model* — they are **not** data, even
  though some (soil moisture, SWE) can be *independently validated* (your colleagues' term:
  **calibration**).
- **Predictions** are model outputs (the probability of failure).
- **Labels** are *independent* observations of actual landslides, used only to score the
  prediction — never as model inputs.

| Field | Category | Source / how obtained | Confidence | Limitation & influence on susceptibility |
|---|---|---|---|---|
| `topographic__elevation` (DEM) | **raw, static** | USGS 10 m 3DEP | High | Smooths <10 m gullies; sets slope $\theta$ and contributing area $a/b$ — **dominant geometric control** |
| Soil texture, depth, $K_{sat}$, cohesion, $\phi$ | **raw, static** | SOLUS100 / POLARIS (see Pillar 1) | Medium–low | Static, smoothed at 30–100 m; sets $\tilde C$, $T$, $D$ — **strong, and the most uncertain priors** |
| Burn severity (dNBR) | **raw, static** (per event) — *post-fire debris flows only* | MTBS/BAER | Medium | **Not used for shallow/deep landslide susceptibility.** For the post-fire case only: lowers cohesion / raises runoff |
| Land cover / vegetation | **raw, static** | NLCD | Medium | Sets root cohesion $C_r$ and ET; moderate influence |
| Precipitation, $T_{min}$/$T_{max}$ | **raw, dynamic** | PRISM (staged by gaia-cli) | Medium | 800 m–4 km; the proximate **trigger** — drives recharge $R$ |
| Contributing area $a/b$ | **derived, static** | flow routing on the DEM | High (given DEM) | Inherits DEM error; controls $w$ |
| SWE, snowmelt | **derived, dynamic** | snow component (rain/snow partition) | Medium | Mispartition shifts the timing of $R$ in snow-affected terrain |
| PET, **soil moisture** | **derived, dynamic** | ecohydrology component | Medium | **Calibratable** against in-situ/Pillar-1 ground truth — the key intermediate check |
| Recharge $R$, transmissivity $T$ | **derived, dynamic** | routed recharge | Low–medium | Direct inputs to $w$; large parameter uncertainty → propagated by Monte Carlo |
| Relative wetness $w$ | **derived, dynamic** | wetness index (§2.3) | — | The hydrologic state variable entering $FS$ |
| **Probability of failure $P_f$** | **PREDICTION** | `LandslideProbability` | — | The nowcast product |
| Landslide masks / inventories | **LABEL** | Sentinel SAR/InSAR & optical [@mondini2021; @handwerger2022]; post-event DEM/lidar differencing [@bernard2021] | Varies | Used only to **score** $P_f$ (§2.6) — not a model input |

### 2.5 The prediction pipeline

Landslide probability is produced by
[`gaia-hazlab/landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) (the
"MMP" multi-model-probability workflow), which chains the Landlab components exactly along the
taxonomy above:

```
terrain (DEM, flow accumulation)
   → static_inputs (soil, vegetation, transmissivity, cohesion
                    [+ burn severity — post-fire debris flows only])
   → daily_forcing (PRISM ppt, tmin, tmax)
   → snow (rain/snow partition, SWE, melt)
   → ecohydrology (PET, soil moisture)
   → landslides (routed recharge → LandslideProbability → P_f)
   → exports (GeoTIFF / ASC)
```

As currently configured for the Stehekin/Pioneer events, this is the **post-fire debris-flow**
workflow — hence the burn-severity layer and fire-reduced cohesion. The core **shallow** and
**deep-seated** landslide susceptibility runs the *same* stability engine and hydrology
**without** the burn-severity input. It **consumes the data prepared in Pillar 1**
([`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml) and the SOLUS/PRISM
staging). Today it still reads hardcoded local paths for those inputs; aligning it with the
[DataHub Integration Guide](datahub-integration-guide) is the integration task that connects
Pillars 1 and 2.

### 2.6 Calibration and validation

Two distinct checks, often conflated:

- **Calibration** — verify the *intermediate fields* against observations: soil moisture and
  SWE against in-situ sensors and the Pillar-1 ground-truth networks. This tunes the hydrology
  before any landslide claim is made.
- **Validation** — score the *prediction* $P_f$ against **independent landslide labels**:
  Sentinel-1 InSAR / SAR detections [@mondini2021; @handwerger2022] and, for the post-wildfire
  niche, **post-event DEM/lidar differencing** masks [@bernard2021]. These labels never enter
  the model.

Metrics (ROC/precision-recall and Brier score for $P_f$, spatial IoU for mapped failures,
alert lead time) are defined in [HazEvalHub](hazevalhub).

### 2.7 Repository naming (suggestions)

The current names obscure what the repos do and should be clarified (tracked in the
[DataHub Integration Guide](datahub-integration-guide)):

- [`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) actually computes
  **shallow-landslide probability** (its internal package is `debris_landlab`), not only debris
  flows → suggest **`gaia-model-landslide`** (the susceptibility *model*).
- [`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml) is **data
  preparation** → suggest **`gaia-dataprep-landslide`**.
- This makes the **data-prep (Pillar 1) → model (Pillar 2)** split explicit in the repo names.

## 3. Liquefaction & ground failure *(next pass)*

:::{note}
**Scoped, scheduled for a later pass this week.** Led by the Sanger/Maurer line of work.
:::

We will model earthquake-triggered liquefaction and ground failure
([hazard page](hazard-liquefaction-ground-failure)) building on geospatial surrogate models
for liquefaction hazard and impact [@sanger2025jgge; @sanger2026geoai; @sanger2026geocongress]
and parametric $V_s$ profiles [@sanger2025vs]. Two concrete next steps:

1. **Unconditional liquefaction susceptibility** — the geospatial baseline independent of a
   specific earthquake.
2. **Couple groundwater-level modeling** (see [Groundwater & Soil Moisture](groundwater-soil-moisture))
   to assess how **long-term sea-level rise and seasonal water-table variations** modulate
   liquefaction — a direct consumer of the Pillar-1 water-table product.

This will require adding the corresponding geotechnical and groundwater layers to the
[DataHub](datahub) inventory and a liquefaction modeling component in [ModelHub](modelhub).

## 4. Evaluation & metrics

See [HazEvalHub](hazevalhub): event-based detection (POD, FAR, CSI), spatial agreement
(IoU/Dice), probabilistic calibration (Brier, reliability diagrams) for $P_f$, and alert lead
time.

## 5. Open questions & roadmap

- Split the landslide hazard pages into the three process-specific subpages (§2.1).
- Quantify how prior uncertainty in static soil layers propagates to $P_f$ (sensitivity study).
- Close the Pillar 1 → Pillar 2 data loop by migrating `landlab-debrisflow` onto DataHub.
- Stand up the liquefaction track (§3).

## References
