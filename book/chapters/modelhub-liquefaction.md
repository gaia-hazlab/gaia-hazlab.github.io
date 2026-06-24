# Liquefaction Model — Geospatial GLM Surrogate

:::{note}
**The model-side companion to the liquefaction digital twin.** This page is the ModelHub home
for the **geospatial liquefaction model (GLM)**: the equations it solves, what is *solved*
versus *assumed* inside a geospatial surrogate, the three hazard framings
(conditional / unconditional / event-based), how attenuation and the National Seismic Hazard
Model enter, how it couples to the other GAIA projects (soil reanalysis, the landslide model,
earthquake wavefields), how to make it interoperable with **Earth2Studio**, and how predictions
are evaluated.

It builds on the science in [Pillar 2 §3](pillar-2-nowcasting-susceptibility), draws on the
state from [Pillar 1](pillar-1-soil-reanalysis), and reads the data cataloged in the
[Data Inventory](datahub-inventory). Led by the **Sanger/Maurer**
line of work [@sanger2025jgge; @sanger2026geoai]. Repository pointers in §9 are **placeholders**
for the team (Morgan) to confirm.
:::

## 1. What the model computes (and what it does not)

The product is the **probability and areal extent of liquefaction** and its surface
**manifestation severity**, served in three framings (§4): conditional on a ground motion,
unconditional over a return period, and for a specific event. A **geospatial** model trades
per-site borehole data for spatially continuous proxies — predicting liquefaction from PGV/PGA,
$V_{s30}$, water-table depth, precipitation, and distance to water [@zhu2015; @zhu2017] — so it
covers regions where site investigations do not exist.

What the model does **not** do: it does not replace site-specific CPT/SPT triggering analysis
at an engineered site; it does not solve transient 3-D groundwater flow (it *consumes* a
water-table field, §6); and it does not by itself produce ground motion — that comes from a
ShakeMap (event) or the NSHM (probabilistic), §4–§5.

## 2. The physics — the equations we solve

The simplified procedure [@seedidriss1971; @idrissboulanger2006] compares seismic **demand** to
soil **capacity**. The cyclic stress ratio (demand) is

$$
\mathrm{CSR} = 0.65\,\frac{a_{max}}{g}\,\frac{\sigma_{v0}}{\sigma'_{v0}}\,r_d ,
$$

the cyclic resistance ratio $\mathrm{CRR}$ is the capacity, and triggering is expected when the
factor of safety

$$
\mathrm{FS}_{liq} = \frac{\mathrm{CRR}}{\mathrm{CSR}} \le 1 .
$$

Surface severity is summarized by manifestation indices — the Liquefaction Potential Index
[@iwasaki1978] and the Liquefaction Severity Number [@vanballegooy2014]. Two **Pillar-1 state
variables** enter directly:

- **Hydrology (water table).** Pore pressure sets the effective stress
  $\sigma'_{v0}=\sigma_{v0}-u$, which appears in *both* demand (the $\sigma_{v0}/\sigma'_{v0}$
  ratio in CSR) and capacity (overburden correction of $V_{s1}$). Only **saturated** soil below
  the water table can liquefy — saturation is a binary gate. A shallower water table raises
  demand and exposes more liquefiable column.
- **Rigidity (shear-wave velocity).** $V_s$ is the small-strain stiffness proxy
  ($G_{max}=\rho V_s^2$). It raises **capacity** — CRR increases with overburden-corrected
  $V_{s1}$ [@andrusstokoe2000] — and modulates **demand**, because $V_{s30}$ controls site
  amplification of $a_{max}$. Stiffer ground resists triggering, but soft sites amplify shaking.

## 3. The geospatial surrogate — what is solved vs. assumed

Classical triggering (§2) is evaluated per soil column. The **geospatial** model regresses the
*outcome* (liquefaction occurrence / manifestation) on spatially available proxies, and GAIA's
GLM uses the **mechanics-informed ML surrogate** of [@sanger2025jgge], which emulates
physics-based triggering at national scale and in near-real time, demonstrated for the PNW in
[@sanger2026geoai].

