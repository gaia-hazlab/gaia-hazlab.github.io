"""Build the QuakeXNet results section of the HazEvalHub landslides page.

Pulls published QuakeXNet artefacts at pinned commits and writes:

- book/chapters/includes/quakexnet-results.md   (tables, included by hazevalhub-landslides.md)
- book/img/hazevalhub/quakexnet-*.svg            (charts)
- book/img/hazevalhub/quakexnet-classifier-comparison.png  (figure copied from the notebook)

Run from the repo root (network access needed, ~15 MB download):

    pixi run python scripts/hazevalhub/quakexnet_results.py

Sources, all public:

- Akashkharita/pnw_seismic_event_detection (continuous detection, 2010-2025):
  the located catalog embedded in data/enveloc_dashboard.html is recomputed here;
  the PNSN comparison is read from the stored outputs of two notebooks, not rerun.
- Akashkharita/PNW_Seismic_Event_Classification (MIT; trace-level classifier comparison):
  the comparison figure and the model sizes typed into the notebook source.

To refresh, bump the SHAs below and rerun. Edit this file, not its outputs.
"""

import base64
import json
import re
import urllib.request
from collections import Counter
from html import escape
from pathlib import Path

DET_REPO = "Akashkharita/pnw_seismic_event_detection"
DET_SHA = "d91b386a8744eaf55753fc50d73d26e214f4b155"  # 2026-09-08
CLS_REPO = "Akashkharita/PNW_Seismic_Event_Classification"
CLS_SHA = "f952edfc8d0e6ced8ca028a85d75b5f4ed5363c5"  # 2026-01-07

ROOT = Path(__file__).resolve().parents[2]
IMG = ROOT / "book" / "img" / "hazevalhub"
INC = ROOT / "book" / "chapters" / "includes" / "quakexnet-results.md"

# Chart style. Series colours validated with the dataviz palette checker (light surface).
SU_COL = "#eb6834"   # surface events, orange as on the dashboard
PX_COL = "#2a78d6"   # explosions
ALL_COL = "#4b2e83"  # both classes together (site purple)
SURFACE = "#fcfcfb"
INK = "#2a1a4f"
MUTED = "#6f6890"
GRID = "#e6e3ee"
FONT = "Inter, Helvetica, Arial, sans-serif"


def fetch(repo, sha, path):
    url = f"https://raw.githubusercontent.com/{repo}/{sha}/{path}"
    with urllib.request.urlopen(url, timeout=120) as r:
        return r.read().decode("utf-8")


def cell_text(cell):
    out = []
    for o in cell.get("outputs", []):
        if o.get("output_type") == "stream":
            out.append("".join(o["text"]))
        elif "text/plain" in o.get("data", {}):
            out.append("".join(o["data"]["text/plain"]))
    return "\n".join(out)


def find_output(nb, marker):
    for c in nb["cells"]:
        t = cell_text(c)
        if marker in t:
            return t
    raise SystemExit(f"marker not found in notebook outputs: {marker!r}")


def num(s):
    return int(s.replace(",", ""))


# --------------------------------------------------------------------------- data

def load_catalog():
    html = fetch(DET_REPO, DET_SHA, "data/enveloc_dashboard.html")
    i = html.index("const D = ") + len("const D = ")
    data, _ = json.JSONDecoder().raw_decode(html[i:])
    return data


def load_pnsn():
    nb = json.loads(fetch(DET_REPO, DET_SHA,
                          "notebooks/analyzing_quakexnet_15_years_detection_results.ipynb"))
    t = find_output(nb, "=== MATCHING RESULTS ===")
    r = {}
    m = re.search(r"PNSN events matched:\s+([\d,]+)", t); r["matched"] = num(m.group(1))
    m = re.search(r"PNSN events missed:\s+([\d,]+)", t); r["missed"] = num(m.group(1))
    r["recall"] = {k: (int(a), int(b)) for k, a, b in
                   re.findall(r"^\s+(su|px): (\d+)/(\d+) = ", t, re.M)}
    conf = {}
    for row in ("px", "su"):
        m = re.search(rf"^{row}\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)$", t, re.M)
        conf[row] = dict(zip(("eq", "px", "su", "all"), map(int, m.groups())))
    r["confusion"] = conf
    m = re.search(r"^50%\s+([\d.]+)$", t, re.M); r["median_dt"] = float(m.group(1))
    m = re.search(r"Total novel detections: ([\d,]+)", t); r["novel"] = num(m.group(1))
    blk = t[t.index("=== RECALL BY YEAR ==="):]
    r["by_year"] = [(int(y), int(n), int(k), float(p)) for y, n, k, p in
                    re.findall(r"^\s*(\d{4})\s+(\d+)\s+(\d+)\s+([\d.]+)$", blk, re.M)]
    assert r["matched"] + r["missed"] == sum(n for _, n, _, _ in r["by_year"])

    diag = json.loads(fetch(DET_REPO, DET_SHA, "notebooks/quakexnet_diagnostic.ipynb"))
    t = find_output(diag, "=== SU events (within 70 km) ===")
    outcomes = {}
    for cls in ("SU", "PX"):
        blk = t.split(f"=== {cls} events (within 70 km) ===")[1].split("===")[0]
        outcomes[cls.lower()] = {k: int(v) for k, v in re.findall(r"^(\w+)\s+(\d+)$", blk, re.M)}
    r["outcomes"] = outcomes
    return r


