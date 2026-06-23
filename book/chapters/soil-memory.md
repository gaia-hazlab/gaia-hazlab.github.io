# Soil Hydromechanical Memory

## 1. Critical Zone as Atmosphere-Solid Earth Gate.

The soil hydromechanical structure has a major control on how water flows through the soils to replenish the subsurface of groundwater, evaporate to bring moisture back to the lower atmosphere, or blocks water from traveling through soils, leading to erosion and flooding. Plants, animals, geomorphological, weathering, and tectonic processes alter dynamically the soil structure, which challenges predictive understanding of the soil's effect on natural hazards and atmospheric dynamics and justify the need to 1) **monitor its state in spate and time**, and 2) **characterize the governing and coupled processes**, so that we can predict hazards today and in the future.

## 2. Characterizing Soil Properties.

How can we characterize the soil properties?

- plants (NDVI)
- geological structure
- DEM


---

## 3. Turning seismic to saturation and water table


*Two implementation angles: (A) Distributed Acoustic Sensing (DAS) cross-sections and (B) Regional seismic networks*


We aim to estimate two key geohydrologic state variables using time-lapse shear-wave velocity:

1) **Water table depth**: $d_{wt}(x,t)$ (or hydraulic head $h(x,t)$)  
2) **Vadose-zone saturation in the top meter**: $S_w(x,z,t)$ for $z\in[0,1\ \text{m}]$

**Inputs**
- Time-lapse shear-wave velocity (or an equivalent velocity proxy):
  - DAS angle: $V_s(x,z,t)$ on a dense cross-section
  - Regional network angle: $V_s(\mathbf{r},z,t)$ or depth-averaged $dv/v(\mathbf{r},t)$ from coda-wave interferometry / ambient noise
- Rainfall time series $P(t)$ (optionally spatial $P(x,t)$ or $P(\mathbf{r},t)$)
- Soil and rock hydromechanical priors (porosity, density, retention curve parameters, acoustoelastic/poroelastic constants)
- Optional boreholes for anchoring baseline water table and/or moisture

**Core idea**
- Below the water table, time-lapse $dv/v$ is dominated by **poroelastic/acoustoelastic** sensitivity to pressure/head changes.
- Above the water table (top meter), time-lapse $V_s$ varies primarily with **saturation-dependent density** and **effective stress / suction** (capillary) effects.

We implement a **coupled inversion** that alternates between:
- estimating $d_{wt}(x,t)$ (or $h$) from saturated-zone $dv/v$, and
- estimating $S_w(x,z,t)$ in the top meter from a soil physics forward model.

---

### 1) Definitions and conventions

#### Coordinates
- $z$: depth (m), positive downward from ground surface.
- DAS cross-section: $x$ (along profile), $z$ (depth), time $t$.
- Regional network: horizontal location $\mathbf{r}=(x,y)$, depth $z$, time $t$.

#### Velocity perturbation
Select a baseline time $t_0$ and define:
$$
\Delta v(\cdot,t) = \frac{V_s(\cdot,t) - V_s(\cdot,t_0)}{V_s(\cdot,t_0)}.
$$
When only coda time shifts are available, use:
$$
\frac{\Delta t}{t} = -\frac{\Delta v}{v}.
$$

---

### 2) Physical model components

We treat the observed velocity perturbation as a superposition of hydrologic contributions, optionally augmented with correction factors:
$$
\Delta v_{\text{obs}} \approx \Delta v_{\text{sat}} + \Delta v_{\text{pe}} \quad (+\ \text{thermal / other terms if needed}),
$$
and optionally:
$$
\Delta v_{\text{obs}} \approx \chi_{\text{sat}}\Delta v_{\text{sat}} + \chi_{\text{pe}}\Delta v_{\text{pe}}.
$$
This “physics + correction factor” framing is valuable when rock physics over/underestimates effective-stress transmission or coupling strength.

---

### 3) Saturated-zone mapping: $dv/v \rightarrow \Delta h \rightarrow d_{wt}$

#### 3.1 Poroelastic/acoustoelastic link
Assume the hydrologic component in the saturated zone follows a proportionality:
$$
\left(\frac{dv}{v}\right)_{\text{hyd}} = -\frac{S_{sk}\,\beta}{B}\,\Delta h,
$$
where:
- $S_{sk}$: skeletal specific storage (or an equivalent sensitivity factor)
- $\beta$: acoustoelastic parameter (velocity sensitivity to volumetric strain)
- $B$: Skempton coefficient
- $\Delta h$: change in hydraulic head (m)

Thus:
$$
\Delta h = -\frac{B}{S_{sk}\,\beta_{\text{eff}}}\left(\frac{dv}{v}\right)_{\text{hyd}}.
$$