| Element | What it *solves* | What it *assumes* |
|---|---|---|
| Geospatial predictors → $P(\text{liq})$ | logistic / ML mapping from PGV, $V_{s30}$, water table, precip, distance-to-water [@zhu2017] | proxies stand in for unmeasured geotechnical state; training-region transferability [@rashidian2020] |
| Mechanics-informed surrogate | fast emulation of the simplified-procedure FS over a region [@sanger2025jgge] | the surrogate is trained on / constrained by the mechanics; valid within its training envelope |
| Manifestation model | fragility from FS / LPI to damage state [@geyin2020fragility; @geyin2020field; @maurer2015] | surface manifestation is a function of integrated triggering + site |
| $V_s$ field | parametric CONUS $V_s$ profiles [@sanger2025vs] | functional form + geospatial ML capture the near-surface profile |

The surrogate's value is **speed and coverage**: it runs the conditional model everywhere, fast
enough for the unconditional integral (§4) and for Earth2Studio ensembles (§7).

## 4. The three hazard framings

A GLM digital twin must serve three distinct questions, each with different ground-motion input
and data/model need:

| Framing | Question | Ground-motion input | Output | Data / model need |
|---|---|---|---|---|
| **Conditional (national)** | $P(\text{liq}\mid IM)$ — given shaking | a specified IM (PGA/PGV) | probability / extent given that IM | the national GLM surrogate [@sanger2025jgge]; high-res $V_{s30}$, water table, geology |
| **Unconditional (return period)** | total liquefaction hazard in $T$ years | integrated over the **NSHM** hazard curve | return-period liquefaction hazard | $\lambda_{liq}=\int P(\text{liq}\mid IM)\,\lvert d\lambda(IM)\rvert$; NSHM curves [@petersen2024] via [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) |
| **Event-based (scenario)** | liquefaction footprint of *this* quake | a ShakeMap IM field | deterministic spatial map | rupture → ShakeMap → GLM; the nowcasting mode |

The **unconditional** product is the "total risk for a return period" baseline; the
**event-based** product is the real-time nowcast for a specific rupture (e.g. a Cascadia or
[Nisqually](wa-2001-2031-nisqually-earthquake) scenario). All three call the *same* conditional
surrogate — they differ only in how the ground motion is supplied and integrated.

## 5. Attenuation, $\kappa_0$, and the NSHM

High-frequency ground motion — and therefore $a_{max}$ — is controlled by **attenuation**,
parameterized by the site spectral-decay term $\kappa_0$ [@andersonhough1984]. Two questions
the GAIA seismic networks help answer:

- **Where is $\kappa_0$ measured?** From the high-frequency slope of recorded acceleration
  spectra ($A(f)\propto e^{-\pi\kappa f}$); the zero-distance intercept is the site $\kappa_0$.
  GAIA's dense seismic/DAS data make this estimable per site.
- **Can $\kappa_0$ vary in time?** It is dominated by attenuation in the shallow,
  moisture-sensitive subsurface, so it is **not** strictly static — seasonal variation has been
  observed [@haendel2025; @ktenidou2015]. This couples to the Pillar-1 soil reanalysis (the same
  near-surface saturation GAIA monitors via $dv/v$).

