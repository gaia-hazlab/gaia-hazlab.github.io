# GAIA HazLab — Website Relaunch Plan

*Prepared June 2026 — a rebirth of the project, bringing partners back.*

This document is the working plan for upgrading the GAIA HazLab website. It is meant to
be handed around the team: Section 6 breaks the JupyterBook into per-owner assignments so
each person responsible for a piece can update it independently.

---

## 1. Goals

The relaunch has five concrete goals:

1. **A cleaner, more modern site** that reads as *smart sensing of the living Earth* rather
   than a generic hazard portal.
2. **A cinematic hero** — a full-bleed looping video behind the opening headline, with a
   graceful poster-image fallback until the footage is ready.
3. **The dashboard as its own page** — the CRESST catalog map is currently buried inside the
   DataHub chapter. It deserves a dedicated, full-bleed page (`dashboard.html`) linked from
   the main navigation.
4. **Modern iconography** — replace the fault-line / text-only cards with a clean, custom
   line-icon set themed around soil, landslides, liquefaction, evaporation, and sensing.
5. **Deeper physical content in the JupyterBook** — every technology and science chapter
   should carry the governing equations and physical models, not just prose. This is the
   piece that gets distributed to owners (Section 6).

## 2. Current state (audit)

| Layer | Files | Notes |
|-------|-------|-------|
| Landing page | `website/index.html` (deployed), `index.html` (stale dev copy) | Purple gradient, text-only cards, static banner image, no real iconography. |
| People page | `website/people.html`, `website/js/team-loader.js`, `website/data/team.json` | Team renders dynamically from JSON — keep this mechanism. |
| JupyterBook | `book/` (MyST), builds into `website/book/` | Strong `soil-memory.md` (full equations). Most other chapters are prose-only. |
| Dashboard | external iframe `https://gaia-hazlab.github.io/catalog/` | Embedded mid-chapter in `datahub.md`; not discoverable. |
| Deploy | `.github/workflows/deploy.yml` → uploads `website/` | No build step for the landing page; pure static HTML. **Keep it that way.** |

**Architecture decision:** keep the site as a no-build static deploy. A lab site edited by
many students and partners benefits more from plain HTML/CSS than from a JS framework and a
toolchain. We get the "trendy" feel from design, custom SVG icons, and the hero video — not
from React. The MyST book stays as the technical/equation layer.

> Housekeeping: the root-level `index.html` / `people.html` are stale duplicates of the ones
> in `website/`. The relaunch standardizes on `website/` (the deployed folder) and keeps the
> root copies in sync (or removes them) to avoid confusion.

## 3. Visual design system — "Earthy + sensing-tech"

A grounded, high-tech palette: terrain tones carrying electric-cyan sensing accents.

| Token | Value | Use |
|-------|-------|-----|
| `--ink` | `#10201c` | Near-black base text / dark sections |
| `--soil` | `#2c3a32` | Deep soil green-slate, section backgrounds |
| `--moss` | `#3f6f5a` | Primary green |
| `--terra` | `#c2843c` | Ochre / earth accent |
| `--stone` | `#6b7775` | Muted slate for secondary text |
| `--sense` | `#1fd8c0` | Electric cyan — the "smart sensing" signal color |
| `--signal` | `#ffb454` | Warm amber highlight |
| `--paper` | `#f6f4ee` | Warm off-white page background |

- **Type:** Montserrat for display headings (kept), **Inter** for body (replaces Roboto — a
  more modern, screen-optimized text face).
- **Motifs:** subtle sensor-node grids, faint waveform/seismic-trace lines, layered-ground
  cross-sections. Glass cards over the hero; solid cards on light sections.
- **Motion:** restrained — hover lifts, a scroll cue, the hero video. No gimmicks.

## 4. The hero (cinematic video)

The hero is built to drop a real film in later. Until then it runs on a poster image and the
gradient, so nothing looks broken.

```html
<video autoplay muted loop playsinline poster="img/hero-poster.jpg">
  <source src="img/hero.webm" type="video/webm">
  <source src="img/hero.mp4"  type="video/mp4">
</video>
```

**Footage spec for when you shoot/source it:**
- 1080p minimum (4K master, export a compressed 1080p web cut), H.264 `.mp4` **and** `.webm`.
- 10–20 s seamless loop, **no audio**, target < 6 MB so it doesn't stall first paint.
- Slow, calm motion that survives a dark overlay and text on top: drone over saturated
  terrain, rain on soil, a DAS/fiber install, river sediment plumes, instrument close-ups.
- Always ship a `hero-poster.jpg` (first frame) — it shows on mobile/data-saver and while the
  video loads.

