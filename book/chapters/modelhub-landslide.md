# Landslide Model — Landlab Implementation

:::{note}
**The model-side companion to the landslide digital twin.** This page is the ModelHub home for
the **shallow + deep-seated** landslide susceptibility model: the equations it solves, the
raw-and-derived data it uses, what is *solved* versus *assumed* inside
[Landlab](https://landlab.csdms.io), how it couples to the other GAIA projects (soil
hydromechanical memory, liquefaction, the weather/forecast leg), the spatial-domain
constraints (watershed / single-drainage closed systems), where Landlab limits a digital twin,
how to make it interoperable with **Earth2Studio**, and how predictions are evaluated.

It builds on the science in [Pillar 2 §2](pillar-2-nowcasting-susceptibility), draws on the
state from [Pillar 1](pillar-1-soil-reanalysis), and reads the data cataloged in the
[Data Inventory](datahub-inventory). **Post-fire debris flows** are a
specialized case on their [own page](hazard-postfire-debris-flows) — the core shallow/deep
model below takes **no burn-severity input**.
:::

## 1. What the model computes (and what it does not)

The product is a single field: the **probability of failure**
$P_f = \Pr(FS<1)\in[0,1]$ — a continuous susceptibility surface, *not* a binary map and *not* a
runout footprint. It is produced by Landlab's `LandslideProbability` component [@strauch2018]
driven by a hydrology closure that sets the **relative wetness** of the soil column.

**Shallow** and **deep-seated** landslides run the *same* stability engine and differ only in
the hydrology closure and the soil-column depth $D$ (§2.5):

- **Shallow** — failure in the 0.5–3 m soil mantle, triggered by storm infiltration; wetness
  from a steady-state *topographic* index.
- **Deep-seated** — failure meters–tens of meters down, controlled by groundwater head on
  seasonal–multiyear scales; wetness from the *water-table* field of the
  [Soil Reanalysis Product](pillar-1-soil-reanalysis).

What the model does **not** do: it does not solve transient 3-D groundwater flow, does not
mobilize or route the failed mass (runout), and does not by itself ingest a forecast — those
are coupling and extension problems addressed in §5–§7.

## 2. The physics — the equations we solve

The pipeline is a chain of three physical problems on one shared grid: a **hillslope water
balance** that turns precipitation into recharge, a **topographic wetness** closure that turns
recharge into a saturation state, and an **infinite-slope stability** calculation that turns
wetness into a probability of failure.

### 2.1 Hillslope water balance (ecohydrology)

The `SoilMoisture` + PET components solve a root-zone bucket balance — the whiteboard equation
$L\,\dot S = P - R - Q$ written explicitly. For a root zone of depth $Z_r$ and porosity $n$,
the degree of saturation $S\in[0,1]$ evolves as

$$
n\,Z_r\,\frac{\partial S}{\partial t} \;=\; I \;-\; \mathrm{ET}(S) \;-\; L_z(S) \;-\; Q_s ,
$$

where $I$ is the infiltrating water input, $\mathrm{ET}(S)$ actual evapotranspiration (PET
modulated by water stress and vegetation), $L_z(S)$ deep leakage below the root zone, and $Q_s$
saturation-excess surface runoff. The infiltrating input is the rain-plus-melt term from the
snow partition,

$$
I = P_{\text{rain}} + M, \qquad
P_{\text{rain}} = P\,(1-f_{\text{snow}}), \quad
P_{\text{snow}} = P\,f_{\text{snow}},
$$

with $f_{\text{snow}}$ a linear rain–snow fraction between threshold temperatures
$T_{\text{snow}}$ and $T_{\text{rain}}$, and snowmelt $M$ from a degree-day model
($M = \text{melt\_factor}\cdot\max(T-T_{\text{base}},0)$, bookkept as
$SWE_t = SWE_{t-1}+P_{\text{snow}}-M$).

The **recharge** that forces slope stability is the deep leakage, summarized over the antecedent
window $\{t-k_N,\dots,t_0\}$ (the soil-memory window of [Pillar 1](soil-memory)):

$$
R = \big\langle L_z(S) \big\rangle_{\text{window}} \quad(\text{mean or max}).
$$

Drainage onset and stress thresholds are set by the field-capacity and wilting saturations
$S_{fc}=\theta_{fc}/n$, $S_{wp}=\theta_{wp}/n$ derived from soil properties.

### 2.2 Topographic relative wetness (the shallow closure)

