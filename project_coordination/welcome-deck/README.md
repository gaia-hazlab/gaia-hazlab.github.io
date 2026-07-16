# GAIA Welcome Deck — Source & Brand Spec

> **Scope: the NSF CSSI kickoff.** This is the CSSI project's welcome/onboarding deck —
> it grounds the team in GAIA's original **science + CI mission** and the CSSI expansions
> (Alaska, geodesy/SAR, agents+evals). It is *not* a lab-wide or multi-program deck; the
> sibling programs appear only as **lineage** ([§4](#4-narrative-arc-15-slides), and
> [07-programs-and-partners.md](../07-programs-and-partners.md)).
>
> **Delivery: project-owned Google Slides.** The live deck lives in Google Slides under
> `gaia.ci@` (consistent with the Workspace decision,
> [01 §5](../01-project-coordination.md)) — editable by the team, presentable at the
> kickoff, exportable to PDF for the Announce list + website. **This folder is the
> source-of-truth spec** (brand tokens, logo manifest, narrative arc) that the Slides
> template is built from — not a repo-built binary deck. (A `.pptx`/reveal.js build from
> this spec stays an option if we ever want it version-controlled.)
>
> Brand matches **gaia-hazlab.github.io exactly** (tokens lifted from `people.html`), in
> the same family as the FrugalMind EvalHub sibling site
> (<https://mdenolle.github.io/frugalmind/>: "evidence over hype," clean data-forward
> layout).
>
> ⚠ **Placeholders marked `‹confirm›`** are program-history items I won't invent — Marine
> fills or removes them (see §4 lineage).

## 1. Brand tokens (exact — from the website CSS)

| Token | Hex | Use |
|---|---|---|
| Ink | `#2A1A4F` | body text, dark footers |
| **UW Purple** | `#4B2E83` | primary; titles, key fills |
| Purple deep | `#341F63` | gradient end, emphasis |
| Periwinkle | `#6D5BD0` | accent, links, roles |
| Peri-light | `#C3B8F0` | kickers, on-dark accents, grid motif |
| Stone | `#6F6890` | secondary text |
| Lavender | `#F5F3FB` | light slide background |
| Lav-2 | `#ECE8F7` | alt panel background |
| Paper | `#FFFFFF` | cards |

- **Signature gradient** (section/title slides): `linear-gradient(135deg, #4B2E83 0%, #341F63 100%)`, white text, `#C3B8F0` kicker.
- **Grid motif** (hero overlay): faint periwinkle 54px grid, radial-masked to top-right — the `.page-header::after` pattern. Use sparingly on title/section dividers only.
- **Cards:** white, radius 18px, 1px `rgba(42,26,79,0.10)` border, soft purple shadow `0 18px 40px rgba(75,46,131,0.13)`.

## 2. Typography

- **Headings / titles:** **Montserrat** (700–800), tight letter-spacing (`-0.5px`).
- **Body / captions:** **Inter** (300–500).
- Kicker style: Inter 600, uppercase, `letter-spacing: 2.5px`, `#C3B8F0` on dark / `#6D5BD0` on light.
- Mirror the site scale: hero title clamp ~2.2–3.4rem, section titles ~1.7–2.3rem.

## 3. Logo manifest — systematic placement

Two rows appear on the **title slide footer** and a dedicated **"Who we are" slide**:
**Funders** (top) and **Partner institutions** (bottom). Keep all logos greyscale-on-light
or white-knockout-on-purple for consistency; equal optical height; align on a baseline.

| Logo | Row | In repo? | Source to fetch (official) |
|---|---|---|---|
| **NSF** | Funder | ✗ | nsf.gov brand assets (use official NSF logo) |
| **FFST** (Fund for Future Science/Tech seed) | Funder | ✅ `images/sponsors/FFST-Hero.png` | in repo |
| **University of Washington** | Funder/Inst | ✗ | UW brand (Block W / signature) |
| **UW eScience Institute** | Funder | ✗ | escience.washington.edu |
| **UW College of the Environment** | Funder | ✅ `images/sponsors/coenv-logo.png` | in repo (kept for continuity) |
| **EarthScope Consortium** | Institution | ✗ | earthscope.org |
| **University of Alaska Fairbanks (UAF)** | Institution | ✗ | uaf.edu (also ASF sits under UAF) |
| **Alaska Satellite Facility (ASF)** | Institution | ✗ | asf.alaska.edu ‹confirm as partner logo› |
| **Concord Consortium** | Institution | ✗ | concord.org ‹confirm role — education/broadening partner› |
| **GAIA HazLab mark** | brand | ✅ `book/img/gaia-hazalab-logo.png` | in repo |

> Fetching external logos = downloading files, which I'll do only on your OK (I'll list
> exact URLs first). Drop any you already have into `welcome-deck/logos/` and I'll wire them.

