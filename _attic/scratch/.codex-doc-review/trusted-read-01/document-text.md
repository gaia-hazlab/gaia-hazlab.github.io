# OpenEarthAI_IDSS_Cat2_ProjectDescription_v4

- Document ID: 1_0biYxew7Ii6RVLBJf3tFLoAHj1lbkT6HEjW6JbKQXI
- Revision ID: AIroW342psuroOiQuHPY8z9AzlHjiF_cD2hbDd0VHLarwoNyureH_1-y32SCFghHX_tov05LL1fFI8D1IO0ahsUiP8Umeik6KSkMKljXyJo
- Selected tab: t.0
- Protected controls: 0
- Opaque controls: 0
- Authoritative dropdowns: 0

Protected-control annotations are preservation instructions. Do not insert their displayed placeholder text to recreate a native control.

## Tab 1 (t.0)

[P00001 | 1:92 | NORMAL_TEXT]
Category II: OpenEarthAI — Multi-Hazard Foundation Models on Multimodal Earth Science Data

[P00002 | 92:204 | NORMAL_TEXT]
Geophysical AI-driven Integration and Assimilation: Scaling a National Operational Hazard-Science Data Platform

[P00003 | 204:247 | NORMAL_TEXT]
1. Vision, Goals, and Driving Requirements

[P00004 | 247:258 | NORMAL_TEXT]
1.1 Vision

[P00005 | 258:1528 | NORMAL_TEXT]
The most damaging natural hazards in the United States today are cascades of natural hazards, where their compounding effects aggravate the damages and yet sit at the nexus of multi-disciplinary Earth system science (REF, Yanites et al, 2025, Science). A series of atmospheric rivers rapidly saturates soils on a slope already weakened by wildfire burns severity (REF), a moderate earthquake liquefies fill that rainfall has been recharging the shallow water table for weeks (REF). These near-surface hazards are too sudden to be caught by satellite imagery, yet too localized to be resolved spatially by high-sampling rate ground-based sensors. The data required for these geological hazards are not solely seismic, or meterological, or geotechnical; it’s only them all together that can provide a sufficiently high spatial and temporal resolution of the subsurface hydromechanical properties and failures. Geological hazards can be observed and analyzed by seismic, infrasound, GNSS, SAR, meteorological, soil moisture, snowpack, streamflow, and XXX. Yet, the facilities that archive sensor data span different agencies, such as the NSF Geophysical Facility (operated by the EarthScope Consortium-ES), NASA (SAR Alaska Satellite Facility-ASF),  NOAA (XXX), and USGS. 

[P00006 | 1528:1529 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00007 | 1529:1735 | NORMAL_TEXT]
What is missing is a national, AI-ready operational infrastructure that fuses them to deliver actionable data models that can advance multi-hazards by researchers, agency partners, and communities at risk.

