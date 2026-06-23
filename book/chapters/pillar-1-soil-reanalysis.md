# Pillar 1 — Soil Reanalysis Product

:::{note}
**Actively developed.** Pillar 1 of the [Digital Twin Framework](digital-twin-overview).
The hydromechanical inversion methods are detailed in
[Soil Hydromechanical Memory](soil-memory); the land-surface physics in
[Soil Reanalysis Science](soil-reanalysis-science). References on this page have
Crossref-verified DOIs.
:::

## 1. Why a "soil reanalysis"?

Atmospheric science has *weather reanalysis* — a continuously updated, physically consistent
estimate of the state of the atmosphere that blends models with all available observations
(e.g. ERA5-Land [@munozsabater2021]). Geohazard prediction needs the analogous product for
the ground: a **soil reanalysis** that estimates the state of soils and shallow subsurface
water at the **space and time scales relevant to hazards and resource management** — tens of
meters and sub-daily, resolving the hillslope and the vadose-to-water-table column, not the
9–25 km surface layer that global products deliver.

The defining idea is to build a **holistic, multi-perspective state of the soil's
hydromechanics**, because two coupled subsystems jointly govern hazard susceptibility:

1. **Water partitioning** — how water infiltrates as soil moisture, drains to the
   groundwater table, and returns to the atmosphere through evaporation and capillary rise.
   This is the unsaturated-flow problem [@richards1931] closed by a soil-water retention
   curve [@vangenuchten1980].
2. **Mechanical state** — how water content and lithological structure control the elastic
   properties of a granular or fractured-rock model of the soil, and therefore its
   **cohesion and strength**. Increasing saturation lowers suction and effective stress
   [@lu2010], reducing the strength that resists slope failure and liquefaction.

No existing product delivers both, coupled, at hazard scale. That gap is what Pillar 1
fills, and it is what distinguishes a *soil reanalysis* from a *soil-moisture product*. The
mapping from observations to these state variables — turning time-lapse seismic velocity
into water-table depth and saturation — is developed in
[Soil Hydromechanical Memory](soil-memory).

## 2. State variables

The product estimates, in space and time, the variables that downstream hazard and
resource models use:

| Variable | Symbol | Used by |
|---|---|---|
| Vadose-zone saturation / soil moisture | $S_w(x,z,t)$ | landslide triggering, flood runoff, liquefaction |
| Water-table depth / hydraulic head | $d_{wt}(x,t)$, $h(x,t)$ | deep-seated landslides, groundwater resources |
| Effective stress / suction stress | $\sigma'(x,z,t)$ | slope stability, ground failure |
| Elastic moduli / stiffness | $G(x,z,t)$ | ground-motion site response, $dv/v$ forward model |
| Static soil & lithologic properties | texture, $K_{sat}$, depth-to-bedrock, $\phi$ | priors for all of the above |

These feed the [Hazards](hazard-landslides) pages and the resource-management work in
[Groundwater & Soil Moisture](groundwater-soil-moisture). Landscape-evolution and
debris-flow surrogates built on Landlab [@hobley2017; @barnhart2020], and the
ground-failure / liquefaction models in [ModelHub](modelhub), each require a specific subset
of these layers — defining that requirement list is a core DataHub task (§5).

## 3. Data to build the state of soils

The data are **multi-scale, multi-source, and span static to highly dynamic** in time. We
organize them into a small taxonomy, and require every layer to carry an explicit
**provenance statement**: *data source · sensor/measurement · resolution · uncertainty*.

### 3.1 Static soil & terrain properties
Type, texture, lithology, depth to bedrock, and topography. National-to-global digital
soil-mapping products provide priors: POLARIS at 30 m [@chaney2019], the USGS SOLUS100 soil
layers (100 m, used today in our debris-flow data prep — §5), SoilGrids globally
[@hengl2017; @poggio2021], and USDA SSURGO/gSSURGO. Topography comes from the USGS 10 m DEM.
These set the parameter priors ($\phi$, retention parameters, $K_{sat}$) for the physics, but
they are static and smooth meter-scale heterogeneity.

### 3.2 Water-related dynamic state
- **Past rainfall** — from regression of gauge records through to physics/AI rainfall models;
  the proximate trigger and the dominant control on antecedent wetness
  [@guzzetti2008]. Already staged through GAIA via PRISM and HRRR (see §5).
