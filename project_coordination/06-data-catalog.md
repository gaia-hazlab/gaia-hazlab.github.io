# Alaska Data Catalog

> The observational inventory that underpins the Alaska + geodesy + SAR expansion. A
> **machine-readable, auto-refreshed catalog** of the SAR, seismic/infrasound, and GNSS
> assets GAIA will use — designed to *feed the dashboard* and the DataHub pages, not to
> live in a spreadsheet. Partner: **Alaska Satellite Facility (ASF)** for SAR;
> **EarthScope / FDSN** for seismic, infrasound, and GNSS.
>
> **Principle:** the catalog is a **git-tracked data artifact** (CSV + GeoJSON in
> `data/catalog/`), refreshed by scheduled collectors, and rendered on the dashboard.
> Humans may curate a *wishlist* in a Google Sheet, but the canonical, dashboard-feeding
> catalog is in the repo ([01 §5](01-project-coordination.md) on the Sheet↔repo split).

## 1. Why a catalog (and why it's tricky)

Each modality is indexed differently, so a naive "one row per file" catalog explodes:

- **SAR (ASF)** is **frame- and date-based** — every acquisition is a (path/track, frame,
  date) tuple; enumerating them is millions of rows. **Solution:** index by **track
  (relative orbit)**, not by frame-date. A track row carries its geometry, the frames
  that cover our Alaska AOIs, orbit direction, temporal span, and acquisition *count* —
  and defers per-frame-date retrieval to on-demand ASF/HyP3 queries. "The tracks provide
  the information."
- **Seismic + infrasound (FDSN)** is **station/channel-based** — stable, enumerable.
  One row per station (with channel groups), from the FDSN station service.
- **GNSS** is **site-based but multi-use** — the same site serves strain, reflectometry,
  and TEC/PWV depending on data rate and processing. One row per site, tagged by the
  use-cases it supports.

## 2. Scope (what goes in)

### 2.1 SAR — via ASF
- **Missions:** Sentinel-1 (A/C) now; **NISAR** when available; ALOS-2/PALSAR where relevant.
- **Index unit:** relative orbit / **track**, ascending & descending, over defined Alaska
  **AOIs** (e.g. subduction margin, interior permafrost, glaciated terrain, urban
  Anchorage/Fairbanks).
- **Per-track fields:** `track`, `flight_direction`, `frames[]`, `aoi[]`, `t_start`,
  `t_end`, `n_acquisitions`, `beam_mode`, `asf_vertex_url`, `hyp3_ready` (bool).
- **Products (downstream, DataHub):** InSAR pairs/time-series via **ASF HyP3** and MintPy;
  deformation/velocity as Zarr. Not enumerated in the catalog — generated on demand.

### 2.2 Seismic & infrasound — via EarthScope / FDSN
- **Networks (Alaska):** AK (Alaska Regional), AV (Alaska Volcano Observatory), AT, TA
  (Transportable Array remnants), US, II/IU (global backbone), plus active temporary
  deployments. Confirm the live list from the FDSN station service, don't hard-code.
- **Infrasound** rides the same stations as pressure channels — select by channel code
  (`?DF`: `BDF`/`HDF`/`LDF`). Tag rows `has_infrasound=true` when present.
- **Per-station fields:** `net`, `sta`, `lat`, `lon`, `elev`, `channels[]`,
  `sensor_types` (seismic / infrasound), `start`, `end`, `restricted` (bool),
  `data_availability` (from fdsnws-availability where offered).

### 2.3 GNSS — via EarthScope (GAGE), Nevada Geodetic Lab, gnssrefl
- **Uses (tag columns), the three the PI called out:**
  - `strain` — daily positions / velocities for crustal strain & seismogeodesy
    (EarthScope GAGE, Nevada Geodetic Lab time series).
  - `reflectometry` — GNSS-IR (snow depth, soil moisture, water level) via **gnssrefl**;
    needs sites with usable SNR RINEX and good reflection geometry.
  - `tec_pwv` — ionospheric **TEC** (dual-frequency) and tropospheric **ZTD → PWV**
    (precipitable water) from high-rate + met-equipped sites.
- **Per-site fields:** `site`, `lat`, `lon`, `height`, `receiver`, `antenna`,
  `sample_rate` (daily / 1 Hz / high-rate), `data_start`, `data_end`, `provider`,
  `uses[]` (subset of {strain, reflectometry, tec_pwv}), `rinex_available` (bool).

## 3. Catalog schema (the contract)