[P00008 | 1735:2816 | NORMAL_TEXT]
OpenEarthAI aim to become the IDSS (spell that out) infrastructure that advanced Earth science across disciplinary boundaries and data modalities. Building directly on three operational predecessors that already serve U.S. researchers (the EarthScope operated National Science Foundation National Geophysical Facility (NSF-NGF), the NASA-NSF Alaska Satellite Facility, and UW labs that have prototyped OpenEarthAI at a regional scale, this Category II project scales and broadens the existing capabilities into a single, national, operational, AI-native multi-hazard data platform. OpenEarthAI delivers a federated multi-modal data layer harmonized across agencies; an open multi-hazard foundation-model registry with reproducible training pipelines and public weights; a national hazard-evaluation benchmark suite with held-out golden data sets; and a suite of agents that will support researchers, industries, and citizens to discover, explain, and process data for their own individualized use. By end of award year 1, OpenEarthAI reaches full operations as a national service.

[P00009 | 2816:3454 | NORMAL_TEXT]
OpenEarthAI serves the highest-priority national needs. Climate-amplified hazards threaten public safety, critical infrastructure, insurance markets, and military readiness across all 50 states. The April 2025 NSF priority statement identifies artificial intelligence as a Federal R&D priority area; Executive Order 14303 (Gold Standard Science) requires reproducibility, transparency, and uncertainty communication in federally supported research; and the NAIRR Pilot calls for highly performant interconnected data infrastructure for AI-driven research. OpenEarthAI is the operational hazard-science data platform that meets all three.

[P00010 | 3454:3464 | NORMAL_TEXT]
1.2 Goals

[P00011 | 3464:3586 | NORMAL_TEXT]
OpenEarthAI pursues four measurable goals, each tied to performance objectives in §4 and to operational milestones in §3:

[P00012 | 3586:3933 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G1 — National Multi-Earth Data Integration. Operate, by end of award year 1, a production-grade, FAIR-aligned, AI-ready federated data layer spanning EarthScope, ASF, NOAA, USGS, NSF NEON, and HydroFrame archives, accessible from any U.S. institution. Scale the GAIA HazLab DataHub from single-region (Washington State) coverage to all 50 states.

[P00013 | 3933:4318 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G2 — Multi-Earth Foundation Models. Train, evaluate, document, and openly release at least three multimodal foundation models (geophysical sensor, SAR/Sentinel, hydro-meteorological, Earth structural, and across these modalities) with public weights, model cards, and reproducible training pipelines. Extend the GAIA HazLab ModelHub from research-lab to national operational registry.

[P00014 | 4318:4555 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G3 — National Earth Model Evaluation. Operate a public benchmark suite (e.g., HazEvalHub at national scale) with hidden test partitions, leaderboards, and uncertainty quantification aligned with WMO, USGS, and AI/ML community standards.

[P00015 | 4555:4924 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G4 — Cross-Modality Earth Agents. Operate a suite of provenance-aware agents that help users discover what data are available across modalities for a given location, time window, or hazard type, and that compose reproducible workflow stubs. Agent scope is deliberately constrained to data discovery and workflow scaffolding — not autonomous scientific decision-making.

[P00016 | 4924:4967 | NORMAL_TEXT]
1.3 Existing System Performance and Demand

[P00017 | 4967:5200 | NORMAL_TEXT]
Per NSF 26-509 Category II requirements, OpenEarthAI is a transition of operational systems already serving demonstrated user communities to broader national scale. Three lines of operational-system evidence motivate the transition.

[P00018 | 5200:6327 | NORMAL_TEXT]
EarthScope National Geophysical Facility (NGF, lead institution operational system). The NGF is the operational successor to the IRIS and UNAVCO data centers and is the steward of NSF's continental seismic and geodetic networks. Quantitative metrics over the most recent reporting period (2023–2025; detailed numbers and trend lines in Supplementary Cost Estimate): registered active users in the [thousands] across [hundreds] of U.S. institutions in all 50 states; data egress at the [petabytes-per-year] scale with cloud-native object-store distribution since the 2023 migration; year-over-year growth in active users and egress volume documented and continuing. NGF performance objectives currently in place include service availability, data completeness, time-to-data after acquisition, and user-satisfaction surveys; current-against-target performance is tracked at the EarthScope operations dashboard. The NGF demonstrates that EarthScope can build, operate, and scale national CI; it does not yet provide multi-modal AI-ready fusion, multi-hazard foundation models, or cross-modality discovery — the OpenEarthAI scope.

[P00019 | 6327:6922 | NORMAL_TEXT]
NASA-NSF Alaska Satellite Facility (ASF, federation partner). ASF distributes Sentinel-1 and forthcoming NISAR SAR data products and OPERA InSAR time-series products to a U.S. user community measured in [thousands] of registered users and [hundreds of TB] per month of egress. ECMWF reanalysis data (ERA5 / ERA-Land) is co-located in AWS S3 at ASF, providing the atmospheric layer needed for hazard fusion already in the cloud and ready to integrate. ASF is integrated as a federation partner via STAC catalog interoperability and AWS co-location (Letter of Collaboration on file); no subaward.

[P00020 | 6922:8586 | NORMAL_TEXT]
UW regional-scale labs. First, the GAIA HazLab regional prototype (subawardee). Since 2024, the UW Earth & Space Sciences and eScience Institute, with support from UW College of the Environment and the UW Fund for Future Science and Technology (FFST), have operated GAIA HazLab — a regional, multi-modal hazard-science platform covering Washington State and surrounding Pacific Northwest (see gaia-hazlab.github.io). GAIA HazLab demonstrates the core technical concepts at sub-national scale: a DataHub (streamlined cross-agency data ingestion of NOAA precipitation and streamflow, USGS seismic, NSF GNSS, ASF SAR, and Synoptic weather observations); a ModelHub (registry of operational models for AR-driven flood forecasting, storm detection, earthquake wavefield reconstruction, ground-failure surrogate modeling, hydromechanical memory inversion, post-fire debris flow modeling, and convective-storm characterization); and a HazEvalHub (fair-evaluation framework with hidden test partitions are developed in partnership with the AI Institute for Dynamical Systems, AI2, and Kaggle). The prototype has informed concrete hazard analyses across four named recent events documented on the public site: the 2025 Western Washington atmospheric-river floods and landslides, the Nisqually earthquake liquefaction record (2001–2031 monitoring envelope), the 2025 Stehekin post-fire debris flow, and convective-thunderstorm severity. GAIA HazLab establishes the science case, the technical readiness, and named user demand; what it does not provide today is national reach, operational SRE-grade footing, federated identity at scale, or release-grade foundation models. 

[P00021 | 8586:9277 | NORMAL_TEXT]
Second, the UW FiberLab is the largest optical fiber sensing cost center at academic instituions with 7 interrogators that have been utilized by United States communities and abroad to pursue a wide range of research applications spanning volcanology (REF), cryospheric science (REF - Lipovsky, Manos), oceanography (REF), marine bioacoustics (REF), geotechnical engineering, earthquake science (REF), mountain hazards (REF), agriculture (REF). The UW Fiberlab already prorotyped a cloud-native object store with Earthscope Consortium Data Services (Ni et al, 2024-DAsstore) and delivers some of its data publicly from MinIO stores, but has collected 2PB of data across these earth systems.

[P00022 | 9277:9438 | NORMAL_TEXT]
Third, the UW escience Software Science and Engineer Center (SSEC) is the first to prototype research agent labs to support scientific software developers etc.

[P00023 | 9438:9439 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00024 | 9439:9479 | NORMAL_TEXT]
Those are the Category II deliverables.

[P00025 | 9479:9897 | NORMAL_TEXT]
Together these operational systems form the substrate OpenEarthAI scales. The Category II investment is is a transition from sub-national operational capability to national operational capability, executed by teams who have already done the equivalent transitions before (GeoSciCloud and GeoSciFramework into the NGF; the Pangeo ecosystem at UW eScience; and GAIA HazLab from regional prototype to growing user base).

[P00026 | 9897:9921 | NORMAL_TEXT]
1.4 Reference Use Cases

[P00027 | 9921:10465 | NORMAL_TEXT]
OpenEarthAI is anchored by four reference hazard-cascade use cases. Each is drawn from a distinct hazard regime and a distinct geographic class of impact, and each requires the multi-modal AI-ready data fusion that no current national CI provides. Each is documented at the Washington-state scale today via OpenEarthAI and is scaled to national reach by OpenEarthAI. Each involves at least three of the disciplinary communities served by OpenEarthAI: solid Earth, hydrology and atmospheric science, ecology and land-surface science, and AI/ML.

[P00028 | 10465:10912 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U1 — Atmospheric-river-driven flood and shallow landslide cascades. AR events affect the entire West Coast (CA, OR, WA, AK) and increasingly the Northeast. Fusion of NOAA QPE and reanalysis precipitation, USGS streamflow, GNSS-IR soil moisture and SWE, InSAR pre-event deformation, and vegetation-stress imagery is required. Today: regional prototype on GAIA HazLab covers WA only; national coverage is the Cat II deliverable through OpenEarthAI.

[P00029 | 10912:11435 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U2 — Earthquake-induced ground failure with antecedent-moisture modulation. Liquefaction and seismic landslides are amplified by hydromechanical state. Fusion of seismic ground-motion records, antecedent precipitation and soil moisture, GNSS, InSAR, and post-event imagery is required. Today: Nisqually and other Pacific NW events analyzed via OpenEarthAI HazLab; the New Madrid Seismic Zone, Cascadia, Charleston (SC), and Alaska are operationally underserved for moisture-modulated hazard. Cat II adds national coverage.

[P00030 | 11435:11843 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U3 — Post-wildfire debris-flow hazard. Post-fire watersheds across the western U.S. (CO, NM, MT, ID, WA, OR, CA) are primed for debris flows by fire-altered soil hydrology. Fusion of fire perimeters and burn severity, soil moisture, DEM/slope, precipitation forecasts, and post-event imagery is required. Today: Stehekin (WA) covered by GAIA HazLab; the operational gap nationally is the Cat II deliverable.

[P00031 | 11843:12328 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U4 — Convective-storm intensification by land-atmosphere feedback. Severe convective storms across the Plains, Midwest, and Southeast are shaped by soil-moisture and surface-energy feedbacks. Fusion of NOAA radar and reanalysis, NEON tower and Ameriflux fluxes, GNSS-IR soil moisture, and seismic detection of thunderstorm signatures (an operational GAIA HazLab capability at national scale) is required. Today: WA-anchored prototype; Cat II extends to the convective corridor states.

[P00032 | 12328:12548 | NORMAL_TEXT]
These four use cases collectively span solid-Earth, hydrologic, atmospheric, ecological, and AI methodology communities — directly satisfying the IDSS "transdisciplinary and demonstrably multi-disciplinary" requirement.

[P00033 | 12548:12573 | NORMAL_TEXT]
1.5 Driving Requirements

[P00034 | 12573:12663 | NORMAL_TEXT]
Requirements derived from the use cases drive §2 architecture and §4 performance targets:

[P00035 | 12663:12857 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R1 — Federated AI-ready data: ≥10 federated agency archives, Zarr v3 / Parquet / STAC-JSON 1.x as primary serializations, tensor-ready outputs to PyTorch DataLoader, JAX, Hugging Face datasets.

[P00036 | 12857:12991 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R2 — National coverage, all 50 states: catalog and ingest harmonized observations across CONUS, Alaska, Hawaii, and U.S. territories.

[P00037 | 12991:13158 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R3 — Multi-hazard foundation models: at least three models released with public weights, training pipelines, and model cards by end of year 2; documented uncertainty.

[P00038 | 13158:13355 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R4 — Hazard evaluation rigor: held-out test partitions for each foundation model; public leaderboards with anti-leakage controls; uncertainty quantification consistent with WMO and USGS standards.

[P00039 | 13355:13536 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R5 — Cross-modality discovery agents: small-scope, deterministic-where-possible, provenance-logged; every agent action produces a versioned artifact reproducible without the agent.

[P00040 | 13536:13671 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R6 — Federated identity at national scale: CILogon-based identity supporting ≥150 institutions; merit-based plus open-tier allocation.

[P00041 | 13671:13868 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R7 — Reproducibility, transparency, uncertainty (Gold Standard Science): provenance (W3C PROV) on every product; uncertainty as first-class metadata; container-pinned, data-DOI-anchored workflows.

[P00042 | 13868:14018 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R8 — Open license: OpenEarthAI-developed software under Apache License 2.0; data products under CC-BY-4.0 or equivalent consistent with source terms.

[P00043 | 14018:14058 | NORMAL_TEXT]
2. Project Definition and Specification

[P00044 | 14058:14075 | NORMAL_TEXT]
2.1 Architecture

[P00045 | 14075:14493 | NORMAL_TEXT]
OpenEarthAI is organized as four operational layers — DataHub at national scale, ModelHub at national scale, HazEvalHub at national scale, and a small Discovery Agents layer — operating on a shared cloud-native foundation. Layer names are inherited from the OpenEarthAI HazLab regional prototype to preserve continuity for existing users; the Cat II work is the operational and scientific scaling beneath those names.

[P00046 | 14493:15745 | NORMAL_TEXT]
DataHub (national). Streaming ingestion (Apache Kafka) and batch ETL of: EarthScope-managed seismic, GNSS, and high-rate GNSS streams; ASF-managed Sentinel-1 SAR and OPERA InSAR products plus co-located ECMWF ERA5/ERA-Land reanalysis; NOAA precipitation, streamflow, radar, and reanalysis; USGS hazard catalogs, hydrography, and burn severity; NSF NEON tower and ecology data; HydroFrame hydrology products; Synoptic and MesoWest weather observations; UW DAS archive (FiberLab); and curated physics-based simulation outputs from SCEC CyberShake and dynamic-rupture and debris-flow ensembles. Storage is cloud-native object store (AWS S3 primary, with multi-cloud-portable formats throughout): Zarr v3 with IceChunk for n-d arrays, Apache Iceberg / Parquet for tabular and event data, MiniSEED+StationXML preserved alongside cloud-optimized siblings. Catalog is STAC-JSON 1.x with PROV-O provenance and a STAC API targeting sub-second p95 latency at 10⁹ records. Coordinate systems and time bases are unified; quality, calibration, and uncertainty are first-class fields. The Cat II DataHub work scales the OpenEarthAI HazLab regional integration of NOAA + USGS + EarthScope + ASF + Synoptic data to national coverage and operational SRE-grade footing.

[P00047 | 15745:17047 | NORMAL_TEXT]
ModelHub (national). The model registry hosts versioned, model-carded, container-pinned hazard models. Cat II adds three new multimodal foundation models trained to address the four reference use cases: (i) a Ground-Failure Foundation Model fusing seismic, geodetic, hydrologic, and antecedent-moisture inputs to predict liquefaction and seismic-landslide susceptibility (extending the existing OpenEarthAI HazLab surrogate work of Sanger and Ni); (ii) a Hydro-Meteorological Cascade Model fusing NOAA precipitation, GNSS-IR soil moisture and SWE, InSAR pre-event deformation, and vegetation indices for AR-driven flood and shallow landslide cascades (extending the AR forecasting work with ACE2 / Clima-X); (iii) a Post-Fire Debris-Flow Model fusing burn severity, soil moisture, slope, and short-fuse precipitation forecasts. Models are released under Apache 2.0 with public weights, training data manifests, and reproducible training pipelines deposited at NAIRR-compatible registries. Existing operational OpenEarthAI HazLab models — storm detection from seismic + weather (Kharita, Anderson-Frey, Denolle), earthquake-wavefield reconstruction (Ni), heatwave forecasting (Hakim), and the hydromechanical memory inversion (Köpfli) — are migrated to operational footing as part of the same registry.

[P00048 | 17047:17630 | NORMAL_TEXT]
HazEvalHub (national). The evaluation framework provides fair-evaluation, anti-leakage benchmarking with hidden test partitions, public leaderboards, and standardized metrics (classification, regression, segmentation, probabilistic calibration). Evaluation standards align with WMO meteorology, USGS seismic, ISO risk-assessment, and ML community best practices. Cat II scales the existing OpenEarthAI HazLab evaluation framework — built in collaboration with the AI Institute for Dynamical Systems (Kutz), AI2, and Kaggle — to national coverage and to the four reference use cases.

[P00049 | 17630:18787 | NORMAL_TEXT]
Cross-Modality Discovery Agents (small, focused). Three narrowly scoped agents operate on the OpenEarthAI stack: (i) a Data-Availability Agent that, given a location, time window, and hazard type, returns a structured manifest of which modalities are available, at what spatial and temporal resolution, with what quality flags, across all federated archives; (ii) a Cross-Modality Coverage Agent that audits co-availability of complementary modalities (e.g., is GNSS-IR soil moisture co-available with InSAR coherence and NOAA precipitation for a given event window?); (iii) a Workflow-Stub Agent that returns a versioned, container-pinned, data-DOI-anchored notebook scaffold for a chosen use case, including provenance metadata. Agents are deterministic where possible, retrieval-augmented where not, sandboxed (no autonomous data modification), and audited (every agent action produces a logged artifact). The agents do not replace human scientific judgment; they remove friction in data discovery. The Cat II work prototypes and operationalizes these three agents on the OpenEarthAI stack, deliberately limiting agent scope to maintain trustworthiness.

[P00050 | 18787:18812 | NORMAL_TEXT]
2.2 Systems and Services

[P00051 | 18812:18981 | NORMAL_TEXT]
OpenEarthAI delivers six user-visible services. Three transition from sub-national operational status to national operational status; three are new at the Cat II scope.

[P00052 | 18981:19134 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S1 — National Federated Catalog and STAC API (transitioning the OpenEarthAI HazLab catalog to national reach plus federation with NGF and ASF catalogs).

[P00053 | 19134:19248 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S2 — AI-Ready Data Distribution (Zarr / Parquet / Iceberg tensor-ready outputs; co-located cloud compute access).

[P00054 | 19248:19337 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S3 — Multi-Hazard Foundation-Model Registry and Inference Endpoints (national ModelHub).

[P00055 | 19337:19418 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S4 — Hazard Evaluation Benchmarks and Public Leaderboards (national HazEvalHub).

[P00056 | 19418:19499 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S5 — Cross-Modality Discovery Agents (the three small agents described in §2.1).

[P00057 | 19499:19632 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S6 — On-Ramp Cloud Education and Training (extending EarthScope's existing On-Ramp platform; integrated with UW eScience Hackweeks).

[P00058 | 19632:19651 | NORMAL_TEXT]
2.3 Intended Users

[P00059 | 19651:19744 | NORMAL_TEXT]
OpenEarthAI is built for five user categories with target sizes at full operations (year 3):

[P00060 | 19744:19928 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Domain research scientists across solid Earth, hydrology, atmospheric science, ecology, and hazards — primary consumers. Target: 4,000 active users / 150 institutions / all 50 states.

[P00061 | 19928:20126 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
AI/ML methods developers — consumers of HazEvalHub benchmarks and ModelHub artifacts; contributors of new models. Target: 500 active users / 50 institutions including AI Institutes and NAIRR users.

[P00062 | 20126:20327 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Federal and state agency partners — NOAA, USGS, NASA, FEMA, state geological surveys, state emergency-management offices: operational consumers of OpenEarthAI-trained foundation models and benchmarks.

[P00063 | 20327:20480 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Educators and learners — instructors using On-Ramp curricula, Hackweek participants. Target: 150 instructors and 1,800 learners cumulative over 3 years.

[P00064 | 20480:20622 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Industry users (insurance, hazard engineering, infrastructure resilience, utilities) — open-tier access with documented commercial-use terms.

[P00065 | 20622:20657 | NORMAL_TEXT]
2.4 Data Lifecycle Reference Model

[P00066 | 20657:21040 | NORMAL_TEXT]
OpenEarthAI adopts the FAIR Data Principles together with the NIST/NSDS reference data lifecycle. OpenEarthAI primarily supports acquisition, transfer, harmonization (curation), exploration, analysis, sharing, and synthesis stages. Long-term archiving and preservation remain the responsibility of source facilities; per IDSS rules, no long-term storage costs are budgeted (see §6).

[P00067 | 21040:21099 | NORMAL_TEXT]
2.5 Leveraging and Connecting to Other Cyberinfrastructure

[P00068 | 21099:21198 | NORMAL_TEXT]
OpenEarthAI federates with named operational partners, with concrete interoperability commitments:

[P00069 | 21198:21303 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
EarthScope NGF — lead institution; operating envelope, identity, governance, and user-support framework.

[P00070 | 21303:21448 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NASA-NSF ASF — joint Sentinel-1, NISAR, OPERA InSAR, ECMWF reanalysis services; STAC catalog interoperability already in place; AWS co-location.

[P00071 | 21448:21615 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NOAA (NCEP, NCEI, NWS) — precipitation, streamflow, radar, reanalysis. Integration follows existing OpenEarthAI HazLab ingestion patterns scaled to national coverage.

[P00072 | 21615:21690 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
USGS — earthquake catalogs, hydrography, ShakeMap, burn-severity products.

[P00073 | 21690:21766 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NSF NEON, OOI, HydroFrame, CUAHSI — cross-facility STAC catalog federation.

[P00074 | 21766:21931 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NAIRR Pilot — OpenEarthAI serves as a hazard-science data layer for NAIRR-supported AI compute; foundation-model artifacts deposited in NAIRR-accessible registries.

[P00075 | 21931:22056 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
ACCESS — federated identity (CILogon) supports OpenEarthAI users running training and inference on ACCESS-allocated compute.

[P00076 | 22056:22196 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Domain centers (SCEC, CRESCENT, AVERT/VICTOR, SZ4D, DesignSafe) — early adopters and scientific advisors; Letters of Collaboration on file.

[P00077 | 22196:22367 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
AI Institute partners (AI Institute for Dynamical Systems, AI2) — co-developed evaluation frameworks (already in place via OpenEarthAI HazLab) extended to national scope.

[P00078 | 22367:22414 | NORMAL_TEXT]
2.6 Uniqueness, Complementarity, and Synergies

[P00079 | 22414:22671 | NORMAL_TEXT]
OpenEarthAI is unique within the national CI landscape because it is the only operational, multi-agency, multi-hazard, multimodal, AI-ready data and foundation-model platform under open public stewardship. We differentiate explicitly from related programs.

[P00080 | 22671:23193 | NORMAL_TEXT]
Within OAC. CSSI funds innovation and prototype development; OpenEarthAI HazLab itself was developed under research-program support and the Cat II work is operationalization, not innovation. CC* supports campus and regional CI; OpenEarthAI serves any U.S. institution. ACSS provides advanced national computing; OpenEarthAI provides the complementary national hazard-data layer. ACCESS coordinates compute allocation; OpenEarthAI exposes hazard-data services that ACCESS-allocated jobs consume through standard protocols.

[P00081 | 23193:23754 | NORMAL_TEXT]
Within NSF beyond OAC. AI Institutes generate AI methods; OpenEarthAI is the operational hazard-data layer those methods consume. NSF Major Facilities (NEON, OOI, EarthScope) operate observing systems and produce data; OpenEarthAI operates the cross-facility, cross-modality hazard-integration layer on top of them and does not duplicate them. EarthScope is the lead institution; OpenEarthAI is not an EarthScope-only service — it is the multi-agency, multi-facility integration platform EarthScope operates on behalf of the broader hazards research community.

[P00082 | 23754:24472 | NORMAL_TEXT]
Sister federal agencies. NAIRR Pilot provides AI compute and foundation-model access; OpenEarthAI provides the hazard-data layer that supplies NAIRR-style workflows. NASA Earth Science Data Systems are NASA-mission focused on Earth observation; OpenEarthAI operates the cross-mission integration layer combining NASA data with NSF, NOAA, USGS, and academic data sources for hazard science specifically. NOAA Big Data and NCEI are NOAA-mission focused on weather, water, and climate; OpenEarthAI integrates NOAA products as one of multiple modalities in a hazard-cascade fusion. DOE programs (ESnet, OSTI, OLCF/ALCF/NERSC data) serve DOE-lab users; OpenEarthAI serves the broader academic and agency hazards community.

[P00083 | 24472:24963 | NORMAL_TEXT]
Commercial platforms. Google Earth Engine, Microsoft Planetary Computer, Google AlphaEarth, NVIDIA Earth-2, IBM Terramind, AI2 OlmoEarth are valuable but vendor-locked, ToS-driven, not federated under public stewardship, and not aligned with NSF FAIR/Open Science mandates. OpenEarthAI is the public, community-governed, FAIR counterpart for hazard science. We integrate with these platforms (mirrored benchmarks, shared model cards) wherever doing so serves the public-good user community.

[P00084 | 24963:25336 | NORMAL_TEXT]
Synergies. OpenEarthAI actively builds: federated identity and catalogs across EarthScope, ASF, NEON, OOI; bidirectional data and model sharing with NAIRR; co-developed evaluation with AI Institute partners (already in place via OpenEarthAI HazLab); shared hazard benchmarks with CRESCENT, SCEC, AVERT/VICTOR, SZ4D; and joint workforce programs with UW eScience Hackweeks.

[P00085 | 25336:25355 | NORMAL_TEXT]
3. Operations Plan

[P00086 | 25355:25416 | NORMAL_TEXT]
3.1 Operations Transition Timeline (Full Operations by EOY1)

[P00087 | 25416:25664 | NORMAL_TEXT]
OpenEarthAI reaches full operations by end of award year 1 through a phased rollout with explicit go/no-go gates. Full operations is achievable on this schedule because the Cat II work is transition of operational systems, not a clean-sheet build.

[P00088 | 25664:26055 | NORMAL_TEXT]
Phase 1, months 1–3 (architecture and operational baseline). Architecture finalization within EarthScope's existing AWS cloud envelope; subaward agreement with UW executed; Smartsheet schedule, risk register, and change-control governance stood up; security baseline established; OpenEarthAI HazLab regional services migrated to the EarthScope cloud environment under the federated catalog.

[P00089 | 26055:26520 | NORMAL_TEXT]
Phase 2, months 3–9 (national scale-out). DataHub federation with NOAA, USGS, NEON, HydroFrame extended to all 50 states; ModelHub national operational footing achieved; HazEvalHub leaderboards live for the four reference use cases; the three Discovery Agents released to internal testers; federated identity (CILogon) integrated; documentation published. First two foundation models (Ground-Failure, Hydro-Meteorological Cascade) trained and version 0.1 released.

[P00090 | 26520:27110 | NORMAL_TEXT]
Phase 3, months 9–12 (integrated testing and early operations). Named early adopters across all four reference use cases (CRESCENT and SCEC, NOAA Disasters and FEMA partners, USGS Landslide Hazards Program, NSF NEON ecology, AI Institute partners — Letters of Collaboration on file) onboarded. Performance, load, and reliability tests against the §4 KPIs. Acceptance package prepared. Third foundation model (Post-Fire Debris-Flow) released. NSF-conducted operational readiness review at end of month 12, potentially as a Reverse Site Visit; upon acceptance, transition to full operations.

[P00091 | 27110:27431 | NORMAL_TEXT]
Phases 4–5, years 2–3 (full operations and DevOps evolution). Continuous operations measured against §4 KPIs; model-refresh cadence (quarterly model evaluation, semi-annual re-training as data accumulates); ingestion of new modalities (DAS in year 2; additional simulation archives); year-3 NSF renewal-readiness review.

[P00092 | 27431:27474 | NORMAL_TEXT]
3.2 Modes of Operation and Functionalities

[P00093 | 27474:27893 | NORMAL_TEXT]
OpenEarthAI operates 24/7/365 with three service tiers: interactive (catalog, metadata, modest egress, agent queries) with sub-second response targets; batch (large data egress, model training data preparation) with throughput SLAs; inference (foundation-model endpoints) with bounded-latency SLAs. Maintenance windows are scheduled, announced, and never affect the interactive tier without ≥7-day notice and failover.

[P00094 | 27893:27948 | NORMAL_TEXT]
3.3 User Engagement, Onboarding, Training, and Support

[P00095 | 27948:28933 | NORMAL_TEXT]
User engagement extends EarthScope's national user-support office and UW eScience's national Hackweek model. Onboarding: self-service account creation via CILogon, automated open-tier allocation, merit-reviewed allocation for high-throughput workloads via a quarterly community review committee. Training: On-Ramp cloud notebooks (extending EarthScope's existing platform; new hazard-specific modules added in year 1); annual OpenEarthAI Hazard Hackweek run by UW eScience (capacity 50–80 participants, open application across all 50 states); two domain-focused short courses per year; classroom-ready curricula released openly. Documentation: comprehensive user guides, OpenAPI 3.x reference, runnable example notebooks for each reference use case, and a model card for every released model. Support: ticket system with documented response SLAs by tier, weekly virtual office hours, community discussion forum. Agent-assisted help is layered on top of, not instead of, human support.

[P00096 | 28933:28979 | NORMAL_TEXT]
3.4 Personnel: Numbers, Types, Qualifications

[P00097 | 28979:29739 | NORMAL_TEXT]
OpenEarthAI is staffed by ~14 FTE at full operations. Operations team (~6 FTE at EarthScope): site reliability engineers, DevOps and cloud engineer, security engineer, user-support specialists, training and documentation lead. Development and AI/ML team (~6 FTE distributed across EarthScope and UW): data engineers, ML engineers / RSEs, foundation-model lead (UW), agentic-AI engineer (UW). Scientific staff (~2 FTE distributed across EarthScope and UW): hazard-domain liaisons; data-steward function. Specific qualifications include AWS Solutions Architect/SysOps for SREs, NIST 800-171-aware training for the security lead, documented prior CI-operations or open-source-project experience for engineering staff. Named individuals and positions are in §5.2.

[P00098 | 29739:29796 | NORMAL_TEXT]
3.5 Resource Allocation: Broad, Open, Merit-Based Access

[P00099 | 29796:30667 | NORMAL_TEXT]
OpenEarthAI adopts a two-tier allocation policy aligned with NSF open-access principles. Open tier: every account holder has no-questions-asked access to catalog search, metadata, modest data egress, agent queries, and inference on hosted foundation models, subject to fair-use rate limits. Merit tier: high-throughput training data preparation, large-scale Feature Store materialization, and reserved inference capacity, allocated quarterly through a community advisory committee using NSF-style merit review. Allocation outcomes (request, decision, rationale) are publicly posted to satisfy the solicitation's open-access requirement. Geographic and institutional distribution is monitored as a §4 KPI to ensure OpenEarthAI serves all 50 states, EPSCoR jurisdictions, community colleges, primarily undergraduate institutions, MSIs, and HBCUs as institutional partners.

[P00100 | 30667:30694 | NORMAL_TEXT]
3.6 Early-User Access Plan

[P00101 | 30694:31494 | NORMAL_TEXT]
Early access begins month 9 with named community partners across all four reference use cases. Letters of Collaboration are submitted with this proposal, in the intent-only format required by NSF 26-509: AR / flood / shallow landslide partners (NOAA Center for Western Weather and Water Extremes; USGS Landslide Hazards; NWS Western Region); earthquake / liquefaction partners (CRESCENT; SCEC; WSDOT geotechnical); post-fire debris-flow partners (USGS; U.S. Forest Service; state-DOT partners in CO, NM, MT); convective-storm partners (NOAA NSSL; NCAR/MMM; AI Institute for Dynamical Systems via existing OpenEarthAI HazLab collaboration). Early-user feedback is collected weekly and feeds directly into the Phase-3 acceptance package; pre-acceptance outputs are tracked in the public issue tracker.

[P00102 | 31494:31536 | NORMAL_TEXT]
3.7 Technology Refresh and Public Metrics

[P00103 | 31536:32319 | NORMAL_TEXT]
Cloud-native architecture makes hardware lifecycle a managed-service concern; refresh strategy focuses on software-stack evolution (Zarr v3 maturation, IceChunk, PyTorch/JAX/Hugging Face dataloader API evolution, foundation-model architecture refresh as the field advances) and on absorbing new modalities (DAS in year 2, simulation archives in year 2, additional sensors as they come online). At least 15% of operations effort is reserved for innovation during operations, satisfying the IDSS requirement. A public metrics dashboard exposes uptime, latency, throughput, user counts, geographic distribution, allocation outcomes, and scientific-impact metrics in real time, satisfying the solicitation's open-metrics requirement and aligning with Gold Standard Science transparency.

[P00104 | 32319:32356 | NORMAL_TEXT]
3.8 Operations-Side Security Summary

[P00105 | 32356:32782 | NORMAL_TEXT]
Operations-side security is summarized here; full plan in §5.6. OpenEarthAI inherits EarthScope's established security program (documented controls, MFA, role-based access, vulnerability scanning, audit logging) and extends it for AI-specific risks (model exfiltration, training-data leakage, prompt-injection in agentic workflows). Important Notice 149 obligations are met for all Senior Personnel at award start (see §5.6).

[P00106 | 32782:32821 | NORMAL_TEXT]
4. Performance Objectives and Measures

[P00107 | 32821:32846 | NORMAL_TEXT]
4.1 Objective Categories

[P00108 | 32846:33518 | NORMAL_TEXT]
OpenEarthAI tracks performance across six objective categories calibrated to national-scale operational CI norms: (i) continuous operations (uptime, MTBF, MTTR); (ii) end-to-end performance (latency, throughput); (iii) user-community growth (registered users, institutions, geographic reach); (iv) user experience and usability; (v) scientific and operational hazard-science impact (publications, datasets and models published, agency uptake); (vi) Gold-Standard-Science alignment (workflow reproducibility, uncertainty coverage). Cat II baselines are higher than a clean-sheet build because OpenEarthAI inherits operational footing from NGF, ASF, and OpenEarthAI HazLab.

[P00109 | 33518:33542 | NORMAL_TEXT]
4.2 Performance Targets

[P00110 | 33545:33553 | NORMAL_TEXT | TABLE row=0 col=0]
Outcome

[P00111 | 33554:33558 | NORMAL_TEXT | TABLE row=0 col=1]
KPI

[P00112 | 33559:33574 | NORMAL_TEXT | TABLE row=0 col=2]
Y1 (Early Ops)

[P00113 | 33575:33585 | NORMAL_TEXT | TABLE row=0 col=3]
Y2 Target

[P00114 | 33586:33596 | NORMAL_TEXT | TABLE row=0 col=4]
Y3 Target

[P00115 | 33598:33613 | NORMAL_TEXT | TABLE row=1 col=0]
Continuous ops

[P00116 | 33614:33640 | NORMAL_TEXT | TABLE row=1 col=1]
Uptime (interactive tier)

[P00117 | 33641:33645 | NORMAL_TEXT | TABLE row=1 col=2]
97%

[P00118 | 33646:33652 | NORMAL_TEXT | TABLE row=1 col=3]
99.0%

[P00119 | 33653:33659 | NORMAL_TEXT | TABLE row=1 col=4]
99.5%

[P00120 | 33661:33676 | NORMAL_TEXT | TABLE row=2 col=0]
Continuous ops

[P00121 | 33677:33695 | NORMAL_TEXT | TABLE row=2 col=1]
MTTR (severity-1)

[P00122 | 33696:33700 | NORMAL_TEXT | TABLE row=2 col=2]
2 h

[P00123 | 33701:33705 | NORMAL_TEXT | TABLE row=2 col=3]
1 h

[P00124 | 33706:33713 | NORMAL_TEXT | TABLE row=2 col=4]
30 min

[P00125 | 33715:33730 | NORMAL_TEXT | TABLE row=3 col=0]
Continuous ops

[P00126 | 33731:33749 | NORMAL_TEXT | TABLE row=3 col=1]
MTBF (severity-1)

[P00127 | 33750:33755 | NORMAL_TEXT | TABLE row=3 col=2]
30 d

[P00128 | 33756:33761 | NORMAL_TEXT | TABLE row=3 col=3]
60 d

[P00129 | 33762:33767 | NORMAL_TEXT | TABLE row=3 col=4]
90 d

[P00130 | 33769:33781 | NORMAL_TEXT | TABLE row=4 col=0]
Performance

[P00131 | 33782:33822 | NORMAL_TEXT | TABLE row=4 col=1]
Catalog query p95 latency (10⁹ records)

[P00132 | 33823:33829 | NORMAL_TEXT | TABLE row=4 col=2]
1.5 s

[P00133 | 33830:33837 | NORMAL_TEXT | TABLE row=4 col=3]
750 ms

[P00134 | 33838:33845 | NORMAL_TEXT | TABLE row=4 col=4]
500 ms

[P00135 | 33847:33859 | NORMAL_TEXT | TABLE row=5 col=0]
Performance

[P00136 | 33860:33896 | NORMAL_TEXT | TABLE row=5 col=1]
Sustained ML data-loader throughput

[P00137 | 33897:33905 | NORMAL_TEXT | TABLE row=5 col=2]
30 GB/s

[P00138 | 33906:33914 | NORMAL_TEXT | TABLE row=5 col=3]
75 GB/s

[P00139 | 33915:33924 | NORMAL_TEXT | TABLE row=5 col=4]
150 GB/s

[P00140 | 33926:33938 | NORMAL_TEXT | TABLE row=6 col=0]
Performance

[P00141 | 33939:33978 | NORMAL_TEXT | TABLE row=6 col=1]
Foundation-model inference p95 latency

[P00142 | 33979:33983 | NORMAL_TEXT | TABLE row=6 col=2]
5 s

[P00143 | 33984:33988 | NORMAL_TEXT | TABLE row=6 col=3]
2 s

[P00144 | 33989:33993 | NORMAL_TEXT | TABLE row=6 col=4]
1 s

[P00145 | 33995:34010 | NORMAL_TEXT | TABLE row=7 col=0]
User community

[P00146 | 34011:34035 | NORMAL_TEXT | TABLE row=7 col=1]
Registered active users

[P00147 | 34036:34042 | NORMAL_TEXT | TABLE row=7 col=2]
1,200

[P00148 | 34043:34049 | NORMAL_TEXT | TABLE row=7 col=3]
2,800

[P00149 | 34050:34056 | NORMAL_TEXT | TABLE row=7 col=4]
5,000

[P00150 | 34058:34073 | NORMAL_TEXT | TABLE row=8 col=0]
User community

[P00151 | 34074:34101 | NORMAL_TEXT | TABLE row=8 col=1]
Distinct U.S. institutions

[P00152 | 34102:34105 | NORMAL_TEXT | TABLE row=8 col=2]
50

[P00153 | 34106:34110 | NORMAL_TEXT | TABLE row=8 col=3]
100

[P00154 | 34111:34115 | NORMAL_TEXT | TABLE row=8 col=4]
180

[P00155 | 34117:34132 | NORMAL_TEXT | TABLE row=9 col=0]
User community

[P00156 | 34133:34158 | NORMAL_TEXT | TABLE row=9 col=1]
States with active users

[P00157 | 34159:34162 | NORMAL_TEXT | TABLE row=9 col=2]
40

[P00158 | 34163:34166 | NORMAL_TEXT | TABLE row=9 col=3]
48

[P00159 | 34167:34170 | NORMAL_TEXT | TABLE row=9 col=4]
50

[P00160 | 34172:34188 | NORMAL_TEXT | TABLE row=10 col=0]
User experience

[P00161 | 34189:34220 | NORMAL_TEXT | TABLE row=10 col=1]
Avg. satisfaction (1–5 survey)

[P00162 | 34221:34225 | NORMAL_TEXT | TABLE row=10 col=2]
3.8

[P00163 | 34226:34230 | NORMAL_TEXT | TABLE row=10 col=3]
4.1

[P00164 | 34231:34235 | NORMAL_TEXT | TABLE row=10 col=4]
4.4

[P00165 | 34237:34253 | NORMAL_TEXT | TABLE row=11 col=0]
User experience

[P00166 | 34254:34286 | NORMAL_TEXT | TABLE row=11 col=1]
Time-to-first-result (new user)

[P00167 | 34287:34295 | NORMAL_TEXT | TABLE row=11 col=2]
≤45 min

[P00168 | 34296:34304 | NORMAL_TEXT | TABLE row=11 col=3]
≤25 min

[P00169 | 34305:34313 | NORMAL_TEXT | TABLE row=11 col=4]
≤15 min

[P00170 | 34315:34333 | NORMAL_TEXT | TABLE row=12 col=0]
Scientific impact

[P00171 | 34334:34366 | NORMAL_TEXT | TABLE row=12 col=1]
Publications citing OpenEarthAI

[P00172 | 34367:34369 | NORMAL_TEXT | TABLE row=12 col=2]
8

[P00173 | 34370:34373 | NORMAL_TEXT | TABLE row=12 col=3]
40

[P00174 | 34374:34378 | NORMAL_TEXT | TABLE row=12 col=4]
120

[P00175 | 34380:34398 | NORMAL_TEXT | TABLE row=13 col=0]
Scientific impact

[P00176 | 34399:34426 | NORMAL_TEXT | TABLE row=13 col=1]
Foundation models released

[P00177 | 34427:34429 | NORMAL_TEXT | TABLE row=13 col=2]
1

[P00178 | 34430:34432 | NORMAL_TEXT | TABLE row=13 col=3]
3

[P00179 | 34433:34435 | NORMAL_TEXT | TABLE row=13 col=4]
5

[P00180 | 34437:34455 | NORMAL_TEXT | TABLE row=14 col=0]
Scientific impact

[P00181 | 34456:34488 | NORMAL_TEXT | TABLE row=14 col=1]
Datasets / benchmarks published

[P00182 | 34489:34491 | NORMAL_TEXT | TABLE row=14 col=2]
8

[P00183 | 34492:34495 | NORMAL_TEXT | TABLE row=14 col=3]
30

[P00184 | 34496:34499 | NORMAL_TEXT | TABLE row=14 col=4]
75

[P00185 | 34501:34515 | NORMAL_TEXT | TABLE row=15 col=0]
GSS alignment

[P00186 | 34516:34559 | NORMAL_TEXT | TABLE row=15 col=1]
% workflows reproducible (container + DOI)

[P00187 | 34560:34564 | NORMAL_TEXT | TABLE row=15 col=2]
70%

[P00188 | 34565:34569 | NORMAL_TEXT | TABLE row=15 col=3]
90%

[P00189 | 34570:34574 | NORMAL_TEXT | TABLE row=15 col=4]
97%

[P00190 | 34576:34590 | NORMAL_TEXT | TABLE row=16 col=0]
GSS alignment

[P00191 | 34591:34631 | NORMAL_TEXT | TABLE row=16 col=1]
% public products w/ uncertainty fields

[P00192 | 34632:34636 | NORMAL_TEXT | TABLE row=16 col=2]
75%

[P00193 | 34637:34641 | NORMAL_TEXT | TABLE row=16 col=3]
92%

[P00194 | 34642:34646 | NORMAL_TEXT | TABLE row=16 col=4]
98%

[P00195 | 34647:34675 | NORMAL_TEXT]
4.3 Measurement Methodology

[P00196 | 34675:35611 | NORMAL_TEXT]
Operational metrics (uptime, MTBF, MTTR, latency, throughput) are collected via Prometheus-class telemetry and surfaced on the public dashboard. User-community metrics are drawn from the federated identity and allocation databases (privacy-preserving aggregates only). User satisfaction is measured by a quarterly survey with documented methodology and public summary reports. Time-to-first-result is measured via the On-Ramp cohort timing pipeline. Scientific impact is tracked through DOI-linked publications, model-card download counts, DataCite dataset-DOI citations, and an annual hazard-science impact case-study series. GSS-alignment metrics are computed from the workflow registry (every registered workflow is automatically scanned for container pinning and data-DOI references; every public product is scanned for uncertainty-field presence). All metrics are reported annually to NSF and continuously to the public dashboard.

[P00197 | 35611:35633 | NORMAL_TEXT]
5. Project Management

[P00198 | 35633:35682 | NORMAL_TEXT]
5.1 Project Leadership Team and Their Experience

[P00199 | 35682:35988 | NORMAL_TEXT]
OpenEarthAI is led by a team with substantial prior experience operating national-scale data CI for large user communities. Cat II review weights operational track record heavily; the team's record is summarized below and detailed in the Project Personnel and Partner Organizations supplementary document.

[P00200 | 35988:36340 | NORMAL_TEXT]
Principal Investigator: Dr. David Mencin (EarthScope) — scientific direction, cross-agency alignment, final authority on scientific scope. PI commitment: 3.0 person-months/year (substantial). Mencin leads EarthScope's NGF data and computation portfolio and has directed prior CSSI-to-operations transitions (GeoSciCloud, GeoSciFramework into the NGF).

[P00201 | 36340:36620 | NORMAL_TEXT]
Project Director: Sarah Deutsch, Director of Project Management, EarthScope — execution authority, governance, schedule, risk, vendor oversight. Deutsch has documented experience overseeing multi-year, multi-facility CI programs at EarthScope. Commitment: 6.0 person-months/year.

[P00202 | 36620:36749 | NORMAL_TEXT]
Technical Lead (EarthScope, named in supplementary docs) — systems architecture, integration oversight. 12.0 person-months/year.

[P00203 | 36749:36849 | NORMAL_TEXT]
Operations Lead (EarthScope) — DevOps, SRE, monitoring, incident response. 12.0 person-months/year.

[P00204 | 36849:36944 | NORMAL_TEXT]
Security Lead (EarthScope) — security architecture, IN 149 compliance. 6.0 person-months/year.

[P00205 | 36944:36976 | NORMAL_TEXT]
Subaward co-Investigators (UW):

[P00206 | 36976:37201 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Marine Denolle (UW ESS, co-PI) — scientific lead for multi-hazard foundation models; PI of the existing OpenEarthAI HazLab regional prototype being scaled. Co-supervises postdocs and CSE graduate student. 1.0 month/year.

[P00207 | 37201:37328 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Vikram Iyer (UW CSE, co-PI) — lead for Cross-Modality Discovery Agents; agent benchmarking and evaluation. 0.5 month/year.

[P00208 | 37328:37477 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Vani Mandava (UW eScience, co-PI) — RSE leadership, agentic-AI software engineering best practices, On-Ramp and Hackweek operations. 0.5 month/year.

[P00209 | 37477:37615 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Nicoleta Cristea (UW, co-PI) — hydrology integration (HydroFrame, NOAA precipitation, GNSS-IR soil moisture and SWE). 0.5 month/year.

[P00210 | 37615:37767 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Scott Henderson (UW eScience, Senior Personnel) — cloud CI for fused NASA + ASF + EarthScope + HydroFrame data; co-supervises RSEs. 1.0 month/year.

[P00211 | 37767:37856 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Brad Lipovsky (UW, Senior Personnel) — DAS data-service curation (FiberLab archive).

[P00212 | 37856:38174 | NORMAL_TEXT]
External advisory: a Science and Operations Advisory Group of 5–7 experts drawn from federal agencies (NOAA, USGS, NASA), NSF Major Facilities (NEON, OOI, ASF, IceCube), and AI research (NSF AI Institutes, NAIRR users) provides advisory input. Execution authority remains centralized within the EarthScope PI and PMO.

[P00213 | 38174:38229 | NORMAL_TEXT]
5.2 Project Organization, Work Breakdown, and Timeline

[P00214 | 38229:38566 | NORMAL_TEXT]
EarthScope is the single accountable lead. The UW subaward operates under a named scope of work with monthly reporting, quarterly milestone reviews, and binding authority of the EarthScope PMO over schedule, cost, and acceptance criteria. Reporting chain: UW subaward lead → EarthScope PMO (Deutsch) → PI (Mencin) → NSF Program Officer.

[P00215 | 38566:38739 | NORMAL_TEXT]
Work Breakdown Structure (Level 2). Major work areas, lead organizations, and indicative 3-year direct-cost budgets (detailed estimates in the Supplementary Cost Estimate):

[P00216 | 38742:38746 | NORMAL_TEXT | TABLE row=0 col=0]
WBS

[P00217 | 38747:38757 | NORMAL_TEXT | TABLE row=0 col=1]
Work Area

[P00218 | 38758:38763 | NORMAL_TEXT | TABLE row=0 col=2]
Lead

[P00219 | 38764:38776 | NORMAL_TEXT | TABLE row=0 col=3]
3-Yr Direct

[P00220 | 38778:38782 | NORMAL_TEXT | TABLE row=1 col=0]
1.0

[P00221 | 38783:38859 | NORMAL_TEXT | TABLE row=1 col=1]
DataHub National Federation (NOAA, USGS, EarthScope, ASF, NEON, HydroFrame)

[P00222 | 38860:38871 | NORMAL_TEXT | TABLE row=1 col=2]
EarthScope

[P00223 | 38872:38880 | NORMAL_TEXT | TABLE row=1 col=3]
~$1.40M

[P00224 | 38882:38886 | NORMAL_TEXT | TABLE row=2 col=0]
2.0

[P00225 | 38887:38928 | NORMAL_TEXT | TABLE row=2 col=1]
ModelHub: Multi-Hazard Foundation Models

[P00226 | 38929:38955 | NORMAL_TEXT | TABLE row=2 col=2]
UW (Denolle) + EarthScope

[P00227 | 38956:38964 | NORMAL_TEXT | TABLE row=2 col=3]
~$1.50M

[P00228 | 38966:38970 | NORMAL_TEXT | TABLE row=3 col=0]
3.0

[P00229 | 38971:39000 | NORMAL_TEXT | TABLE row=3 col=1]
HazEvalHub at National Scale

[P00230 | 39001:39017 | NORMAL_TEXT | TABLE row=3 col=2]
UW + EarthScope

[P00231 | 39018:39026 | NORMAL_TEXT | TABLE row=3 col=3]
~$0.65M

[P00232 | 39028:39032 | NORMAL_TEXT | TABLE row=4 col=0]
4.0

[P00233 | 39033:39065 | NORMAL_TEXT | TABLE row=4 col=1]
Cross-Modality Discovery Agents

[P00234 | 39066:39084 | NORMAL_TEXT | TABLE row=4 col=2]
UW (Iyer/Mandava)

[P00235 | 39085:39093 | NORMAL_TEXT | TABLE row=4 col=3]
~$0.65M

[P00236 | 39095:39099 | NORMAL_TEXT | TABLE row=5 col=0]
5.0

[P00237 | 39100:39173 | NORMAL_TEXT | TABLE row=5 col=1]
Hydrology / Critical Zone Integration via HydroFrame & CUAHSI federation

[P00238 | 39174:39187 | NORMAL_TEXT | TABLE row=5 col=2]
UW (Cristea)

[P00239 | 39188:39196 | NORMAL_TEXT | TABLE row=5 col=3]
~$0.40M

[P00240 | 39198:39202 | NORMAL_TEXT | TABLE row=6 col=0]
6.0

[P00241 | 39203:39245 | NORMAL_TEXT | TABLE row=6 col=1]
User Engagement, On-Ramp, Hazard Hackweek

[P00242 | 39246:39271 | NORMAL_TEXT | TABLE row=6 col=2]
EarthScope + UW eScience

[P00243 | 39272:39280 | NORMAL_TEXT | TABLE row=6 col=3]
~$0.55M

[P00244 | 39282:39286 | NORMAL_TEXT | TABLE row=7 col=0]
7.0

[P00245 | 39287:39327 | NORMAL_TEXT | TABLE row=7 col=1]
National Operations, SRE, Security, PMO

[P00246 | 39328:39339 | NORMAL_TEXT | TABLE row=7 col=2]
EarthScope

[P00247 | 39340:39348 | NORMAL_TEXT | TABLE row=7 col=3]
~$1.20M

[P00248 | 39350:39351 | NORMAL_TEXT | TABLE row=8 col=0]
⟦EMPTY PARAGRAPH⟧

[P00249 | 39352:39415 | NORMAL_TEXT | TABLE row=8 col=1]
Total Direct (3 yr; indicative; refine in Supp. Cost Estimate)

[P00250 | 39416:39417 | NORMAL_TEXT | TABLE row=8 col=2]
⟦EMPTY PARAGRAPH⟧

[P00251 | 39418:39426 | NORMAL_TEXT | TABLE row=8 col=3]
~$6.35M

[P00252 | 39427:39902 | NORMAL_TEXT]
Temporal stages: Phase 1 architecture and operational baseline (months 1–3); Phase 2 national scale-out (months 3–9); Phase 3 integrated testing and early operations (months 9–12) culminating in the NSF operational-readiness review at end of year 1; Phase 4 continuous operations and DevOps evolution (years 2–3). Detailed quarter-by-quarter Gantt with milestones is maintained in Smartsheet under formal change control and provided in the Project Execution Plan upon award.

[P00253 | 39902:40365 | NORMAL_TEXT]
Multi-organization governance. EarthScope's PMO has binding authority over schedule, cost, and acceptance for all subawards. A change-control board chaired by Deutsch reviews scope or schedule changes monthly. Decision-making rights and escalation paths are documented in the Project Execution Plan filed with NSF post-award. Pre-full-ops performance is demonstrated through Phase-3 acceptance testing against the §4 KPIs and the named early-user access program.

[P00254 | 40365:40381 | NORMAL_TEXT]
5.3 Outsourcing

[P00255 | 40381:40509 | NORMAL_TEXT]
OpenEarthAI outsources only what is more efficient or specialized to outsource. Major outsourced services with measurable SLAs:

[P00256 | 40509:40707 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
AWS Enterprise Support: 99.99% S3 SLA per AWS published terms; severity-1 case response ≤15 minutes; dedicated Technical Account Manager. Vendor performance reviewed monthly by the Operations Lead.

[P00257 | 40707:40759 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
GitHub Enterprise (code hosting, CI/CD): 99.9% SLA.

[P00258 | 40759:40832 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Atlassian (issue tracking, internal docs): standard enterprise-tier SLA.

[P00259 | 40832:40895 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Smartsheet (project management): standard enterprise-tier SLA.

[P00260 | 40895:41071 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Specialized data-engineering or AI-MLOps consulting may be procured for bounded scopes under fixed-price contracts; capped at 10% of any year's direct costs with PMO approval.

[P00261 | 41071:41430 | NORMAL_TEXT]
EarthScope has documented experience overseeing vendor contracts of this kind for the NGF program. All outsourced work is subject to facility-grade oversight: contract review by EarthScope counsel, monthly performance metrics, risks logged in the project Risk Register, and acceptance against operational-readiness standards before deliverables are accepted.

[P00262 | 41430:41443 | NORMAL_TEXT]
5.4 Software

[P00263 | 41443:41608 | NORMAL_TEXT]
OpenEarthAI-developed software is released under the Apache License 2.0 (stated explicitly per IDSS requirement). Major components and develop-vs-acquire decisions:

[P00264 | 41608:42073 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Develop in-house: National DataHub federation extensions; ModelHub registry and inference orchestration; HazEvalHub leaderboard and anti-leakage controls; the three Cross-Modality Discovery Agents; provenance and reproducibility tooling. Justification: no acceptable open-source equivalent exists at the integration scope and hazard-science focus OpenEarthAI requires; the team has shipped equivalent components before (NGF; OpenEarthAI HazLab regional prototype).

[P00265 | 42073:42268 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Adopt and extend open-source: Zarr, Apache Iceberg, IceChunk, STAC, PyTorch, Hugging Face datasets, Apache Kafka, CILogon, TorchGeo. Upstream contributions where domain extensions are developed.

[P00266 | 42268:42478 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
License or hosted service: SageMaker base layer (extended in-house); AWS Bedrock for inference endpoint hosting as an option. Each licensed component is benchmarked against open-source alternatives biennially.

[P00267 | 42478:42768 | NORMAL_TEXT]
Software engineering practices: secure CI/CD with automated testing (unit, integration, regression), automated vulnerability scanning, mandatory ≥1-engineer code review, semantic versioning, public release notes, and reproducibility audits. Documentation is part of the definition of done.

[P00268 | 42768:42788 | NORMAL_TEXT]
5.5 Risk Management

[P00269 | 42788:42894 | NORMAL_TEXT]
Risks are tracked in a Smartsheet Risk Register reviewed monthly by the PMO. Major risks and mitigations:

[P00270 | 42897:42902 | NORMAL_TEXT | TABLE row=0 col=0]
Risk

[P00271 | 42903:42912 | NORMAL_TEXT | TABLE row=0 col=1]
Category

[P00272 | 42913:42919 | NORMAL_TEXT | TABLE row=0 col=2]
Prob.

[P00273 | 42920:42927 | NORMAL_TEXT | TABLE row=0 col=3]
Impact

[P00274 | 42928:42939 | NORMAL_TEXT | TABLE row=0 col=4]
Mitigation

[P00275 | 42941:42987 | NORMAL_TEXT | TABLE row=1 col=0]
Foundation-model training cost exceeds budget

[P00276 | 42988:43010 | NORMAL_TEXT | TABLE row=1 col=1]
Financial / technical

[P00277 | 43011:43018 | NORMAL_TEXT | TABLE row=1 col=2]
Medium

[P00278 | 43019:43024 | NORMAL_TEXT | TABLE row=1 col=3]
High

[P00279 | 43025:43188 | NORMAL_TEXT | TABLE row=1 col=4]
NAIRR allocation as primary compute path; documented re-baseline triggers; model-size caps reviewed quarterly; reuse of OpenEarthAI HazLab pre-trained components.

[P00280 | 43190:43231 | NORMAL_TEXT | TABLE row=2 col=0]
Subaward delivery slips on AI components

[P00281 | 43232:43253 | NORMAL_TEXT | TABLE row=2 col=1]
Technical / schedule

[P00282 | 43254:43261 | NORMAL_TEXT | TABLE row=2 col=2]
Medium

[P00283 | 43262:43267 | NORMAL_TEXT | TABLE row=2 col=3]
High

[P00284 | 43268:43342 | NORMAL_TEXT | TABLE row=2 col=4]
Phased gates; PMO binding authority; contingency RSE staff at EarthScope.

[P00285 | 43344:43412 | NORMAL_TEXT | TABLE row=3 col=0]
Discovery Agents introduce reproducibility / trustworthiness issues

[P00286 | 43413:43431 | NORMAL_TEXT | TABLE row=3 col=1]
Technical / trust

[P00287 | 43432:43439 | NORMAL_TEXT | TABLE row=3 col=2]
Medium

[P00288 | 43440:43447 | NORMAL_TEXT | TABLE row=3 col=3]
Medium

[P00289 | 43448:43603 | NORMAL_TEXT | TABLE row=3 col=4]
Deliberate scope limitation (data discovery only); deterministic where possible; provenance-logged; phased external rollout; internal red-team evaluation.

[P00290 | 43605:43674 | NORMAL_TEXT | TABLE row=4 col=0]
Community adoption slower than projected outside the Pacific NW core

[P00291 | 43675:43684 | NORMAL_TEXT | TABLE row=4 col=1]
Adoption

[P00292 | 43685:43692 | NORMAL_TEXT | TABLE row=4 col=2]
Medium

[P00293 | 43693:43698 | NORMAL_TEXT | TABLE row=4 col=3]
High

[P00294 | 43699:43848 | NORMAL_TEXT | TABLE row=4 col=4]
Letters-of-Collaboration commitments at submission across all four use-case regions; named early-adopter program; quarterly user-engagement reviews.

[P00295 | 43850:43887 | NORMAL_TEXT | TABLE row=5 col=0]
Vendor failure or AWS pricing change

[P00296 | 43888:43912 | NORMAL_TEXT | TABLE row=5 col=1]
Outsourcing / financial

[P00297 | 43913:43917 | NORMAL_TEXT | TABLE row=5 col=2]
Low

[P00298 | 43918:43925 | NORMAL_TEXT | TABLE row=5 col=3]
Medium

[P00299 | 43926:44027 | NORMAL_TEXT | TABLE row=5 col=4]
Multi-cloud-portable formats by design; vendor-agnostic STAC; documented exit plan per major vendor.

[P00300 | 44029:44052 | NORMAL_TEXT | TABLE row=6 col=0]
Cybersecurity incident

[P00301 | 44053:44062 | NORMAL_TEXT | TABLE row=6 col=1]
Security

[P00302 | 44063:44067 | NORMAL_TEXT | TABLE row=6 col=2]
Low

[P00303 | 44068:44077 | NORMAL_TEXT | TABLE row=6 col=3]
Critical

[P00304 | 44078:44184 | NORMAL_TEXT | TABLE row=6 col=4]
NIST-aligned controls (§5.6); annual penetration test; incident-response plan and notification procedure.

[P00305 | 44186:44219 | NORMAL_TEXT | TABLE row=7 col=0]
Research-security non-compliance

[P00306 | 44220:44231 | NORMAL_TEXT | TABLE row=7 col=1]
Compliance

[P00307 | 44232:44236 | NORMAL_TEXT | TABLE row=7 col=2]
Low

[P00308 | 44237:44246 | NORMAL_TEXT | TABLE row=7 col=3]
Critical

[P00309 | 44247:44388 | NORMAL_TEXT | TABLE row=7 col=4]
IN 149 training tracked in PMO; MFTRP certified annually; Confucius Institute compliance verified before submission and reverified annually.

[P00310 | 44390:44443 | NORMAL_TEXT | TABLE row=8 col=0]
Funding-policy change (e.g., 15% IDC cap activation)

[P00311 | 44444:44463 | NORMAL_TEXT | TABLE row=8 col=1]
Financial / policy

[P00312 | 44464:44471 | NORMAL_TEXT | TABLE row=8 col=2]
Medium

[P00313 | 44472:44479 | NORMAL_TEXT | TABLE row=8 col=3]
Medium

[P00314 | 44480:44590 | NORMAL_TEXT | TABLE row=8 col=4]
Budget at negotiated rate per current law; contingency plan if NSF 25-034 activates; quarterly policy review.

[P00315 | 44592:44629 | NORMAL_TEXT | TABLE row=9 col=0]
Long-term sustainability after award

[P00316 | 44630:44645 | NORMAL_TEXT | TABLE row=9 col=1]
Sustainability

[P00317 | 44646:44653 | NORMAL_TEXT | TABLE row=9 col=2]
Medium

[P00318 | 44654:44659 | NORMAL_TEXT | TABLE row=9 col=3]
High

[P00319 | 44660:44816 | NORMAL_TEXT | TABLE row=9 col=4]
Operations-cost trajectory engineered to integrate into NGF facility ops post-award; partnership and fee-based mechanisms for long-term storage costs (§6).

[P00320 | 44817:44850 | NORMAL_TEXT]
5.6 Security and Trustworthiness

[P00321 | 44850:45289 | NORMAL_TEXT]
OpenEarthAI inherits and extends EarthScope's established security program. Reference policy regimes: NIST SP 800-53 / 800-171 (moderate baseline), CIS Benchmarks for AWS, OWASP Top 10 for web services, MITRE ATLAS for AI-system threats. Roles: Security Lead reports to the PI; CISO-equivalent at EarthScope retains organizational security authority. Risk assessments are conducted annually with a third-party penetration test biennially.

[P00322 | 45289:45936 | NORMAL_TEXT]
Technical safeguards: TLS-everywhere; encryption at rest (S3 SSE-KMS); least-privilege IAM with mandatory MFA; network segmentation between public and internal subnets; comprehensive audit logging via CloudTrail and OpenSearch; automated vulnerability scanning; SBOM generation; dependency pinning; container-image signing. Agentic-AI-specific controls (essential because Discovery Agents are user-facing): prompt-injection defenses, tool-call allowlists, output provenance logging, and human-in-the-loop gates for any action that could modify state. Discovery Agents have read-only access to data layers and cannot mutate the catalog or storage.

[P00323 | 45936:46461 | NORMAL_TEXT]
Administrative safeguards: annual security awareness training for all personnel; quarterly access reviews; documented incident-response plan with notification procedures to NSF (within 24 hours of confirmed material incident), to the user community (per CISA disclosure best practices), and to law enforcement as appropriate. Effectiveness is evaluated through annual tabletop exercises, biennial penetration testing, and a quarterly metrics review (mean time to detect, mean time to contain, security-finding closure rate).

[P00324 | 46461:46967 | NORMAL_TEXT]
Important Notice 149 obligations are explicitly addressed: every Senior Personnel listed has completed (or will complete prior to submission) Research Security Training within the 1-year IN 149 window; every Senior Personnel executes annual MFTRP certification; the lead institution (EarthScope) and the subaward institution (UW) confirm the absence of any Confucius Institute agreement; FFDR reporting follows the IN 149 timeline. The Security Lead coordinates IN 149 compliance across both institutions.

[P00325 | 46967:46988 | NORMAL_TEXT]
6. Budget Estimation

[P00326 | 46988:47406 | NORMAL_TEXT]
OpenEarthAI is proposed as a Category II project, 3 years, with total cost below the $9M Category II cap. The summary below outlines the budget shape; the detailed cost estimate (organized by phase and by WBS element, with basis of estimates) is provided in the Supplementary Cost Estimate document, with budget justifications by institution (EarthScope lead, UW subaward) following PAPPG and NSF 26-509 requirements.

[P00327 | 47406:47429 | NORMAL_TEXT]
6.1 Total Cost Summary

[P00328 | 47432:47437 | NORMAL_TEXT | TABLE row=0 col=0]
Year

[P00329 | 47438:47450 | NORMAL_TEXT | TABLE row=0 col=1]
Direct ($M)

[P00330 | 47451:47465 | NORMAL_TEXT | TABLE row=0 col=2]
Indirect ($M)

[P00331 | 47466:47477 | NORMAL_TEXT | TABLE row=0 col=3]
Total ($M)

[P00332 | 47479:47506 | NORMAL_TEXT | TABLE row=1 col=0]
1 (Transition + Scale-Out)

[P00333 | 47507:47513 | NORMAL_TEXT | TABLE row=1 col=1]
~2.30

[P00334 | 47514:47520 | NORMAL_TEXT | TABLE row=1 col=2]
~1.05

[P00335 | 47521:47527 | NORMAL_TEXT | TABLE row=1 col=3]
~3.35

[P00336 | 47529:47559 | NORMAL_TEXT | TABLE row=2 col=0]
2 (Full Ops + Model Releases)

[P00337 | 47560:47566 | NORMAL_TEXT | TABLE row=2 col=1]
~2.20

[P00338 | 47567:47573 | NORMAL_TEXT | TABLE row=2 col=2]
~1.00

[P00339 | 47574:47580 | NORMAL_TEXT | TABLE row=2 col=3]
~3.20

[P00340 | 47582:47610 | NORMAL_TEXT | TABLE row=3 col=0]
3 (Full Ops + Renewal Prep)

[P00341 | 47611:47617 | NORMAL_TEXT | TABLE row=3 col=1]
~1.85

[P00342 | 47618:47624 | NORMAL_TEXT | TABLE row=3 col=2]
~0.85

[P00343 | 47625:47631 | NORMAL_TEXT | TABLE row=3 col=3]
~2.70

[P00344 | 47633:47661 | NORMAL_TEXT | TABLE row=4 col=0]
Total (3 yr; under $9M cap)

[P00345 | 47662:47668 | NORMAL_TEXT | TABLE row=4 col=1]
~6.35

[P00346 | 47669:47675 | NORMAL_TEXT | TABLE row=4 col=2]
~2.90

[P00347 | 47676:47697 | NORMAL_TEXT | TABLE row=4 col=3]
~9.25 → trim to ≤$9M

[P00348 | 47698:48214 | NORMAL_TEXT]
Indirect costs are computed at each institution's federally negotiated rate (UW: 55.5% MTDC on-campus per cognizant-agency letter; EarthScope: per its negotiated agreement). The 15% IDC cap of NSF 25-034 is currently not in effect (court vacated); awards include a contingency term that may apply the cap if NSF is later permitted to implement, and the budget will be re-baselined if that occurs. Final budget is tuned in the Supplementary Cost Estimate to land below the $9M Cat II cap with reasonable contingency.

[P00349 | 48214:48245 | NORMAL_TEXT]
6.2 Cost by Category and Phase

[P00350 | 48245:48849 | NORMAL_TEXT]
Personnel (~70% of direct): operations team scales up across year 1; development effort heaviest in year 1; foundation-model training compute heaviest in year 2 with model releases. Cloud infrastructure (~15% of direct): grows with usage; engineered for cost-per-query reduction year over year. Travel and training (~5%): includes annual NSF PI meeting, major CI conference travel, and annual OpenEarthAI Hazard Hackweek travel support. Outsourced services and software licenses (~5%): vendor SLAs disclosed in §5.3. Equipment (~5%): minor end-user laptops and modest on-premise compute for development.

[P00351 | 48849:48904 | NORMAL_TEXT]
6.3 Other Funding Sources and Scope-Overlap Prevention

[P00352 | 48904:49906 | NORMAL_TEXT]
EarthScope's base NGF Cooperative Agreement supports the underlying facility (continued data collection, archive operations, user support for non-AI workflows). OpenEarthAI's scope is the cross-agency, multi-hazard, AI-ready integration layer and is distinct from the NGF base scope; the boundary is documented in a Memorandum of Understanding between EarthScope's NGF and OpenEarthAI programs and audited annually. The UW subaward is scoped to OpenEarthAI-specific activities and does not duplicate scope already supported by other NSF, NASA, or NOAA awards held by the UW investigators (Current and Pending Support documents disclose all overlap and confirm none in scope). Forbidden cost categories — long-term data hosting/storage/curation, building renovation, and individual research enabled by the infrastructure — are excluded from the OpenEarthAI budget; long-term storage is funded via existing NGF facility mechanisms or partnership/fee-based arrangements as encouraged by the solicitation.

[P00353 | 49906:49954 | NORMAL_TEXT]
6.4 Cat II Transition Plan from Current Funding

[P00354 | 49954:50952 | NORMAL_TEXT]
The UW OpenEarthAI HazLab regional prototype is currently supported by the UW eScience Institute, UW College of the Environment, and the UW Fund for Future Science and Technology (FFST). Those funding sources are research-program-scale and are scheduled to conclude or transition to other purposes during year 1 of OpenEarthAI. The transition plan: months 1–6, OpenEarthAI HazLab regional services continue under current UW support while integration with the EarthScope cloud envelope is completed; months 6–12, OpenEarthAI HazLab national-scale services run in parallel under OpenEarthAI Cat II support while regional-only endpoints are deprecated; month 12, transition complete and all services run under OpenEarthAI Cat II support. Continuity of service is guaranteed for current OpenEarthAI HazLab users throughout the transition. Similarly, the existing NGF and ASF user-facing services are not interrupted; OpenEarthAI scope is additive and complementary to both during and after transition.

[P00355 | 50952:50968 | NORMAL_TEXT]
Broader Impacts

[P00356 | 50968:51184 | NORMAL_TEXT]
OpenEarthAI delivers broad national benefit aligned with the America COMPETES Reauthorization Act broader-impacts goals 1–6 (and 7 in an open-to-all-Americans framing) and with the April 2025 NSF priority statement.

[P00357 | 51184:51832 | NORMAL_TEXT]
Public safety, infrastructure resilience, and economic competitiveness (goals 1–2). Multi-hazard cascades — atmospheric-river floods and landslides, earthquake-induced ground failure, post-fire debris flows, severe convective storms — affect public safety, critical infrastructure, insurance markets, agriculture, and military readiness across all 50 states. OpenEarthAI’s national multi-hazard foundation models and benchmarks lower the barrier for agency partners, hazard engineering and insurance industry, and state and local emergency-management offices to use modern AI methods, directly serving U.S. economic competitiveness and resilience.

[P00358 | 51832:52370 | NORMAL_TEXT]
Workforce development (goal 2). OpenEarthAI trains the next generation of hazard-AI engineers, data scientists, and domain researchers through On-Ramp cloud notebooks, an annual OpenEarthAI Hackweek run by UW eScience, and two domain-focused short courses per year. Together these activities will train at least 1,800 researchers and students cumulatively over three years, open to applicants from all U.S. institutions in all 50 states and EPSCoR jurisdictions. Geographic distribution of training participants is monitored as a §4 KPI.

[P00359 | 52370:52768 | NORMAL_TEXT]
Geographic reach and institutional access. OpenEarthAI is engineered to reach all 50 U.S. states, EPSCoR jurisdictions, community colleges, primarily undergraduate institutions, MSIs, and HBCUs as institutional partners. Cloud-native delivery removes the on-premise hardware barrier; the open-tier allocation policy ensures no-questions-asked entry-level access for any U.S. researcher or student.

[P00360 | 52768:53122 | NORMAL_TEXT]
Academia–industry partnership (goal 4). OpenEarthAI’s open foundation models, benchmarks, and APIs lower the entry barrier for U.S. startups and innovation users in hazard engineering, insurance, infrastructure resilience, and utilities. The reusable feature library and hazard benchmarks materially advance the U.S. AI-for-hazards innovation ecosystem.

[P00361 | 53122:53480 | NORMAL_TEXT]
Pre-K–12 and undergraduate STEM education (goals 5–6). Modular, classroom-ready hazard-science materials mapped to Next Generation Science Standards Earth and Space Sciences strands will be released openly to all U.S. educators. Undergraduate Carpentries-style lessons and ready-to-teach Jupyter notebooks will accompany each foundation model and benchmark.

[P00362 | 53480:54007 | NORMAL_TEXT]
Open access and Gold Standard Science. Every OpenEarthAI software component is released under Apache License 2.0; every data product under CC-BY-4.0 or equivalent; every foundation model with weights, model card, and training pipeline; every public dashboard exposes operational and scientific-impact metrics in real time. These practices materially advance the Gold Standard Science tenets of EO 14303 — reproducibility, transparency, communication of error and uncertainty, peer review, and absence of conflicts of interest.

[P00363 | 54007:54599 | NORMAL_TEXT]
Integration with the national CI ecosystem. OpenEarthAI is complementary to and integrates with the NAIRR Pilot (data layer for AI compute), ACCESS (data services for ACCESS-allocated jobs), the NSF AI Institutes (data layer for AI methods research), NASA ESDS, NOAA Big Data, USGS, DOE programs, and NSF Major Facilities (NEON, OOI, IceCube). By filling the cross-facility, multimodal, AI-ready, multi-hazard integration gap that no single program currently fills, OpenEarthAI strengthens the entire national research-data ecosystem and advances U.S. leadership in AI-driven hazard science.