Following steady-state shallow subsurface flow [@beven1979; @montgomery1994], the relative
wetness $w$ (saturated fraction of the soil column) rises with recharge and upslope contributing
area and falls with transmissivity and slope:

$$
w = \min\!\left(\frac{R}{T}\,\frac{a}{b}\,\frac{1}{\sin\theta},\; 1\right),
$$

with soil transmissivity $T = K_{sat}\,D$ (the code uses $T=K_{sat}\cdot 2.5\cdot h_s$ with a
floor), **specific contributing area** $a/b$ — upslope drainage area per unit contour width,
obtained from flow routing on the DEM (§5) — and slope $\theta$. This is the SHALSTAB/SINMAP
family [@montgomery1994; @pack1998]; the unsaturated extension through suction stress is
[@lu2008; @iverson2000].

The crucial point for the digital twin: $w$ depends on the **routed** contributing area $a/b$,
which only has meaning over a hydrologically complete domain — this is what forces the watershed
framing of §5.

### 2.3 Infinite-slope factor of safety

On a planar failure surface at slope $\theta$, the factor of safety is the ratio of resisting to
driving stress, in the dimensionless form of the Landlab component [@strauch2018]:

$$
FS = \frac{\tilde C}{\sin\theta\cos\theta}
   + \left(1 - w\,\frac{\rho_w}{\rho_s}\right)\frac{\tan\phi}{\tan\theta},
$$

where $\tilde C = (C_r + C_s)/(\rho_s g D)$ is combined root + soil cohesion normalized by the
saturated soil weight, $D$ the soil (column) depth, $\phi$ the internal friction angle,
$\rho_s,\rho_w$ soil and water densities, and $w$ the relative wetness from §2.2. Failure is
expected when $FS<1$. Increasing wetness $w$ lowers effective stress and drives $FS$ down — the
hydromechanical coupling that links water to strength [@lu2010].

### 2.4 From factor of safety to probability of failure

The inputs $R, T, \tilde C, \phi$ are uncertain. `LandslideProbability` draws them from
distributions (cohesion as a triangular min/mode/max; recharge as a spatial distribution with
$\sigma = 0.1\,\mu$ in the current setup) and runs a **Monte Carlo** ensemble of $N$ iterations
(default 1000), yielding a distribution of $FS$. The susceptibility is the failure fraction:

$$
P_f = \Pr(FS<1) \approx \frac{1}{N}\sum_{i=1}^{N}\mathbb{1}\!\left[FS^{(i)}<1\right],
$$

with two diagnostic by-products: the **mean relative wetness** $\bar w$ and the **probability of
saturation** $\Pr(w\ge1)$. $N$ controls only sampling noise — it is a convergence knob, **not** a
calibration parameter.

### 2.5 Shallow vs deep-seated: one engine, swapped closure

| | **Shallow** | **Deep-seated** |
|---|---|---|
| Soil-column depth $D$ | thin (soil mantle, 0.5–3 m) | thick (to the deep rupture surface) |
| Wetness $w$ from | steady-state topographic index (§2.2) | water-table / head $h(x,t)$ — imported from [Pillar 1](pillar-1-soil-reanalysis) or solved on-grid (§6.1) |
| Dominant uncertain params | recharge $R$, transmissivity $T$, root+soil cohesion | head $h$, deep strength, transmissivity at depth |
| Timescale of forcing | hours–days (event) | seasonal–multiyear (memory-rich) |
| Burn-severity input | **No** | **No** |

This is why both live in one model: the difference is the **wetness closure and the depth**, not
a different solver.

## 3. What is solved vs. assumed inside Landlab

Each Landlab component reads and writes named fields on the shared grid. The table makes the
**solved / assumed** split explicit so a reviewer knows where the physics is real and where it
is parameterized.

| Component | What it *solves* | What it *assumes* | Key fields out |
|---|---|---|---|
| `FlowAccumulator` (+ `FlowDirector`) | flow routing, drainage area, specific contributing area | a routing rule (single- vs multiple-flow direction); hydrologically complete domain with defined outlet (§5) | `drainage_area`, `surface_water__discharge` |
| snow (degree-day) | rain/snow partition, SWE, melt | linear temperature partition; degree-day melt; no energy-balance snowpack | `swe`, `water_input` |
| `SoilMoisture` + PET | root-zone water balance (§2.1) | single bucket per PFT; `ksat_factor` infiltration scaling; PET from prescribed vegetation parameters | `soil_moisture__saturation_fraction`, `…root_zone_leakage` (→ recharge) |
| recharge routing | upslope-averaged recharge | recharge can be advected by topographic routing (`routed_recharge = discharge/area`) | `groundwater__recharge_mean/std` |
| `LandslideProbability` | infinite-slope $FS$ + Monte Carlo $P_f$ (§2.3–2.4) | planar slope-parallel failure; steady-state wetness; parameters independent across draws | `landslide__probability_of_failure`, `soil__mean_relative_wetness` |