def load_classifier():
    nb = json.loads(fetch(CLS_REPO, CLS_SHA, "notebooks/performance_comparisons_of_all_models.ipynb"))
    fig = None
    sizes = None
    for c in nb["cells"]:
        src = "".join(c.get("source", ""))
        if fig is None and "common_test_report_QuakeXNet_2d" in src:
            for o in c.get("outputs", []):
                if "image/png" in o.get("data", {}):
                    fig = base64.b64decode(o["data"]["image/png"])
        if sizes is None and "values_ss" in src and "Trained Model Sizes" in src:
            names = re.findall(r"'([^']+\(M2\)|[^']+\((?:1D|2D)\))'",
                               src.split("variables = [")[1].split("]")[0])
            vals = [float(v) for v in re.findall(r"[\d.]+",
                                                 src.split("values_ss = [")[1].split("]")[0])]
            sizes = list(zip(names, vals))
    assert fig and sizes and len(sizes) == 12
    return fig, sizes


# --------------------------------------------------------------------------- SVG

class Svg:
    def __init__(self, w, h, title):
        self.w, self.h = w, h
        self.parts = [f'<rect width="{w}" height="{h}" fill="{SURFACE}"/>']
        self.title = title

    def text(self, x, y, s, size=13, color=INK, anchor="start", weight=400):
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>')

    def line(self, x1, y1, x2, y2, color=GRID, w=1):
        self.parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                          f'stroke="{color}" stroke-width="{w}"/>')

    def bar(self, x, y, w, h, color, tip):
        # rounded data end, square baseline
        r = min(4, w / 2, h)
        d = (f"M{x:.1f},{y + h:.1f} V{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} "
             f"H{x + w - r:.1f} Q{x + w:.1f},{y:.1f} {x + w:.1f},{y + r:.1f} V{y + h:.1f} Z")
        self.parts.append(f'<path d="{d}" fill="{color}"><title>{escape(tip)}</title></path>')

    def poly(self, pts, color, tip):
        p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.parts.append(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="2" '
                          f'stroke-linejoin="round" stroke-linecap="round"/>')
        for (x, y), t in zip(pts, tip):
            self.parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}" '
                              f'stroke="{SURFACE}" stroke-width="2"><title>{escape(t)}</title></circle>')

    def save(self, name):
        body = "\n".join(self.parts)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
               f'role="img"><title>{escape(self.title)}</title>\n{body}\n</svg>\n')
        (IMG / name).write_text(svg)


def nice_max(v):
    for mag in range(-1, 7):
        for step in (1, 2, 2.5, 5):
            top = step * 10 ** mag
            if top >= v:
                return top
    return v


def axis_y(s, x0, x1, y0, y1, vmax, fmt, n=4):
    for k in range(n + 1):
        v = vmax * k / n
        y = y1 - (y1 - y0) * k / n
        s.line(x0, y, x1, y, GRID if k else MUTED)
        s.text(x0 - 8, y + 4, fmt(v), 12, MUTED, "end")