- **Groundwater table** — the saturated-zone boundary condition.
- **Soil moisture** — the vadose-zone state. Gridded estimates are available from
  reanalysis/regional models (e.g. CONUS404 `SMOIS`/`TSLB`, already pulled by
  [`gaia-data-downloaders`](https://github.com/gaia-hazlab/gaia-data-downloaders)), and
  `gaia-cli` already emits a standardized `soil_moisture` variable — but these inherit the
  coarse support and limitations of §3.3 and §4, which the reanalysis must reconcile against
  ground truth.

### 3.3 Two observational modalities (with honest limitations)

**Ground-based sensors** stream data at uneven cadence from very heterogeneous sources, but
[gaia-cli](research-software) and agentic download give us good access. These are our
**ground truth**, both climatological and hydrological:
- *Hydromet networks* — rain gauges, streamflow, in-situ soil-moisture and well/piezometer
  data (the kind aggregated by the International Soil Moisture Network [@dorigo2021]).
- *Geophysical networks* — a modality absent from every comparable product (§4):
  - **surface strain / kinematics** (GNSS, InSAR, tilt) — deformation of the ground;
  - **subsurface mechanical change** via time-lapse seismic velocity $dv/v$ (DAS and
    regional networks), which responds to pore pressure and saturation
    [@sensschonfelder2006; @clements2018; @mao2022];
  - **seismogenic signatures** — the seismic fingerprints of the hazards themselves
    (landslides, debris flows).

**Satellite imagery** offers good spatial but sparse temporal resolution, and is *so-so* for
soils. Several caveats must be handled explicitly:
- *Footprint leakage.* Agencies reprocess raw measurements into Level-2+ products, but a
  reprojected/retiled product inherits the **native measurement footprint** — a downscaled
  9 km soil-moisture pixel (e.g. SMAP L4 [@reichle2017], ESA CCI [@dorigo2017; @gruber2019])
  still has a 9–25 km support, and these artifacts leak into downstream products (e.g.
  hydrologic-framework regridding) unless explicitly tracked.
- *Regionalization of proxies.* Indices such as NDVI are not always appropriate in the
  Pacific Northwest because the proxy-to-state model (e.g. NDVI → soil moisture) is
  miscalibrated for this region.
- *Clouds and snow.* Optical imagery is cloud-contaminated (Sentinel de-clouding helps) and
  loses contrast over snow — limiting usefulness exactly when winter hazards peak.

## 4. State of the art — and the gap GAIA fills

Mature products exist for pieces of this problem, but none delivers a hazard-scale,
hydro-**mechanical** soil state.

| Product | Native resolution | What it provides | Limitation for PNW hazards |
|---|---|---|---|
| ERA5-Land [@munozsabater2021] | ~9 km, hourly | soil moisture/temp, snow, ET | too coarse for ridge–valley gradients; no land DA |
| GLDAS / NLDAS-2 [@rodell2004; @xia2012] | 12–25 km, sub-daily | multi-layer moisture, fluxes | orographic precip/snow smoothed |
| SMAP L4 [@reichle2017] | 9 km, 3-hourly | surface + root-zone moisture | EnKF on Catchment model; degraded under forest/snow |
| SMOS / ESA CCI [@kerr2010; @dorigo2017] | 25–50 km, daily | surface moisture | masked over forest, complex terrain, snow |
| NOAA NWM [@cosgrove2024] | 1 km land, hourly | streamflow, moisture, snow | sparse high-elevation gauging |
| ParFlow-CONUS / HydroFrame [@maxwell2015] | 1 km | 3D groundwater, water table | hillslope/perched water tables unresolved |
| SoilGrids / POLARIS [@poggio2021; @chaney2019] | 30–250 m, static | texture, $K_{sat}$, retention | static; uncertain on steep forested slopes |
| GRACE/-FO [@tapley2004] | >100 km, monthly | total water storage anomaly | far too coarse; regional context only |

**How GAIA differentiates** — Pillar 1 is designed to complement, not duplicate, these:

1. **Hydromechanical, not just hydrological.** We estimate effective stress, stiffness, and
   strength — the variables that actually govern failure — by coupling water and mechanics
   ([soil-memory](soil-memory)). Comparable products stop at moisture.
2. **Hazard-relevant resolution and depth.** Tens of meters, sub-daily, resolving the
   vadose-to-water-table column rather than a 0–5 cm surface layer.
3. **Geophysical in-situ constraint.** Dense seismic/DAS $dv/v$ and strain give direct
   subsurface state observations — a modality no listed product uses.
4. **Physically-informed fusion with explicit provenance.** We fuse sparse ground truth with
   satellite imagery (§3.3) and track per-layer footprint and uncertainty, rather than
   letting downscaling artifacts leak downstream.
5. **Operational and cloud-native.** Delivered through [DataHub](datahub)/gaia-cli as a
   continuously updated state, not a static climatology — feeding the
   [nowcast](pillar-2-nowcasting-susceptibility) and
   [forecast](pillar-3-forecasting-susceptibility) in real time.
6. **Targeted where global products are weakest** — the forested, snow-affected, steep PNW.

## 5. Homogenization and the GAIA DataHub

The scientific core of Pillar 1 is a **homogenization scheme** that fuses heterogeneous
ground sensors with satellite imagery into improved space–time fields of the soil's
hydromechanical state — proper interpolation and gap-filling regularized by physical models,
not statistical regridding (which propagates the footprint artifacts of §3.3).

GAIA already has the skeleton of a [DataHub](datahub) to build this on; Pillar 1's job is to
make the **soil state a first-class product** within it. The current architecture is a
convention with three layers:

- **Object store** — a shared `s3://cresst` bucket (anonymous read, authenticated write) is
  the de-facto hub, holding COG/Zarr/Parquet under `s3://cresst/{user}/`.
- **STAC catalogs** — per-dataset static STAC catalogs on GitHub make data discoverable and
  `odc.stac.load`-able into `xarray`:
  [`solus-stac`](https://github.com/gaia-hazlab/solus-stac) (SOLUS100 soil, 18 properties × 7
  depths, 100 m), [`prism-stac`](https://github.com/gaia-hazlab/prism-stac) /
  [`precip-stac`](https://github.com/gaia-hazlab/precip-stac) (precipitation), and
  [`landlab-stac`](https://github.com/gaia-hazlab/landlab-stac) (derived 10 m soil + terrain +
  geotech model inputs).
- **Staging & discovery** — [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli)
  (`gaia stage prism|hrrr|synoptic|all -i AOI -s START -e END -o ZARR`) clips, harmonizes, and
  writes a Zarr `DataTree`; the [`catalog`](datahub) web map is the human-facing index.

**The gap Pillar 1 closes.** Today gaia-cli and the STAC catalogs mostly cover
precipitation/meteorology, while the *soil layers the hazard models actually use are still
produced by ad-hoc pipelines and only retroactively cataloged, or not at all.* The same
SOLUS100 layers appear twice — as hardcoded GCS URLs inside
[`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml) /
[`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) (which also commit
personal absolute paths like `/mnt/c/Users/.../Downloads/...`) and as a structured catalog in
`solus-stac` — with no shared mechanism. Two soil vocabularies run in parallel (SOLUS100 at
100 m vs POLARIS at 30 m in
[`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin)), and the
[liquefaction & ground-failure](hazard-liquefaction-ground-failure) work in
[`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) has no soil
inputs wired yet. The Soil Reanalysis Product is precisely the layer that closes this gap.

**Recommended DataHub work (steered by this use case):**
- Promote the soil state to a **first-class STAC product on `s3://cresst`**, following the
  solus-stac/landlab-stac pattern, with per-layer provenance — *source · measurement ·
  resolution · uncertainty*.
- Extend `gaia-cli` with a **soil-state staging path** (static SOLUS/POLARIS priors + dynamic
  CONUS404 `SMOIS`/`TSLB` + the seismic-derived $S_w$/$d_{wt}$ of [soil-memory](soil-memory))
  alongside the existing precip stages.
- **Reconcile** the SOLUS100 vs POLARIS vocabularies and map them to the Landlab `soil__*`
  variable names the models expect.
- **Migrate** the ad-hoc data-prep repos onto this pattern and codify per-hazard variable
  requirement lists.

The concrete, repo-by-repo migration steps and the "DataHub-ready" checklist live in the
**[DataHub Integration Guide](datahub-integration-guide)** — the guide the data-prep
repositories can improve from.

## 6. Evaluation & metrics

Pillar 1 outputs are validated against the ground-truth networks of §3.3 — see
[HazEvalHub](hazevalhub):
- **State accuracy** — RMSE/bias of $S_w$ and $d_{wt}$ against in-situ soil-moisture sensors,
  wells, and ET products;
- **Dynamics** — temporal correlation and lag of the storm response;
- **Physical consistency** — hydrostatic and mass-balance checks across the fused field;
- **Footprint honesty** — propagated, not hidden, uncertainty from satellite support scales.

## 7. Open questions & roadmap

- The data-assimilation scheme that blends $dv/v$, rainfall, and remote sensing into a single
  consistent state (the analog of atmospheric DA, which most listed products lack for land).
- Spatial upscaling from dense DAS cross-sections to regional reanalysis grids.
- Calibrating rock-physics closures ([@dvorkin1996]; see [soil-memory](soil-memory)) and
  retention parameters [@vangenuchten1980] from sparse PNW boreholes.
- Defining the per-hazard soil-property requirement lists with the Landlab and ground-failure
  modeling groups.

## References
