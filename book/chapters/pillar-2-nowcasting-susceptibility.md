# Pillar 2 — Nowcasting Hazard Susceptibility

:::{note}
**Actively developed (landslide track).** Pillar 2 of the
[Digital Twin Framework](digital-twin-overview). It draws on the real-time state from
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

- **(a) Landslides** — advanced; modeled with Landlab — full equations, pipeline, and limits on
  the [Landslide Model](modelhub-landslide) page (§2).
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

Several of these layers (DEM, soil saturation, water table, precipitation) are **shared with
other hazards**. The consolidated, icon-tagged cross-hazard inventory — marking which layer
serves landslides, post-fire debris flows, liquefaction, or floods — is in §3.6.

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
**without** the burn-severity input. It **uses the data prepared in Pillar 1**
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

## 3. Liquefaction & ground failure

:::{note}
**In development (liquefaction track), led by the Sanger/Maurer line of work.** Repository
pointers in §3.8 are **placeholders** for the team (Morgan) to confirm.
:::

Earthquake shaking can turn saturated, loose granular soils into a fluid-like state —
liquefaction — driving settlement, lateral spreading, and ground failure
([hazard page](hazard-liquefaction-ground-failure)). Unlike landslides, the trigger is
**seismic**, not meteorological; but the *susceptibility* is set by the same Pillar-1 state —
saturation and water-table depth — coupled to the soil's stiffness. GAIA builds a **ground
liquefaction model (GLM) digital twin** on the geospatial-modeling line of [@zhu2015; @zhu2017]
as advanced by Sanger, Geyin & Maurer
[@sanger2025jgge; @sanger2026geoai; @sanger2026geocongress; @sanger2025vs].

### 3.1 The geospatial liquefaction model (GLM)

Classical liquefaction assessment is site-specific (borehole CPT/SPT). **Geospatial** models
trade per-site geotechnical data for spatially continuous proxies — predicting the probability
and areal extent of liquefaction from PGV/PGA, $V_{s30}$, modeled water-table depth,
precipitation, and distance to water [@zhu2017; @rashidian2020], with manifestation severity
captured by fragility functions [@geyin2020fragility; @geyin2020field]. GAIA's GLM uses the
mechanics-informed ML surrogates of [@sanger2025jgge], which emulate physics-based triggering
at national scale and in near-real time, demonstrated for the PNW in [@sanger2026geoai].

### 3.2 Fundamental equations — where hydrology and rigidity enter

The simplified procedure [@seedidriss1971; @idrissboulanger2006] compares seismic **demand**
to soil **capacity**. Demand is the cyclic stress ratio,

$$ \mathrm{CSR} = 0.65\,\frac{a_{max}}{g}\,\frac{\sigma_{v0}}{\sigma'_{v0}}\,r_d, $$

capacity is the cyclic resistance ratio $\mathrm{CRR}$, and triggering is expected when

$$ \mathrm{FS}_{liq} = \frac{\mathrm{CRR}}{\mathrm{CSR}} \le 1. $$

Surface severity is summarized by manifestation indices — LPI [@iwasaki1978] and LSN
[@vanballegooy2014]. Two **Pillar-1 state variables** enter the physics directly:

- **Hydrology (water table).** Pore pressure sets the effective stress
  $\sigma'_{v0}=\sigma_{v0}-u$, which appears in *both* demand (the $\sigma_{v0}/\sigma'_{v0}$
  ratio in CSR) and capacity (overburden correction of $V_{s1}$). Only **saturated** soil below
  the water table can liquefy — saturation is a binary gate. A shallower water table raises
  demand and exposes more liquefiable column. This is the direct consumer of the Pillar-1
  **water-table product** and the [groundwater modeling](groundwater-soil-moisture).
