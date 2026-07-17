#!/usr/bin/env python3
"""FDSN seismic + infrasound station collector for the GAIA Data Catalog.

Queries the EarthScope FDSN station service (level=channel) over the Alaska AOIs and
writes one row per station, tagging infrasound where pressure channels (?DF) are present.
Public metadata — no token required. See project_coordination/06-data-catalog.md.

Run:  python scripts/catalog/collect_fdsn.py --out data/catalog/seismic_stations.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    requests = None

# EarthScope FDSN station service (text output, level=channel).
FDSN_STATION = "https://service.iris.edu/fdsnws/station/1/query"
INFRASOUND_CODES = ("DF",)  # channel band+instrument suffix, e.g. BDF/HDF/LDF (pressure)


def _aoi_bboxes(aoi_path: Path) -> list[dict]:
    """Return [{id, minlat, maxlat, minlon, maxlon}] from the shared AOI GeoJSON."""
    fc = json.loads(aoi_path.read_text())
    out = []
    for feat in fc.get("features", []):
        coords = feat["geometry"]["coordinates"][0]
        lons = [c[0] for c in coords]
        lats = [c[1] for c in coords]
        out.append({
            "id": feat["properties"].get("id", "aoi"),
            "minlat": min(lats), "maxlat": max(lats),
            "minlon": min(lons), "maxlon": max(lons),
        })
    return out


def _query_aoi(box: dict) -> list[list[str]]:
    """Query one bbox; return raw channel rows (pipe-delimited text)."""
    params = {
        "level": "channel",
        "format": "text",
        "minlatitude": box["minlat"], "maxlatitude": box["maxlat"],
        "minlongitude": box["minlon"], "maxlongitude": box["maxlon"],
        "includerestricted": "true",
        "nodata": "404",
    }
    r = requests.get(FDSN_STATION, params=params, timeout=60)
    if r.status_code != 200:
        print(f"[warn] fdsn {box['id']}: HTTP {r.status_code}", file=sys.stderr)
        return []
    rows = []
    for line in r.text.splitlines():
        if not line or line.startswith("#"):
            continue
        rows.append([c.strip() for c in line.split("|")])
    return rows


def collect(aoi_path: Path, generated_utc: str) -> list[dict]:
    """Aggregate channel rows into one record per (net, sta)."""
    if requests is None:
        print("[warn] requests not installed; emitting empty catalog", file=sys.stderr)
        return []
    stations: dict[tuple, dict] = {}
    for box in _aoi_bboxes(aoi_path):
        for row in _query_aoi(box):
            # text channel columns: Net|Sta|Loc|Chan|Lat|Lon|Elev|Depth|Az|Dip|SensorDesc|Scale|...|Start|End
            if len(row) < 16:
                continue
            net, sta, _loc, chan = row[0], row[1], row[2], row[3]
            key = (net, sta)
            rec = stations.setdefault(key, {
                "id": f"{net}.{sta}", "modality": "seismic", "provider": "FDSN/EarthScope",
                "net": net, "sta": sta, "lat": row[4], "lon": row[5], "elev": row[6],
                "channels": set(), "sensor_types": set(),
                "t_start": row[15], "t_end": row[16] if len(row) > 16 else "",
                # The level=channel text format has no restriction column, so we cannot
                # determine open/restricted here. Leave "unknown" rather than assert False;
                # enrich via fdsnws-station StationXML (restrictedStatus) when needed.
                "restricted": "unknown", "aoi": box["id"], "source_url": FDSN_STATION,
                "last_seen_utc": generated_utc,
            })
            rec["channels"].add(chan)
            rec["sensor_types"].add("infrasound" if chan[-2:] in INFRASOUND_CODES else "seismic")
    return [
        {**r, "channels": ";".join(sorted(r["channels"])),
         "sensor_types": ";".join(sorted(r["sensor_types"])),
         "has_infrasound": "infrasound" in r["sensor_types"]}
        for r in stations.values()
    ]


FIELDS = ["id", "modality", "provider", "net", "sta", "lat", "lon", "elev",
          "channels", "sensor_types", "has_infrasound", "t_start", "t_end",
          "restricted", "aoi", "source_url", "last_seen_utc"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="data/catalog/seismic_stations.csv")
    ap.add_argument("--aois", default="scripts/catalog/aois.geojson")
    ap.add_argument("--utc", default=os.environ.get("CATALOG_UTC", "1970-01-01T00:00:00Z"))
    args = ap.parse_args()

    records = collect(Path(args.aois), args.utc)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for rec in sorted(records, key=lambda r: r["id"]):
            w.writerow(rec)
    n_infra = sum(1 for r in records if r.get("has_infrasound"))
    print(f"Wrote {out}: {len(records)} stations ({n_infra} with infrasound)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
