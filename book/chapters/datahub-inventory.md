# Data Inventory

:::{note}
**The single, cross-hazard data inventory for the GAIA digital twins.** This page catalogs
every dataset that flows through any hazard model — from **raw external products**, through
**deterministically derived layers**, to **model outputs** — with sources, access/sensitivity,
spatial/temporal resolution, and limitations. Each layer is tagged with the **hazard(s) it
serves**, so the inventory is shared and de-duplicated rather than rebuilt per hazard.

It is the data companion to the [DataHub](datahub) and follows the four-part provenance
standard (source · measurement · resolution · uncertainty) defined in the
[DataHub Integration Guide §2](datahub-integration-guide). Variable names follow the Landlab
`field__name` vocabulary where applicable.
:::

## How to read this inventory

**Hazard legend (the `Serves` column):** ⛰️ landslides (shallow / deep-seated) · 🔥 post-fire
debris flows · 🏚️ liquefaction & ground failure · 🌊 floods.

Data are grouped by **provenance tier**, because that determines how they should be trusted,
stored, and calibrated:

1. **Raw / observed inputs** — imported from an external archive; treated as observations or
   prepared inputs, *not* model outputs. Calibration holds these fixed.
2. **Derived variables** — computed deterministically from raw inputs and documented rules.
   Not observed, but fully reproducible given the input stack and config.
3. **Modelled variables & outputs** — produced by the model components during a run. These
   carry model assumptions and uncertainty.

**Access / sensitivity** flags keys, licenses, or withheld locations; **Native resolution** and
**Cadence** record the support a value actually has (so a downscaled 9 km pixel is never
mistaken for a 10 m one — the [footprint-leakage](pillar-1-soil-reanalysis) problem);
**Limitations** captures the caveat a downstream modeler needs before using the layer.

The **primary targets** the pipelines exist to produce are
`landslide__probability_of_failure` ($P_f$ ⛰️ 🔥) and the **probability / extent of
liquefaction** $P(\text{liq})$ with its manifestation severity (LPI / LSN 🏚️).

## 1. Raw / observed inputs (external products)

Fetched from external archives and prepared onto the working grid — the fixed foundation of the
models and of calibration.