Canonical files in `data/catalog/`, one per modality, plus a rollup:

```
data/catalog/
  sar_tracks.csv          # one row per ASF track over an AOI
  seismic_stations.csv    # one row per FDSN station (seismic + infrasound)
  gnss_sites.csv          # one row per GNSS site, multi-use tagged
  catalog.geojson         # all of the above as map features (tracks=polygons, stations/sites=points)
  summary.json            # counts + coverage for the dashboard (see §5)
```

Shared columns across every row so the map/dashboard can treat them uniformly:
`id, modality, provider, lat, lon, geometry_ref, t_start, t_end, tags[], source_url,
last_seen_utc`. Modality-specific columns extend these (§2).

## 4. Collectors (auto-refresh)

One collector per source, in [`../scripts/catalog/`](../scripts/catalog/), scheduled by a
catalog Action (mirrors the Metrics Observatory pattern — commit-if-changed). All degrade
gracefully so one source being down never fails the run.

| Collector | Source / API | Emits |
|---|---|---|
| `collect_fdsn.py` | `fdsnws-station` (level=channel) + `fdsnws-availability`, EarthScope | `seismic_stations.csv` (seismic + infrasound) |
| `collect_asf.py` | ASF Search API / `asf_search` (grouped by relativeOrbit over AOIs) | `sar_tracks.csv` |
| `collect_gnss.py` | EarthScope GAGE metadata + Nevada Geodetic Lab site list; gnssrefl station lists | `gnss_sites.csv` |
| `build_catalog.py` | merges the three → `catalog.geojson` + `summary.json` | dashboard inputs |

**Auth:** FDSN and ASF search are public (no token for metadata); restricted seismic data
is flagged, not fetched. Keep any ASF/EarthScope tokens in GitHub Secrets if used for
availability at scale.

**AOIs:** defined once in `scripts/catalog/aois.geojson` (Alaska subregions) so ASF and
FDSN queries share the same footprints. Start with 2–3 AOIs; expand as science targets firm up.

## 5. Dashboard integration

The catalog gets its **own panel/tab** on [`../dashboard.html`](../dashboard.html),
alongside the impact metrics ([04 §6](04-metrics-observatory.md)). It reads
`data/catalog/summary.json` + `catalog.geojson` — static, GitHub-Pages friendly, no backend.

`summary.json` shape:

```json
{
  "generated_utc": "2026-07-11T06:00:00Z",
  "sar":     { "tracks": 0, "asc": 0, "desc": 0, "aois": 3, "acquisitions": 0 },
  "seismic": { "stations": 0, "with_infrasound": 0, "networks": [] },
  "gnss":    { "sites": 0, "strain": 0, "reflectometry": 0, "tec_pwv": 0 }
}
```

Dashboard panel:
- **Map** — SAR tracks as polygons (asc/desc styled), seismic/infrasound stations as
  points (icon by sensor type), GNSS sites colored by use (strain/reflectometry/TEC-PWV).
- **Counts** — the `summary.json` tiles, with coverage over AOIs.
- **Freshness** — `last_seen_utc` so stale sources are visible.
- Follow the **dataviz** conventions (accessible categorical palette, light/dark).

## 6. DataHub page

`book/chapters/datahub-geodesy-sar-inventory.md` ([02 §3.1](02-website-evolution.md))
documents the catalog for humans: the AOIs, the track-vs-frame decision, the FDSN
networks, the GNSS multi-use tagging, and how to regenerate on-demand SAR products via
HyP3. It embeds/links the live `summary.json` counts.

## 7. Phasing

| When | Milestone |
|---|---|
| Y1 Q1 | Define AOIs; `collect_fdsn.py` produces `seismic_stations.csv` (seismic + infrasound); dashboard catalog tab stub. |
| Y1 | ASF track collector over AOIs; GNSS site collector with use-tags; `catalog.geojson` + map live. |
| Y2 | On-demand HyP3 InSAR products linked from tracks; availability enrichment; NISAR-ready fields. |
| Y3 | Catalog drives HazEvalHub tasks (InSAR deformation, GNSS-IR); coverage gaps → targeted requests to ASF/EarthScope. |

## 8. Guardrails

- Catalog **metadata** lives in git; **bulk data** never does (ASF/EarthScope/Zenodo hold it).
- Index SAR by **track**, not frame-date — keep the catalog small and queryable.
- Don't hard-code station/network lists — **query FDSN** and record `last_seen_utc`.
- The Google Sheet (if used) is a *wishlist/curation* surface only; the repo is canonical.
