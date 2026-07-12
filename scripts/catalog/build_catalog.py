#!/usr/bin/env python3
"""Merge the GAIA Data Catalog CSVs into dashboard inputs.

Reads data/catalog/{seismic_stations,sar_tracks,gnss_sites}.csv and writes:
  - data/catalog/catalog.geojson  (points for stations/sites; tracks added when ASF lands)
  - data/catalog/summary.json     (counts for the dashboard's Data Catalog tab)

See project_coordination/06-data-catalog.md sec 5 for the summary.json contract.
Missing/empty inputs are treated as zero — the dashboard shows "not yet collected".

Run:  python scripts/catalog/build_catalog.py
"""
from __future__ import annotations

import argparse
import csv
import json
import os
from pathlib import Path


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def _aoi_count(aoi_path: Path) -> int:
    if not aoi_path.exists():
        return 0
    try:
        return len(json.loads(aoi_path.read_text()).get("features", []))
    except (ValueError, KeyError):
        return 0


def build(catalog_dir: Path, generated_utc: str, aoi_path: Path) -> tuple[dict, dict]:
    seismic = _read(catalog_dir / "seismic_stations.csv")
    sar = _read(catalog_dir / "sar_tracks.csv")
    gnss = _read(catalog_dir / "gnss_sites.csv")
    n_aois = _aoi_count(aoi_path)

    features = []
    for s in seismic:
        try:
            features.append({
                "type": "Feature",
                "properties": {"id": s["id"], "modality": "seismic",
                               "sensor_types": s.get("sensor_types", ""),
                               "has_infrasound": s.get("has_infrasound", "")},
                "geometry": {"type": "Point", "coordinates": [float(s["lon"]), float(s["lat"])]},
            })
        except (KeyError, ValueError):
            continue
    for g in gnss:
        try:
            features.append({
                "type": "Feature",
                "properties": {"id": g["id"], "modality": "gnss", "uses": g.get("uses", "")},
                "geometry": {"type": "Point", "coordinates": [float(g["lon"]), float(g["lat"])]},
            })
        except (KeyError, ValueError):
            continue
    # SAR tracks (polygons) are appended once collect_asf.py provides geometry.

    geojson = {"type": "FeatureCollection", "generated_utc": generated_utc, "features": features}

    def _count_use(rows, use):
        return sum(1 for r in rows if use in (r.get("uses", "")))

    summary = {
        "generated_utc": generated_utc,
        "sar": {"tracks": len(sar),
                "asc": sum(1 for r in sar if r.get("flight_direction", "").upper().startswith("ASC")),
                "desc": sum(1 for r in sar if r.get("flight_direction", "").upper().startswith("DESC")),
                "aois": n_aois,
                "acquisitions": sum(int(r.get("n_acquisitions", 0) or 0) for r in sar)},
        "seismic": {"stations": len(seismic),
                    "with_infrasound": sum(1 for r in seismic if str(r.get("has_infrasound", "")).lower() in ("true", "1")),
                    "networks": sorted({r.get("net", "") for r in seismic if r.get("net")})},
        "gnss": {"sites": len(gnss),
                 "strain": _count_use(gnss, "strain"),
                 "reflectometry": _count_use(gnss, "reflectometry"),
                 "tec_pwv": _count_use(gnss, "tec_pwv")},
    }
    return geojson, summary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", default="data/catalog")
    ap.add_argument("--aois", default="scripts/catalog/aois.geojson")
    ap.add_argument("--utc", default=os.environ.get("CATALOG_UTC", "1970-01-01T00:00:00Z"))
    args = ap.parse_args()

    d = Path(args.dir)
    d.mkdir(parents=True, exist_ok=True)
    geojson, summary = build(d, args.utc, Path(args.aois))
    (d / "catalog.geojson").write_text(json.dumps(geojson) + "\n")
    (d / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(f"Catalog: {summary['seismic']['stations']} seismic, "
          f"{summary['gnss']['sites']} gnss, {summary['sar']['tracks']} sar tracks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
