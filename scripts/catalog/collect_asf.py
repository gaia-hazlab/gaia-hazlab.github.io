#!/usr/bin/env python3
"""ASF SAR track collector for the GAIA Data Catalog (STUB).

Indexes Sentinel-1 (and later NISAR) by TRACK (relative orbit) over the Alaska AOIs,
not by frame-date — see project_coordination/06-data-catalog.md sec 2.1. Emits one row
per (track, flight_direction) with the frames covering each AOI, temporal span, and
acquisition count. Retrieval of individual InSAR products is deferred to on-demand
ASF HyP3 queries.

Implementation plan (Y1):
  pip install asf_search
  import asf_search as asf
  for aoi in aois:
      results = asf.geo_search(platform=asf.PLATFORM.SENTINEL1, intersectsWith=aoi_wkt,
                               processingLevel='SLC')
      group results by (result.properties['pathNumber'], flightDirection)
      -> track, flight_direction, frames[], aoi[], t_start, t_end, n_acquisitions

Run:  python scripts/catalog/collect_asf.py --out data/catalog/sar_tracks.csv
"""
from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

FIELDS = ["id", "modality", "provider", "track", "flight_direction", "frames",
          "aoi", "beam_mode", "t_start", "t_end", "n_acquisitions",
          "hyp3_ready", "source_url", "last_seen_utc"]


def collect(aoi_path: Path, generated_utc: str) -> list[dict]:
    # TODO: implement with asf_search (see module docstring). Returns [] until then so
    # build_catalog.py and the dashboard handle "not yet collected" gracefully.
    return []


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="data/catalog/sar_tracks.csv")
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
    print(f"Wrote {out}: {len(records)} SAR tracks (stub — implement with asf_search)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
