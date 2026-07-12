#!/usr/bin/env python3
"""GAIA Metrics Observatory collector (kickoff scaffold).

Writes data/metrics/latest.json following the contract in
project_coordination/04-metrics-observatory.md, and appends a dated snapshot to
data/metrics/history/. Starts GitHub-only; add Zenodo/HF/Google collectors as tokens
land (see the collector table in doc 04).

Design: each source is an independent function that returns a dict of metrics and
degrades gracefully (returns partial/empty on auth or network failure) so the weekly
Action never hard-fails just because one API is down or a token is missing.

Run:  python scripts/metrics/collect.py --out data/metrics/latest.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:  # keep the script importable without deps for --help
    requests = None

GITHUB_ORG = "gaia-hazlab"
API = "https://api.github.com"

# Year 1 targets from doc 04 (Delivery Table 1 / Usage Table 2). Update per project year.
TARGETS_Y1 = {
    "D1_ci_templates": 3,
    "D2_containers": 3,
    "D3_datasets": 5,
    "D4_model_cards": 1,
    "M2_pulls_downloads": 500,
    "M2_derived_agents": 2,
    "M3_unique_institutions": 20,
    "M4_modalities_median": ">2",
}


def _gh_headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN", "")
    h = {"Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def collect_github() -> dict:
    """D1 (CI-template repos passing tests) from GitHub.

    Counts `gaia-template-*` repos whose default-branch CI is passing (real). M3
    (unique institutions) is left as an explicit stub (None) until the
    contributor/registration data source is wired — see build_payload().
    """
    out = {"D1_ci_templates": 0, "M3_unique_institutions": None, "source": "github"}
    if requests is None:
        return out
    try:
        repos, page = [], 1
        while True:
            r = requests.get(
                f"{API}/orgs/{GITHUB_ORG}/repos",
                headers=_gh_headers(),
                params={"per_page": 100, "page": page},
                timeout=30,
            )
            if r.status_code != 200:
                break
            batch = r.json()
            if not batch:
                break
            repos.extend(batch)
            page += 1
        templates = [x for x in repos if x.get("name", "").startswith("gaia-template-")]
        passing = 0
        for repo in templates:
            runs = requests.get(
                f"{API}/repos/{GITHUB_ORG}/{repo['name']}/actions/runs",
                headers=_gh_headers(),
                params={"branch": repo.get("default_branch", "main"), "per_page": 1},
                timeout=30,
            )
            if runs.status_code == 200:
                items = runs.json().get("workflow_runs", [])
                if items and items[0].get("conclusion") == "success":
                    passing += 1
        out["D1_ci_templates"] = passing
    except Exception as e:  # never hard-fail the weekly run
        print(f"[warn] github collector: {e}", file=sys.stderr)
    return out


def collect_zenodo() -> dict:
    """D3 datasets + M2 derived agents (IsDerivedFrom). Stub until ZENODO_TOKEN is set."""
    if not os.environ.get("ZENODO_TOKEN"):
        return {}
    # TODO: query the GAIA Zenodo community; count records and IsDerivedFrom edges.
    return {}


def collect_huggingface() -> dict:
    """D4 model cards. Stub until HF_TOKEN is set."""
    if not os.environ.get("HF_TOKEN"):
        return {}
    # TODO: list gaia-hazlab HF models; count versioned cards.
    return {}


def build_payload(generated_utc: str, project_year: int) -> dict:
    gh = collect_github()
    delivery = {
        "D1_ci_templates": {
            "value": gh.get("D1_ci_templates", 0),
            "target": TARGETS_Y1["D1_ci_templates"],
            "source": "github",
        },
    }
    # M3 is not yet collected: pass None through (serializes as null) and label the
    # source "pending" so the dashboard renders it as "not measured", never a real 0.
    m3 = gh.get("M3_unique_institutions")
    usage = {
        "M3_unique_institutions": {
            "value": m3,
            "target": TARGETS_Y1["M3_unique_institutions"],
            "source": "github+slack" if m3 is not None else "pending (not implemented)",
        },
    }
    # Merge optional sources when their tokens exist.
    for extra in (collect_zenodo(), collect_huggingface()):
        # placeholder: real collectors will populate delivery/usage keys
        _ = extra
    return {
        "generated_utc": generated_utc,
        "project_year": project_year,
        "delivery": delivery,
        "usage": usage,
        "composite": {"score": None, "under_engaged": []},
        "note": "Kickoff scaffold — GitHub-only. See project_coordination/04-metrics-observatory.md.",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default="data/metrics/latest.json")
    ap.add_argument("--utc", default=os.environ.get("METRICS_UTC", "1970-01-01T00:00:00Z"),
                    help="Generation timestamp (Action passes date -u; avoids nondeterminism).")
    ap.add_argument("--year", type=int, default=int(os.environ.get("PROJECT_YEAR", "1")))
    args = ap.parse_args()

    payload = build_payload(args.utc, args.year)
    body = json.dumps(payload, indent=2) + "\n"

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body)
    print(f"Wrote {out}")

    # Versioned weekly snapshot for trend lines (contract in doc 04 sec 1). The week id is
    # derived from --utc (deterministic — no Date.now), so a re-run for the same week
    # overwrites its own snapshot rather than creating duplicates.
    try:
        iso = datetime.strptime(args.utc, "%Y-%m-%dT%H:%M:%SZ").isocalendar()
        week_id = f"{iso[0]}-W{iso[1]:02d}"
    except ValueError:
        week_id = "unknown"
    hist = out.parent / "history" / f"{week_id}.json"
    hist.parent.mkdir(parents=True, exist_ok=True)
    hist.write_text(body)
    print(f"Wrote {hist}")

    print(f"  D1 CI-template repos passing: {payload['delivery']['D1_ci_templates']['value']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
