# Liquefaction Data Inventory

:::{note}
**The authoritative data inventory for the liquefaction digital twin.** This page catalogs
every dataset that flows through the [liquefaction](hazard-liquefaction-ground-failure) digital
twin — from **raw external products**, through **deterministically derived layers**, to **model
outputs** — with sources, access/sensitivity, spatial/temporal resolution, and limitations.

It is the liquefaction-specific companion to the [DataHub](datahub) and follows the four-part
provenance standard (source · measurement · resolution · uncertainty) defined in the
[DataHub Integration Guide §2](datahub-integration-guide). The model that consumes it is the
[Liquefaction Model](modelhub-liquefaction); the science is in
[Pillar 2 §3](pillar-2-nowcasting-susceptibility).
:::

## How to read this inventory

Each layer is tagged with the **hazard purpose** it serves, so the DataHub inventory is shared
and de-duplicated across hazards rather than rebuilt per hazard.

**Legend:** ⛰️ landslides (shallow/deep) · 🔥 post-fire debris flows · 🏚️ liquefaction &
ground failure · 🌊 floods

Data are grouped by **provenance tier**, because that determines how they should be trusted,
stored, and calibrated:

1. **Raw / observed inputs** — imported from an external archive; held fixed in calibration.
2. **Derived variables** — computed deterministically from raw inputs and documented rules.
3. **Modelled variables & outputs** — produced by the GLM during a run; carry assumptions and
   uncertainty.

The **primary target** is the **probability / areal extent of liquefaction** $P(\text{liq})$ and
its manifestation severity (LPI / LSN), in the three framings of
[modelhub-liquefaction §4](modelhub-liquefaction).

## 1. Raw / observed inputs (external products)