- **Rigidity (shear-wave velocity).** $V_s$ is the small-strain stiffness proxy
  ($G_{max}=\rho V_s^2$). It enters **capacity** — CRR rises with overburden-corrected $V_{s1}$
  [@andrusstokoe2000] — *and* **demand**, because $V_{s30}$ controls site amplification of
  $a_{max}$. Stiffer ground resists triggering, but soft sites amplify shaking. GAIA's $V_s$
  comes from the parametric CONUS profiles of [@sanger2025vs] and, dynamically, from the
  seismic monitoring of [soil-memory](soil-memory).

### 3.3 Three hazard framings: conditional, unconditional, event-based

A GLM digital twin must serve three distinct questions, each with different data and modeling
needs:

| Framing | Question | Ground-motion input | Output | Data / model need |
|---|---|---|---|---|
| **Conditional (national)** | $P(\text{liq}\mid IM)$ — given shaking | a specified intensity measure (PGA/PGV) | probability / extent given that IM | the national GLM surrogate [@sanger2025jgge]; geospatial $V_{s30}$, water table |
| **Unconditional (return period)** | total liquefaction hazard in $T$ years | integrated over the **NSHM** hazard curve | return-period liquefaction hazard | $\lambda_{liq}=\int P(\text{liq}\mid IM)\,\lvert d\lambda(IM)\rvert$; NSHM curves [@petersen2024] via [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) |
| **Event-based (scenario)** | liquefaction footprint of *this* quake | a ShakeMap IM field | deterministic spatial map | rupture → ShakeMap → GLM; the nowcasting mode |

The **unconditional** product is the "total risk for a return period" baseline; the
**event-based** product is the real-time nowcast for a specific rupture (e.g. a Cascadia or
[Nisqually](wa-2001-2031-nisqually-earthquake) scenario).

### 3.4 Attenuation, $\kappa_0$, and the NSHM (an open question)

High-frequency ground motion — and therefore $a_{max}$ — is controlled by **attenuation**,
parameterized by the site spectral-decay term $\kappa_0$ [@andersonhough1984]. The GAIA
seismic networks can help answer two questions the team has flagged:

- **Where is $\kappa_0$ measured?** From the high-frequency slope of recorded acceleration
  spectra ($A(f)\propto e^{-\pi\kappa f}$); the zero-distance intercept is the site $\kappa_0$.
  GAIA's dense seismic/DAS data make this estimable per site.