**Open integration question.** The [NSHM](https://www.usgs.gov/programs/earthquake-hazards)
embeds a *fixed* reference-rock $\kappa_0$ and $V_{s30}$ site term [@petersen2024]; how to feed a
**time-varying** site term ($\kappa_0(t)$, $V_s(t)$) back into the hazard input for the
unconditional product (§4) is unresolved and a GAIA research target.

## 6. Coupling map — where the other GAIA projects plug in

**(a) Soil reanalysis** ([Pillar 1](pillar-1-soil-reanalysis), [soil-memory](soil-memory)). The
water-table depth $d_{wt}(x,t)$ and saturation $S_w$ are the **dynamic** liquefaction controls
(§2); the seismic $dv/v$ inversion also delivers a **time-varying $V_s$** for both the capacity
term and the site amplification. This is the direct line from the reanalysis to liquefaction
susceptibility, and the route by which **sea-level rise and seasonal water-table change** modulate
hazard (via the [groundwater modeling](groundwater-soil-moisture)).

**(b) The landslide model** ([modelhub-landslide](modelhub-landslide)). Liquefaction and
landslides share the **same antecedent hydromechanical state** — saturation and water table —
but couple it to a *seismic* trigger (PGA/PGV) rather than rainfall recharge. The landslide
engine's **Monte-Carlo-over-uncertain-strength** structure is the template the liquefaction
surrogate mirrors: both are "soil state + trigger → probability of failure."

**(c) Earthquake wavefields & the NSHM.** The ground-motion field comes from ShakeMap (event) or
the NSHM (probabilistic, via [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg));
GAIA's wavefield reconstruction/forecasting work is the natural source of refined, possibly
time-varying, site ground motion.

## 7. Interoperability with Earth2Studio

The **dynamic** half of the GLM twin needs forecast forcing, routed through
[Earth2Studio](https://github.com/NVIDIA/earth2studio) — the same AI weather/climate stack the
[landslide model](modelhub-landslide) and [Pillar 3 forecasting](pillar-3-forecasting-susceptibility)
use:

- **Climate/weather → groundwater → water table.** Earth2Studio forecasts (precipitation, plus
  sea-level-rise and seasonal scenarios) drive the groundwater model that sets $d_{wt}$ — the
  dynamic liquefaction control.
- **GLM surrogate as a diagnostic model.** The fast mechanics-informed surrogate
  [@sanger2025jgge] can be wrapped with the Earth2Studio diagnostic signature for large scenario
  / return-period ensembles on GPU.
- **Time-varying site terms.** Seismic-derived $V_s(t)$ / $\kappa_0(t)$ feed the ground-motion
  side (§5), closing the dynamic loop.

## 8. Evaluation & metrics

As for the landslide model, separate **calibration** of intermediate states from **validation**
of the prediction; full metric definitions live in [HazEvalHub](hazevalhub).

- **Calibration** — against the geotechnical case-history record (CPT/SPT triggering, manifestation
  fragility [@geyin2020fragility; @maurer2015]) and the $V_s$ / water-table inputs.
- **Validation** — against **observed liquefaction maps** from past earthquakes (the
  [Nisqually](wa-2001-2031-nisqually-earthquake) 2001 event is the regional target): probabilistic
  skill (Brier, reliability), spatial agreement (IoU) of mapped manifestation, and — for the
  unconditional product — consistency with return-period expectations.

## 9. Repositories *(placeholders — for Morgan to confirm)*

- [`da-seis-groundfailure`](https://github.com/gaia-hazlab/da-seis-groundfailure) — the
  liquefaction / ground-failure modeling repo (hydrology + seismology + geotech).
- [`gaia-nhsm-deagg`](https://github.com/gaia-hazlab/gaia-nhsm-deagg) — USGS NSHM disaggregation
  client feeding the unconditional integration.
- `gaia-model-liquefaction` *(proposed)* — the GLM surrogate digital twin (conditional /
  unconditional / event-based runners).
- `gaia-vs-conus` *(proposed)* — the parametric $V_s$-profile product [@sanger2025vs].

*Proposed repositories do not exist yet — the names are placeholders for the team to
create/confirm.*

## Related

- [Pillar 2 — Nowcasting Hazard Susceptibility](pillar-2-nowcasting-susceptibility) — the science
  framing.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) ·
  [Groundwater & Soil Moisture](groundwater-soil-moisture) — the soil state and water-table this
  model consumes.
- [Liquefaction & Ground Failure](hazard-liquefaction-ground-failure) — the hazard page.
- [Data Inventory](datahub-inventory) — every input/output with sources,
  resolution, and the data-prep pipeline.
- [Landslide Model](modelhub-landslide) — the sibling model this one mirrors.
- [HazEvalHub](hazevalhub) — metric definitions.

## References