**Optional correction factor**
If applying a correction (e.g., to handle partial connectivity / attenuation of stress transmission),
$$
\beta_{\text{eff}} = \chi_{\text{pe}}\,\beta,
$$
with $\chi_{\text{pe}}$ either constant (site-calibrated) or a function of near-surface saturation.

#### 3.2 Robust depth aggregation (DAS cross-section)
Because velocity estimates at a given depth can be noisy, define a saturated-depth mask using the current water table estimate:
$$
\mathcal{Z}_{\text{sat}}(x,t) = \{z : z > d_{wt}(x,t) + \delta\},
$$
with a buffer $\delta$ (e.g., 0.2–0.5 m) to stay below the capillary fringe.

Compute a robust statistic:
$$
\overline{\Delta v}_{\text{sat}}(x,t) = \text{median}_{z\in\mathcal{Z}_{\text{sat}}}\left[\Delta v(x,z,t)\right].
$$
Then:
$$
\Delta h(x,t)= -\frac{B}{S_{sk}\beta_{\text{eff}}}\overline{\Delta v}_{\text{sat}}(x,t).
$$

#### 3.3 Convert head to water table depth
Let $d_{wt,0}(x)$ be the baseline water table depth at $t_0$. Then:
$$
d_{wt}(x,t)=d_{wt,0}(x)-\Delta h(x,t).
$$
(Head rise $\Delta h>0$ makes the water table shallower.)

---

### 4) Vadose-zone mapping in the top meter: $V_s \rightarrow S_w$

We use:
$$
V_s = \sqrt{\frac{G}{\rho_b}},
$$
with saturation-dependent bulk density $\rho_b(S_w)$ and stiffness $G$ controlled by an effective pressure $P_e$ that accounts for suction and dynamic capillarity.

#### 4.1 Bulk density mixing
$$
\rho_b(S_w) = (1-\phi)\rho_s + \phi\left(S_w\rho_w + (1-S_w)\rho_a\right),
$$
where:
- $\phi$ porosity
- $\rho_s$ solid grain density
- $\rho_w$ water density
- $\rho_a$ air density

#### 4.2 Effective saturation and capillary pressure
Define effective saturation:
$$
S_e = \frac{S_w - S_r}{1 - S_r},\quad S_e\in[0,1],
$$
where $S_r$ is residual saturation.

Use a van Genuchten soil-water retention curve:
$$
P_c(S_e) = \frac{1}{\alpha}\left(S_e^{-1/m}-1\right)^{1/n}.
$$
($\alpha,n,m$ depend on texture and are calibrated from priors/boreholes.)

#### 4.3 Effective pressure including suction and dynamics
Use:
$$
P_e = \sigma - p - S_e P_c + \tau \frac{dS_w}{dt},
$$
where:
- $\sigma$ mean confining stress (often approximated from overburden)
- $p$ pore pressure (often ~0 gauge in vadose zone)
- $\tau$ dynamic capillary coefficient (optional; increases temporal coupling)

#### 4.4 Stiffness closure
A stable, commonly used closure is a Hertz–Mindlin-like power law:
$$
G(P_e) = G_{\text{ref}}\left(\frac{P_e}{P_{\text{ref}}}\right)^{n_{\text{exp}}},\quad n_{\text{exp}}\approx 1/3.
$$
Clip $P_e$ to a small positive value to avoid nonphysical results.

#### 4.5 Forward model
Given $S_w$ and $\dot S_w$:
$$
V_s^{\text{pred}}(S_w) = \sqrt{\frac{G(P_e(S_w,\dot S_w))}{\rho_b(S_w)}}.
$$

#### 4.6 Inversion for $S_w$ (time-recursive)
For each $x$, each depth $z\in[0,1\ \text{m}]$, and each time step $t_k$:

- If $z \ge d_{wt}(x,t_k)$: enforce **saturation** $S_w=1$.
- Else solve a bounded root problem:
  $$
  V_s^{\text{pred}}(S_w) - V_s^{\text{obs}}(x,z,t_k)=0,\quad S_w\in[S_r,1].
  $$
- Approximate:
  $$
  \dot S_w \approx \frac{S_w(t_k)-S_w(t_{k-1})}{\Delta t}.
  $$
This makes the inversion mildly implicit in time (through the dynamic term).

---

### 5) Rainfall as a dynamical prior (stabilization)

Velocity-derived saturation can be noisy; rainfall provides a physically meaningful prior. A minimal “bucket + relaxation” model:

$$
S_w^{\text{prior}}(t_k) = S_w^{\text{prior}}(t_{k-1}) + \gamma\,P(t_k) - \frac{S_w^{\text{prior}}(t_{k-1})-S_{w,\text{fc}}}{\tau_{\text{dry}}}\Delta t,
$$
clipped to $[S_r,1]$, where:
- $\gamma$ infiltration scaling (calibrated; depends on rainfall units)
- $S_{w,\text{fc}}$ field capacity saturation
- $\tau_{\text{dry}}$ drying timescale

