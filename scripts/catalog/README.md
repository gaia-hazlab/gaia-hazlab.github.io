# GAIA Data Catalog collectors

Auto-refreshed observational inventory for the Alaska + geodesy + SAR expansion.
Specified in [`../../project_coordination/06-data-catalog.md`](../../project_coordination/06-data-catalog.md).

Each collector queries a public metadata service and writes a CSV to `data/catalog/`;
`build_catalog.py` merges them into `catalog.geojson` + `summary.json` for the dashboard.
All degrade gracefully — one source being down never fails the run.

| Script | Source | Output | Status |
|---|---|---|---|
| `collect_fdsn.py` | FDSN station service (EarthScope) | `data/catalog/seismic_stations.csv` | working scaffold |
| `collect_asf.py` | ASF Search API (`asf_search`) | `data/catalog/sar_tracks.csv` | stub (needs AOIs + asf_search) |
| `collect_gnss.py` | EarthScope GAGE + Nevada Geodetic Lab | `data/catalog/gnss_sites.csv` | stub |
| `build_catalog.py` | merges the CSVs | `catalog.geojson`, `summary.json` | stub |

- **AOIs** shared by ASF + FDSN queries live in `aois.geojson` (start with 2–3 Alaska
  subregions; expand as science targets firm up).
- SAR is indexed by **track (relative orbit)**, not frame-date — see doc 06 §2.1.
- Scheduled by a catalog GitHub Action (mirror `metrics-observatory.yml`, gated off).

## Run locally

```bash
pip install requests
python scripts/catalog/collect_fdsn.py --out data/catalog/seismic_stations.csv
```
