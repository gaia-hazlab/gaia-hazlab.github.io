#!/usr/bin/env python3
"""GNSS multi-use site collector for the GAIA Data Catalog (STUB).

One row per GNSS site over the Alaska AOIs, tagged by the use-cases it supports:
  - strain          : daily positions/velocities (EarthScope GAGE, Nevada Geodetic Lab)
  - reflectometry   : GNSS-IR (snow/soil-moisture/water level) via gnssrefl; needs SNR RINEX
  - tec_pwv         : ionospheric TEC (dual-freq) + tropospheric ZTD->PWV (high-rate + met)

See project_coordination/06-data-catalog.md sec 2.3.

Implementation plan (Y1):
  - EarthScope GAGE station metadata API (or the Nevada Geodetic Lab site list) for
    positions/coords/receiver/antenna and data span.
  - Cross-reference gnssrefl's station lists for reflectometry-capable sites.
  - Flag high-rate (1 Hz+) and met-equipped sites for tec_pwv.
  - Emit uses[] as the subset of {strain, reflectometry, tec_pwv} each site supports.

Run:  python scripts/catalog/collect_gnss.py --out data/catalog/gnss_sites.csv
"""
from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

FIELDS = ["id", "modality", "provider", "site", "lat", "lon", "height",
          "receiver", "antenna", "sample_rate", "uses", "rinex_available",
          "data_start", "data_end", "source_url", "last_seen_utc"]


def collect(aoi_path: Path, generated_utc: str) -> list[dict]:
    # TODO: implement against EarthScope GAGE / Nevada Geodetic Lab (see docstring).
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="data/catalog/gnss_sites.csv")
    ap.add_argument("--aois", default="scripts/catalog/aois.geojson")
    ap.add_argument("--utc", default=os.environ.get("CATALOG_UTC", "1970-01-01T00:00:00Z"))
    args = ap.parse_args()

    records = collect(Path(args.aois), args.utc)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        w.writeheader()
        for rec in records:
            w.writerow(rec)
    print(f"Wrote {out}: {len(records)} GNSS sites (stub — implement with EarthScope/NGL)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
