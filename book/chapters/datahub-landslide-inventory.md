# Landslide Data Inventory

:::{note}
**The authoritative data inventory for the landslide digital twin.** This page catalogs
every dataset that flows through the shallow / deep-seated [landslide](hazard-landslides)
digital twin — from **raw external products**, through **deterministically derived layers**,
to **model outputs** — with sources, access/sensitivity, spatial/temporal resolution, and
limitations. For derived and modelled products it also records the **model used**, its **raw
inputs**, and its **assumptions**.

It is the landslide-specific companion to the [DataHub](datahub) and follows the four-part
provenance standard (source · measurement · resolution · uncertainty) defined in the
[DataHub Integration Guide §2](datahub-integration-guide). Variable names follow the Landlab
`field__name` vocabulary so layers drop straight into the
[`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) backend.
:::

## How to read this inventory

Data are grouped by **provenance tier**, because that determines how they should be trusted,
stored, and calibrated:

1. **Raw / observed inputs** — imported from an external archive. Treated as observations or
   prepared inputs, *not* model outputs. Calibration should hold these fixed.
2. **Derived variables** — computed deterministically from raw inputs and documented rules.
   Not observed, but fully reproducible given the input stack and config.
3. **Modelled variables & outputs** — produced by the ecohydrology and slope-stability
   components during a run. These carry model assumptions and uncertainty.

Every column matters: **Access / sensitivity** flags keys, licenses, or withheld locations;
**Native resolution** and **Cadence** record the support a value actually has (so a
downscaled 9 km pixel is never mistaken for a 10 m one — the
[footprint-leakage](pillar-1-soil-reanalysis) problem); **Limitations** captures the caveat a
downstream modeler needs before using the layer.

The **primary target** the whole pipeline exists to produce is
`landslide__probability_of_failure` ($P_f$, dimensionless 0–1). The `fire-debrisflow-ml`
targets `dem_diff` / `debris_flow` are a *different* ML target and must not be confused with
the DT hazard target.

## 1. Raw / observed inputs (external products)

These are fetched from external archives and prepared onto the working grid. They are the
fixed foundation of the model and of calibration.

| Layer / product | Source · archive (API / website) | Access / sensitivity | Native spatial res · CRS | Temporal cadence | Units | Key limitations |
|---|---|---|---|---|---|---|
| **DEM** → `topographic__elevation` | USGS 3DEP via OpenTopography ([opentopography.org](https://opentopography.org/), [USGS 3DEP](https://www.usgs.gov/3d-elevation-program)) | Public / open; OpenTopography API needs a **free key** | ~10 m (1/3 arc-sec); lidar 1 m where available | Static (re-flown irregularly) | m | Vertical accuracy & vintage vary; voids; current `.asc` stack **does not embed CRS** (config asserts EPSG:32610) |
| **Soil texture & properties** → `clay__total`, `sand__total`, `silt__total`, `pH`, `dry__bulk_density`, `cation__exchange_capacity`, soil depth | USDA SOLUS100 (Soil Landscapes of the U.S., 100 m); public GCS `solus100pub`; STAC [`solus-stac`](https://github.com/gaia-hazlab/solus-stac) | Public / open | 100 m · EPSG:5070; depths 0,5,15,30,60,100,150 cm | Static (ML estimate) | %, pH, g cm⁻³, cmol(+)/kg, cm | ML-predicted with **uncertainty bands (l/h)**; CONUS-only; variable definitions differ from POLARIS |
| **Soil hydraulic / strength priors** (alt. provider) | POLARIS 30 m ([hydrology.cee.duke.edu/POLARIS](http://hydrology.cee.duke.edu/POLARIS/)); used by [`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin) | Public / open | 30 m; same depth scheme; p5/p50/p95 | Static (statistical) | varies (per property) | Statistically downscaled SSURGO; **different vocabulary, depths, stats & units from SOLUS** — a conversion table is required before mixing the two |
| **Landcover** → `vegetation__plant_functional_type` source | USGS/MRLC NLCD ([mrlc.gov](https://www.mrlc.gov/)) | Public / open | 30 m | ~2–3 yr epochs (annual in newest) | categorical class id | Class generalization; mapping-epoch lag; needs a class→PFT lookup |
| **Burn severity** → `burn__severity` *(post-fire variant only)* | MTBS dNBR / RdNBR ([mtbs.gov](https://www.mtbs.gov/)); local dNBR products | Public / open | 30 m | Per-fire / annual since 1984 | categorical / severity index | Only large fires mapped; dNBR depends on image timing; **not used by core shallow/deep landslide** model |
| **Observed precipitation & temperature** → daily forcing | PRISM Climate Group ([prism.oregonstate.edu](https://prism.oregonstate.edu/)); STAC [`prism-stac`](https://github.com/gaia-hazlab/prism-stac); staged via [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) | 4 km free; **800 m AN81 is license-restricted** | 4 km (800 m licensed) | Daily | mm day⁻¹; °C | Coarse for steep terrain; gauge-sparse interpolation error; daily step only |
| **Forecast precipitation** → `tp` / `APCP_surface` | NVIDIA Earth2Studio ([github.com/NVIDIA/earth2studio](https://github.com/NVIDIA/earth2studio)): GraphCast, AIFS, Pangu, StormCast | Software open; **per-model weight licenses vary** | 0.25° (~25 km) global; StormCast 3 km regional | Forecast: init / lead, sub-daily→daily | m step⁻¹ or kg m⁻² (accum.) | Precip is the **least-skillful** field; accumulation vs stepwise conventions differ by model; needs downscaling + careful mm/day conversion |
| **Soil-moisture target** (calibration) | NASA SMAP L4 `SPL4SMGP` via NSIDC DAAC ([nsidc.org/data/spl4smgp](https://nsidc.org/data/spl4smgp)) | Free but **NASA Earthdata login required** | ~9 km | 3-hourly | m³ m⁻³ | Coarse footprint; model-assimilated (not pure obs); L-band senses only ~top 5 cm |
| **Snow-water-equivalent target** (calibration) | ECMWF ERA5 / ERA5-Land via Copernicus CDS ([cds.climate.copernicus.eu](https://cds.climate.copernicus.eu/)) | Free but **CDS account + API key + license acceptance** | ERA5 ~31 km; ERA5-Land ~9 km | Hourly | m w.e. / mm | Reanalysis SWE biased in complex terrain; coarse |
| **In-situ met stations** | Synoptic Data ([synopticdata.com](https://synopticdata.com/), [docs](https://docs.synopticdata.com/)) | **API token required** (free for academic via Open Access Program); some networks restricted | Point | Sub-hourly | varies | Heterogeneous networks; uneven density; gaps |
| **Landslide inventories** → validation labels | USGS Landslide Hazards ([usgs.gov](https://www.usgs.gov/programs/landslide-hazards)); WA DNR inventory ([dnr.wa.gov](https://www.dnr.wa.gov/)); lidar interpretation | Public, but **some initiation locations withheld**; private-land sensitivity | Vector (points / polygons) | Event-based / historical | presence / absence | Completeness & recency bias; mapping subjectivity; uncertain initiation dates |
| **Seismic trigger** (future extension) → PGA, PGV, MMI, Arias | USGS ShakeMap ([earthquake.usgs.gov/data/shakemap](https://earthquake.usgs.gov/data/shakemap/)); waveforms via EarthScope/IRIS ([ds.iris.edu](https://ds.iris.edu/)) | Public / open | Event grid / station | Event-based | g, cm s⁻¹, intensity | ShakeMap & GMM epistemic uncertainty; **not yet wired** into the landslide DT |

## 2. Derived variables (deterministic transformations)

Computed from the raw stack and documented rules — reproducible, not observed. They should be
**traceable**, with their generating rule recorded.

| Derived variable | Computed from | Units / dims | Equation or rule | Why it matters |
|---|---|---|---|---|
| `drainage_area` | DEM + boundary conditions + Landlab `FlowAccumulator` | m², `[n_nodes]` | Landlab flow routing | Upslope area & routing diagnostic |
| `topographic__slope` | DEM | gradient, `[n_nodes]` | `topographic__steepest_slope` copied to required field name | Required by `LandslideProbability`; **unit convention (gradient vs degrees) must be explicit** |
| `topographic__specific_contributing_area` | `drainage_area`, `grid.dx` | m, `[n_nodes]` | $a = A_d / \Delta x$ | Hydrologic term in relative wetness |
| Aspect, hillshade | DEM | `[n_nodes]` | GIS terrain derivations | Diagnostics / interpretation only |
| `soil__transmissivity` | $K_{sat}$, soil thickness | m² day⁻¹, `[n_nodes]` | $T = K_{sat}\cdot 2.5 \cdot h_s$, floor 0.01 | Static transmissivity proxy; **2.5 anisotropy factor is a calibration lever** |
| `vegetation__live_leaf_area_index` | PFT lookup | `[n_nodes]` | grass 1.5, shrub 2.0, tree 4.0, bare 1.0 | Controls PET & vegetation response |
| `vegetation__cover_fraction` | LAI | `[n_nodes]` | $\text{cover} = \text{LAI}/4$ | Ecohydrology vegetation cover input |
| `soil_moisture__initial_saturation_fraction` | SMAP $\theta_0$ (or midpoint heuristic), porosity | `[n_cells]` | $S_0 = \theta_0 / n$ | Initial water state — **shifts the whole event response** |
| `field_capacity_saturation` | `field__capacity`, porosity | `[n_cells]` | $S_{fc} = \mathrm{clip}(\theta_{fc}/n, 0.05, 0.98)$ | Drainage-onset threshold |
| `wilting_point_saturation` | `wilting__point`, porosity | `[n_cells]` | $S_{wp} = \mathrm{clip}(\theta_{wp}/n, 0.01, 0.95);\ S_{wp}\le S_{fc}-0.01$ | Water-stress threshold |
| `snow_fraction_arrays` | precip, Tmin, Tmax | `[time, n_nodes]` | linear rain–snow partition between $T_{snow}$ and $T_{rain}$ | Splits storm water rain vs snow |
| `rain_depth` / `snow_depth` | precip + snow fraction | mm, `[time, n_nodes]` | $P_{rain}=P(1-f_{snow})$, $P_{snow}=Pf_{snow}$ | Liquid vs frozen inputs |
| `swe_arrays` | initial SWE, snow, melt | mm, `[time, n_nodes]` | $SWE_t = SWE_{t-1} + \text{snow} - \text{melt}$ | Snow storage (calibrate vs ERA5 SWE) |
| `water_input_arrays` | rain + melt | mm, `[time, n_nodes]` | $W_{in} = \text{rain} + \text{melt}$ | Liquid water into ecohydrology |
| `mean_recharge` / `max_recharge` | daily recharge arrays | mm day⁻¹, `[n_nodes]` | temporal mean / max | Scenario-ready recharge summaries |
| `routed_recharge_max` | `max_recharge` + routing | recharge-equiv., `[n_nodes]` | `surface_water__discharge` / `drainage_area` | Upslope-averaged recharge scenario |
| `groundwater__recharge_mean` / `std` | local or routed recharge | mm day⁻¹, `[n_nodes]` | `std = 0.1 × mean` (active setup) | Direct input to `LandslideProbability` recharge sampling |

:::{warning}
**Current notebook state (active run).** The final `LandslideProbability` call currently uses
**local `max_recharge`**, *not* `routed_recharge_max` (which is computed but not the active
forcing). The burn-severity cohesion block is present but **does not currently reduce
cohesion**. Both are flagged calibration / structural choices in §5–§6 below.
:::

## 3. Modelled variables & outputs

Produced by the ecohydrology and slope-stability components. These carry model assumptions and
should be published with provenance and uncertainty.

| Output | Producing component | Units / dims | Meaning | Primary use |
|---|---|---|---|---|
| `soil_moisture__saturation_fraction` | `SoilMoisture` | fraction, `[time, n_cells]` | Root-zone saturation | Hydrologic state; **SMAP comparison** (× porosity) |
| `soil_moisture__root_zone_leakage` | `SoilMoisture` | mm, `[time, n_cells]` | Deep leakage below root zone | Recharge source for landslide forcing |
| `surface__runoff` | `SoilMoisture` | mm, `[time, n_cells]` | Daily surface runoff | Runoff diagnostics & routing |
| `surface__evapotranspiration` | `SoilMoisture` + PET | mm, `[time, n_cells]` | Actual ET | Water-balance diagnostic |
| `vegetation__water_stress` | `SoilMoisture` | fraction-like, `[time, n_cells]` | Plant stress | Ecohydrology interpretation |
| `surface_water__discharge` | `FlowAccumulator` | volume time⁻¹, `[n_nodes]` | Routed flow | Builds routed recharge / runoff |
| `soil__mean_relative_wetness` | `LandslideProbability` | 0–1, `[n_nodes]` | Mean wetness term in infinite-slope FS | Landslide-state diagnostic |
| `soil__probability_of_saturation` | `LandslideProbability` | 0–1, `[n_nodes]` | $\Pr(\text{wetness}\ge 1)$ over MC samples | Secondary saturation-risk layer |
| **`landslide__probability_of_failure`** | `LandslideProbability` | 0–1, `[n_nodes]` / `[time,y,x]` / forecast `[init,lead,y,x]` | $\Pr(FS \le 1)$ | **Primary hazard target** (map, API, dashboard) |
| `routed_runoff_m3_day` | `FlowAccumulator` post-proc | m³ day⁻¹, `[n_nodes]` | Routed runoff discharge | Hydrologic diagnostic only |

## 4. Data-prep pipeline for the shallow + deep landslide DT

This is the exact sequence that converts the raw products of §1 into a **validated,
Landlab-ready layer stack on a single watershed grid**, plus the dynamic forcing. It implements
the [DataHub Integration Guide](datahub-integration-guide) conventions and feeds the
[Landlab model](modelhub-landslide). **Post-fire debris flows are a specialized case**: they
reuse every step below and add only (i) a `burn__severity` layer and (ii) a fire-reduced
cohesion step — the core shallow/deep pipeline omits both.

```
A. domain        AOI → watershed / HUC polygon; target CRS + resolution; single outlet
B. acquire       STAC / provider:  DEM · SOLUS100|POLARIS soil · NLCD landcover
                                    (+ MTBS burn severity — post-fire only)
C. harmonize     reproject + resample to ONE grid contract (nearest=categorical,
                 bilinear/cubic=continuous); set nodata; record manifest
D. derive        slope, specific contributing area  (FlowAccumulator on the CLOSED watershed)
                 pedotransfer → friction φ, cohesion(min/mode/max), Ksat → transmissivity
                 landcover → PFT → LAI, cover, root cohesion
                 field-capacity / wilting saturations
E. force         PRISM (hindcast, via gaia-cli)  |  Earth2Studio tp/APCP (forecast)
                 → downscale to grid → mm/day → snow partition → water balance → recharge
F. soil state    deep-seated: import water-table/head h(x,t) + S_w from Pillar 1 / soil-memory
                 init S0 from SMAP (+ post-fire: reduce cohesion by burn-severity class)
G. validate      input contract: shape · CRS · transform · nodata · units · required fields
H. publish       COG / Zarr on s3://cresst + STAC items with source·measurement·res·uncertainty
```

**Step A — close the hydrology first.** Clip to a watershed/subwatershed (HUC) with the outlet
as the single open boundary and all other edges closed, so contributing area is physically
correct (see [model §5](modelhub-landslide)). Do **not** prepare on arbitrary tiles.

**Step C — the grid contract.** Every raster must arrive on one grid before model execution,
and every layer carries a manifest entry:

| Grid-contract field | Example | Why |
|---|---|---|
| CRS | EPSG:32610 (event UTM) | must be **embedded** in outputs (`.asc` does not carry it) |
| affine transform · width · height | 790 × 650 @ 10 m | co-registration of all layers |
| resolution | 10 m (watershed) / coarser (regional) | sets cost and detail |
| nodata | −999999 → NaN/mask | consistent masking before model math |
| resampling | nearest (categorical) / bilinear (continuous) | avoids class-mixing |
| units + conversion | %, m, Pa, mm day⁻¹ | Landlab expects specific units (e.g. slope as gradient) |
| provenance | source · timestamp · version | reproducibility & later surrogate training |

**Steps D–E — what differs between shallow and deep.** Both build the same static stack and run
the same engine; they diverge at the **wetness closure**: the *shallow* run derives recharge →
topographic wetness from PRISM/forecast forcing (steps D–E), while the *deep-seated* run imports
the **water-table/head field** from Pillar 1 (step F) as its wetness driver and uses a thicker
soil-column depth $D$.

**Current state to fix (from the active notebook).** Inputs are still read from hardcoded local
paths and `.asc` files without embedded CRS; the active run forces with local `max_recharge`
(not routed); and the burn-severity cohesion step is present but inactive. De-personalizing the
config and sourcing from STAC (`solus-stac`, `prism-stac`, `gaia-cli stage`) is the migration
called for in the [Integration Guide §3](datahub-integration-guide).

## 5. Models behind the derived & modelled products

Each derived/modelled product above is generated by one of the following model components.
For each: what it does, its **raw inputs** (and their limitations), and its **assumptions**.

### Infinite-slope slope stability — Landlab `LandslideProbability`

Produces the primary target $P_f$ and the wetness/saturation diagnostics. Solves the
**infinite-slope factor of safety** probabilistically: a Monte Carlo draw over uncertain
parameters yields $P_f = \Pr(FS \le 1)$ (full equations in
[Pillar 2 §2.3](pillar-2-nowcasting-susceptibility)) [@strauch2018].

- **Inputs:** `topographic__slope`, `topographic__specific_contributing_area`,
  `soil__thickness`, `soil__density`, `soil__internal_friction_angle`,
  `soil__transmissivity`, `soil__{min,mode,max}_total_cohesion`, and
  `groundwater__recharge_mean/std`.
- **Limitations of inputs:** soil strength & cohesion come from pedotransfer/lookup on
  SOLUS/POLARIS (large uncertainty); transmissivity inherits the 2.5 anisotropy assumption;
  recharge forcing depends on the upstream ecohydrology and recharge-scenario choice.
- **Assumptions:** infinite-slope geometry (planar failure, slope-parallel flow); steady-state
  topographic wetness from recharge & transmissivity [@beven1979; @montgomery1994]; cohesion
  represented as a triangular min/mode/max distribution; parameters spatially independent
  across Monte Carlo draws; `number_of_iterations` (1000) controls only sampling noise, **not**
  a physical parameter.

The **shallow vs deep-seated** distinction is a swapped *hydrology closure* into this same
engine — shallow uses vadose-zone topographic wetness, deep-seated uses the water-table / head
field from the [Soil Reanalysis Product](pillar-1-soil-reanalysis) — not a different model.

### Ecohydrology water balance — Landlab `SoilMoisture` + PET

Generates root-zone saturation, leakage (the recharge source), runoff, ET, and water stress.

- **Inputs:** `water_input_arrays` (rain + melt), `field_capacity_saturation`,
  `wilting_point_saturation`, porosity, $K_{sat}$, LAI/cover by PFT, and PET drivers
  (latitude, albedo, vegetation height, wind, humidity, lapse rate).
- **Limitations of inputs:** PRISM forcing is 4 km; PET parameters are largely heuristic;
  field-capacity/wilting thresholds inherit soil-product uncertainty.
- **Assumptions:** single root-zone bucket per PFT; `ksat_factor = 0.5` scales infiltration /
  leakage / runoff partition; cover fraction = LAI/4; ET from a PET formulation with prescribed
  vegetation parameters.

### Snow partition & melt — degree-day

Splits precipitation into rain and snow and tracks SWE.

- **Inputs:** PRISM precip, Tmin, Tmax; initial SWE.
- **Assumptions:** linear rain–snow partition between $T_{snow}$ and $T_{rain}$; degree-day
  melt with `melt_factor` and base temperature $T_{base}$; SWE bookkeeping
  $SWE_t = SWE_{t-1} + \text{snow} - \text{melt}$. Calibrate against ERA5 SWE.

### Flow routing — Landlab `FlowAccumulator`

Computes `drainage_area`, `surface_water__discharge`, and the routed-recharge / routed-runoff
diagnostics.

- **Inputs:** DEM, boundary conditions, `water__unit_flux_in`.
- **Limitations:** routing is sensitive to the DEM and the **boundary-condition elevation
  cutoff (337 m)**; arbitrary tiling can break hydrologic routing — watersheds are the safer
  model unit.
- **Assumptions:** single-/multiple-flow-direction routing on the working grid; contributing
  area is well-defined only within the routed domain.

### Precipitation → recharge conversion

Turns observed/forecast precipitation (after the water balance) into the recharge forcing for
the slope-stability model, summarized as `mean`/`max`, optionally routed.

- **Assumptions:** the chosen recharge summary (mean vs max) and the **local vs routed**
  scenario are *structural* choices that change the spatial pattern of forcing; recharge
  uncertainty modeled as `std = 0.1 × mean`.

### Forecast weather leg — NVIDIA Earth2Studio

A *weather-provider* branch (GraphCast / AIFS / Pangu / StormCast), **not** the landslide model
itself. It extracts model precipitation, converts `tp`/`APCP` to consistent mm/day, downscales
to the working grid, converts to recharge, then runs the same Landlab backend (or a future
surrogate) to produce a forecast $P_f$.

- **Limitations:** precipitation is the least-skillful forecast field; accumulation conventions
  differ by model; coarse global grids need downscaling; weight licenses vary by model.
- **Assumptions:** forecast precip is the dominant dynamic driver; static layers and model
  parameters are held fixed across the forecast horizon. Forecast outputs must retain
  `init_time`, `lead_time`, `valid_time`, `model_name`, `forecast_version`.

:::{note}
**ML surrogate (future).** A surrogate is *not* a replacement for Landlab. Trained on
accumulated Landlab labels + historical/forecast forcing, its role is **acceleration** for
PNW-wide screening and large ensembles, with Landlab retained as the reference model to
generate labels and audit high-risk areas.
:::

## 6. Calibration targets

Calibration should constrain parameters against the **right observable**, not only against the
final landslide map. Targets, in recommended sequence:

| Observable target | Best constrains | How to compare | Priority |
|---|---|---|---|
| **SMAP** daily soil moisture | initial saturation, `ksat_factor`, root-zone depths, field/wilting thresholds | AOI / core-node mean volumetric SM time series | High |
| SMAP sub-daily (Pacific-time) | timing & aggregation mismatch | overlay sub-daily SMAP vs daily model states | Medium |
| **ERA5 SWE** | $T_{snow}$/$T_{rain}$, `melt_factor`, $T_{base}$, initial SWE | daily SWE mean & depletion timing | High (winter events) |
| **Mapped landslide initiation** | recharge-scenario choice, cohesion reduction, strength fields, transmissivity | presence/absence, hit rate, precision–recall, spatial overlap | **Highest** (final hazard) |
| Known stable / non-failure areas | false-positive control | specificity / precision | High |
| Runoff / streamflow (if available) | hydrologic partitioning, recharge realism | daily event hydrograph / basin runoff index | High when available |

**Highest-value calibration levers** (current notebook): initial water state; conductivity /
transmissivity scaling (`ksat_factor`, the 2.5 anisotropy factor); snow partition & melt
parameters; root-zone depth family; recharge-scenario choice (local vs routed); and post-fire
cohesion reduction. `number_of_iterations` is **not** a calibration parameter (convergence
testing only).

## 7. Known gaps, risks & sensitivities

- **CRS leakage.** Local `.asc` stacks lack an embedded CRS though config asserts EPSG:32610;
  GeoTIFF/Zarr outputs **must** carry CRS explicitly.
- **Soil-vocabulary mismatch.** POLARIS and SOLUS differ in variable definitions, depths,
  statistics, and units — a provider conversion table is required before mixing them.
- **Slope units.** Landlab expects slope as gradient/tan(θ); some GIS products store degrees —
  make the convention explicit.
- **Precip accumulation.** AI-weather precip may be cumulative or stepwise; daily-recharge
  conversion must be tested per model.
- **Cost.** High-resolution Landlab everywhere in the PNW daily is too expensive — use a hybrid
  of coarse regional screening, targeted high-res watersheds, and (future) surrogate
  acceleration.
- **Hydrologic tiling.** Arbitrary tiles break routing; use **watersheds/subwatersheds** for
  model execution and chunks/tiles for storage.
- **Access sensitivities.** OpenTopography (free key), PRISM 800 m (license), SMAP (Earthdata
  login), ERA5 (CDS license), Synoptic (API token), and some landslide-inventory locations
  (withheld) all require credentials or carry access constraints — see §1.
- **Active-run caveats.** Local `max_recharge` (not routed) is the active forcing, and the
  burn-severity cohesion reduction is currently inactive (§2 warning).

## Related

- [Landslides](hazard-landslides) — the hazard page this inventory serves.
- [DataHub](datahub) · [DataHub Integration Guide](datahub-integration-guide) — platform,
  provenance standard, and repo migration path.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) — the science driving the
  static-layer requirements.
- [Pillar 2 — Nowcasting Hazard Susceptibility](pillar-2-nowcasting-susceptibility) — the model
  equations behind the outputs in §3 and §5.
- Repos: [`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin) ·
  [`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) ·
  [`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml) ·
  [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) ·
  [`solus-stac`](https://github.com/gaia-hazlab/solus-stac) ·
  [`prism-stac`](https://github.com/gaia-hazlab/prism-stac)
