# Programs & Partners

> GAIA sits inside a constellation of projects, seed grants, and facility partnerships.
> This doc draws the boundary: **what the GAIA operating system actively coordinates**
> (CSSI + CRESST), versus **lineage/affiliated programs** we contextualize but don't run,
> versus **facility & network partners** we integrate with. Keeps the
> [coordination plan](01-project-coordination.md) honest about scope.
>
> Placeholders marked `‹confirm›` are facts I won't invent — fill or cut. Mirrors the
> welcome-deck lineage slide ([welcome-deck/README.md §4](welcome-deck/README.md)).

## 1. The tiers at a glance

| Tier | Program / entity | Lead | GAIA coordination |
|---|---|---|---|
| **Core** | **GAIA-CSSI** (NSF CSSI) | **Marine Denolle (UW)** | Full operating system — this repo |
| **Core** | **CRESST** (UW seed / FFST) | **Marine Denolle (UW)** | Full operating system — shares boards, cadence, metrics |
| Lineage | **SCOPED** | **Carl Tape** (UAF; **new co-PI**) | Proven model we inherit; loosely coupled |
| Lineage | **GeoSMART** | **Nicoleta Cristea** (UW) | ML training / hackweeks lineage |
| Lineage | **CAIG / FAIM-WG** (wildfire geohazards) | **Erkan Istanbulluoglu** (UW) | Affiliated; align where useful |
| Partner (facility) | **EarthScope Consortium** | — | Data + station metadata (FDSN); RC1 co-lead role |
| Partner (facility) | **Alaska Satellite Facility (ASF)** (UAF) | — | SAR / InSAR (HyP3); Alaska expansion |
| Partner (network) | **PNSN** (Pacific NW Seismic Network) | — | Seismic + infrasound data; PNW use cases |
| Partner (network) | **AEC** (Alaska Earthquake Center) | — | Alaska seismic data; regional expertise |

## 2. Core — what GAIA actively coordinates

**GAIA-CSSI** and **CRESST** are both led by Marine Denolle and share **one** operating
system: the same GitHub org/boards, Slack, meeting cadence, templates, and
[Metrics Observatory](04-metrics-observatory.md). Treat them as a single coordinated
program with two funding lines — CSSI is the multi-institution expansion; CRESST is the
UW seed that de-risked it. Everything in docs [00](00-kickoff-plan.md)–[06](06-data-catalog.md)
applies to this core.

## 3. Lineage & affiliated programs — context, not command

We **contextualize** these (welcome deck, website lineage) and **borrow their playbooks**,
but we do not run their coordination:

- **SCOPED** — the direct methodological ancestor. It **bridged big data and big
  compute** — massive simulations on **HPC** (e.g. SPECFEM wavefields) and massive data
  mining on the **cloud** — but stopped **short of data assimilation**: it connected the
  two ends without fusing data into models in a decision-relevant loop. **That
  assimilation layer is precisely GAIA's advance** (the assimilative digital twin). GAIA
  also inherits SCOPED's container/hackweek model and its community-metrics dashboard
  (which the [Metrics Observatory](04-metrics-observatory.md) extends). **Carl Tape joins
  GAIA-CSSI as a co-PI**, making SCOPED the closest lineage program and the bridge for
  Alaska seismology.
- **GeoSMART** (Nicoleta Cristea) — ML-in-geoscience training + hackweeks; the education /
  broadening-participation lineage. Coordinate on shared training materials and hackweek
  logistics when calendars align.
- **CAIG / FAIM-WG** (Erkan Istanbulluoglu, UW) — *"Collaborative Research: CAIG:
  Framework for Artificial Intelligence-Enhanced Modeling of Wildfire Geohazards
  (FAIM-WG)."* Wildfire-geohazard AI modeling; natural science overlap (post-fire debris
  flows, soil/hydrology) — align on shared methods and data where it helps, no shared
  governance.
- **GeoSciCloud** (David Mencin, UNAVCO/IRIS → now **EarthScope**) — NSF **EarthCube**
  project evaluating facility-scale geoscience data + services in commercial (AWS) and
  private (XSEDE Jetstream) clouds. Direct **cloud-CI ancestry** for GAIA's laptop→cloud→HPC
  federation, and it runs through the same people as the **EarthScope partnership** (§4) —
  the lineage and the partner overlap here.

**Coordination touch:** lineage leads are welcome in the GAIA Slack and the monthly
project-wide update, invited to give talks, and listed on the website lineage — but they
are **not** on the funded-member reporting cadence ([01 §7](01-project-coordination.md)).

## 4. Partners — facilities & networks we integrate with

Formal, active technical partnerships (distinct from lineage):

- **EarthScope Consortium** — FDSN station metadata + seismic/GNSS data; co-leads the
  RC1 "repurpose seismic stations as soil sensors" thrust. Feeds the
  [Data Catalog](06-data-catalog.md) (`collect_fdsn.py`, GNSS).
- **Alaska Satellite Facility (ASF)** (under UAF) — SAR/InSAR via HyP3; the backbone of
  the Alaska + SAR expansion ([02](02-website-evolution.md), [06 §2.1](06-data-catalog.md)).
- **PNSN** — regional seismic + infrasound for Pacific-NW use cases (Nisqually, Stehekin).
- **AEC (Alaska Earthquake Center)** — Alaska regional seismic data + local expertise;
  natural partner for AEC/AK/AV network coverage in the catalog.

**Coordination touch:** each partner gets a dedicated Slack channel, a **quarterly CI/data
summary**, and an **annual architecture sync** ([01 §6](01-project-coordination.md)); data
standards are agreed in the [Data Catalog](06-data-catalog.md). Onboard via
[templates/partner-onboarding.md](templates/partner-onboarding.md).

## 5. Why the boundary matters

- **Scope control** — the funded reporting cadence and metrics apply to the **core**
  (CSSI + CRESST). Lineage/partners are engaged, not governed, so we don't over-promise
  coordination we can't staff ([01](01-project-coordination.md) is a lightweight,
  low-cost plan by design).
- **Attribution** — lineage programs get credited on the website + welcome deck; partners
  get co-authorship/acknowledgment per contribution. Keeps NSF broadening-participation
  and facility-integration stories accurate.
- **Metrics (M3)** — partners and lineage count toward *breadth/institutions* in the
  [Observatory](04-metrics-observatory.md), but only the core drives *delivery* (D1–D5).

## 6. Open items

- [x] ~~Confirm CAIG full name and Erkan's surname~~ — **CAIG / FAIM-WG**, Erkan
      Istanbulluoglu (UW).
- [x] ~~Confirm SCOPED co-PI role scope for Carl Tape~~ — Alaska seismology bridge; SCOPED
      = big-data↔big-compute lineage, GAIA adds the assimilation layer.
- [x] ~~Confirm whether GeoSciCloud belongs on the lineage list~~ — **yes**: NSF EarthCube,
      UNAVCO/IRIS → EarthScope, David Mencin; cloud-CI ancestry (overlaps the EarthScope partner).
- [ ] Get the correct partner-logo assets ([welcome-deck §3](welcome-deck/README.md)).