| Layer / product | Source · archive | Access / sensitivity | Native res · CRS | Cadence | Units | Serves | Key limitations |
|---|---|---|---|---|---|---|---|
| **Shear-wave velocity** → $V_{s30}$, $V_s(z)$ | parametric CONUS $V_s$ [@sanger2025vs]; USGS National Crustal Model; proxy $V_{s30}$ from slope/geology | Public / open | parametric; proxy ~250–1000 m | Static (→ dynamic via seismic) | m s⁻¹ | 🏚️ ⛰️ | Proxy $V_{s30}$ has large scatter; profile uncertainty; **rigidity is high-influence** |
| **Water-table depth** → $d_{wt}$ | [Pillar 1 Soil Reanalysis](pillar-1-soil-reanalysis); [groundwater modeling](groundwater-soil-moisture); modeled WTD (Zhu GLM) | Mixed | tens of m target; coarse priors | **Dynamic** (seasonal, sea-level) | m | 🏚️ ⛰️ 🌊 | Saturation is a **binary gate**; coarse priors smear hazard; the key dynamic control |
| **Surficial geology / soil type** | state geologic surveys; USGS; SOLUS/POLARIS texture | Public / open | varies (1:24k–1:100k) | Static | categorical | 🏚️ ⛰️ | Map-scale generalization; susceptibility class boundaries uncertain |
| **Ground motion (event)** → PGA, PGV, MMI | USGS ShakeMap ([earthquake.usgs.gov/data/shakemap](https://earthquake.usgs.gov/data/shakemap/)) | Public / open | event grid | Per-event | g, cm s⁻¹ | 🏚️ | ShakeMap & GMM epistemic uncertainty; the conditional/event **demand** input |
| **Seismic hazard (probabilistic)** → hazard curves $\lambda(IM)$ | USGS NSHM [@petersen2024] via [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) | Public / open | site / gridded | Static (model epoch) | rate vs IM | 🏚️ | Fixed reference-rock site term (§5 open question); model-epoch dependence |
| **Attenuation** → $\kappa_0$ | high-frequency spectral decay of recordings [@andersonhough1984]; GAIA seismic/DAS | Public / network | per site/station | Static (→ dynamic) | s | 🏚️ | Band/method-dependent; seasonal variability [@haendel2025] — not yet wired |
| **Geotechnical case histories** (calibration) | CPT/SPT liquefaction databases (Christchurch, etc. [@vanballegooy2014]) | Public / curated | point | Event-based | varies | 🏚️ | Geographic bias; the surrogate's training/validation base |
| **Precipitation / climate** (for groundwater) | PRISM / HRRR via [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli); Earth2Studio forecast | 4 km free; 800 m licensed | 4 km (→ forecast) | Daily / forecast | mm day⁻¹ | ⛰️ 🔥 🌊 🏚️ | Drives the **dynamic** water table; least-skillful forecast field |
| **Observed liquefaction maps** → validation labels | post-earthquake reconnaissance (e.g. 2001 [Nisqually](wa-2001-2031-nisqually-earthquake)); GEER | Public / curated | vector | Per-event | presence / severity | 🏚️ | Mapping completeness & subjectivity; used only to **score**, never as input |

## 2. Derived variables (deterministic transformations)

| Derived variable | Computed from | Units | Rule | Why it matters |
|---|---|---|---|---|
| Total / effective stress $\sigma_{v0}$, $\sigma'_{v0}$ | overburden + water table $d_{wt}$ | kPa | $\sigma'_{v0}=\sigma_{v0}-u$ | Couples **hydrology** into CSR & CRR |
| Stress-corrected velocity $V_{s1}$ | $V_s$, $\sigma'_{v0}$ | m s⁻¹ | $V_{s1}=V_s\,(P_a/\sigma'_{v0})^{0.25}$ | Overburden-normalized **rigidity** for CRR [@andrusstokoe2000] |
| Cyclic stress ratio $\mathrm{CSR}$ | $a_{max}$, $\sigma_{v0}/\sigma'_{v0}$, $r_d$ | – | §2 of [model page](modelhub-liquefaction) | Seismic **demand** |
| Magnitude / overburden corrections | $M$, $\sigma'_{v0}$ | – | MSF, $K_\sigma$ | Normalizes CSR to a reference |
| Compound topographic index / distance-to-water | DEM; hydrography | – | GIS derivations | Geospatial GLM saturation proxies [@zhu2015] |

## 3. Modelled variables & outputs

| Output | Producing model | Units / dims | Meaning | Primary use |
|---|---|---|---|---|
| **$P(\text{liq})$** | GLM surrogate [@sanger2025jgge] | 0–1, `[y,x]` (event) / `[lead,y,x]` | probability of liquefaction | **Primary hazard target** |
| Liquefaction areal extent | GLM | fraction / km² | spatial extent | loss estimation |
| LPI / LSN | manifestation model [@iwasaki1978; @vanballegooy2014] | index | surface severity | damage / impact |
| Return-period liquefaction hazard | unconditional integration over NSHM | annual rate / 50-yr prob. | $\lambda_{liq}$ | planning baseline |

## 4. Data-prep pipeline

```
A. domain     AOI / region; target CRS + resolution (high-res even for static layers)
B. acquire    Vs30/Vs profiles · water table (Pillar 1) · geology · ShakeMap|NSHM ground motion
C. harmonize  reproject + resample to one grid contract; record manifest + provenance
D. derive     effective stress σ'v (from water table) · Vs1 · CSR · saturation proxies
E. condition  conditional GLM P(liq|IM)  →  (unconditional: integrate over NSHM;
                                              event: apply ShakeMap IM field)
F. dynamic    couple groundwater (sea-level / seasonal) + time-varying Vs/κ0 (§5 open question)
G. validate   input contract: shape · CRS · units · required fields
H. publish    COG / Zarr on s3://cresst + STAC items with source·measurement·res·uncertainty
```

The **high-resolution requirement** (even for static $V_{s30}$, geology, water table) is central:
liquefaction is controlled by meter-scale contrasts, so coarse inputs systematically smear hazard
and bias loss estimates (see [Pillar 2 §3](pillar-2-nowcasting-susceptibility)).

## 5. Known gaps, risks & sensitivities

- **Static vs dynamic water table.** Most GLMs use a *modeled, static* water table; GAIA's
  contribution is the **dynamic** $d_{wt}$ (seasonal, sea-level rise) from Pillar 1 — the
  inventory must distinguish the two.
- **Time-varying site term.** $\kappa_0(t)$ / $V_s(t)$ are not yet wired into the NSHM-based
  unconditional product (the open question in [model §5](modelhub-liquefaction)).
- **$V_{s30}$ proxy uncertainty.** Slope/geology-based $V_{s30}$ carries large scatter; the
  parametric profiles [@sanger2025vs] reduce but do not remove it.
- **Training transferability.** Geospatial GLMs trained on one region (e.g. Christchurch, Kobe)
  need regional efficacy checks before PNW use [@rashidian2020; @geyin2020field].
- **Ground-motion epistemic uncertainty.** ShakeMap and GMM/NSHM uncertainty propagate directly
  into the demand side.

## Related

- [Liquefaction & Ground Failure](hazard-liquefaction-ground-failure) — the hazard page this
  inventory serves.
- [Liquefaction Model](modelhub-liquefaction) — the model that consumes these layers.
- [DataHub](datahub) · [DataHub Integration Guide](datahub-integration-guide) — platform,
  provenance standard, and repo migration path.
- [Landslide Data Inventory](datahub-landslide-inventory) — the sibling inventory; shared layers
  (DEM, water table, saturation, precipitation) are tagged across both.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) — the dynamic water-table source.
- Repos: [`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) ·
  [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) ·
  [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) · `gaia-model-liquefaction` *(proposed)* ·
  `gaia-vs-conus` *(proposed)*.