For the deep-seated variant the topographic-wetness assumption is replaced by a **water-table /
head field** $h(x,t)$ — either imported from [Pillar 1](pillar-1-soil-reanalysis) or **solved
on-grid** with Landlab's transient `GroundwaterDupuitPercolator` component (§6.1). What Landlab
does *not* solve is full 3-D variably-saturated (Richards) flow (§6.2).

## 4. Coupling map — where the other GAIA projects plug in

The landslide model is one of several models that draw on a shared soil state. Three couplings matter, and each
attaches at a specific field in the chain above.

**(a) The weather / forecast angle.** Precipitation $P$ (and $T_{min}/T_{max}$) is the proximate
trigger and the only fast-dynamic input. In hindcast/nowcast it is observed PRISM; in forecast it
is AI-weather precipitation from the Earth2Studio leg (§7). Either way it enters at the **snow /
water-balance** step (§2.1) after downscaling to the working grid and conversion to mm/day. The
antecedent window $\{t-k_N,\dots,t_0\}$ on the whiteboard is exactly the **soil-memory** integral
that makes today's recharge depend on prior weather [@guzzetti2008].

**(b) Soil hydromechanical memory** ([soil-memory](soil-memory)). The time-lapse-seismic
inversion turns $dv/v$ into the two state variables this model needs as **priors and calibration
targets**: vadose-zone saturation $S_w(x,z,t)$ and water-table depth $d_{wt}(x,t)$. For the
**shallow** model, $S_w$ initializes and calibrates the water balance (§2.1) — the
$S\!\to\!\text{SMAP}$ check on the whiteboard. For the **deep-seated** model, $d_{wt}/h$ *is* the
wetness closure (§2.5). This is the direct line from Pillar 1's mechanical state to the cohesion
and effective-stress terms in $FS$ [@lu2010].

**(c) Liquefaction & ground failure** ([hazard page](hazard-liquefaction-ground-failure),
[Pillar 2 §3](pillar-2-nowcasting-susceptibility)). Liquefaction shares the **same antecedent
hydromechanical state** — saturation and water-table depth — but couples it to a *seismic*
ground-motion field (PGA/PGV) rather than rainfall recharge. The shared design pattern is the
reuse: both are "soil state + trigger → probability of failure" models reading the Pillar 1
product; the landslide engine's Monte-Carlo-over-uncertain-strength structure is the template the
liquefaction surrogate [@sanger2025jgge; @sanger2026geoai] can mirror. A future **seismic
trigger** for landslides (PGA/Arias as an additional destabilizing term) is the natural place the
two tracks merge.

## 5. Spatial domain — drainage, watersheds, and closed systems

**Yes — the hydrology must be solved on a hydrologically closed unit with a single outlet.** The
relative wetness $w$ (§2.2) depends on the **specific contributing area** $a/b$, which is the
integral of all upslope flow reaching a node. That integral is only well-defined if every
interior node's drainage path stays inside the modeled domain until it leaves through a known
outlet.

The practical consequences for Landlab:

- **Use watersheds / subwatersheds (HUCs) as the model unit.** A watershed clipped to its outlet
  is a closed system: set the outlet node as the single **open** boundary and **close** all other
  boundaries, so `FlowAccumulator` routes all interior recharge to that one outlet (the "HUC $i$"
  on the whiteboard). Contributing area is then physically correct.
- **Do not tile arbitrarily.** Rectangular tiles cut flow paths at their edges: water that should
  cross the boundary is lost, contributing area is underestimated near edges, and $w$ — hence
  $P_f$ — is biased low along every tile seam. Tiles are fine for *storage and ML inference
  chunking*, but **not** for the routing step.
- **Routing rule matters.** A single-flow director (D8/steepest descent) concentrates flow into
  one downslope neighbor; a multiple-flow director (Dʞ / D-infinity) spreads it. Convergent
  hollows — where shallow failures preferentially initiate — are sensitive to this choice, so it
  should be set deliberately and recorded.
- **Boundary-condition realism.** The current notebook uses an elevation cutoff (337 m) to define
  routing boundaries; this kind of structural choice should be **validated against the known
  outlet/watershed geometry before** any hydrologic calibration (it changes $a/b$ everywhere
  upstream).