## 4. Narrative arc (≈15 slides)

Content below is drawn from `CSSI_GAIA_2025.pdf` (submitted 2025-12-01) unless marked
`‹confirm›`.

1. **Title** — "GAIA — Geophysical AI-driven Integration & Assimilation." Subtitle: *An open, agentic, multi-hazard cyberinfrastructure for real-time geohazard prediction.* Funder + institution logo rows. Gradient + grid motif.
2. **The problem** — Geohazards (quakes, landslides, floods) cause hundreds of billions in annual damage; cascading, physically interconnected — yet CI is fragmented per-hazard. (Fig 1 "Earth System → Digital Twin.")
3. **The opportunity** — Data explosion (satellites, DAS, dense networks) + exascale simulation + foundation/agentic AI make real-time data-assimilative digital twins possible — but *not yet routine*.
4. **Where we come from (lineage)** — SCOPED (550+ participants, ~1,000 survey responses, 90% repeat) · GeoSMART (ML training + hackweeks) · GeoSciCloud. ‹confirm: proto STC-CIMG/WEDGE · GAIA-CRESST · LLMoxie · the data-mining project — add logos/one-liners or cut›.
5. **The GAIA vision** — Fuse multimodal data + physical models + literature + software via AI-aided operators; physics-aware surrogates; research-assisting agents. Runs laptop → cloud → HPC.
6. **The scientific question** — *How does time-varying soil hydromechanical memory — set by moisture history, freeze–thaw, and mechanical damage — control where and when the ground fails?* Two thrusts answer it.
7. **RC1 — Soil Hydromechanical Memory** (UW + EarthScope lead) — repurpose 100k+ seismic stations as soil sensors via dv/v; separate thermoelastic / hydrological / mechanical-damage signals; fuse with weather + GNSS-TEC → time-varying soil strength. (Fig 2.)
8. **RC2 — Landslide initiation & co-event dynamics** — characterize + model failure using fused seismic + GNSS + SAR/satellite; link precondition states to triggers.
9. **The three CSSI expansions** — ① **Alaska** as a first-class region · ② new **modalities**: geodesy/GNSS, SAR/InSAR (ASF), infrasound · ③ **agents + evals** (HazEvalHub).
10. **The data substrate** — Event-Centric Inventories (Alaska + PNW), Simulation datasets (landlab, ParFlow/hf_hydrodata, SPECFEM), Text/embedding sets for RAG agents. All FAIR: Zenodo DOI + Hugging Face + GitHub.
11. **The four hubs** — DataHub · ModelHub · HazEvalHub (agents & evals + CTF) · the coordination/website layer.
12. **The ecosystem** — Interconnect national facilities (EarthScope, ASF, NASA, ECMWF, CUAHSI/HydroShare) + hazard centers (SCEC, CRESCENT, ClasH, SZ4D, VICTOR, CIG, DesignSafe) + AI institutes (OMAI, AI2, AI2ES) + CSSI siblings (QuakeWorx, HydroFrame, landlab–ASPECT).
13. **How impact is measured** — the Metrics Observatory: delivery D1–D5 + usage M1–M4, automated weekly, DOI-archived. (Screenshot of the dashboard.)
14. **How we work together** — the team + institutions; monthly cadence (PI sync, forum, office hours, thrust sync, project-wide update); GitHub = system of record, Google = human mirror; Slack channels.
15. **Your first week** — fill the intake form, GitHub org + Slack, pick a `good-first-issue`, add talks to the calendar, join the (optional) newsletter. QR/link to the intake form.

## 5. Build checklist

- [ ] Confirm §4 lineage placeholders (STC-CIMG/WEDGE, GAIA-CRESST, LLMoxie, data-mining).
- [ ] Approve logo list; fetch missing logos → `welcome-deck/logos/`.
- [ ] Build the **Google Slides template** under `gaia.ci@`: two master layouts (gradient
      title/section + light content) and a card-grid layout, in the brand tokens above.
- [ ] Populate the §4 narrative arc into the Slides template.
- [ ] Pull the Fig 1 / Fig 2 assets from the proposal for slides 2 and 7.
- [ ] Export a PDF for the Announce list + website; link the Slides URL from the kickoff issue.
- [ ] _(Optional)_ Generate a version-controlled `.pptx`/reveal.js build from this spec.