| Layer / product | Serves | Source · archive (API / website) | Access / sensitivity | Native spatial res · CRS | Cadence | Units | Key limitations |
|---|---|---|---|---|---|---|---|
| **DEM** → `topographic__elevation`, slope, contributing area | ⛰️ 🔥 🏚️ 🌊 | USGS 3DEP via OpenTopography ([opentopography.org](https://opentopography.org/), [USGS 3DEP](https://www.usgs.gov/3d-elevation-program)) | Public / open; OpenTopography API needs a **free key** | ~10 m (1/3 arc-sec); lidar 1 m where available | Static (re-flown irregularly) | m | Vertical accuracy & vintage vary; voids; `.asc` stacks **do not embed CRS** |
| **Soil texture & properties** → `clay/sand/silt__total`, `pH`, `dry__bulk_density`, CEC, soil depth | ⛰️ 🔥 🏚️ | USDA SOLUS100 (100 m); public GCS `solus100pub`; STAC [`solus-stac`](https://github.com/gaia-hazlab/solus-stac) | Public / open | 100 m · EPSG:5070; depths 0,5,15,30,60,100,150 cm | Static (ML estimate) | %, pH, g cm⁻³, cmol(+)/kg, cm | ML-predicted with **uncertainty bands (l/h)**; CONUS-only; vocabulary differs from POLARIS |
| **Soil hydraulic / strength priors** (alt.) | ⛰️ 🏚️ | POLARIS 30 m ([hydrology.cee.duke.edu/POLARIS](http://hydrology.cee.duke.edu/POLARIS/)); used by [`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin) | Public / open | 30 m; same depth scheme; p5/p50/p95 | Static (statistical) | varies | Downscaled SSURGO; **different vocabulary, depths, stats & units from SOLUS** — conversion table required |
| **Shear-wave velocity** → $V_{s30}$, $V_s(z)$ | 🏚️ ⛰️ | parametric CONUS $V_s$ [@sanger2025vs]; USGS National Crustal Model; slope/geology proxy $V_{s30}$ | Public / open | parametric; proxy ~250–1000 m | Static (→ dynamic via seismic) | m s⁻¹ | Proxy $V_{s30}$ has large scatter; **rigidity is high-influence** for liquefaction |
| **Surficial geology / soil type** | 🏚️ ⛰️ | state geologic surveys; USGS | Public / open | 1:24k–1:100k | Static | categorical | Map-scale generalization; susceptibility class boundaries uncertain |
| **Landcover** → `vegetation__plant_functional_type` | ⛰️ 🔥 | USGS/MRLC NLCD ([mrlc.gov](https://www.mrlc.gov/)) | Public / open | 30 m | ~2–3 yr epochs | categorical | Class generalization; epoch lag; needs class→PFT lookup |
| **Burn severity** → `burn__severity` | 🔥 | MTBS dNBR/RdNBR ([mtbs.gov](https://www.mtbs.gov/)) | Public / open | 30 m | Per-fire / annual since 1984 | severity index | Only large fires mapped; dNBR depends on image timing; **post-fire only** |
| **Observed precipitation & temperature** → daily forcing | ⛰️ 🔥 🌊 🏚️ | PRISM Climate Group ([prism.oregonstate.edu](https://prism.oregonstate.edu/)); STAC [`prism-stac`](https://github.com/gaia-hazlab/prism-stac); staged via [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) | 4 km free; **800 m AN81 license-restricted** | 4 km (800 m licensed) | Daily | mm day⁻¹; °C | Coarse for steep terrain; gauge-sparse interpolation error |
| **Forecast precipitation** → `tp` / `APCP_surface` | ⛰️ 🔥 🌊 🏚️ | NVIDIA Earth2Studio ([github.com/NVIDIA/earth2studio](https://github.com/NVIDIA/earth2studio)) | Software open; **weight licenses vary** | 0.25° global; StormCast 3 km | Forecast: init / lead | m or kg m⁻² (accum.) | Precip is the **least-skillful** field; accumulation conventions differ; needs downscaling |
| **Water-table depth** → $d_{wt}$ | 🏚️ ⛰️ 🌊 | [Pillar 1 Soil Reanalysis](pillar-1-soil-reanalysis); [groundwater modeling](groundwater-soil-moisture); modeled WTD (Zhu GLM) | Mixed | tens of m target; coarse priors | **Dynamic** (seasonal, sea-level) | m | Saturation is a **binary gate** for liquefaction; coarse priors smear hazard |
| **Soil-moisture target** (calibration) | ⛰️ 🏚️ | NASA SMAP L4 `SPL4SMGP` via NSIDC ([nsidc.org/data/spl4smgp](https://nsidc.org/data/spl4smgp)) | **NASA Earthdata login** | ~9 km | 3-hourly | m³ m⁻³ | Coarse footprint; model-assimilated; senses only ~top 5 cm |
| **Snow-water-equivalent target** (calibration) | ⛰️ 🌊 | ECMWF ERA5 / ERA5-Land via CDS ([cds.climate.copernicus.eu](https://cds.climate.copernicus.eu/)) | **CDS account + license** | ERA5 ~31 km; ERA5-Land ~9 km | Hourly | m w.e. | Reanalysis SWE biased in complex terrain |
| **In-situ met stations** | ⛰️ 🔥 🌊 🏚️ | Synoptic Data ([synopticdata.com](https://synopticdata.com/)) | **API token** (free academic) | Point | Sub-hourly | varies | Heterogeneous networks; uneven density; gaps |
| **Ground motion (event)** → PGA, PGV, MMI | 🏚️ ⛰️ | USGS ShakeMap ([earthquake.usgs.gov/data/shakemap](https://earthquake.usgs.gov/data/shakemap/)) | Public / open | event grid | Per-event | g, cm s⁻¹ | ShakeMap & GMM epistemic uncertainty; the **demand** input (future seismic trigger for ⛰️) |
| **Seismic hazard (probabilistic)** → hazard curves $\lambda(IM)$ | 🏚️ | USGS NSHM [@petersen2024] via [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) | Public / open | site / gridded | Static (model epoch) | rate vs IM | **Fixed** reference-rock site term (§7); model-epoch dependence |
| **Attenuation** → $\kappa_0$ | 🏚️ | high-frequency spectral decay [@andersonhough1984]; GAIA seismic / DAS | Public / network | per site/station | Static (→ dynamic) | s | Band/method-dependent; seasonal variability [@haendel2025]; **not yet wired** |
| **Geotechnical case histories** (calibration) | 🏚️ | CPT/SPT liquefaction databases [@vanballegooy2014] | Public / curated | point | Event-based | varies | Geographic bias; the surrogate's training/validation base |
| **Hazard inventories / maps** → validation labels | ⛰️ 🏚️ | USGS / WA DNR landslide inventories ([usgs.gov](https://www.usgs.gov/programs/landslide-hazards), [dnr.wa.gov](https://www.dnr.wa.gov/)); post-EQ liquefaction reconnaissance (e.g. 2001 [Nisqually](wa-2001-2031-nisqually-earthquake)) | Public; **some locations withheld** | vector | Event / historical | presence / severity | Completeness & recency bias; used only to **score**, never as input |

## 2. Derived variables (deterministic transformations)

Computed from the raw stack and documented rules — reproducible, not observed.

### 2.1 Hydrology & terrain ⛰️ 🔥 🌊

| Derived variable | Computed from | Units / dims | Equation or rule | Why it matters |
|---|---|---|---|---|
| `drainage_area` | DEM + boundaries + Landlab `FlowAccumulator` | m² | flow routing | upslope area & routing diagnostic |
| `topographic__slope` | DEM | gradient | steepest slope → required field | required by `LandslideProbability`; **gradient vs degrees must be explicit** |
| `topographic__specific_contributing_area` | `drainage_area`, `grid.dx` | m | $a = A_d/\Delta x$ | hydrologic term in relative wetness |
| `soil__transmissivity` | $K_{sat}$, soil thickness | m² day⁻¹ | $T=K_{sat}\cdot 2.5\cdot h_s$, floor 0.01 | **2.5 anisotropy factor is a calibration lever** |
| `vegetation__live_leaf_area_index`, `cover_fraction` | PFT lookup; LAI | – | grass 1.5 / shrub 2.0 / tree 4.0; cover = LAI/4 | controls PET & vegetation response |
| `*_saturation` (initial, field-capacity, wilting) | SMAP $\theta_0$ / soil props, porosity | – | $S=\theta/n$ (clipped) | initial state & drainage/stress thresholds — **shift the whole event response** |
| `snow_fraction`, `rain_depth`, `snow_depth`, `swe`, `water_input` | precip, Tmin/Tmax, melt | mm, `[time,n]` | linear rain–snow partition; degree-day melt; $SWE_t=SWE_{t-1}+\text{snow}-\text{melt}$ | splits storm water; snow storage (calibrate vs ERA5 SWE) |
| `mean/max_recharge`, `routed_recharge_max`, `groundwater__recharge_mean/std` | daily recharge + routing | mm day⁻¹ | temporal stat; `discharge/area`; `std=0.1×mean` | direct input to `LandslideProbability` recharge sampling |

### 2.2 Liquefaction 🏚️

| Derived variable | Computed from | Units | Rule | Why it matters |
|---|---|---|---|---|
| Total / effective stress $\sigma_{v0}$, $\sigma'_{v0}$ | overburden + water table $d_{wt}$ | kPa | $\sigma'_{v0}=\sigma_{v0}-u$ | couples **hydrology** into CSR & CRR |
| Stress-corrected velocity $V_{s1}$ | $V_s$, $\sigma'_{v0}$ | m s⁻¹ | $V_{s1}=V_s\,(P_a/\sigma'_{v0})^{0.25}$ | overburden-normalized **rigidity** for CRR [@andrusstokoe2000] |
| Cyclic stress ratio $\mathrm{CSR}$, MSF, $K_\sigma$ | $a_{max}$, stresses, $r_d$, $M$ | – | see [Liquefaction Model §2](modelhub-liquefaction) | seismic **demand**, normalized to a reference |
| CTI / distance-to-water | DEM; hydrography | – | GIS derivations | geospatial GLM saturation proxies [@zhu2015] |

## 3. Modelled variables & outputs

| Output | Serves | Producing model | Units / dims | Meaning |
|---|---|---|---|---|
| `soil_moisture__saturation_fraction`, `…root_zone_leakage`, `surface__runoff/ET` | ⛰️ 🔥 🌊 | `SoilMoisture` + PET | `[time, n_cells]` | hydrologic state; recharge source; **SMAP comparison** |
| `soil__mean_relative_wetness`, `…probability_of_saturation` | ⛰️ 🔥 | `LandslideProbability` | 0–1 | wetness / saturation-risk diagnostics |
| **`landslide__probability_of_failure`** | ⛰️ 🔥 | `LandslideProbability` | 0–1, `[n]`/`[time,y,x]`/`[init,lead,y,x]` | $\Pr(FS\le1)$ — **primary landslide target** |
| **$P(\text{liq})$ + areal extent** | 🏚️ | GLM surrogate [@sanger2025jgge] | 0–1, `[y,x]` | probability / extent of liquefaction — **primary liquefaction target** |
| **LPI / LSN** | 🏚️ | manifestation model [@iwasaki1978; @vanballegooy2014] | index | surface severity / damage |
| Return-period liquefaction hazard | 🏚️ | unconditional integration over NSHM | rate / 50-yr prob. | $\lambda_{liq}$ planning baseline |

## 4. Data-prep pipelines

### 4.1 Landslide (Landlab) ⛰️ 🔥

```
A. domain     AOI → watershed / HUC polygon; target CRS + resolution; single outlet
B. acquire    DEM · SOLUS100|POLARIS soil · NLCD landcover (+ MTBS burn severity — post-fire only)
C. harmonize  reproject + resample to ONE grid contract; nodata; manifest
D. derive     slope, specific contributing area (FlowAccumulator on the CLOSED watershed);
              pedotransfer → φ, cohesion; Ksat → transmissivity; landcover → PFT → LAI
E. force      PRISM (hindcast) | Earth2Studio tp/APCP (forecast) → mm/day → snow → balance → recharge
F. soil state deep-seated: import water-table h(x,t) + S_w from Pillar 1; init S0 from SMAP
G. validate   input contract: shape · CRS · transform · nodata · units · required fields
H. publish    COG / Zarr on s3://cresst + STAC items with source·measurement·res·uncertainty
```

Close the hydrology first (clip to a watershed with a single outlet — see
[Landslide Model §5](modelhub-landslide)); do **not** prepare on arbitrary tiles. Inputs are
still read from hardcoded local paths in the active notebook; de-personalizing and sourcing from
STAC (`solus-stac`, `prism-stac`, `gaia-cli stage`) is the migration in the
[Integration Guide §3](datahub-integration-guide).

### 4.2 Liquefaction (GLM) 🏚️

```
A. domain     AOI / region; target CRS + resolution (high-res even for static layers)
B. acquire    Vs30/Vs profiles · water table (Pillar 1) · geology · ShakeMap | NSHM ground motion
C. harmonize  reproject + resample to one grid contract; manifest + provenance
D. derive     effective stress σ'v (from water table) · Vs1 · CSR · saturation proxies
E. condition  conditional GLM P(liq|IM)  →  (unconditional: integrate over NSHM;
                                             event: apply ShakeMap IM field)
F. dynamic    couple groundwater (sea-level / seasonal) + time-varying Vs/κ0 (§7 open question)
G. validate   input contract: shape · CRS · units · required fields
H. publish    COG / Zarr on s3://cresst + STAC items
```

The **high-resolution requirement** (even for static $V_{s30}$, geology, water table) is central:
liquefaction is controlled by meter-scale contrasts, so coarse inputs systematically smear hazard.

## 5. Models behind the products

Each derived/modelled product is generated by a model component. Full physics and
solved-vs-assumed breakdowns are on the model pages
([Landslide Model](modelhub-landslide), [Liquefaction Model](modelhub-liquefaction)).

- **Landlab `LandslideProbability`** ⛰️ 🔥 — infinite-slope $FS$ + Monte Carlo $P_f=\Pr(FS\le1)$
  [@strauch2018]; assumes planar failure, steady-state topographic wetness [@beven1979;
  @montgomery1994]. Shallow vs deep-seated = a swapped hydrology closure, not a different model.
- **Ecohydrology `SoilMoisture` + PET / snow / `FlowAccumulator`** ⛰️ 🔥 🌊 — root-zone water
  balance, snow partition, and flow routing that produce recharge and the hydrologic state.
- **Geospatial liquefaction surrogate** 🏚️ — mechanics-informed ML emulating the
  simplified-procedure FS at national scale [@sanger2025jgge; @zhu2017], with manifestation
  fragility [@geyin2020fragility; @maurer2015]; consumes $V_s$, water table, ground motion.
- **Forecast weather leg — NVIDIA Earth2Studio** ⛰️ 🔥 🌊 🏚️ — a weather-provider branch
  (GraphCast / AIFS / StormCast) supplying forecast precipitation (and groundwater forcing for
  liquefaction); not a hazard model itself.

## 6. Calibration targets

| Observable target | Serves | Best constrains | Priority |
|---|---|---|---|
| **SMAP** daily soil moisture | ⛰️ 🏚️ | initial saturation, `ksat_factor`, root-zone depths | High |
| **ERA5 SWE** | ⛰️ 🌊 | snow partition & melt parameters | High (winter) |
| **Mapped landslide initiation** | ⛰️ | recharge scenario, cohesion, strength, transmissivity | **Highest** (landslide) |
| **Geotech case histories / observed liquefaction maps** | 🏚️ | GLM surrogate, manifestation fragility, $V_s$ / water-table inputs | **Highest** (liquefaction) |
| Runoff / streamflow (if available) | ⛰️ 🌊 | hydrologic partitioning, recharge realism | High when available |

`number_of_iterations` (landslide Monte Carlo) is a convergence knob, **not** a calibration
parameter.

## 7. Known gaps, risks & sensitivities

- **CRS leakage.** Local `.asc` stacks lack an embedded CRS; GeoTIFF/Zarr outputs **must** carry
  CRS explicitly.
- **Soil-vocabulary mismatch.** POLARIS and SOLUS differ in variables, depths, statistics, and
  units — a conversion table is required before mixing them.
- **Static vs dynamic water table.** Most GLMs use a *static* modeled water table; GAIA's
  contribution is the **dynamic** $d_{wt}$ (seasonal, sea-level rise) from Pillar 1 — distinguish
  the two.
- **Time-varying site term.** $\kappa_0(t)$ / $V_s(t)$ are not yet wired into the NSHM-based
  unconditional liquefaction product (the open question in [Liquefaction Model §5](modelhub-liquefaction)).
- **$V_{s30}$ proxy uncertainty.** Slope/geology $V_{s30}$ carries large scatter; parametric
  profiles [@sanger2025vs] reduce but do not remove it.
- **Precip accumulation.** AI-weather precip may be cumulative or stepwise; daily-recharge
  conversion must be tested per model.
- **Cost & tiling.** High-resolution everywhere in the PNW daily is expensive; use watersheds for
  routing, tiles only for storage; surrogates for acceleration.
- **Access sensitivities.** OpenTopography (key), PRISM 800 m (license), SMAP (Earthdata), ERA5
  (CDS), Synoptic (token), and some hazard-inventory locations (withheld) — see §1.

## Related

- [Landslides](hazard-landslides) · [Post-fire debris flows](hazard-postfire-debris-flows) ·
  [Liquefaction & Ground Failure](hazard-liquefaction-ground-failure) — the hazard pages.
- [Landslide Model](modelhub-landslide) · [Liquefaction Model](modelhub-liquefaction) — the model
  pages whose outputs and inputs this inventory catalogs.
- [DataHub](datahub) · [DataHub Integration Guide](datahub-integration-guide) — platform,
  provenance standard, and repo migration path.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) — the dynamic soil-state source.
- Repos: [`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) ·
  [`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin) ·
  [`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) ·
  [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) ·
  [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) ·
  [`solus-stac`](https://github.com/gaia-hazlab/solus-stac) ·
  [`prism-stac`](https://github.com/gaia-hazlab/prism-stac).