- **Regional coverage = mosaic of closed runs.** For PNW-wide products, run per-watershed (with a
  one-cell halo if cross-divide flow matters), then mosaic — rather than running one giant grid
  with artificial edges. This is also the unit at which the hybrid coarse-screening / targeted
  high-res strategy is organized.

## 6. Where Landlab limits a digital twin — and what is actually removable

Several "limits" people attribute to Landlab are really properties of the **current closure
choice** (the steady-state topographic wetness inside `LandslideProbability`, §2.2), not of
Landlab itself. They are worth separating, because most are removable by adding components — and
only a few are genuine.

### 6.1 Removable — add a component or wrap the I/O

- **Steady-state wetness → transient.** The instantaneous recharge↔wetness equilibrium is the
  TOPMODEL-style closure in `LandslideProbability` (§2.2), not a Landlab constraint. Drive the
  chain with **daily / sub-daily rainfall** and step the hydrology, and the forcing is already
  transient; the wetness becomes quasi-transient with one stability solve per timestep.
- **Transient groundwater & a real water table.** Landlab ships the
  **`GroundwaterDupuitPercolator`** component, which solves transient Dupuit–Forchheimer flow for
  an unconfined aquifer with a free water table, coupled recharge, and seepage. Coupling it lets
  us **solve** the deep-seated water table $h(x,t)$ on-grid instead of only importing it — turning
  "no transient groundwater" from a limitation into a modeling choice. [Pillar 1](pillar-1-soil-reanalysis)
  then becomes an **assimilation / calibration target** for that water table rather than its sole
  source.
- **Cloud-native.** This is pure engineering, not a limitation: wrap the run for COG / Zarr / STAC
  I/O on `s3://cresst` (the `landlab-debrisflow` → DataHub alignment task). No physics obstacle.

### 6.2 Genuine residual limits — design around these

- **Dupuit ≠ full 3-D Richards.** The groundwater component is **depth-integrated** (hydrostatic,
  mostly-lateral flow) — a large step up from steady-state, but not full 3-D variably-saturated
  flow [@richards1931]. Strongly layered, perched, or deep fractured-rock systems may still need
  an external 3-D model (ParFlow-class) or the Pillar 1 product.
- **Infinite-slope / triggering only.** `LandslideProbability` predicts *initiation*: planar
  slope-parallel failure, no 3-D failure surface, and **no runout** — mobilization and travel
  distance are separate physics (a dedicated runout component or model).
- **Differentiability & throughput.** Native components are NumPy / CPU and **not autodiff-able**,
  so Landlab cannot sit *inside* a gradient-based or torch-tensor forecast graph; cost scales with
  node count, so PNW-wide daily high-resolution stays expensive. This — not the hydrology caveats
  above — is the real motivation for a differentiable **surrogate** (§7).
- **Uncertainty only where parameterized.** Monte Carlo covers the chosen uncertain parameters;
  structural error (closure choice, DEM, soil priors) is not propagated automatically.

**Net:** with a daily-rainfall + transient-groundwater closure and a cloud-native wrapper, the
operative limits shrink to (i) Dupuit vs full 3-D, (ii) triggering-only / no runout, and
(iii) differentiability/throughput. The design response is the **hybrid**: keep Landlab as the
trusted reference and label generator; add a differentiable ML surrogate for regional screening,
ensembles, and the Earth2Studio loop (§7); and expose both through a provider interface.

## 7. Interoperability with Earth2Studio — invoking a future land digital twin