- **Can $\kappa_0$ vary in time?** It is dominated by attenuation in the shallow,
  moisture-sensitive subsurface, so it is **not** strictly static — seasonal variation has been
  observed [@haendel2025; @ktenidou2015]. This is a natural coupling to the Pillar-1 soil
  reanalysis (the same near-surface saturation GAIA monitors via $dv/v$). **Open integration
  question:** the [NSHM](https://www.usgs.gov/programs/earthquake-hazards) embeds a *fixed*
  reference-rock $\kappa_0$ and $V_{s30}$ site term [@petersen2024]; how to feed a
  **time-varying** site term back into the hazard input for the unconditional product is
  unresolved and a GAIA research target.

### 3.5 Why high-resolution GLMs — even for static layers

A national GLM cannot be coarse. Liquefaction is controlled by **meter-scale** contrasts in
saturation, $V_s$, and geology, so even the **static but spatially-resolved** layers
($V_{s30}$, geology, water-table depth) must be high-resolution — otherwise the inputs average
away the very heterogeneity that localizes ground failure, systematically smearing hazard and
biasing loss estimates. This is the same resolution argument made for the
[soil reanalysis](pillar-1-soil-reanalysis). On top of the static layers, GAIA adds **dynamic,
time-varying** hydrological (water table from sea-level rise and seasonal recharge) and
mechanical ($V_s$, $\kappa_0$) effects — the novel contribution beyond a static national map.

### 3.6 Data inventory (cross-checked against landslides)

Every layer is tagged with the hazard purpose it serves, so the [DataHub](datahub) inventory is
shared and de-duplicated across hazards.

**Legend:** ⛰️ landslides (shallow/deep) · 🔥 post-fire debris flows · 🏚️ liquefaction &
ground failure · 🌊 floods

| Layer | Role | Source | Serves |
|---|---|---|---|
| DEM / terrain (slope, CTI) | static | USGS 3DEP | ⛰️ 🔥 🏚️ 🌊 |
| $V_{s30}$ / $V_s$ profiles | static → dynamic | [@sanger2025vs]; seismic ([soil-memory](soil-memory)) | 🏚️ ⛰️ |
| Water-table depth $d_{wt}$ | **dynamic** | [Pillar 1](pillar-1-soil-reanalysis); [groundwater modeling](groundwater-soil-moisture) | 🏚️ ⛰️ 🌊 |
| Soil saturation $S_w$ | **dynamic** | [Pillar 1](pillar-1-soil-reanalysis) | ⛰️ 🔥 🏚️ 🌊 |
| Surficial geology / soil type | static | SOLUS / POLARIS, state surveys | 🏚️ ⛰️ |
| Precipitation | dynamic | PRISM / HRRR (gaia-cli) | ⛰️ 🔥 🌊 |
| Ground motion (PGA/PGV) | event / probabilistic | ShakeMap; NSHM [@petersen2024] | 🏚️ |
| $\kappa_0$ / attenuation | static → dynamic | seismic spectra [@andersonhough1984] | 🏚️ |
| Burn severity (dNBR) | static (per event) | MTBS / BAER | 🔥 |

The **water-table** and **saturation** rows are exactly the layers shared with the landslide
data taxonomy (§2.4) — the soil reanalysis serves both hazards, which is why the inventory and
icons are unified rather than per-hazard.

### 3.7 Integration with Earth2Studio

The **dynamic** half of the GLM twin needs forecast forcing, routed through
[NVIDIA Earth2Studio](https://github.com/gaia-hazlab/earth2studio-test) — the same AI
weather/climate stack the
[landslide digital twin](https://github.com/gaia-hazlab/landslide-digital-twin) and
[Pillar 3 forecasting](pillar-3-forecasting-susceptibility) use:

- **Climate/weather → groundwater → water table.** Earth2Studio forecasts (precipitation, plus
  sea-level-rise and seasonal scenarios) drive the groundwater model that sets $d_{wt}$ — the
  dynamic liquefaction control.
- **GLM surrogate as an Earth2Studio model.** The fast mechanics-informed surrogate
  [@sanger2025jgge] can be wrapped as a pipeline component for large scenario / return-period
  ensembles.
- **Time-varying site terms.** Seismic-derived $V_s(t)$ / $\kappa_0(t)$ feed the ground-motion
  side, closing the dynamic loop (§3.4).

### 3.8 Repositories *(placeholders — for Morgan to confirm)*

- [`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) — the
  liquefaction / ground-failure modeling repo (hydrology + seismology + geotech).
- [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) — USGS NSHM disaggregation
  client feeding the unconditional integration.
- `gaia-model-liquefaction` *(proposed)* — the GLM surrogate digital twin (conditional /
  unconditional / event-based runners).
- `gaia-vs-conus` *(proposed)* — the parametric $V_s$-profile product [@sanger2025vs].

*Proposed repositories do not exist yet — the names are placeholders for the team to
create/confirm.*

## 4. Evaluation & metrics

See [HazEvalHub](hazevalhub): event-based detection (POD, FAR, CSI), spatial agreement
(IoU/Dice), probabilistic calibration (Brier, reliability diagrams) for $P_f$, and alert lead
time.

## 5. Open questions & roadmap

- Quantify how prior uncertainty in static soil layers propagates to $P_f$ (sensitivity study).
- Close the Pillar 1 → Pillar 2 data loop by migrating `landlab-debrisflow` onto DataHub.
- Liquefaction: integrate a **time-varying** site term ($\kappa_0(t)$, $V_s(t)$) into the NSHM
  hazard input for the unconditional product (§3.4).
- Liquefaction: stand up the proposed repositories (§3.8) and the groundwater coupling for
  sea-level-rise/seasonal effects.

## References