def chart_years(cat):
    years = [str(y) for y in range(2010, 2026)]
    s = Svg(900, 520, "Located QuakeXNet events per year, Mount Rainier, 2010-2025")
    panels = [("su", "Surface events", SU_COL, 40), ("px", "Explosions", PX_COL, 285)]
    for key, label, col, top in panels:
        c = Counter(ym[:4] for ym in cat[key]["ym"])
        vals = [c.get(y, 0) for y in years]
        vmax = nice_max(max(vals))
        x0, x1, y0, y1 = 70, 880, top + 28, top + 200
        s.text(x0, top + 12, f"{label} (n = {sum(vals):,})", 14, INK, weight=600)
        axis_y(s, x0, x1, y0, y1, vmax, lambda v: f"{v:,.0f}")
        bw = (x1 - x0) / len(years)
        for i, (y, v) in enumerate(zip(years, vals)):
            h = (y1 - y0) * v / vmax
            s.bar(x0 + i * bw + 2, y1 - h, bw - 4, h, col, f"{label}, {y}: {v:,}")
            if top > 200:
                s.text(x0 + i * bw + bw / 2, y1 + 18, y, 12, MUTED, "middle")
    s.save("quakexnet-events-per-year.svg")
    return {k: Counter(ym[:4] for ym in cat[k]["ym"]) for k in ("su", "px")}


def chart_share(cat, field, labels, title, xlabel, name, conv):
    s = Svg(900, 330, title)
    x0, x1, y0, y1 = 70, 800, 30, 260
    shares = {}
    for key in ("su", "px"):
        c = Counter(conv(v) for v in cat[key][field])
        n = sum(c.values())
        shares[key] = [100 * c.get(i, 0) / n for i in range(len(labels))]
    vmax = nice_max(max(max(v) for v in shares.values()))
    axis_y(s, x0, x1, y0, y1, vmax, lambda v: f"{v:g}%")
    step = (x1 - x0) / (len(labels) - 1)
    for i, lab in enumerate(labels):
        if lab:
            s.text(x0 + i * step, y1 + 20, lab, 12, MUTED, "middle")
    s.text((x0 + x1) / 2, y1 + 44, xlabel, 12, MUTED, "middle")
    ends = []
    for key, label, col in (("su", "Surface events", SU_COL), ("px", "Explosions", PX_COL)):
        pts = [(x0 + i * step, y1 - (y1 - y0) * v / vmax) for i, v in enumerate(shares[key])]
        tips = [f"{label}, {labels[i] or i}: {v:.1f}%" for i, v in enumerate(shares[key])]
        s.poly(pts, col, tips)
        ends.append([pts[-1][1] + 4, label])
    ends.sort()
    if ends[1][0] - ends[0][0] < 15:  # keep the two end labels apart
        mid = (ends[0][0] + ends[1][0]) / 2
        ends[0][0], ends[1][0] = mid - 8, mid + 8
    for y, label in ends:
        s.text(x1 + 10, y, label, 12, INK)
    s.save(name)
    return shares


def chart_recall_year(by_year):
    s = Svg(900, 330, "Share of PNSN surface events and explosions matched by QuakeXNet, per year")
    x0, x1, y0, y1 = 70, 880, 30, 260
    axis_y(s, x0, x1, y0, y1, 100, lambda v: f"{v:.0f}%")
    bw = (x1 - x0) / len(by_year)
    for i, (y, n, k, p) in enumerate(by_year):
        h = (y1 - y0) * p / 100
        partial = y == 2026
        s.bar(x0 + i * bw + 2, y1 - h, bw - 4, h, MUTED if partial else ALL_COL,
              f"{y}: {k} of {n} matched ({p:.1f}%)" + (" - partial year" if partial else ""))
        s.text(x0 + i * bw + bw / 2, y1 + 18, str(y) + ("*" if partial else ""), 12, MUTED, "middle")
    s.save("quakexnet-pnsn-recall-by-year.svg")


# --------------------------------------------------------------------------- include

