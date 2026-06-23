# DataHub Integration Guide

:::{note}
**A guide for GAIA repositories to improve from.** This page turns the
[Soil Reanalysis Product](pillar-1-soil-reanalysis) requirements into concrete, repo-by-repo
steps for aligning data preparation with the GAIA [DataHub](datahub). It documents the
*current* architecture (as it exists in the code today) and a migration path. It is meant to
be actionable by maintainers of the data-prep repositories.
:::

## 1. The target architecture (what already exists)

There is no monolithic "DataHub" service — the DataHub is a **convention** with three layers
that already exist in the org and should be the common target for all data work:

```
provider ──► STAC catalog (GitHub, static JSON) ──► COG/Zarr assets (s3://cresst, GCS)
                                                          │
                                  gaia-cli stage ─────────┘──► harmonized Zarr DataTree
                                                                    │
                                                          catalog web map + downstream models
```

| Layer | Implementation today | Repos |
|---|---|---|
| **Object store** | `s3://cresst` (us-west-2): anonymous read, authenticated write via `obstore` (`AWS_PROFILE=cresst-user`), layout `s3://cresst/{user}/`, formats **Zarr / COG / Parquet**. SOLUS lives in public GCS `solus100pub`. | documented in [`gaia-data-downloaders`](https://github.com/gaia-hazlab/gaia-data-downloaders) `agents_docs/aws_s3_integration.md` |
| **STAC catalogs** | Per-dataset **static** STAC (`stac_version 1.1.0`), built with `rio-stac`/`pystac`, consumed with `odc.stac.load(...)`. | [`solus-stac`](https://github.com/gaia-hazlab/solus-stac), [`prism-stac`](https://github.com/gaia-hazlab/prism-stac), [`landlab-stac`](https://github.com/gaia-hazlab/landlab-stac), [`precip-stac`](https://github.com/gaia-hazlab/precip-stac) (WIP) |
| **Staging** | [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli): `gaia stage prism\|hrrr\|synoptic\|all -i AOI -s START -e END -o ZARR`; harmonizes to an `xarray.DataTree` (`stations/…`, `rasters/…`) with standardized variable names/units/CRS; writes Zarr. | `gaia-cli` |
| **Discovery** | [`catalog`](https://github.com/gaia-hazlab/catalog) Leaflet web map (published at [gaia-hazlab.github.io/catalog](https://gaia-hazlab.github.io/catalog)). | `catalog` |

**Conventions to adopt everywhere:**
- **Storage:** write cloud-native **COG** (rasters) or **Zarr v3** (cubes) to `s3://cresst/{user}/…`; never commit data or personal absolute paths to git.
- **CRS & grid:** declare the CRS explicitly (SOLUS native is EPSG:5070; event Landlab stacks use a local UTM, e.g. EPSG:32610; gaia-cli harmonizes rasters to EPSG:4326). Co-register event layers to a single DEM grid.
- **Naming:** use the Landlab double-underscore field names for model-ready layers (e.g. `soil__saturated_hydraulic_conductivity`, `clay__total`) so they drop straight into Landlab components.
- **Depth:** index static soil layers by depth (SOLUS: `0, 5, 15, 30, 60, 100, 150 cm`) rather than flattening to one surface value.

## 2. The provenance standard

Every layer the DataHub serves must carry a four-part provenance statement, expressed as STAC
properties so it travels with the data:

| Provenance field | Where it goes in STAC | Example |
|---|---|---|
| **Source** | `providers`, custom namespace (e.g. `prism:`) | USDA SOLUS100; PRISM Climate Group |
| **Measurement / sensor** | asset `description`, `eo`/instrument fields | "L-band radiometer brightness temperature"; "100 m ML soil estimate" |
| **Resolution** | `proj:shape`, `proj:transform`, `gsd` | 100 m; 0.1° (~9 km) |
| **Uncertainty** | per-asset stats / extra fields (low/high estimate, p5/p95) | SOLUS `l`/`h` estimate bands; POLARIS p5/p95 |

This is the rule that prevents the **footprint-leakage** problem described in
[Pillar 1 §3.3](pillar-1-soil-reanalysis): a downscaled 9 km pixel must keep its 9 km support
recorded, so downstream models can weight it honestly.

## 3. Migration recipe for an ad-hoc data-prep repo

The pattern below converts a repo like
[`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml) or
[`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) (today: hardcoded
`/mnt/c/Users/.../Downloads/...` paths, one-off SOLUS GCS URLs, local `.asc` outputs) into a
DataHub-aligned module.

1. **De-personalize the config.** Replace absolute local paths with an AOI + run config; keep
   a sanitized `config/base.example.yaml` as the committed template (the
   `base.example.yaml` pattern already used in `fire-debrisflow-ml`). No data, no
   `~/Downloads`, no `/mnt/c` in git.
2. **Consume STAC instead of hardcoded URLs.** Replace the per-property SOLUS GCS URLs with a
   `solus-stac` read:
   ```python
   import pystac, odc.stac
   cat = pystac.Catalog.from_file(
       "https://raw.githubusercontent.com/gaia-hazlab/solus-stac/main/stac/catalog.json")
   ds = odc.stac.load(items, bands=["claytotal", "sandtotal", "dbovendry"], resolution=10)
   ```
   Same for precipitation via `prism-stac` / `gaia-cli stage prism`.
3. **Stage forcing through gaia-cli.** Replace bespoke PRISM/HRRR/Synoptic downloaders with
   `gaia stage … -i AOI -s START -e END -o s3://cresst/{user}/…`, inheriting the standardized
   variable names and units.
4. **Publish derived event layers as a STAC collection.** When the repo produces a co-registered
   event stack (the 22-layer eagle-creek set is the worked example), write the COGs to
   `s3://cresst/{user}/{event}/` and emit a STAC collection exactly like `landlab-stac`. Tag
   COGs as COG (the current `landlab-stac` assets are plain GeoTIFF — fix that).
5. **Attach provenance + resolution + uncertainty** (§2) to every asset.
6. **Codify the model's input contract** (§4) so the catalog can validate that an event stack
   is complete before a model run.

## 4. Per-hazard variable requirement lists

Codify, per model, exactly which layers the reanalysis must deliver. Two are already legible
from the code:

**Landlab `LandslideProbability`** (from `landlab-debrisflow` / `landlab-stac`):
`topographic__elevation`, `soil__thickness`, `soil__density`,
`soil__internal_friction_angle`, `soil__saturated_hydraulic_conductivity`, `porosity`,
`field__capacity`, `wilting__point`, `soil__{min,mode,max}_total_cohesion`,
`vegetation__plant_functional_type` + daily PRISM forcing (`ppt`, `tmin`, `tmax`). The
**`burn__severity`** layer is required **only for the post-fire debris-flow** variant; the core
shallow/deep landslide susceptibility omits it.

**Liquefaction & ground failure** ([`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure),
[hazard page](hazard-liquefaction-ground-failure)): currently only seismic waveforms are
wired; it still needs water-table depth ($d_{wt}$), saturation ($S_w$), $V_{s}$ profiles, and
geotech indices — i.e. the Soil Reanalysis Product outputs. This is a concrete first consumer.

Mapping the **SOLUS100** (static, 100 m) and **POLARIS** (30 m, used by
[`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin)) vocabularies
onto these Landlab field names — and adding the **dynamic** CONUS404 `SMOIS`/`TSLB` and
seismic-derived states — is the unifying task of [Pillar 1](pillar-1-soil-reanalysis).

## 5. Repo-by-repo action items

| Repo | Status | Recommended action |
|---|---|---|
| [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) | precip/met staging; emits `soil_moisture` | Add a **soil-state stage** (SOLUS/POLARIS priors + CONUS404 dynamic + seismic states); move "recipes" from hardcoded constants to a declarative config |
| [`solus-stac`](https://github.com/gaia-hazlab/solus-stac) | solid SOLUS catalog | Add explicit **uncertainty** assets (`l`/`h` bands) and `raster:` stats; reference from gaia-cli |
| [`prism-stac`](https://github.com/gaia-hazlab/prism-stac) | working | Keep as the precipitation reference; ensure `tmean`/`ppt` both COG |
| [`precip-stac`](https://github.com/gaia-hazlab/precip-stac) | WIP, no STAC JSON yet | Finish the `multiband → per-day COG → STAC` build; publish assets to `cresst` |
| [`landlab-stac`](https://github.com/gaia-hazlab/landlab-stac) | 1 event, plain GeoTIFF | Tag assets as **COG**; add provenance; generalize beyond `eagle-creek` |
| [`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml) | ad-hoc, hardcoded paths | Apply §3; **consider renaming** to reflect its role (e.g. `gaia-dataprep-landslide`); consume `solus-stac`; publish outputs as STAC |
| [`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) | hardcoded `/mnt/c` paths | Apply §3; de-personalize `config/mmp_landslide.yaml`; source inputs from STAC |
| [`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin) | cloud-native, STAC disabled | **Enable STAC** (`io.stac.enabled: true`); align POLARIS layers with the soil vocabulary |
| [`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) | seismic only | Wire the soil-state inputs (§4) as its first consumer of the reanalysis |
| [`catalog`](https://github.com/gaia-hazlab/catalog) | reads raw COGs, ignores STAC | Make it **consume the STAC catalogs** (its own "merged inventory (maybe STAC)" TODO) |
| [`gaia-data-downloaders`](https://github.com/gaia-hazlab/gaia-data-downloaders) | broad downloads, no STAC | Fold the useful sources (CONUS404 `SMOIS`/`TSLB`) into gaia-cli stages |
| [`awesome-gaia`](https://github.com/gaia-hazlab/awesome-gaia) | empty placeholder | Populate as the **curated index** of these repos, grouped by DataHub / ModelHub / hazard |

## 6. "DataHub-ready" checklist

A data-prep step is DataHub-ready when:

- [ ] No data files or personal absolute paths are committed to git.
- [ ] Inputs are read from a STAC catalog (or gaia-cli stage), not hardcoded URLs.
- [ ] Outputs are cloud-native (COG/Zarr) on `s3://cresst/{user}/…`.
- [ ] Every layer carries source · measurement · resolution · uncertainty (§2).
- [ ] CRS, grid, and depth indexing are declared explicitly.
- [ ] Model-ready layers use the agreed Landlab `field__name` vocabulary.
- [ ] The model's input contract (§4) is documented and validated before a run.
- [ ] A sanitized `*.example.yaml` config is the committed template.

## Related

- [DataHub](datahub) — the platform overview and catalog web map.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) — the science driving these requirements.
- `DOCS_ROADMAP.md` — phased plan and owners.