[Earth2Studio](https://github.com/NVIDIA/earth2studio) (NVIDIA) is an inference framework for
AI weather/climate models built around four composable pieces: **data sources**, **prognostic
models** (advance the atmospheric state), **diagnostic models** (map a state to a derived
quantity), and an **IO / coupling** layer operating on GPU/torch tensors. The path to a land
digital twin that Earth2Studio can *invoke* is to express the landslide pipeline as a
**diagnostic model** hanging off the atmospheric forecast:

1. **Forcing via a provider interface.** Wrap precipitation acquisition (PRISM hindcast or
   Earth2Studio prognostic output `tp`/`APCP`) behind one provider API so observed and forecast
   forcing are interchangeable — never hard-wire a single source.
2. **Downscale & convert.** Regrid the 0.25° (~25 km) global / 3 km regional precipitation to the
   working watershed grid and convert accumulation conventions to mm/day, preserving
   `init_time`, `lead_time`, `valid_time`, `model_name`, `forecast_version`.
3. **Recharge bridge.** Apply the §2.1 water balance / recharge conversion as a stateless operator
   that carries antecedent wetness across forecast lead times.
4. **Land "diagnostic model."** Expose `P_f = f(static layers, recharge, soil state)` with the
   Earth2Studio diagnostic signature. Back it with **either** the Landlab backend (reference,
   CPU) **or** a torch surrogate (fast, differentiable, GPU) trained on accumulated Landlab runs —
   the surrogate is what lets the land DT run at ensemble × lead-time scale inside the E2S graph.
5. **IO to Zarr/STAC.** Emit `landslide__probability_of_failure[init_time, lead_time, y, x]`
   through an Earth2Studio IO backend to the same `s3://cresst` Zarr/STAC the DataHub serves.

The result is a **coupled atmosphere→land forecast**: Earth2Studio advances the weather, and the
land diagnostic turns each forecast precipitation field into a forecast susceptibility — a future
land digital twin invoked from the same orchestration as the weather model. Landlab remains the
reference used to generate surrogate labels and to audit high-risk areas.

## 8. Evaluation & metrics

Evaluation separates two checks that are routinely conflated — **calibration** of the
*intermediate physical states* and **validation** of the *prediction* — because they use
different data and answer different questions. Full metric definitions live in
[HazEvalHub](hazevalhub).

**Calibration (intermediate states, before any hazard claim).** Tune the hydrology against
independent observations, in sequence: match event-start soil moisture and the soil-moisture
trajectory against **SMAP** ($S\to$ SMAP on the whiteboard); calibrate the snow timing against
**ERA5 SWE**; then the soil-water partition (`ksat_factor`, root-zone depths, field/wilting
thresholds). Metrics: RMSE, bias, temporal correlation, and storm-response lag. These never use
landslide labels.

**Validation (the prediction $P_f$, against independent landslide labels).** Labels are *never*
model inputs. Sources and how each scores $P_f$:

- **Probabilistic skill** — Brier score and reliability diagrams (is a 0.3 probability right 30%
  of the time?), and ROC-AUC / **precision–recall** (PR is the honest choice for rare failures).
- **Deterministic skill** at a decision threshold — POD, FAR, CSI.
- **Spatial agreement** — IoU / Dice of thresholded $P_f$ against mapped failure polygons.
- **Temporal skill** — alert **lead time** for the forecast product.

Label sources, in increasing directness:

- **Remote-sensing change detection** — Sentinel-1 InSAR/SAR and optical change masks
  [@mondini2021; @handwerger2022] (the "Sentinel … landslide map detection → GTD" path on the
  whiteboard, building a **ground-truth-data grid** of event / non-event cells).
- **Lidar / DEM differencing** — pre- vs post-event elevation $\Delta e = e_{\text{pre}} -
  e_{\text{post}}$ and storage change $\Delta S_x$, flagging erosion/initiation where the change
  exceeds a threshold (the whiteboard's $d\Delta\phi_i < -0.05 \Rightarrow$ erosion rule)
  [@bernard2021]; the most direct initiation evidence where repeat lidar exists.
- **Inventories** — USGS / WA DNR mapped landslide locations for historical backtesting.

The **highest-value validation target is mapped initiation location** — recharge-scenario choice
(local vs routed), cohesion reduction, and strength fields should ultimately be judged there,
while intermediate hydrology is judged against SMAP/SWE.

## Related

- [Pillar 2 — Nowcasting Hazard Susceptibility](pillar-2-nowcasting-susceptibility) — the science
  framing and three-process taxonomy.
- [Pillar 1 — Soil Reanalysis Product](pillar-1-soil-reanalysis) ·
  [Soil Hydromechanical Memory](soil-memory) — the soil state and $dv/v$ inversion this model
  uses.
- [Landslides](hazard-landslides) · [Post-fire debris flows](hazard-postfire-debris-flows) ·
  [Liquefaction & Ground Failure](hazard-liquefaction-ground-failure) — the hazard pages.
- [Data Inventory](datahub-inventory) — every input/output with sources,
  resolution, and the **data-prep pipeline** that feeds this model.
- [HazEvalHub](hazevalhub) — metric definitions.
- Repos: [`landlab-debrisflow`](https://github.com/gaia-hazlab/landlab-debrisflow) ·
  [`landslide-digital-twin`](https://github.com/gaia-hazlab/landslide-digital-twin) ·
  [`fire-debrisflow-ml`](https://github.com/gaia-hazlab/fire-debrisflow-ml).

## References