def write_include(cat, years, pnsn, sizes, month_share, hour_share):
    su_n, px_n = len(cat["su"]["ym"]), len(cat["px"]["ym"])
    conf = pnsn["confusion"]
    rsu, rpx = pnsn["recall"]["su"], pnsn["recall"]["px"]
    tot = pnsn["matched"] + pnsn["missed"]
    oc = pnsn["outcomes"]

    def pct(a, b):
        return f"{100 * a / b:.1f}%"

    def med(xs):
        xs = sorted(xs); n = len(xs)
        return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2

    peak_su = max(range(12), key=lambda i: month_share["su"][i])
    low_su = min(range(12), key=lambda i: month_share["su"][i])
    months = ("January February March April May June July August September October "
              "November December").split()
    su_sta = Counter(cat["su"]["sta"])

    L = []
    w = L.append
    w("<!-- Generated by scripts/hazevalhub/quakexnet_results.py. Do not edit by hand. -->\n")
    w(f"**Sources.** [`{DET_REPO}`](https://github.com/{DET_REPO}/tree/{DET_SHA}) at "
      f"`{DET_SHA[:7]}` and [`{CLS_REPO}`](https://github.com/{CLS_REPO}/tree/{CLS_SHA}) at "
      f"`{CLS_SHA[:7]}`. Catalog figures are recomputed from the located catalog embedded in the "
      "dashboard. PNSN comparison figures are read from stored notebook outputs and were not "
      "rerun.\n")

    w("### Trace-level classification\n")
    w("Twelve classifiers, eight feature-based and four deep-learning, scored on a common "
      "test set of labelled PNW waveforms in four classes [@kharita2026]. Hatched bars are "
      "deep-learning models.\n")
    w(":::{figure} ../img/hazevalhub/quakexnet-classifier-comparison.png\n"
      ":alt: Precision, recall and accuracy for twelve classifiers across earthquake, "
      "explosion, surface and noise classes\n"
      ":width: 100%\n\n"
      f"Precision and recall per class, and overall accuracy. Figure from "
      f"`notebooks/performance_comparisons_of_all_models.ipynb` in `{CLS_REPO}` (MIT), "
      "Akash Kharita.\n:::\n")
    w("Accuracy is close between the best deep models; size is not. Trained model sizes as "
      "recorded in the same notebook:\n")
    w("| Model | Size (MB) |\n|---|---:|")
    for name, mb in sizes:
        w(f"| {name} | {mb:g} |")
    w("")
    w("The per-class scores behind the figure live in `results/*.pkl` files that are not in the "
      "repository, so the figure is the only public record of them (R7).\n")

    w("### The fifteen-year catalog\n")
    w(f"| Class | Located events, 2010–2025 | Median stations per event | Median distance from summit (km) |\n"
      f"|---|---:|---:|---:|")
    for key, label in (("su", "Surface events"), ("px", "Explosions")):
        w(f"| {label} | {len(cat[key]['ym']):,} | {med(cat[key]['sta']):g} | "
          f"{med(cat[key]['dist']):.1f} |")
    w(f"| **Total** | **{su_n + px_n:,}** | | |\n")
    lo = min(su_sta)
    w(f"The fewest stations on any located event is {lo}; {su_sta[lo]:,} surface events "
      f"({pct(su_sta[lo], su_n)}) sit at that minimum.\n")
    w(":::{figure} ../img/hazevalhub/quakexnet-events-per-year.svg\n"
      ":alt: Bar charts of located surface events and explosions per year, 2010 to 2025\n"
      ":width: 100%\n\nLocated events per year. Station coverage changed over the period, "
      "so a trend here mixes activity with network growth.\n:::\n")
    w(":::{figure} ../img/hazevalhub/quakexnet-month-of-year.svg\n"
      ":alt: Line chart of the share of each class by calendar month\n"
      ":width: 100%\n\n"
      f"Share of each class by calendar month. Surface events peak in {months[peak_su]} and "
      f"are fewest in {months[low_su]}; the peak month has "
      f"{month_share['su'][peak_su] / month_share['su'][low_su]:.1f} times the events of the "
      "quietest, a weak seasonal cycle.\n:::\n")
    w(":::{figure} ../img/hazevalhub/quakexnet-hour-of-day.svg\n"
      ":alt: Line chart of the share of each class by hour of day in UTC\n"
      ":width: 100%\n\n"
      "Share of each class by hour of day, UTC.\n:::\n")
    day = {k: sum(hour_share[k][h] for h in range(15, 24)) for k in ("su", "px")}
    w("Blasting happens in daylight, so the explosion class should crowd into Pacific working "
      "hours, 08:00 to 17:00 PDT or 15:00 to 00:00 UTC. A flat curve would put "
      f"{100 * 9 / 24:.1f}% of events in those nine hours. Explosions put {day['px']:.1f}% "
      f"there and surface events {day['su']:.1f}%. "
      + ("There is no daytime excess, so the explosion class is not dominated by blasting. "
         if day["px"] <= 100 * 9 / 24 + 2 else
         "The daytime excess is what blasting would produce. ")
      + "The time-zone bands here ignore the switch to PST in winter, which shifts them by one "
      "hour and does not change the conclusion.\n")

    w("### Against the PNSN catalog\n")
    w(f"PNSN analysts label surface events (`su`) and explosions (`px`). The comparison takes "
      f"the {tot:,} PNSN events of those two types, 2010 to April 2026, for which at least half "
      "the reporting stations lie within 50 km of the summit. A PNSN event counts as matched if "
      "the unfiltered QuakeXNet catalog of network detections has an event starting within "
      "60 s of the PNSN origin time.\n")
    w("| PNSN label | PNSN events | Matched | Recall | Labelled `su` | Labelled `px` | Labelled `eq` |\n"
      "|---|---:|---:|---:|---:|---:|---:|")
    for key, label, (k, n) in (("su", "Surface event", rsu), ("px", "Explosion", rpx)):
        c = conf[key]
        w(f"| {label} | {n:,} | {k:,} | {pct(k, n)} | {c['su']:,} | {c['px']:,} | {c['eq']:,} |")
    w(f"| **Both** | **{tot:,}** | **{pnsn['matched']:,}** | **{pct(pnsn['matched'], tot)}** | | | |\n")
    w(f"Of matched PNSN surface events, {pct(conf['su']['su'], conf['su']['all'])} carry the "
      f"surface-event label; of matched explosions, {pct(conf['px']['px'], conf['px']['all'])} "
      f"carry the explosion label. The two errors are not symmetric: {conf['su']['px']:,} PNSN "
      f"surface events were called explosions, against {conf['px']['su']:,} explosions called "
      f"surface events. The median offset between PNSN origin time and "
      f"QuakeXNet detection start is {pnsn['median_dt']:.1f} s, set by how detections are "
      "windowed and rounded to 10 s rather than by timing accuracy.\n")
    w(":::{figure} ../img/hazevalhub/quakexnet-pnsn-recall-by-year.svg\n"
      ":alt: Bar chart of the share of PNSN events matched each year, 2010 to 2026\n"
      ":width: 100%\n\nShare of PNSN `su` and `px` events matched, per year. "
      "*2026 is partial: the PNSN extract runs to 22 April, and the QuakeXNet catalog read "
      "in the diagnostic notebook ends on 11 March.\n:::\n")
    w("| Year | PNSN events | Matched | Recall |\n|---|---:|---:|---:|")
    for y, n, k, p in pnsn["by_year"]:
        w(f"| {y}{'*' if y == 2026 else ''} | {n} | {k} | {p:.1f}% |")
    w("")
    w("A second cut, from `notebooks/quakexnet_diagnostic.ipynb`, uses PNSN events whose "
      "location is within 70 km and lets a PNSN event match several QuakeXNet classes at once:\n")
    names = {"correct": "Correct class only", "ambiguous": "Correct class and another",
             "confused": "Another class only", "missed": "No detection"}
    w("| Outcome | PNSN surface events | PNSN explosions |\n|---|---:|---:|")
    for grp, label in names.items():
        a = sum(v for k, v in oc["su"].items() if k.startswith(grp))
        b = sum(v for k, v in oc["px"].items() if k.startswith(grp))
        w(f"| {label} | {a:,} | {b:,} |")
    w(f"| **Total** | **{sum(oc['su'].values()):,}** | **{sum(oc['px'].values()):,}** |\n")
    w(f"**Precision is not measured.** QuakeXNet finds {pnsn['novel']:,} network events with no "
      "PNSN counterpart. PNSN does not try to catalogue every surface event, so these are a mix "
      "of real events PNSN never listed and false detections, and nothing on this page separates "
      "the two. That needs an independently labelled sample of novel detections.\n")
    INC.parent.mkdir(parents=True, exist_ok=True)
    INC.write_text("\n".join(L))


def main():
    IMG.mkdir(parents=True, exist_ok=True)
    cat = load_catalog()
    print(f"catalog: {len(cat['su']['ym']):,} surface events, {len(cat['px']['ym']):,} explosions")
    pnsn = load_pnsn()
    fig, sizes = load_classifier()
    (IMG / "quakexnet-classifier-comparison.png").write_bytes(fig)

    years = chart_years(cat)
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    month_share = chart_share(cat, "ym", months,
                              "Share of located events by calendar month", "Month",
                              "quakexnet-month-of-year.svg", lambda ym: int(ym[5:7]) - 1)
    hours = [f"{h:02d}" if h % 3 == 0 else "" for h in range(24)]
    hour_share = chart_share(cat, "hour", hours, "Share of located events by hour of day (UTC)",
                "Hour of day, UTC", "quakexnet-hour-of-day.svg", int)
    chart_recall_year(pnsn["by_year"])
    write_include(cat, years, pnsn, sizes, month_share, hour_share)
    print(f"wrote {INC.relative_to(ROOT)} and charts in {IMG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