Use this prior to:
- initialize the root solve,
- penalize unrealistic jumps in $S_w$,
- help interpret storm response.

---

### 6) Coupled inversion algorithm (explicit workflow)

#### Inputs
- $V_s$ (DAS: $V_s(x,z,t)$; Network: $dv/v(\mathbf{r},t)$ or $V_s(\mathbf{r},z,t)$ if available)
- Rainfall $P(t)$ or $P(\mathbf{r},t)$
- Priors: $\phi,\rho_s,S_r,\alpha,n,m,\tau,G_{\text{ref}},P_{\text{ref}},n_{\text{exp}},S_{sk},\beta,B$
- Baseline water table depth $d_{wt,0}$

#### Iterative scheme (per $x$ or $\mathbf{r}$)
1. Compute $\Delta v$ relative to baseline.
2. Initialize $d_{wt}^{(0)}(t)=d_{wt,0}$.
3. Repeat for $i=0,\dots,N_{\text{iter}}-1$:
   - **(A) Update head / water table**
     - compute robust saturated-zone $\overline{\Delta v}_{\text{sat}}(t)$
     - $\Delta h^{(i)}(t)=-(B/(S_{sk}\beta_{\text{eff}}))\overline{\Delta v}_{\text{sat}}(t)$
     - $d_{wt}^{(i+1)}(t)=d_{wt,0}-\Delta h^{(i)}(t)$
   - **(B) Update saturation in the top meter**
     - for each $z\le 1$ m and time, invert $S_w^{(i+1)}(z,t)$ from $V_s$
     - enforce $S_w=1$ for $z\ge d_{wt}^{(i+1)}(t)$
   - Optionally update $\chi_{\text{pe}}$ from shallow $S_w$ (if using correction factors).
4. Output $d_{wt}(t)$ and $S_w(z,t)$ (top 1 m).

---

### 7) Two angles: DAS cross-section vs regional network

#### Angle A — DAS cross-section (dense spatiotemporal imaging)

**Typical data product**
- $V_s(x,z,t)$ or $dv/v(x,z,t)$ at high spatial sampling (meters to tens of meters) and high cadence.

**Advantages**
- Water table tracking can leverage depth dependence: saturated zone is directly sampled.
- Vadose saturation inversion can be done per depth in top 1 m.
- Spatial continuity allows strong regularization in $x$, improving stability.

**Practical pipeline**
1. DAS preprocessing (noise correlation / surface-wave dispersion / inversion) → $V_s(x,z,t)$
2. Choose baseline $t_0$; compute $\Delta v(x,z,t)$
3. Coupled inversion:
   - $d_{wt}(x,t)$ from saturated depths (median over $z>d_{wt}+\delta$)
   - $S_w(x,z\le 1\text{m},t)$ from vadose physics
4. Outputs:
   - time-lapse cross-sections: $V_s$, $\Delta v$, and $d_{wt}$ overlay
   - shallow saturation panels
   - event response to storms

**Recommended regularization**
- Smoothness of $d_{wt}(x,t)$ in $x$ (water table is not wildly jagged)
- Temporal smoothness of $S_w$ (except during sharp storm infiltration)
- Optional constraints: $S_w\to 1$ approaching the capillary fringe

---

#### Angle B — Regional seismic networks (distributed stations, larger scale)

**Typical data products**
- Coda-wave interferometry or ambient noise yields:
  - station-pair $dv/v(t)$ (path-averaged)
  - regional maps of $dv/v(\mathbf{r},t)$ via tomographic inversion
- Depth sensitivity is weaker than DAS unless multi-band methods or depth kernels are used.

**What changes**
- You typically have **less direct depth resolution**, so you must:
  - treat $dv/v(\mathbf{r},t)$ as a **weighted integral over depth**:
    $$
    \Delta v(\mathbf{r},t) \approx \int K(z)\,\Delta v(\mathbf{r},z,t)\,dz,
    $$
    where $K(z)$ is a sensitivity kernel (from surface-wave modes, scattering depth sensitivity, etc.).
  - restrict the inversion to **a small number of latent hydrologic parameters**, e.g.:
    - $d_{wt}(\mathbf{r},t)$
    - a depth-averaged top-meter saturation $\overline{S_w}(\mathbf{r},t)$

**Regional inversion approach**
1. Compute regional $dv/v(\mathbf{r},t)$ maps (or station-pair measurements + kernel weights).
2. Use rainfall $P(\mathbf{r},t)$ and a bucket model to build a prior for shallow saturation.
3. Use a simplified two-component model:
   $$
   \Delta v_{\text{obs}}(\mathbf{r},t) \approx a(\mathbf{r})\,\Delta h(\mathbf{r},t) + b(\mathbf{r})\,\Delta \overline{S_w}(\mathbf{r},t),
   $$
   where $a,b$ are calibration coefficients informed by local geology/priors.