Drop the files into `website/img/` as `hero.mp4`, `hero.webm`, `hero-poster.jpg` and they
light up automatically.

## 5. Information architecture

```
website/
├── index.html        ← relaunched landing page (hero video, icons, science + tech, partners, team)
├── dashboard.html    ← NEW dedicated full-page dashboard (CRESST catalog)
├── people.html       ← restyled to match (phase 2)
└── book/             ← MyST JupyterBook (equations + physical models)
```

Primary nav: **About · Science · Technology · Dashboard · People · Docs**

Landing-page sections, in order:
1. Hero (video) + tagline + dual CTA (Explore the Dashboard / Read the Science)
2. Mission strip
3. **What we sense** — Soil memory · Landslides · Liquefaction · Evaporation & land–atmosphere (modern icons)
4. **The platform** — DataHub · ModelHub · HazEvalHub · GAIA Translator · Research Software · Dashboard (modern icons)
5. Live dashboard teaser → full dashboard page
6. Partners & funders ("bringing partners back")
7. Team preview (unchanged data mechanism)
8. Footer

## 6. JupyterBook — physics & equations content plan (per-owner)

Goal: every chapter carries its governing equations and physical model, with MyST math,
assumptions, and references. `soil-memory.md` is the template to match. Suggested owners are
drawn from expertise in `team.json` — adjust as needed.

| Chapter | What to add | Suggested owner(s) |
|---------|-------------|--------------------|
| **soil-memory** ✅ | Already strong (coupled `dv/v` ↔ saturation/water-table inversion). Add a notation table + schematic figure. | Marine Denolle |
| **problem-statement** | A "governing physics" box: the coupled atmosphere–hydrology–geomechanics state equations the project targets. | Marine Denolle / Erkan Istanbulluoglu |
| **datahub** | Sensor physics: what each stream measures (seismic `V_s`, DAS strain rate, precip, streamflow) and the governing observation equations. | Yiyu Ni / Scott Henderson |
| **modelhub** | The ML formulations: PINN loss with physics residuals, surrogate/operator-learning setup, inputs→state mappings. | Marine Denolle / Akash Kharita / Derek Yao |
| **hazevalhub** | Hazard metrics + skill scores: factor-of-safety / infinite-slope model, liquefaction triggering (CSR/CRR), ROC/Brier for evaluation. | Morgan Sanger / Manuela Köpfli |
| **landslides** (new) | Infinite-slope stability, transient pore-pressure (Iverson), antecedent-moisture coupling. | Erkan Istanbulluoglu / Hunter Jimenez |
| **liquefaction** (new) | Effective-stress framework, cyclic stress ratio, excess pore-pressure generation. | Morgan Sanger |
| **evaporation / land–atmosphere** (new) | Surface energy balance, Penman–Monteith ET, soil-moisture ↔ flux feedback. | Nicoleta Cristea / Brandon Kerns |
| **river-floods / sediment** | Shallow-water / routing equations, sediment transport (Exner), debris-flow rheology. | Abdullah Al Mehedi / Hunter Jimenez |
| **convective-thunderstorms** | CAPE/CIN, land-surface feedback on convective initiation. | Brandon Kerns |

A short **author guide** (notation conventions, MyST math syntax, citation style) belongs in
`book/chapters/` so contributors stay consistent. The existing `citation-to-latex`,
`geophysics-derivations`, and `geophysics-lecture-author` skills can accelerate this.

## 7. Phased roadmap

**Phase 1 — this pass (done in this session):**
- New `index.html` (earthy/sensing-tech, hero-video-ready, modern SVG icons).
- New `dashboard.html` as a standalone full-page dashboard.
- This plan + per-owner content assignments.

**Phase 2 — design polish:**
- Restyle `people.html` to match; refresh `book/intro.md` hero; modern favicon/logo.
- Replace the placeholder Google-Slides embed with curated visual highlights.

**Phase 3 — content build-out:**
- Distribute Section 6 chapters to owners; add the three new science chapters.
- Add notation/figure standards and a contributor author guide.

**Phase 4 — hero film + launch:**
- Shoot/source the hero video to spec; swap in real footage.
- Linkcheck, spellcheck, partner logo refresh, announce the relaunch.

## 8. Open items for Marine

- Confirm the **partner/funder logo set** for the relaunch (who's coming back in).
- Provide or greenlight sourcing the **hero footage** (Section 4 spec).
- Approve **chapter owners** in Section 6 before distribution.
- Decide whether to **delete the stale root `index.html`/`people.html`** or keep them synced.