4. Convert $\Delta h \rightarrow d_{wt}$ using baseline constraints (boreholes / hydrologic models).
5. Validate with independent data: groundwater wells, soil moisture products, streamflow, evapotranspiration.

**Key distinction vs DAS**
- DAS supports explicit depth partition (vadose vs saturated).  
- Regional networks generally require kernel-weighted or parameter-reduced inversion.

---

### 8) Calibration strategy (what must be anchored)

#### Essential calibrations
- **Saturated mapping constants**: $S_{sk}\beta/B$ (or equivalently $S_{sk},\beta,B$)
  - Fit using well head changes where available.
- **Vadose parameters**: $\phi,\rho_s,S_r,\alpha,n,m$, and stiffness closure $G_{\text{ref}},n_{\text{exp}}$
  - Fit using shallow soil moisture sensors, lab curves, texture-based priors.

#### Recommended anchoring measurements
- At least one well or piezometer for $d_{wt,0}$ and head changes.
- One shallow moisture sensor profile (even temporary) for $S_w$ validation.
- Soil texture estimates to set priors for van Genuchten parameters.

---

### 9) Diagnostics and sanity checks

#### For water table
- In the saturated zone, inferred $\Delta h$ should be approximately depth-invariant (hydrostatic consistency).
- Spatial continuity: $d_{wt}$ should vary smoothly in $x$ unless strong hydrogeologic contrasts exist.
- Event response: head rise should follow storms with a plausible lag.

#### For saturation
- $S_w\in[S_r,1]$ always.
- Storm response: sharp wetting near surface and slower drainage.
- Consistency: $S_w\to 1$ approaching the water table (capillary fringe behavior).

#### For model mismatch
- If saturation inversion repeatedly hits bounds or cannot bracket solutions:
  - revisit stiffness closure parameters and/or $\sigma(z)$
  - smooth $V_s$ in time
  - reduce or disable dynamic term $\tau \dot S_w$
  - incorporate rainfall prior more strongly

---

### 10) Suggested student/postdoc exercises

1. **Synthetic test (DAS)**
   - Choose a truth $d_{wt}(x,t)$ and $S_w(x,z,t)$.
   - Forward simulate $V_s$.
   - Invert and quantify error sensitivity to noise and parameter misspecification.

2. **Storm event analysis**
   - Identify storm windows.
   - Compare inferred $d_{wt}$ and top-meter $S_w$ responses:
     - lag time
     - peak magnitude
     - recovery timescale

3. **Regional upscaling**
   - Using a regional $dv/v(\mathbf{r},t)$, invert for two latent time series:
     - $\Delta h(\mathbf{r},t)$
     - $\overline{S_w}(\mathbf{r},t)$
   - Compare spatial patterns against precipitation and known aquifer properties.

4. **Parameter identifiability**
   - Which parameters trade off most strongly (e.g., $G_{\text{ref}}$ vs $\alpha$, $S_{sk}$ vs $\beta$)?
   - Use posterior sampling (MCMC) on a single column to visualize uncertainty.

---

### 11) Practical implementation notes

#### Recommended data structures
- Use `xarray` datasets:
  - `Vs(x,z,t)` and `dvv(x,z,t)`
  - `dwt(x,t)`
  - `Sw_top(x,z_top,t)` where `z_top = z[z<=1m]`

#### Numerical stability tips
- Use robust medians for saturated depth averaging.
- Use bounded root solves (`brentq`) for $S_w$.
- Apply temporal smoothing to $V_s$ and/or $S_w$ if needed.
- Keep units consistent: $z$ meters, $t$ seconds, rainfall in mm per time step (document conversions).

---

### 12) Limitations and extensions

**Limitations**
- Depth sensitivity assumptions are strongest for DAS cross-sections and weaker for regional networks.
- Separability between poroelastic and saturation effects can break down near the capillary fringe.
- Thermal and freeze/thaw effects can contaminate $dv/v$ in some environments; add thermal terms when necessary.

**Extensions**
- Add a thermal component and jointly estimate temperature-driven velocity changes.
- Replace the simple stiffness closure with a full Hertz–Mindlin + cementation model.
- Use spatial regularization (e.g., TV or Laplacian) across $x$ and time for robust imaging.

---

### References (papers driving the framework)
- Saturation/density/effective pressure and dynamic capillarity in near-surface velocity response [@shi2025].
- Poroelastic + nonlinear elasticity mapping from $dv/v$ to hydraulic head / pore pressure [@clements2023]; see also tracking groundwater levels from the ambient field [@clements2018].
- Physics-guided + data-driven correction factors for component models and stress-transmission biases [@sun2025].

---
