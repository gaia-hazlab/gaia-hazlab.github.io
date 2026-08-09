# OpenEarthAI_IDSS_Cat2_ProjectDescription_v4

- Document ID: 1_0biYxew7Ii6RVLBJf3tFLoAHj1lbkT6HEjW6JbKQXI
- Revision ID: AIroW36Xnv_iFJciJ-w45wXOsuguFmJZMKs46zDA23BAtn4Gwj_K2psv9m9F8EcLgGiFgNQVZE0G0HUdU5MiA4qAMhzxhIirxg2Spdc6vnI
- Selected tab: all
- Protected controls: 0
- Opaque controls: 0
- Authoritative dropdowns: 0

Protected-control annotations are preservation instructions. Do not insert their displayed placeholder text to recreate a native control.

## ProjectDescription (t.0)

[P00001 | 1:92 | NORMAL_TEXT]
Category II: OpenEarthAI — Multi-Hazard Foundation Models on Multimodal Earth Science Data

[P00002 | 92:204 | NORMAL_TEXT]
Geophysical AI-driven Integration and Assimilation: Scaling a National Operational Hazard-Science Data Platform

[P00003 | 204:247 | NORMAL_TEXT]
1. Vision, Goals, and Driving Requirements

[P00004 | 247:258 | NORMAL_TEXT]
1.1 Vision

[P00005 | 258:1523 | NORMAL_TEXT]
Many of the most consequential U.S. hazards arise as cascades in which one disturbance changes the physical state in which the next occurs (Yanites et al., 2025). Intense precipitation on wildfire-altered terrain can trigger destructive runoff and debris flows (Staley et al., 2017), while rainfall-driven groundwater recharge can raise the water table and increase liquefaction susceptibility during subsequent earthquake shaking (Cox et al., 2021). No single observing system spans the spatial scale, cadence, subsurface sensitivity, and all-weather availability required to resolve these coupled processes. The necessary evidence includes seismic and infrasound records, distributed acoustic sensing (DAS), GNSS, SAR/InSAR, precipitation and weather radar, soil moisture, snowpack, groundwater levels, streamflow, topography, burn severity, vegetation, and land-surface fluxes. These data are currently distributed among facilities and agencies, including the NSF National Geophysical Facility operated by EarthScope Consortium; NASA and the NASA Alaska Satellite Facility for SAR and Earth-observation products; NOAA NCEI, NWS, and NCEP for radar, precipitation, forecasts, and reanalysis; and USGS for earthquakes, streamflow, topography, and hazard products.

[P00006 | 1523:1524 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00007 | 1524:2997 | NORMAL_TEXT]
What is missing is a national, AI-ready operational infrastructure that fuses them to deliver actionable data models that can advance multi-hazards by researchers, agency partners, and communities at risk. OpenEarthAI will serve as an Integrated Data Systems and Services (IDSS) Category II infrastructure for transdisciplinary Earth science across data modalities and spatial scales.OpenEarthAI aims to become the IDSS (spell that out) infrastructure that advanced Earth science across disciplinary boundaries and data modalities. Building directly on twothree operational predecessors that already serve U.S. researchers (the EarthScope-operated National Science Foundation National Geophysical Facility (NSF-NGF), the NASA-NSF Alaska Satellite Facility, and UW labs that have prototyped OpenEarthAI at a regional scale, this Category II project scales and broadens the existing capabilities into a single, national, operational, AI-native multi-hazard data platform. OpenEarthAI delivers a federated multi-modal data layer harmonized across agencies; an open multi-hazard foundation-model registry with reproducible training pipelines and public weights; a national hazard-evaluation benchmark suite with held-out golden data sets; and a suite of agents that will support researchers, industries, and citizens to discover, explain, and process data for their own individualized use. By the end of award year 1, OpenEarthAI reaches full operations as a national service.

[P00008 | 2997:3635 | NORMAL_TEXT]
OpenEarthAI serves the highest-priority national needs. Climate-amplified hazards threaten public safety, critical infrastructure, insurance markets, and military readiness across all 50 states. The April 2025 NSF priority statement identifies artificial intelligence as a Federal R&D priority area; Executive Order 14303 (Gold Standard Science) requires reproducibility, transparency, and uncertainty communication in federally supported research; and the NAIRR Pilot calls for highly performant interconnected data infrastructure for AI-driven research. OpenEarthAI is the operational hazard-science data platform that meets all three.

[P00009 | 3635:3645 | NORMAL_TEXT]
1.2 Goals

[P00010 | 3645:3767 | NORMAL_TEXT]
OpenEarthAI pursues four measurable goals, each tied to performance objectives in §4 and to operational milestones in §3:

[P00011 | 3767:4114 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G1 — National Multi-Earth Data Integration. Operate, by end of award year 1, a production-grade, FAIR-aligned, AI-ready federated data layer spanning EarthScope, ASF, NOAA, USGS, NSF NEON, and HydroFrame archives, accessible from any U.S. institution. Scale the GAIA HazLab DataHub from single-region (Washington State) coverage to all 50 states.

[P00012 | 4114:4499 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G2 — Multi-Earth Foundation Models. Train, evaluate, document, and openly release at least three multimodal foundation models (geophysical sensor, SAR/Sentinel, hydro-meteorological, Earth structural, and across these modalities) with public weights, model cards, and reproducible training pipelines. Extend the GAIA HazLab ModelHub from research-lab to national operational registry.

[P00013 | 4499:4736 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G3 — National Earth Model Evaluation. Operate a public benchmark suite (e.g., HazEvalHub at national scale) with hidden test partitions, leaderboards, and uncertainty quantification aligned with WMO, USGS, and AI/ML community standards.

[P00014 | 4736:5105 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
G4 — Cross-Modality Earth Agents. Operate a suite of provenance-aware agents that help users discover what data are available across modalities for a given location, time window, or hazard type, and that compose reproducible workflow stubs. Agent scope is deliberately constrained to data discovery and workflow scaffolding — not autonomous scientific decision-making.

[P00015 | 5105:5148 | NORMAL_TEXT]
1.3 Existing System Performance and Demand

[P00016 | 5148:5381 | NORMAL_TEXT]
Per NSF 26-509 Category II requirements, OpenEarthAI is a transition of operational systems already serving demonstrated user communities to broader national scale. Three lines of operational-system evidence motivate the transition.

[P00017 | 5381:6508 | NORMAL_TEXT]
EarthScope National Geophysical Facility (NGF, lead institution operational system). The NGF is the operational successor to the IRIS and UNAVCO data centers and is the steward of NSF's continental seismic and geodetic networks. Quantitative metrics over the most recent reporting period (2023–2025; detailed numbers and trend lines in Supplementary Cost Estimate): registered active users in the [thousands] across [hundreds] of U.S. institutions in all 50 states; data egress at the [petabytes-per-year] scale with cloud-native object-store distribution since the 2023 migration; year-over-year growth in active users and egress volume documented and continuing. NGF performance objectives currently in place include service availability, data completeness, time-to-data after acquisition, and user-satisfaction surveys; current-against-target performance is tracked at the EarthScope operations dashboard. The NGF demonstrates that EarthScope can build, operate, and scale national CI; it does not yet provide multi-modal AI-ready fusion, multi-hazard foundation models, or cross-modality discovery — the OpenEarthAI scope.

[P00018 | 6508:7103 | NORMAL_TEXT]
NASA-NSF Alaska Satellite Facility (ASF, federation partner). ASF distributes Sentinel-1 and forthcoming NISAR SAR data products and OPERA InSAR time-series products to a U.S. user community measured in [thousands] of registered users and [hundreds of TB] per month of egress. ECMWF reanalysis data (ERA5 / ERA-Land) is co-located in AWS S3 at ASF, providing the atmospheric layer needed for hazard fusion already in the cloud and ready to integrate. ASF is integrated as a federation partner via STAC catalog interoperability and AWS co-location (Letter of Collaboration on file); no subaward.

[P00019 | 7103:9287 | NORMAL_TEXT]
UW regional-scale systems.UW regional-scale labs. First, the GAIA HazLab regional prototype (subawardee). Since 20254, the UW Earth & Space Sciences and eScience Institute, with support from UW College of the Environment and the UW Fund for Future Science and Technology (FFST), have operated GAIA HazLab — a regional, multi-modal hazard-science platform covering Washington State and surrounding Pacific Northwest (see gaia-hazlab.github.io). GAIA HazLab demonstrates the core technical concepts at sub-national scale: a DataHub (streamlined cross-agency data ingestion of NOAA precipitation, USGS  and streamflow, USGS seismic, SOLUS soil properties,NSF GNSS, ASF SAR, and Synoptic weather observations); a ModelHub (registry of operational models for AR-driven flood forecasting, storm detection, earthquake wavefield reconstruction, ground-failure surrogate modeling, hydromechanical memory inversion, post-fire debris flow modeling, and convective-storm characterization); and a HazEvalHub (fair-evaluation framework with hidden test partitions are developed in partnership with the AI Institute for Dynamical Systems, AI2, and Kaggle). The current public prototype demonstrates two concrete integration patterns: a multimodal dashboard that co-locates ground sensors, weather and hydrology, terrain, soil, and remote-sensing layers; and a virtual-discharge workflow that combines sparse USGS gauges with dense river-seismic observations along the western Mount Rainier corridor during the December 2025 atmospheric-river sequence. These are research demonstrations, not an operational warning system.The prototype has informed concrete hazard analyses across four named recent events documented on the public site: the 2025 Western Washington atmospheric-river floods and landslides, the Nisqually earthquake liquefaction record (2001–2031 monitoring envelope), the 2025 Stehekin post-fire debris flow, and convective-thunderstorm severity. GAIA HazLab establishes the science case, the technical readiness, and named user demand; what it does not provide today is national reach, operational SRE-grade footing, federated identity at scale, or release-grade foundation models. 

[P00020 | 9287:10251 | NORMAL_TEXT]
Second, UW FiberLab operates seven distributed-fiber-sensing interrogators and has acquired approximately 2 PB of DAS data across solid-Earth, cryosphere, ocean, infrastructure, and ecological applications. Peer-reviewed demonstrations show that DAS can resolve volcanic processes (Jousset et al., 2022), glacier runoff and cryospheric dynamics (Manos et al., 2024), coupled calving, fjord circulation, and submarine melt (Gräff et al., 2025), offshore earthquakes and ocean wavefields (Shi et al., 2025), marine-mammal vocalizations (Bouffaut et al., 2022; Abadi et al, 2022), offshore geotechnical structure (Trafford et al., 2022), and mountain mass movements (Paitz et al., 2023). UWFiberLab has also prototyped a cloud-native object-store architecture with EarthScope data services (Ni et al., 2024) and public MinIO-based delivery. Together, these holdings and services provide a concrete instrument-facility-to-national-data-infrastructure transition case.

[P00021 | 10251:12085 | NORMAL_TEXT]
Third, the UW eScience Institute’s Scientific Software Engineering Center (SSEC) has developed LLMoxie as an extensible environment for agent-assisted scientific software engineering and is expanding reusable retrieval and tool libraries through the NAIRR-supported LLMaven effort (UW eScience Institute, 2026). OpenEarthAI will adapt those cross-disciplinary capabilities and the regional GAIA Translator prototype into agents that operate close to governed Earth-science data. A user can ask a place-, time-, hazard-, or workflow-specific question; the agent will call read-only catalog and data tools, assemble cross-modal evidence, and return a cited explanation, versioned data manifest, and reproducible notebook scaffold. HazEvalHub will test groundedness, citation discipline, task completion, appropriate abstention, and unsafe-action rates. Agents will not modify source data or make autonomous scientific, infrastructure, or emergency-management decisions.Third, the UW eScience Institute’s Scientific Software Engineering Center (SSEC) has prototyped LLMoxie and KnowledgeHub services for governed scientific agents and professional-grade research software. The existing pilot combines deterministic tool calls, retrieval from curated scientific knowledge, citation and groundedness checks, workflow-reproducibility checks, and human-in-the-loop controls. The Category II transition will convert this regional pilot into an EarthScope-facing national service for data discovery, workflow setup, documentation, user support, and reproducibility auditing, with explicit evaluation of provenance, groundedness, unsafe-action rates, and task completion. Agents will remain constrained to read-only discovery and workflow scaffolding and will not make autonomous scientific, infrastructure, or emergency-management decisions.

[P00022 | 12085:12086 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00023 | 12086:12126 | NORMAL_TEXT]
Those are the Category II deliverables.

[P00024 | 12126:12608 | NORMAL_TEXT]
Together these operational systems form the substrate OpenEarthAI scales. The Category II investment is is a transition from sub-national operational capability to national operational capability, executed by teams who have already done the equivalent transitions before (GeoSciCloud and GeoSciFramework into the NGF; the Pangeo ecosystem at UW eScience; and GAIA HazLab that stemmed from two CSSI projcets (SCOPED 2021 and GAIA 2026) from regional prototype to growing user base).

[P00025 | 12608:12632 | NORMAL_TEXT]
1.4 Reference Use Cases

[P00026 | 12632:13176 | NORMAL_TEXT]
OpenEarthAI is anchored by four reference hazard-cascade use cases. Each is drawn from a distinct hazard regime and a distinct geographic class of impact, and each requires the multi-modal AI-ready data fusion that no current national CI provides. Each is documented at the Washington-state scale today via OpenEarthAI and is scaled to national reach by OpenEarthAI. Each involves at least three of the disciplinary communities served by OpenEarthAI: solid Earth, hydrology and atmospheric science, ecology and land-surface science, and AI/ML.

[P00027 | 13176:13623 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U1 — Atmospheric-river-driven flood and shallow landslide cascades. AR events affect the entire West Coast (CA, OR, WA, AK) and increasingly the Northeast. Fusion of NOAA QPE and reanalysis precipitation, USGS streamflow, GNSS-IR soil moisture and SWE, InSAR pre-event deformation, and vegetation-stress imagery is required. Today: regional prototype on GAIA HazLab covers WA only; national coverage is the Cat II deliverable through OpenEarthAI.

[P00028 | 13623:14146 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U2 — Earthquake-induced ground failure with antecedent-moisture modulation. Liquefaction and seismic landslides are amplified by hydromechanical state. Fusion of seismic ground-motion records, antecedent precipitation and soil moisture, GNSS, InSAR, and post-event imagery is required. Today: Nisqually and other Pacific NW events analyzed via OpenEarthAI HazLab; the New Madrid Seismic Zone, Cascadia, Charleston (SC), and Alaska are operationally underserved for moisture-modulated hazard. Cat II adds national coverage.

[P00029 | 14146:14554 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U3 — Post-wildfire debris-flow hazard. Post-fire watersheds across the western U.S. (CO, NM, MT, ID, WA, OR, CA) are primed for debris flows by fire-altered soil hydrology. Fusion of fire perimeters and burn severity, soil moisture, DEM/slope, precipitation forecasts, and post-event imagery is required. Today: Stehekin (WA) covered by GAIA HazLab; the operational gap nationally is the Cat II deliverable.

[P00030 | 14554:15039 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
U4 — Convective-storm intensification by land-atmosphere feedback. Severe convective storms across the Plains, Midwest, and Southeast are shaped by soil-moisture and surface-energy feedbacks. Fusion of NOAA radar and reanalysis, NEON tower and Ameriflux fluxes, GNSS-IR soil moisture, and seismic detection of thunderstorm signatures (an operational GAIA HazLab capability at national scale) is required. Today: WA-anchored prototype; Cat II extends to the convective corridor states.

[P00031 | 15039:15259 | NORMAL_TEXT]
These four use cases collectively span solid-Earth, hydrologic, atmospheric, ecological, and AI methodology communities — directly satisfying the IDSS "transdisciplinary and demonstrably multi-disciplinary" requirement.

[P00032 | 15259:15284 | NORMAL_TEXT]
1.5 Driving Requirements

[P00033 | 15284:15374 | NORMAL_TEXT]
Requirements derived from the use cases drive §2 architecture and §4 performance targets:

[P00034 | 15374:15568 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R1 — Federated AI-ready data: ≥10 federated agency archives, Zarr v3 / Parquet / STAC-JSON 1.x as primary serializations, tensor-ready outputs to PyTorch DataLoader, JAX, Hugging Face datasets.

[P00035 | 15568:15702 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R2 — National coverage, all 50 states: catalog and ingest harmonized observations across CONUS, Alaska, Hawaii, and U.S. territories.

[P00036 | 15702:15869 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R3 — Multi-hazard foundation models: at least three models released with public weights, training pipelines, and model cards by end of year 2; documented uncertainty.

[P00037 | 15869:16066 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R4 — Hazard evaluation rigor: held-out test partitions for each foundation model; public leaderboards with anti-leakage controls; uncertainty quantification consistent with WMO and USGS standards.

[P00038 | 16066:16247 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R5 — Cross-modality discovery agents: small-scope, deterministic-where-possible, provenance-logged; every agent action produces a versioned artifact reproducible without the agent.

[P00039 | 16247:16382 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R6 — Federated identity at national scale: CILogon-based identity supporting ≥150 institutions; merit-based plus open-tier allocation.

[P00040 | 16382:16579 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R7 — Reproducibility, transparency, uncertainty (Gold Standard Science): provenance (W3C PROV) on every product; uncertainty as first-class metadata; container-pinned, data-DOI-anchored workflows.

[P00041 | 16579:16729 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
R8 — Open license: OpenEarthAI-developed software under Apache License 2.0; data products under CC-BY-4.0 or equivalent consistent with source terms.

[P00042 | 16729:16769 | NORMAL_TEXT]
2. Project Definition and Specification

[P00043 | 16769:16786 | NORMAL_TEXT]
2.1 Architecture

[P00044 | 16786:17204 | NORMAL_TEXT]
OpenEarthAI is organized as four operational layers — DataHub at national scale, ModelHub at national scale, HazEvalHub at national scale, and a small Discovery Agents layer — operating on a shared cloud-native foundation. Layer names are inherited from the OpenEarthAI HazLab regional prototype to preserve continuity for existing users; the Cat II work is the operational and scientific scaling beneath those names.

[P00045 | 17204:18456 | NORMAL_TEXT]
DataHub (national). Streaming ingestion (Apache Kafka) and batch ETL of: EarthScope-managed seismic, GNSS, and high-rate GNSS streams; ASF-managed Sentinel-1 SAR and OPERA InSAR products plus co-located ECMWF ERA5/ERA-Land reanalysis; NOAA precipitation, streamflow, radar, and reanalysis; USGS hazard catalogs, hydrography, and burn severity; NSF NEON tower and ecology data; HydroFrame hydrology products; Synoptic and MesoWest weather observations; UW DAS archive (FiberLab); and curated physics-based simulation outputs from SCEC CyberShake and dynamic-rupture and debris-flow ensembles. Storage is cloud-native object store (AWS S3 primary, with multi-cloud-portable formats throughout): Zarr v3 with IceChunk for n-d arrays, Apache Iceberg / Parquet for tabular and event data, MiniSEED+StationXML preserved alongside cloud-optimized siblings. Catalog is STAC-JSON 1.x with PROV-O provenance and a STAC API targeting sub-second p95 latency at 10⁹ records. Coordinate systems and time bases are unified; quality, calibration, and uncertainty are first-class fields. The Cat II DataHub work scales the OpenEarthAI HazLab regional integration of NOAA + USGS + EarthScope + ASF + Synoptic data to national coverage and operational SRE-grade footing.

[P00046 | 18456:19758 | NORMAL_TEXT]
ModelHub (national). The model registry hosts versioned, model-carded, container-pinned hazard models. Cat II adds three new multimodal foundation models trained to address the four reference use cases: (i) a Ground-Failure Foundation Model fusing seismic, geodetic, hydrologic, and antecedent-moisture inputs to predict liquefaction and seismic-landslide susceptibility (extending the existing OpenEarthAI HazLab surrogate work of Sanger and Ni); (ii) a Hydro-Meteorological Cascade Model fusing NOAA precipitation, GNSS-IR soil moisture and SWE, InSAR pre-event deformation, and vegetation indices for AR-driven flood and shallow landslide cascades (extending the AR forecasting work with ACE2 / Clima-X); (iii) a Post-Fire Debris-Flow Model fusing burn severity, soil moisture, slope, and short-fuse precipitation forecasts. Models are released under Apache 2.0 with public weights, training data manifests, and reproducible training pipelines deposited at NAIRR-compatible registries. Existing operational OpenEarthAI HazLab models — storm detection from seismic + weather (Kharita, Anderson-Frey, Denolle), earthquake-wavefield reconstruction (Ni), heatwave forecasting (Hakim), and the hydromechanical memory inversion (Köpfli) — are migrated to operational footing as part of the same registry.

[P00047 | 19758:20341 | NORMAL_TEXT]
HazEvalHub (national). The evaluation framework provides fair-evaluation, anti-leakage benchmarking with hidden test partitions, public leaderboards, and standardized metrics (classification, regression, segmentation, probabilistic calibration). Evaluation standards align with WMO meteorology, USGS seismic, ISO risk-assessment, and ML community best practices. Cat II scales the existing OpenEarthAI HazLab evaluation framework — built in collaboration with the AI Institute for Dynamical Systems (Kutz), AI2, and Kaggle — to national coverage and to the four reference use cases.

[P00048 | 20341:21482 | NORMAL_TEXT]
Cross-Modality Discovery Agents . Three narrowly scoped agents operate on the OpenEarthAI stack: (i) a Data-Availability Agent that, given a location, time window, and hazard type, returns a structured manifest of which modalities are available, at what spatial and temporal resolution, with what quality flags, across all federated archives; (ii) a Cross-Modality Coverage Agent that audits co-availability of complementary modalities (e.g., is GNSS-IR soil moisture co-available with InSAR coherence and NOAA precipitation for a given event window?); (iii) a Workflow-Stub Agent that returns a versioned, container-pinned, data-DOI-anchored notebook scaffold for a chosen use case, including provenance metadata. Agents are deterministic where possible, retrieval-augmented where not, sandboxed (no autonomous data modification), and audited (every agent action produces a logged artifact). The agents do not replace human scientific judgment; they remove friction in data discovery. The Cat II work prototypes and operationalizes these three agents on the OpenEarthAI stack, deliberately limiting agent scope to maintain trustworthiness.

[P00049 | 21482:21507 | NORMAL_TEXT]
2.2 Systems and Services

[P00050 | 21507:21676 | NORMAL_TEXT]
OpenEarthAI delivers six user-visible services. Three transition from sub-national operational status to national operational status; three are new at the Cat II scope.

[P00051 | 21676:21829 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S1 — National Federated Catalog and STAC API (transitioning the OpenEarthAI HazLab catalog to national reach plus federation with NGF and ASF catalogs).

[P00052 | 21829:21943 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S2 — AI-Ready Data Distribution (Zarr / Parquet / Iceberg tensor-ready outputs; co-located cloud compute access).

[P00053 | 21943:22032 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S3 — Multi-Hazard Foundation-Model Registry and Inference Endpoints (national ModelHub).

[P00054 | 22032:22113 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S4 — Hazard Evaluation Benchmarks and Public Leaderboards (national HazEvalHub).

[P00055 | 22113:22194 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S5 — Cross-Modality Discovery Agents (the three small agents described in §2.1).

[P00056 | 22194:22327 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
S6 — On-Ramp Cloud Education and Training (extending EarthScope's existing On-Ramp platform; integrated with UW eScience Hackweeks).

[P00057 | 22327:22346 | NORMAL_TEXT]
2.3 Intended Users

[P00058 | 22346:22439 | NORMAL_TEXT]
OpenEarthAI is built for five user categories with target sizes at full operations (year 3):

[P00059 | 22439:22623 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Domain research scientists across solid Earth, hydrology, atmospheric science, ecology, and hazards — primary consumers. Target: 4,000 active users / 150 institutions / all 50 states.

[P00060 | 22623:22821 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
AI/ML methods developers — consumers of HazEvalHub benchmarks and ModelHub artifacts; contributors of new models. Target: 500 active users / 50 institutions including AI Institutes and NAIRR users.

[P00061 | 22821:23022 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Federal and state agency partners — NOAA, USGS, NASA, FEMA, state geological surveys, state emergency-management offices: operational consumers of OpenEarthAI-trained foundation models and benchmarks.

[P00062 | 23022:23175 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Educators and learners — instructors using On-Ramp curricula, Hackweek participants. Target: 150 instructors and 1,800 learners cumulative over 3 years.

[P00063 | 23175:23317 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Industry users (insurance, hazard engineering, infrastructure resilience, utilities) — open-tier access with documented commercial-use terms.

[P00064 | 23317:23352 | NORMAL_TEXT]
2.4 Data Lifecycle Reference Model

[P00065 | 23352:23735 | NORMAL_TEXT]
OpenEarthAI adopts the FAIR Data Principles together with the NIST/NSDS reference data lifecycle. OpenEarthAI primarily supports acquisition, transfer, harmonization (curation), exploration, analysis, sharing, and synthesis stages. Long-term archiving and preservation remain the responsibility of source facilities; per IDSS rules, no long-term storage costs are budgeted (see §6).

[P00066 | 23735:23794 | NORMAL_TEXT]
2.5 Leveraging and Connecting to Other Cyberinfrastructure

[P00067 | 23794:23893 | NORMAL_TEXT]
OpenEarthAI federates with named operational partners, with concrete interoperability commitments:

[P00068 | 23893:23998 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
EarthScope NGF — lead institution; operating envelope, identity, governance, and user-support framework.

[P00069 | 23998:24143 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NASA-NSF ASF — joint Sentinel-1, NISAR, OPERA InSAR, ECMWF reanalysis services; STAC catalog interoperability already in place; AWS co-location.

[P00070 | 24143:24310 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NOAA (NCEP, NCEI, NWS) — precipitation, streamflow, radar, reanalysis. Integration follows existing OpenEarthAI HazLab ingestion patterns scaled to national coverage.

[P00071 | 24310:24385 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
USGS — earthquake catalogs, hydrography, ShakeMap, burn-severity products.

[P00072 | 24385:24461 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NSF NEON, OOI, HydroFrame, CUAHSI — cross-facility STAC catalog federation.

[P00073 | 24461:24626 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
NAIRR Pilot — OpenEarthAI serves as a hazard-science data layer for NAIRR-supported AI compute; foundation-model artifacts deposited in NAIRR-accessible registries.

[P00074 | 24626:24751 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
ACCESS — federated identity (CILogon) supports OpenEarthAI users running training and inference on ACCESS-allocated compute.

[P00075 | 24751:24891 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Domain centers (SCEC, CRESCENT, AVERT/VICTOR, SZ4D, DesignSafe) — early adopters and scientific advisors; Letters of Collaboration on file.

[P00076 | 24891:25062 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
AI Institute partners (AI Institute for Dynamical Systems, AI2) — co-developed evaluation frameworks (already in place via OpenEarthAI HazLab) extended to national scope.

[P00077 | 25062:25109 | NORMAL_TEXT]
2.6 Uniqueness, Complementarity, and Synergies

[P00078 | 25109:25366 | NORMAL_TEXT]
OpenEarthAI is unique within the national CI landscape because it is the only operational, multi-agency, multi-hazard, multimodal, AI-ready data and foundation-model platform under open public stewardship. We differentiate explicitly from related programs.

[P00079 | 25366:25888 | NORMAL_TEXT]
Within OAC. CSSI funds innovation and prototype development; OpenEarthAI HazLab itself was developed under research-program support and the Cat II work is operationalization, not innovation. CC* supports campus and regional CI; OpenEarthAI serves any U.S. institution. ACSS provides advanced national computing; OpenEarthAI provides the complementary national hazard-data layer. ACCESS coordinates compute allocation; OpenEarthAI exposes hazard-data services that ACCESS-allocated jobs consume through standard protocols.

[P00080 | 25888:26449 | NORMAL_TEXT]
Within NSF beyond OAC. AI Institutes generate AI methods; OpenEarthAI is the operational hazard-data layer those methods consume. NSF Major Facilities (NEON, OOI, EarthScope) operate observing systems and produce data; OpenEarthAI operates the cross-facility, cross-modality hazard-integration layer on top of them and does not duplicate them. EarthScope is the lead institution; OpenEarthAI is not an EarthScope-only service — it is the multi-agency, multi-facility integration platform EarthScope operates on behalf of the broader hazards research community.

[P00081 | 26449:27167 | NORMAL_TEXT]
Sister federal agencies. NAIRR Pilot provides AI compute and foundation-model access; OpenEarthAI provides the hazard-data layer that supplies NAIRR-style workflows. NASA Earth Science Data Systems are NASA-mission focused on Earth observation; OpenEarthAI operates the cross-mission integration layer combining NASA data with NSF, NOAA, USGS, and academic data sources for hazard science specifically. NOAA Big Data and NCEI are NOAA-mission focused on weather, water, and climate; OpenEarthAI integrates NOAA products as one of multiple modalities in a hazard-cascade fusion. DOE programs (ESnet, OSTI, OLCF/ALCF/NERSC data) serve DOE-lab users; OpenEarthAI serves the broader academic and agency hazards community.

[P00082 | 27167:27658 | NORMAL_TEXT]
Commercial platforms. Google Earth Engine, Microsoft Planetary Computer, Google AlphaEarth, NVIDIA Earth-2, IBM Terramind, AI2 OlmoEarth are valuable but vendor-locked, ToS-driven, not federated under public stewardship, and not aligned with NSF FAIR/Open Science mandates. OpenEarthAI is the public, community-governed, FAIR counterpart for hazard science. We integrate with these platforms (mirrored benchmarks, shared model cards) wherever doing so serves the public-good user community.

[P00083 | 27658:28031 | NORMAL_TEXT]
Synergies. OpenEarthAI actively builds: federated identity and catalogs across EarthScope, ASF, NEON, OOI; bidirectional data and model sharing with NAIRR; co-developed evaluation with AI Institute partners (already in place via OpenEarthAI HazLab); shared hazard benchmarks with CRESCENT, SCEC, AVERT/VICTOR, SZ4D; and joint workforce programs with UW eScience Hackweeks.

[P00084 | 28031:28050 | NORMAL_TEXT]
3. Operations Plan

[P00085 | 28050:28111 | NORMAL_TEXT]
3.1 Operations Transition Timeline (Full Operations by EOY1)

[P00086 | 28111:28359 | NORMAL_TEXT]
OpenEarthAI reaches full operations by end of award year 1 through a phased rollout with explicit go/no-go gates. Full operations is achievable on this schedule because the Cat II work is transition of operational systems, not a clean-sheet build.

[P00087 | 28359:28750 | NORMAL_TEXT]
Phase 1, months 1–3 (architecture and operational baseline). Architecture finalization within EarthScope's existing AWS cloud envelope; subaward agreement with UW executed; Smartsheet schedule, risk register, and change-control governance stood up; security baseline established; OpenEarthAI HazLab regional services migrated to the EarthScope cloud environment under the federated catalog.

[P00088 | 28750:29215 | NORMAL_TEXT]
Phase 2, months 3–9 (national scale-out). DataHub federation with NOAA, USGS, NEON, HydroFrame extended to all 50 states; ModelHub national operational footing achieved; HazEvalHub leaderboards live for the four reference use cases; the three Discovery Agents released to internal testers; federated identity (CILogon) integrated; documentation published. First two foundation models (Ground-Failure, Hydro-Meteorological Cascade) trained and version 0.1 released.

[P00089 | 29215:29805 | NORMAL_TEXT]
Phase 3, months 9–12 (integrated testing and early operations). Named early adopters across all four reference use cases (CRESCENT and SCEC, NOAA Disasters and FEMA partners, USGS Landslide Hazards Program, NSF NEON ecology, AI Institute partners — Letters of Collaboration on file) onboarded. Performance, load, and reliability tests against the §4 KPIs. Acceptance package prepared. Third foundation model (Post-Fire Debris-Flow) released. NSF-conducted operational readiness review at end of month 12, potentially as a Reverse Site Visit; upon acceptance, transition to full operations.

[P00090 | 29805:30126 | NORMAL_TEXT]
Phases 4–5, years 2–3 (full operations and DevOps evolution). Continuous operations measured against §4 KPIs; model-refresh cadence (quarterly model evaluation, semi-annual re-training as data accumulates); ingestion of new modalities (DAS in year 2; additional simulation archives); year-3 NSF renewal-readiness review.

[P00091 | 30126:30169 | NORMAL_TEXT]
3.2 Modes of Operation and Functionalities

[P00092 | 30169:30588 | NORMAL_TEXT]
OpenEarthAI operates 24/7/365 with three service tiers: interactive (catalog, metadata, modest egress, agent queries) with sub-second response targets; batch (large data egress, model training data preparation) with throughput SLAs; inference (foundation-model endpoints) with bounded-latency SLAs. Maintenance windows are scheduled, announced, and never affect the interactive tier without ≥7-day notice and failover.

[P00093 | 30588:30643 | NORMAL_TEXT]
3.3 User Engagement, Onboarding, Training, and Support

[P00094 | 30643:31628 | NORMAL_TEXT]
User engagement extends EarthScope's national user-support office and UW eScience's national Hackweek model. Onboarding: self-service account creation via CILogon, automated open-tier allocation, merit-reviewed allocation for high-throughput workloads via a quarterly community review committee. Training: On-Ramp cloud notebooks (extending EarthScope's existing platform; new hazard-specific modules added in year 1); annual OpenEarthAI Hazard Hackweek run by UW eScience (capacity 50–80 participants, open application across all 50 states); two domain-focused short courses per year; classroom-ready curricula released openly. Documentation: comprehensive user guides, OpenAPI 3.x reference, runnable example notebooks for each reference use case, and a model card for every released model. Support: ticket system with documented response SLAs by tier, weekly virtual office hours, community discussion forum. Agent-assisted help is layered on top of, not instead of, human support.

[P00095 | 31628:31674 | NORMAL_TEXT]
3.4 Personnel: Numbers, Types, Qualifications

[P00096 | 31674:32434 | NORMAL_TEXT]
OpenEarthAI is staffed by ~14 FTE at full operations. Operations team (~6 FTE at EarthScope): site reliability engineers, DevOps and cloud engineer, security engineer, user-support specialists, training and documentation lead. Development and AI/ML team (~6 FTE distributed across EarthScope and UW): data engineers, ML engineers / RSEs, foundation-model lead (UW), agentic-AI engineer (UW). Scientific staff (~2 FTE distributed across EarthScope and UW): hazard-domain liaisons; data-steward function. Specific qualifications include AWS Solutions Architect/SysOps for SREs, NIST 800-171-aware training for the security lead, documented prior CI-operations or open-source-project experience for engineering staff. Named individuals and positions are in §5.2.

[P00097 | 32434:32491 | NORMAL_TEXT]
3.5 Resource Allocation: Broad, Open, Merit-Based Access

[P00098 | 32491:33362 | NORMAL_TEXT]
OpenEarthAI adopts a two-tier allocation policy aligned with NSF open-access principles. Open tier: every account holder has no-questions-asked access to catalog search, metadata, modest data egress, agent queries, and inference on hosted foundation models, subject to fair-use rate limits. Merit tier: high-throughput training data preparation, large-scale Feature Store materialization, and reserved inference capacity, allocated quarterly through a community advisory committee using NSF-style merit review. Allocation outcomes (request, decision, rationale) are publicly posted to satisfy the solicitation's open-access requirement. Geographic and institutional distribution is monitored as a §4 KPI to ensure OpenEarthAI serves all 50 states, EPSCoR jurisdictions, community colleges, primarily undergraduate institutions, MSIs, and HBCUs as institutional partners.

[P00099 | 33362:33389 | NORMAL_TEXT]
3.6 Early-User Access Plan

[P00100 | 33389:34189 | NORMAL_TEXT]
Early access begins month 9 with named community partners across all four reference use cases. Letters of Collaboration are submitted with this proposal, in the intent-only format required by NSF 26-509: AR / flood / shallow landslide partners (NOAA Center for Western Weather and Water Extremes; USGS Landslide Hazards; NWS Western Region); earthquake / liquefaction partners (CRESCENT; SCEC; WSDOT geotechnical); post-fire debris-flow partners (USGS; U.S. Forest Service; state-DOT partners in CO, NM, MT); convective-storm partners (NOAA NSSL; NCAR/MMM; AI Institute for Dynamical Systems via existing OpenEarthAI HazLab collaboration). Early-user feedback is collected weekly and feeds directly into the Phase-3 acceptance package; pre-acceptance outputs are tracked in the public issue tracker.

[P00101 | 34189:34231 | NORMAL_TEXT]
3.7 Technology Refresh and Public Metrics

[P00102 | 34231:35014 | NORMAL_TEXT]
Cloud-native architecture makes hardware lifecycle a managed-service concern; refresh strategy focuses on software-stack evolution (Zarr v3 maturation, IceChunk, PyTorch/JAX/Hugging Face dataloader API evolution, foundation-model architecture refresh as the field advances) and on absorbing new modalities (DAS in year 2, simulation archives in year 2, additional sensors as they come online). At least 15% of operations effort is reserved for innovation during operations, satisfying the IDSS requirement. A public metrics dashboard exposes uptime, latency, throughput, user counts, geographic distribution, allocation outcomes, and scientific-impact metrics in real time, satisfying the solicitation's open-metrics requirement and aligning with Gold Standard Science transparency.

[P00103 | 35014:35051 | NORMAL_TEXT]
3.8 Operations-Side Security Summary

[P00104 | 35051:35477 | NORMAL_TEXT]
Operations-side security is summarized here; full plan in §5.6. OpenEarthAI inherits EarthScope's established security program (documented controls, MFA, role-based access, vulnerability scanning, audit logging) and extends it for AI-specific risks (model exfiltration, training-data leakage, prompt-injection in agentic workflows). Important Notice 149 obligations are met for all Senior Personnel at award start (see §5.6).

[P00105 | 35477:35516 | NORMAL_TEXT]
4. Performance Objectives and Measures

[P00106 | 35516:35541 | NORMAL_TEXT]
4.1 Objective Categories

[P00107 | 35541:36213 | NORMAL_TEXT]
OpenEarthAI tracks performance across six objective categories calibrated to national-scale operational CI norms: (i) continuous operations (uptime, MTBF, MTTR); (ii) end-to-end performance (latency, throughput); (iii) user-community growth (registered users, institutions, geographic reach); (iv) user experience and usability; (v) scientific and operational hazard-science impact (publications, datasets and models published, agency uptake); (vi) Gold-Standard-Science alignment (workflow reproducibility, uncertainty coverage). Cat II baselines are higher than a clean-sheet build because OpenEarthAI inherits operational footing from NGF, ASF, and OpenEarthAI HazLab.

[P00108 | 36213:36237 | NORMAL_TEXT]
4.2 Performance Targets

[P00109 | 36240:36248 | NORMAL_TEXT | TABLE row=0 col=0]
Outcome

[P00110 | 36249:36253 | NORMAL_TEXT | TABLE row=0 col=1]
KPI

[P00111 | 36254:36269 | NORMAL_TEXT | TABLE row=0 col=2]
Y1 (Early Ops)

[P00112 | 36270:36280 | NORMAL_TEXT | TABLE row=0 col=3]
Y2 Target

[P00113 | 36281:36291 | NORMAL_TEXT | TABLE row=0 col=4]
Y3 Target

[P00114 | 36293:36308 | NORMAL_TEXT | TABLE row=1 col=0]
Continuous ops

[P00115 | 36309:36335 | NORMAL_TEXT | TABLE row=1 col=1]
Uptime (interactive tier)

[P00116 | 36336:36340 | NORMAL_TEXT | TABLE row=1 col=2]
97%

[P00117 | 36341:36347 | NORMAL_TEXT | TABLE row=1 col=3]
99.0%

[P00118 | 36348:36354 | NORMAL_TEXT | TABLE row=1 col=4]
99.5%

[P00119 | 36356:36371 | NORMAL_TEXT | TABLE row=2 col=0]
Continuous ops

[P00120 | 36372:36390 | NORMAL_TEXT | TABLE row=2 col=1]
MTTR (severity-1)

[P00121 | 36391:36395 | NORMAL_TEXT | TABLE row=2 col=2]
2 h

[P00122 | 36396:36400 | NORMAL_TEXT | TABLE row=2 col=3]
1 h

[P00123 | 36401:36408 | NORMAL_TEXT | TABLE row=2 col=4]
30 min

[P00124 | 36410:36425 | NORMAL_TEXT | TABLE row=3 col=0]
Continuous ops

[P00125 | 36426:36444 | NORMAL_TEXT | TABLE row=3 col=1]
MTBF (severity-1)

[P00126 | 36445:36450 | NORMAL_TEXT | TABLE row=3 col=2]
30 d

[P00127 | 36451:36456 | NORMAL_TEXT | TABLE row=3 col=3]
60 d

[P00128 | 36457:36462 | NORMAL_TEXT | TABLE row=3 col=4]
90 d

[P00129 | 36464:36476 | NORMAL_TEXT | TABLE row=4 col=0]
Performance

[P00130 | 36477:36517 | NORMAL_TEXT | TABLE row=4 col=1]
Catalog query p95 latency (10⁹ records)

[P00131 | 36518:36524 | NORMAL_TEXT | TABLE row=4 col=2]
1.5 s

[P00132 | 36525:36532 | NORMAL_TEXT | TABLE row=4 col=3]
750 ms

[P00133 | 36533:36540 | NORMAL_TEXT | TABLE row=4 col=4]
500 ms

[P00134 | 36542:36554 | NORMAL_TEXT | TABLE row=5 col=0]
Performance

[P00135 | 36555:36591 | NORMAL_TEXT | TABLE row=5 col=1]
Sustained ML data-loader throughput

[P00136 | 36592:36600 | NORMAL_TEXT | TABLE row=5 col=2]
30 GB/s

[P00137 | 36601:36609 | NORMAL_TEXT | TABLE row=5 col=3]
75 GB/s

[P00138 | 36610:36619 | NORMAL_TEXT | TABLE row=5 col=4]
150 GB/s

[P00139 | 36621:36633 | NORMAL_TEXT | TABLE row=6 col=0]
Performance

[P00140 | 36634:36673 | NORMAL_TEXT | TABLE row=6 col=1]
Foundation-model inference p95 latency

[P00141 | 36674:36678 | NORMAL_TEXT | TABLE row=6 col=2]
5 s

[P00142 | 36679:36683 | NORMAL_TEXT | TABLE row=6 col=3]
2 s

[P00143 | 36684:36688 | NORMAL_TEXT | TABLE row=6 col=4]
1 s

[P00144 | 36690:36705 | NORMAL_TEXT | TABLE row=7 col=0]
User community

[P00145 | 36706:36730 | NORMAL_TEXT | TABLE row=7 col=1]
Registered active users

[P00146 | 36731:36737 | NORMAL_TEXT | TABLE row=7 col=2]
1,200

[P00147 | 36738:36744 | NORMAL_TEXT | TABLE row=7 col=3]
2,800

[P00148 | 36745:36751 | NORMAL_TEXT | TABLE row=7 col=4]
5,000

[P00149 | 36753:36768 | NORMAL_TEXT | TABLE row=8 col=0]
User community

[P00150 | 36769:36796 | NORMAL_TEXT | TABLE row=8 col=1]
Distinct U.S. institutions

[P00151 | 36797:36800 | NORMAL_TEXT | TABLE row=8 col=2]
50

[P00152 | 36801:36805 | NORMAL_TEXT | TABLE row=8 col=3]
100

[P00153 | 36806:36810 | NORMAL_TEXT | TABLE row=8 col=4]
180

[P00154 | 36812:36827 | NORMAL_TEXT | TABLE row=9 col=0]
User community

[P00155 | 36828:36853 | NORMAL_TEXT | TABLE row=9 col=1]
States with active users

[P00156 | 36854:36857 | NORMAL_TEXT | TABLE row=9 col=2]
40

[P00157 | 36858:36861 | NORMAL_TEXT | TABLE row=9 col=3]
48

[P00158 | 36862:36865 | NORMAL_TEXT | TABLE row=9 col=4]
50

[P00159 | 36867:36883 | NORMAL_TEXT | TABLE row=10 col=0]
User experience

[P00160 | 36884:36915 | NORMAL_TEXT | TABLE row=10 col=1]
Avg. satisfaction (1–5 survey)

[P00161 | 36916:36920 | NORMAL_TEXT | TABLE row=10 col=2]
3.8

[P00162 | 36921:36925 | NORMAL_TEXT | TABLE row=10 col=3]
4.1

[P00163 | 36926:36930 | NORMAL_TEXT | TABLE row=10 col=4]
4.4

[P00164 | 36932:36948 | NORMAL_TEXT | TABLE row=11 col=0]
User experience

[P00165 | 36949:36981 | NORMAL_TEXT | TABLE row=11 col=1]
Time-to-first-result (new user)

[P00166 | 36982:36990 | NORMAL_TEXT | TABLE row=11 col=2]
≤45 min

[P00167 | 36991:36999 | NORMAL_TEXT | TABLE row=11 col=3]
≤25 min

[P00168 | 37000:37008 | NORMAL_TEXT | TABLE row=11 col=4]
≤15 min

[P00169 | 37010:37028 | NORMAL_TEXT | TABLE row=12 col=0]
Scientific impact

[P00170 | 37029:37061 | NORMAL_TEXT | TABLE row=12 col=1]
Publications citing OpenEarthAI

[P00171 | 37062:37064 | NORMAL_TEXT | TABLE row=12 col=2]
8

[P00172 | 37065:37068 | NORMAL_TEXT | TABLE row=12 col=3]
40

[P00173 | 37069:37073 | NORMAL_TEXT | TABLE row=12 col=4]
120

[P00174 | 37075:37093 | NORMAL_TEXT | TABLE row=13 col=0]
Scientific impact

[P00175 | 37094:37121 | NORMAL_TEXT | TABLE row=13 col=1]
Foundation models released

[P00176 | 37122:37124 | NORMAL_TEXT | TABLE row=13 col=2]
1

[P00177 | 37125:37127 | NORMAL_TEXT | TABLE row=13 col=3]
3

[P00178 | 37128:37130 | NORMAL_TEXT | TABLE row=13 col=4]
5

[P00179 | 37132:37150 | NORMAL_TEXT | TABLE row=14 col=0]
Scientific impact

[P00180 | 37151:37183 | NORMAL_TEXT | TABLE row=14 col=1]
Datasets / benchmarks published

[P00181 | 37184:37186 | NORMAL_TEXT | TABLE row=14 col=2]
8

[P00182 | 37187:37190 | NORMAL_TEXT | TABLE row=14 col=3]
30

[P00183 | 37191:37194 | NORMAL_TEXT | TABLE row=14 col=4]
75

[P00184 | 37196:37210 | NORMAL_TEXT | TABLE row=15 col=0]
GSS alignment

[P00185 | 37211:37254 | NORMAL_TEXT | TABLE row=15 col=1]
% workflows reproducible (container + DOI)

[P00186 | 37255:37259 | NORMAL_TEXT | TABLE row=15 col=2]
70%

[P00187 | 37260:37264 | NORMAL_TEXT | TABLE row=15 col=3]
90%

[P00188 | 37265:37269 | NORMAL_TEXT | TABLE row=15 col=4]
97%

[P00189 | 37271:37285 | NORMAL_TEXT | TABLE row=16 col=0]
GSS alignment

[P00190 | 37286:37326 | NORMAL_TEXT | TABLE row=16 col=1]
% public products w/ uncertainty fields

[P00191 | 37327:37331 | NORMAL_TEXT | TABLE row=16 col=2]
75%

[P00192 | 37332:37336 | NORMAL_TEXT | TABLE row=16 col=3]
92%

[P00193 | 37337:37341 | NORMAL_TEXT | TABLE row=16 col=4]
98%

[P00194 | 37342:37370 | NORMAL_TEXT]
4.3 Measurement Methodology

[P00195 | 37370:38306 | NORMAL_TEXT]
Operational metrics (uptime, MTBF, MTTR, latency, throughput) are collected via Prometheus-class telemetry and surfaced on the public dashboard. User-community metrics are drawn from the federated identity and allocation databases (privacy-preserving aggregates only). User satisfaction is measured by a quarterly survey with documented methodology and public summary reports. Time-to-first-result is measured via the On-Ramp cohort timing pipeline. Scientific impact is tracked through DOI-linked publications, model-card download counts, DataCite dataset-DOI citations, and an annual hazard-science impact case-study series. GSS-alignment metrics are computed from the workflow registry (every registered workflow is automatically scanned for container pinning and data-DOI references; every public product is scanned for uncertainty-field presence). All metrics are reported annually to NSF and continuously to the public dashboard.

[P00196 | 38306:38328 | NORMAL_TEXT]
5. Project Management

[P00197 | 38328:38377 | NORMAL_TEXT]
5.1 Project Leadership Team and Their Experience

[P00198 | 38377:38683 | NORMAL_TEXT]
OpenEarthAI is led by a team with substantial prior experience operating national-scale data CI for large user communities. Cat II review weights operational track record heavily; the team's record is summarized below and detailed in the Project Personnel and Partner Organizations supplementary document.

[P00199 | 38683:39035 | NORMAL_TEXT]
Principal Investigator: Dr. David Mencin (EarthScope) — scientific direction, cross-agency alignment, final authority on scientific scope. PI commitment: 3.0 person-months/year (substantial). Mencin leads EarthScope's NGF data and computation portfolio and has directed prior CSSI-to-operations transitions (GeoSciCloud, GeoSciFramework into the NGF).

[P00200 | 39035:39315 | NORMAL_TEXT]
Project Director: Sarah Deutsch, Director of Project Management, EarthScope — execution authority, governance, schedule, risk, vendor oversight. Deutsch has documented experience overseeing multi-year, multi-facility CI programs at EarthScope. Commitment: 6.0 person-months/year.

[P00201 | 39315:39444 | NORMAL_TEXT]
Technical Lead (EarthScope, named in supplementary docs) — systems architecture, integration oversight. 12.0 person-months/year.

[P00202 | 39444:39544 | NORMAL_TEXT]
Operations Lead (EarthScope) — DevOps, SRE, monitoring, incident response. 12.0 person-months/year.

[P00203 | 39544:39639 | NORMAL_TEXT]
Security Lead (EarthScope) — security architecture, IN 149 compliance. 6.0 person-months/year.

[P00204 | 39639:39671 | NORMAL_TEXT]
Subaward co-Investigators (UW):

[P00205 | 39671:39896 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Marine Denolle (UW ESS, co-PI) — scientific lead for multi-hazard foundation models; PI of the existing OpenEarthAI HazLab regional prototype being scaled. Co-supervises postdocs and CSE graduate student. 1.0 month/year.

[P00206 | 39896:40023 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Vikram Iyer (UW CSE, co-PI) — lead for Cross-Modality Discovery Agents; agent benchmarking and evaluation. 0.5 month/year.

[P00207 | 40023:40172 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Vani Mandava (UW eScience, co-PI) — RSE leadership, agentic-AI software engineering best practices, On-Ramp and Hackweek operations. 0.5 month/year.

[P00208 | 40172:40310 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Nicoleta Cristea (UW, co-PI) — hydrology integration (HydroFrame, NOAA precipitation, GNSS-IR soil moisture and SWE). 0.5 month/year.

[P00209 | 40310:40462 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Scott Henderson (UW eScience, Senior Personnel) — cloud CI for fused NASA + ASF + EarthScope + HydroFrame data; co-supervises RSEs. 1.0 month/year.

[P00210 | 40462:40551 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Dr. Brad Lipovsky (UW, Senior Personnel) — DAS data-service curation (FiberLab archive).

[P00211 | 40551:40869 | NORMAL_TEXT]
External advisory: a Science and Operations Advisory Group of 5–7 experts drawn from federal agencies (NOAA, USGS, NASA), NSF Major Facilities (NEON, OOI, ASF, IceCube), and AI research (NSF AI Institutes, NAIRR users) provides advisory input. Execution authority remains centralized within the EarthScope PI and PMO.

[P00212 | 40869:40924 | NORMAL_TEXT]
5.2 Project Organization, Work Breakdown, and Timeline

[P00213 | 40924:41261 | NORMAL_TEXT]
EarthScope is the single accountable lead. The UW subaward operates under a named scope of work with monthly reporting, quarterly milestone reviews, and binding authority of the EarthScope PMO over schedule, cost, and acceptance criteria. Reporting chain: UW subaward lead → EarthScope PMO (Deutsch) → PI (Mencin) → NSF Program Officer.

[P00214 | 41261:41434 | NORMAL_TEXT]
Work Breakdown Structure (Level 2). Major work areas, lead organizations, and indicative 3-year direct-cost budgets (detailed estimates in the Supplementary Cost Estimate):

[P00215 | 41437:41441 | NORMAL_TEXT | TABLE row=0 col=0]
WBS

[P00216 | 41442:41452 | NORMAL_TEXT | TABLE row=0 col=1]
Work Area

[P00217 | 41453:41458 | NORMAL_TEXT | TABLE row=0 col=2]
Lead

[P00218 | 41459:41471 | NORMAL_TEXT | TABLE row=0 col=3]
3-Yr Direct

[P00219 | 41473:41477 | NORMAL_TEXT | TABLE row=1 col=0]
1.0

[P00220 | 41478:41554 | NORMAL_TEXT | TABLE row=1 col=1]
DataHub National Federation (NOAA, USGS, EarthScope, ASF, NEON, HydroFrame)

[P00221 | 41555:41566 | NORMAL_TEXT | TABLE row=1 col=2]
EarthScope

[P00222 | 41567:41575 | NORMAL_TEXT | TABLE row=1 col=3]
~$1.40M

[P00223 | 41577:41581 | NORMAL_TEXT | TABLE row=2 col=0]
2.0

[P00224 | 41582:41623 | NORMAL_TEXT | TABLE row=2 col=1]
ModelHub: Multi-Hazard Foundation Models

[P00225 | 41624:41650 | NORMAL_TEXT | TABLE row=2 col=2]
UW (Denolle) + EarthScope

[P00226 | 41651:41659 | NORMAL_TEXT | TABLE row=2 col=3]
~$1.50M

[P00227 | 41661:41665 | NORMAL_TEXT | TABLE row=3 col=0]
3.0

[P00228 | 41666:41695 | NORMAL_TEXT | TABLE row=3 col=1]
HazEvalHub at National Scale

[P00229 | 41696:41712 | NORMAL_TEXT | TABLE row=3 col=2]
UW + EarthScope

[P00230 | 41713:41721 | NORMAL_TEXT | TABLE row=3 col=3]
~$0.65M

[P00231 | 41723:41727 | NORMAL_TEXT | TABLE row=4 col=0]
4.0

[P00232 | 41728:41760 | NORMAL_TEXT | TABLE row=4 col=1]
Cross-Modality Discovery Agents

[P00233 | 41761:41779 | NORMAL_TEXT | TABLE row=4 col=2]
UW (Iyer/Mandava)

[P00234 | 41780:41788 | NORMAL_TEXT | TABLE row=4 col=3]
~$0.65M

[P00235 | 41790:41794 | NORMAL_TEXT | TABLE row=5 col=0]
5.0

[P00236 | 41795:41868 | NORMAL_TEXT | TABLE row=5 col=1]
Hydrology / Critical Zone Integration via HydroFrame & CUAHSI federation

[P00237 | 41869:41882 | NORMAL_TEXT | TABLE row=5 col=2]
UW (Cristea)

[P00238 | 41883:41891 | NORMAL_TEXT | TABLE row=5 col=3]
~$0.40M

[P00239 | 41893:41897 | NORMAL_TEXT | TABLE row=6 col=0]
6.0

[P00240 | 41898:41940 | NORMAL_TEXT | TABLE row=6 col=1]
User Engagement, On-Ramp, Hazard Hackweek

[P00241 | 41941:41966 | NORMAL_TEXT | TABLE row=6 col=2]
EarthScope + UW eScience

[P00242 | 41967:41975 | NORMAL_TEXT | TABLE row=6 col=3]
~$0.55M

[P00243 | 41977:41981 | NORMAL_TEXT | TABLE row=7 col=0]
7.0

[P00244 | 41982:42022 | NORMAL_TEXT | TABLE row=7 col=1]
National Operations, SRE, Security, PMO

[P00245 | 42023:42034 | NORMAL_TEXT | TABLE row=7 col=2]
EarthScope

[P00246 | 42035:42043 | NORMAL_TEXT | TABLE row=7 col=3]
~$1.20M

[P00247 | 42045:42046 | NORMAL_TEXT | TABLE row=8 col=0]
⟦EMPTY PARAGRAPH⟧

[P00248 | 42047:42110 | NORMAL_TEXT | TABLE row=8 col=1]
Total Direct (3 yr; indicative; refine in Supp. Cost Estimate)

[P00249 | 42111:42112 | NORMAL_TEXT | TABLE row=8 col=2]
⟦EMPTY PARAGRAPH⟧

[P00250 | 42113:42121 | NORMAL_TEXT | TABLE row=8 col=3]
~$6.35M

[P00251 | 42122:42597 | NORMAL_TEXT]
Temporal stages: Phase 1 architecture and operational baseline (months 1–3); Phase 2 national scale-out (months 3–9); Phase 3 integrated testing and early operations (months 9–12) culminating in the NSF operational-readiness review at end of year 1; Phase 4 continuous operations and DevOps evolution (years 2–3). Detailed quarter-by-quarter Gantt with milestones is maintained in Smartsheet under formal change control and provided in the Project Execution Plan upon award.

[P00252 | 42597:43060 | NORMAL_TEXT]
Multi-organization governance. EarthScope's PMO has binding authority over schedule, cost, and acceptance for all subawards. A change-control board chaired by Deutsch reviews scope or schedule changes monthly. Decision-making rights and escalation paths are documented in the Project Execution Plan filed with NSF post-award. Pre-full-ops performance is demonstrated through Phase-3 acceptance testing against the §4 KPIs and the named early-user access program.

[P00253 | 43060:43076 | NORMAL_TEXT]
5.3 Outsourcing

[P00254 | 43076:43204 | NORMAL_TEXT]
OpenEarthAI outsources only what is more efficient or specialized to outsource. Major outsourced services with measurable SLAs:

[P00255 | 43204:43402 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
AWS Enterprise Support: 99.99% S3 SLA per AWS published terms; severity-1 case response ≤15 minutes; dedicated Technical Account Manager. Vendor performance reviewed monthly by the Operations Lead.

[P00256 | 43402:43454 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
GitHub Enterprise (code hosting, CI/CD): 99.9% SLA.

[P00257 | 43454:43527 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Atlassian (issue tracking, internal docs): standard enterprise-tier SLA.

[P00258 | 43527:43590 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Smartsheet (project management): standard enterprise-tier SLA.

[P00259 | 43590:43766 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Specialized data-engineering or AI-MLOps consulting may be procured for bounded scopes under fixed-price contracts; capped at 10% of any year's direct costs with PMO approval.

[P00260 | 43766:44125 | NORMAL_TEXT]
EarthScope has documented experience overseeing vendor contracts of this kind for the NGF program. All outsourced work is subject to facility-grade oversight: contract review by EarthScope counsel, monthly performance metrics, risks logged in the project Risk Register, and acceptance against operational-readiness standards before deliverables are accepted.

[P00261 | 44125:44138 | NORMAL_TEXT]
5.4 Software

[P00262 | 44138:44303 | NORMAL_TEXT]
OpenEarthAI-developed software is released under the Apache License 2.0 (stated explicitly per IDSS requirement). Major components and develop-vs-acquire decisions:

[P00263 | 44303:44768 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Develop in-house: National DataHub federation extensions; ModelHub registry and inference orchestration; HazEvalHub leaderboard and anti-leakage controls; the three Cross-Modality Discovery Agents; provenance and reproducibility tooling. Justification: no acceptable open-source equivalent exists at the integration scope and hazard-science focus OpenEarthAI requires; the team has shipped equivalent components before (NGF; OpenEarthAI HazLab regional prototype).

[P00264 | 44768:44963 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
Adopt and extend open-source: Zarr, Apache Iceberg, IceChunk, STAC, PyTorch, Hugging Face datasets, Apache Kafka, CILogon, TorchGeo. Upstream contributions where domain extensions are developed.

[P00265 | 44963:45173 | NORMAL_TEXT | LIST id=kix.list.1 level=0]
License or hosted service: SageMaker base layer (extended in-house); AWS Bedrock for inference endpoint hosting as an option. Each licensed component is benchmarked against open-source alternatives biennially.

[P00266 | 45173:45463 | NORMAL_TEXT]
Software engineering practices: secure CI/CD with automated testing (unit, integration, regression), automated vulnerability scanning, mandatory ≥1-engineer code review, semantic versioning, public release notes, and reproducibility audits. Documentation is part of the definition of done.

[P00267 | 45463:45483 | NORMAL_TEXT]
5.5 Risk Management

[P00268 | 45483:45589 | NORMAL_TEXT]
Risks are tracked in a Smartsheet Risk Register reviewed monthly by the PMO. Major risks and mitigations:

[P00269 | 45592:45597 | NORMAL_TEXT | TABLE row=0 col=0]
Risk

[P00270 | 45598:45607 | NORMAL_TEXT | TABLE row=0 col=1]
Category

[P00271 | 45608:45614 | NORMAL_TEXT | TABLE row=0 col=2]
Prob.

[P00272 | 45615:45622 | NORMAL_TEXT | TABLE row=0 col=3]
Impact

[P00273 | 45623:45634 | NORMAL_TEXT | TABLE row=0 col=4]
Mitigation

[P00274 | 45636:45682 | NORMAL_TEXT | TABLE row=1 col=0]
Foundation-model training cost exceeds budget

[P00275 | 45683:45705 | NORMAL_TEXT | TABLE row=1 col=1]
Financial / technical

[P00276 | 45706:45713 | NORMAL_TEXT | TABLE row=1 col=2]
Medium

[P00277 | 45714:45719 | NORMAL_TEXT | TABLE row=1 col=3]
High

[P00278 | 45720:45883 | NORMAL_TEXT | TABLE row=1 col=4]
NAIRR allocation as primary compute path; documented re-baseline triggers; model-size caps reviewed quarterly; reuse of OpenEarthAI HazLab pre-trained components.

[P00279 | 45885:45926 | NORMAL_TEXT | TABLE row=2 col=0]
Subaward delivery slips on AI components

[P00280 | 45927:45948 | NORMAL_TEXT | TABLE row=2 col=1]
Technical / schedule

[P00281 | 45949:45956 | NORMAL_TEXT | TABLE row=2 col=2]
Medium

[P00282 | 45957:45962 | NORMAL_TEXT | TABLE row=2 col=3]
High

[P00283 | 45963:46037 | NORMAL_TEXT | TABLE row=2 col=4]
Phased gates; PMO binding authority; contingency RSE staff at EarthScope.

[P00284 | 46039:46107 | NORMAL_TEXT | TABLE row=3 col=0]
Discovery Agents introduce reproducibility / trustworthiness issues

[P00285 | 46108:46126 | NORMAL_TEXT | TABLE row=3 col=1]
Technical / trust

[P00286 | 46127:46134 | NORMAL_TEXT | TABLE row=3 col=2]
Medium

[P00287 | 46135:46142 | NORMAL_TEXT | TABLE row=3 col=3]
Medium

[P00288 | 46143:46298 | NORMAL_TEXT | TABLE row=3 col=4]
Deliberate scope limitation (data discovery only); deterministic where possible; provenance-logged; phased external rollout; internal red-team evaluation.

[P00289 | 46300:46369 | NORMAL_TEXT | TABLE row=4 col=0]
Community adoption slower than projected outside the Pacific NW core

[P00290 | 46370:46379 | NORMAL_TEXT | TABLE row=4 col=1]
Adoption

[P00291 | 46380:46387 | NORMAL_TEXT | TABLE row=4 col=2]
Medium

[P00292 | 46388:46393 | NORMAL_TEXT | TABLE row=4 col=3]
High

[P00293 | 46394:46543 | NORMAL_TEXT | TABLE row=4 col=4]
Letters-of-Collaboration commitments at submission across all four use-case regions; named early-adopter program; quarterly user-engagement reviews.

[P00294 | 46545:46582 | NORMAL_TEXT | TABLE row=5 col=0]
Vendor failure or AWS pricing change

[P00295 | 46583:46607 | NORMAL_TEXT | TABLE row=5 col=1]
Outsourcing / financial

[P00296 | 46608:46612 | NORMAL_TEXT | TABLE row=5 col=2]
Low

[P00297 | 46613:46620 | NORMAL_TEXT | TABLE row=5 col=3]
Medium

[P00298 | 46621:46722 | NORMAL_TEXT | TABLE row=5 col=4]
Multi-cloud-portable formats by design; vendor-agnostic STAC; documented exit plan per major vendor.

[P00299 | 46724:46747 | NORMAL_TEXT | TABLE row=6 col=0]
Cybersecurity incident

[P00300 | 46748:46757 | NORMAL_TEXT | TABLE row=6 col=1]
Security

[P00301 | 46758:46762 | NORMAL_TEXT | TABLE row=6 col=2]
Low

[P00302 | 46763:46772 | NORMAL_TEXT | TABLE row=6 col=3]
Critical

[P00303 | 46773:46879 | NORMAL_TEXT | TABLE row=6 col=4]
NIST-aligned controls (§5.6); annual penetration test; incident-response plan and notification procedure.

[P00304 | 46881:46914 | NORMAL_TEXT | TABLE row=7 col=0]
Research-security non-compliance

[P00305 | 46915:46926 | NORMAL_TEXT | TABLE row=7 col=1]
Compliance

[P00306 | 46927:46931 | NORMAL_TEXT | TABLE row=7 col=2]
Low

[P00307 | 46932:46941 | NORMAL_TEXT | TABLE row=7 col=3]
Critical

[P00308 | 46942:47083 | NORMAL_TEXT | TABLE row=7 col=4]
IN 149 training tracked in PMO; MFTRP certified annually; Confucius Institute compliance verified before submission and reverified annually.

[P00309 | 47085:47138 | NORMAL_TEXT | TABLE row=8 col=0]
Funding-policy change (e.g., 15% IDC cap activation)

[P00310 | 47139:47158 | NORMAL_TEXT | TABLE row=8 col=1]
Financial / policy

[P00311 | 47159:47166 | NORMAL_TEXT | TABLE row=8 col=2]
Medium

[P00312 | 47167:47174 | NORMAL_TEXT | TABLE row=8 col=3]
Medium

[P00313 | 47175:47285 | NORMAL_TEXT | TABLE row=8 col=4]
Budget at negotiated rate per current law; contingency plan if NSF 25-034 activates; quarterly policy review.

[P00314 | 47287:47324 | NORMAL_TEXT | TABLE row=9 col=0]
Long-term sustainability after award

[P00315 | 47325:47340 | NORMAL_TEXT | TABLE row=9 col=1]
Sustainability

[P00316 | 47341:47348 | NORMAL_TEXT | TABLE row=9 col=2]
Medium

[P00317 | 47349:47354 | NORMAL_TEXT | TABLE row=9 col=3]
High

[P00318 | 47355:47511 | NORMAL_TEXT | TABLE row=9 col=4]
Operations-cost trajectory engineered to integrate into NGF facility ops post-award; partnership and fee-based mechanisms for long-term storage costs (§6).

[P00319 | 47512:47545 | NORMAL_TEXT]
5.6 Security and Trustworthiness

[P00320 | 47545:47984 | NORMAL_TEXT]
OpenEarthAI inherits and extends EarthScope's established security program. Reference policy regimes: NIST SP 800-53 / 800-171 (moderate baseline), CIS Benchmarks for AWS, OWASP Top 10 for web services, MITRE ATLAS for AI-system threats. Roles: Security Lead reports to the PI; CISO-equivalent at EarthScope retains organizational security authority. Risk assessments are conducted annually with a third-party penetration test biennially.

[P00321 | 47984:48631 | NORMAL_TEXT]
Technical safeguards: TLS-everywhere; encryption at rest (S3 SSE-KMS); least-privilege IAM with mandatory MFA; network segmentation between public and internal subnets; comprehensive audit logging via CloudTrail and OpenSearch; automated vulnerability scanning; SBOM generation; dependency pinning; container-image signing. Agentic-AI-specific controls (essential because Discovery Agents are user-facing): prompt-injection defenses, tool-call allowlists, output provenance logging, and human-in-the-loop gates for any action that could modify state. Discovery Agents have read-only access to data layers and cannot mutate the catalog or storage.

[P00322 | 48631:49156 | NORMAL_TEXT]
Administrative safeguards: annual security awareness training for all personnel; quarterly access reviews; documented incident-response plan with notification procedures to NSF (within 24 hours of confirmed material incident), to the user community (per CISA disclosure best practices), and to law enforcement as appropriate. Effectiveness is evaluated through annual tabletop exercises, biennial penetration testing, and a quarterly metrics review (mean time to detect, mean time to contain, security-finding closure rate).

[P00323 | 49156:49662 | NORMAL_TEXT]
Important Notice 149 obligations are explicitly addressed: every Senior Personnel listed has completed (or will complete prior to submission) Research Security Training within the 1-year IN 149 window; every Senior Personnel executes annual MFTRP certification; the lead institution (EarthScope) and the subaward institution (UW) confirm the absence of any Confucius Institute agreement; FFDR reporting follows the IN 149 timeline. The Security Lead coordinates IN 149 compliance across both institutions.

[P00324 | 49662:49683 | NORMAL_TEXT]
6. Budget Estimation

[P00325 | 49683:50101 | NORMAL_TEXT]
OpenEarthAI is proposed as a Category II project, 3 years, with total cost below the $9M Category II cap. The summary below outlines the budget shape; the detailed cost estimate (organized by phase and by WBS element, with basis of estimates) is provided in the Supplementary Cost Estimate document, with budget justifications by institution (EarthScope lead, UW subaward) following PAPPG and NSF 26-509 requirements.

[P00326 | 50101:50124 | NORMAL_TEXT]
6.1 Total Cost Summary

[P00327 | 50127:50132 | NORMAL_TEXT | TABLE row=0 col=0]
Year

[P00328 | 50133:50145 | NORMAL_TEXT | TABLE row=0 col=1]
Direct ($M)

[P00329 | 50146:50160 | NORMAL_TEXT | TABLE row=0 col=2]
Indirect ($M)

[P00330 | 50161:50172 | NORMAL_TEXT | TABLE row=0 col=3]
Total ($M)

[P00331 | 50174:50201 | NORMAL_TEXT | TABLE row=1 col=0]
1 (Transition + Scale-Out)

[P00332 | 50202:50208 | NORMAL_TEXT | TABLE row=1 col=1]
~2.30

[P00333 | 50209:50215 | NORMAL_TEXT | TABLE row=1 col=2]
~1.05

[P00334 | 50216:50222 | NORMAL_TEXT | TABLE row=1 col=3]
~3.35

[P00335 | 50224:50254 | NORMAL_TEXT | TABLE row=2 col=0]
2 (Full Ops + Model Releases)

[P00336 | 50255:50261 | NORMAL_TEXT | TABLE row=2 col=1]
~2.20

[P00337 | 50262:50268 | NORMAL_TEXT | TABLE row=2 col=2]
~1.00

[P00338 | 50269:50275 | NORMAL_TEXT | TABLE row=2 col=3]
~3.20

[P00339 | 50277:50305 | NORMAL_TEXT | TABLE row=3 col=0]
3 (Full Ops + Renewal Prep)

[P00340 | 50306:50312 | NORMAL_TEXT | TABLE row=3 col=1]
~1.85

[P00341 | 50313:50319 | NORMAL_TEXT | TABLE row=3 col=2]
~0.85

[P00342 | 50320:50326 | NORMAL_TEXT | TABLE row=3 col=3]
~2.70

[P00343 | 50328:50356 | NORMAL_TEXT | TABLE row=4 col=0]
Total (3 yr; under $9M cap)

[P00344 | 50357:50363 | NORMAL_TEXT | TABLE row=4 col=1]
~6.35

[P00345 | 50364:50370 | NORMAL_TEXT | TABLE row=4 col=2]
~2.90

[P00346 | 50371:50392 | NORMAL_TEXT | TABLE row=4 col=3]
~9.25 → trim to ≤$9M

[P00347 | 50393:50909 | NORMAL_TEXT]
Indirect costs are computed at each institution's federally negotiated rate (UW: 55.5% MTDC on-campus per cognizant-agency letter; EarthScope: per its negotiated agreement). The 15% IDC cap of NSF 25-034 is currently not in effect (court vacated); awards include a contingency term that may apply the cap if NSF is later permitted to implement, and the budget will be re-baselined if that occurs. Final budget is tuned in the Supplementary Cost Estimate to land below the $9M Cat II cap with reasonable contingency.

[P00348 | 50909:50940 | NORMAL_TEXT]
6.2 Cost by Category and Phase

[P00349 | 50940:51544 | NORMAL_TEXT]
Personnel (~70% of direct): operations team scales up across year 1; development effort heaviest in year 1; foundation-model training compute heaviest in year 2 with model releases. Cloud infrastructure (~15% of direct): grows with usage; engineered for cost-per-query reduction year over year. Travel and training (~5%): includes annual NSF PI meeting, major CI conference travel, and annual OpenEarthAI Hazard Hackweek travel support. Outsourced services and software licenses (~5%): vendor SLAs disclosed in §5.3. Equipment (~5%): minor end-user laptops and modest on-premise compute for development.

[P00350 | 51544:51599 | NORMAL_TEXT]
6.3 Other Funding Sources and Scope-Overlap Prevention

[P00351 | 51599:52601 | NORMAL_TEXT]
EarthScope's base NGF Cooperative Agreement supports the underlying facility (continued data collection, archive operations, user support for non-AI workflows). OpenEarthAI's scope is the cross-agency, multi-hazard, AI-ready integration layer and is distinct from the NGF base scope; the boundary is documented in a Memorandum of Understanding between EarthScope's NGF and OpenEarthAI programs and audited annually. The UW subaward is scoped to OpenEarthAI-specific activities and does not duplicate scope already supported by other NSF, NASA, or NOAA awards held by the UW investigators (Current and Pending Support documents disclose all overlap and confirm none in scope). Forbidden cost categories — long-term data hosting/storage/curation, building renovation, and individual research enabled by the infrastructure — are excluded from the OpenEarthAI budget; long-term storage is funded via existing NGF facility mechanisms or partnership/fee-based arrangements as encouraged by the solicitation.

[P00352 | 52601:52649 | NORMAL_TEXT]
6.4 Cat II Transition Plan from Current Funding

[P00353 | 52649:53647 | NORMAL_TEXT]
The UW OpenEarthAI HazLab regional prototype is currently supported by the UW eScience Institute, UW College of the Environment, and the UW Fund for Future Science and Technology (FFST). Those funding sources are research-program-scale and are scheduled to conclude or transition to other purposes during year 1 of OpenEarthAI. The transition plan: months 1–6, OpenEarthAI HazLab regional services continue under current UW support while integration with the EarthScope cloud envelope is completed; months 6–12, OpenEarthAI HazLab national-scale services run in parallel under OpenEarthAI Cat II support while regional-only endpoints are deprecated; month 12, transition complete and all services run under OpenEarthAI Cat II support. Continuity of service is guaranteed for current OpenEarthAI HazLab users throughout the transition. Similarly, the existing NGF and ASF user-facing services are not interrupted; OpenEarthAI scope is additive and complementary to both during and after transition.

[P00354 | 53647:53663 | NORMAL_TEXT]
Broader Impacts

[P00355 | 53663:53879 | NORMAL_TEXT]
OpenEarthAI delivers broad national benefit aligned with the America COMPETES Reauthorization Act broader-impacts goals 1–6 (and 7 in an open-to-all-Americans framing) and with the April 2025 NSF priority statement.

[P00356 | 53879:54527 | NORMAL_TEXT]
Public safety, infrastructure resilience, and economic competitiveness (goals 1–2). Multi-hazard cascades — atmospheric-river floods and landslides, earthquake-induced ground failure, post-fire debris flows, severe convective storms — affect public safety, critical infrastructure, insurance markets, agriculture, and military readiness across all 50 states. OpenEarthAI’s national multi-hazard foundation models and benchmarks lower the barrier for agency partners, hazard engineering and insurance industry, and state and local emergency-management offices to use modern AI methods, directly serving U.S. economic competitiveness and resilience.

[P00357 | 54527:55065 | NORMAL_TEXT]
Workforce development (goal 2). OpenEarthAI trains the next generation of hazard-AI engineers, data scientists, and domain researchers through On-Ramp cloud notebooks, an annual OpenEarthAI Hackweek run by UW eScience, and two domain-focused short courses per year. Together these activities will train at least 1,800 researchers and students cumulatively over three years, open to applicants from all U.S. institutions in all 50 states and EPSCoR jurisdictions. Geographic distribution of training participants is monitored as a §4 KPI.

[P00358 | 55065:55463 | NORMAL_TEXT]
Geographic reach and institutional access. OpenEarthAI is engineered to reach all 50 U.S. states, EPSCoR jurisdictions, community colleges, primarily undergraduate institutions, MSIs, and HBCUs as institutional partners. Cloud-native delivery removes the on-premise hardware barrier; the open-tier allocation policy ensures no-questions-asked entry-level access for any U.S. researcher or student.

[P00359 | 55463:55817 | NORMAL_TEXT]
Academia–industry partnership (goal 4). OpenEarthAI’s open foundation models, benchmarks, and APIs lower the entry barrier for U.S. startups and innovation users in hazard engineering, insurance, infrastructure resilience, and utilities. The reusable feature library and hazard benchmarks materially advance the U.S. AI-for-hazards innovation ecosystem.

[P00360 | 55817:56175 | NORMAL_TEXT]
Pre-K–12 and undergraduate STEM education (goals 5–6). Modular, classroom-ready hazard-science materials mapped to Next Generation Science Standards Earth and Space Sciences strands will be released openly to all U.S. educators. Undergraduate Carpentries-style lessons and ready-to-teach Jupyter notebooks will accompany each foundation model and benchmark.

[P00361 | 56175:56702 | NORMAL_TEXT]
Open access and Gold Standard Science. Every OpenEarthAI software component is released under Apache License 2.0; every data product under CC-BY-4.0 or equivalent; every foundation model with weights, model card, and training pipeline; every public dashboard exposes operational and scientific-impact metrics in real time. These practices materially advance the Gold Standard Science tenets of EO 14303 — reproducibility, transparency, communication of error and uncertainty, peer review, and absence of conflicts of interest.

[P00362 | 56702:57294 | NORMAL_TEXT]
Integration with the national CI ecosystem. OpenEarthAI is complementary to and integrates with the NAIRR Pilot (data layer for AI compute), ACCESS (data services for ACCESS-allocated jobs), the NSF AI Institutes (data layer for AI methods research), NASA ESDS, NOAA Big Data, USGS, DOE programs, and NSF Major Facilities (NEON, OOI, IceCube). By filling the cross-facility, multimodal, AI-ready, multi-hazard integration gap that no single program currently fills, OpenEarthAI strengthens the entire national research-data ecosystem and advances U.S. leadership in AI-driven hazard science.

## References Cited (t.wanzbxpduep4)

[P00363 | 1:18 | HEADING_1]
References Cited

[P00364 | 18:383 | NORMAL_TEXT]
Bodnar, C., Bruinsma, W. P., Lucic, A., Stanley, M., Allen, A., Brandstetter, J., Garvan, P., Riechert, M., Weyn, J. A., Dong, H., Gupta, J. K., Thambiratnam, K., Archibald, A. T., Wu, C.-C., Heider, E., Welling, M., Turner, R. E., & Perdikaris, P. (2025). A foundation model for the Earth system. Nature, 641, 1180–1187. [https://doi.org/10.1038/s41586-025-09005-y](https://doi.org/10.1038/s41586-025-09005-y)

[P00365 | 383:384 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00366 | 384:750 | NORMAL_TEXT]
Bouffaut, L., Taweesintananon, K., Kriesell, H. J., Rørstadbotnen, R. A., Potter, J. R., Landrø, M., Johansen, S. E., Brenne, J. K., Haukanes, A., Schjelderup, O., & Storvik, F. (2022). Eavesdropping at the speed of light: Distributed acoustic sensing of baleen whales in the Arctic. Frontiers in Marine Science, 9, 901348. [https://doi.org/10.3389/fmars.2022.901348](https://doi.org/10.3389/fmars.2022.901348)

[P00367 | 750:751 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00368 | 751:1061 | NORMAL_TEXT]
Cox, S. C., van Ballegooy, S., Rutter, H. K., Harte, D. S., Holden, C., Gulley, A. K., Lacrosse, V., & Manga, M. (2021). Can artesian groundwater and earthquake-induced aquifer leakage exacerbate the manifestation of liquefaction? Engineering Geology, 281, 105982. [https://doi.org/10.1016/j.enggeo.2020.105982](https://doi.org/10.1016/j.enggeo.2020.105982)

[P00369 | 1061:1062 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00370 | 1062:1483 | NORMAL_TEXT]
Gräff, D., Lipovsky, B. P., Vieli, A., Dachauer, A., Jackson, R., Farinotti, D., Schmale, J., Ampuero, J.-P., Berg, E., Dannowski, A., Kneib-Walter, A., Köpfli, M., Kopp, H., van der Loo, E., Mata Flores, D., Mercerat, D., Moser, R., Sladen, A., Walter, F., … Williams, E. F. (2025). Calving-driven fjord dynamics resolved by seafloor fibre sensing. Nature, 644(8076), 404–412. [https://doi.org/10.1038/s41586-025-09347-7](https://doi.org/10.1038/s41586-025-09347-7)

[P00371 | 1483:1484 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00372 | 1484:1757 | NORMAL_TEXT]
Jousset, P., Currenti, G., Schwarz, B., Chalari, A., Tilmann, F., Reinsch, T., Zuccarello, L., Privitera, E., & Krawczyk, C. M. (2022). Fibre optic distributed acoustic sensing of volcanic events. Nature Communications, 13, 1753. [https://doi.org/10.1038/s41467-022-29184-w](https://doi.org/10.1038/s41467-022-29184-w)

[P00373 | 1757:1758 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00374 | 1758:2013 | NORMAL_TEXT]
Manos, J.-M., Gräff, D., Martin, E. R., Paitz, P., Walter, F., Fichtner, A., & Lipovsky, B. P. (2024). DAS to discharge: Using distributed acoustic sensing (DAS) to infer glacier runoff. Journal of Glaciology, 70, e67. [https://doi.org/10.1017/jog.2024.46](https://doi.org/10.1017/jog.2024.46)

[P00375 | 2013:2014 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00376 | 2014:2203 | NORMAL_TEXT]
National Academies of Sciences, Engineering, and Medicine. (2017). Enhancing the resilience of the nation’s electricity system. The National Academies Press. [https://doi.org/10.17226/24836](https://doi.org/10.17226/24836)

[P00377 | 2203:2204 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00378 | 2204:2390 | NORMAL_TEXT]
National Academies of Sciences, Engineering, and Medicine. (2020). A vision for NSF Earth sciences 2020–2030: Earth in time. The National Academies Press. [https://doi.org/10.17226/25761](https://doi.org/10.17226/25761)

[P00379 | 2390:2391 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00380 | 2391:2570 | NORMAL_TEXT]
National Academies of Sciences, Engineering, and Medicine. (2021). The future of electric power in the United States. The National Academies Press. [https://doi.org/10.17226/25968](https://doi.org/10.17226/25968)

[P00381 | 2570:2571 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00382 | 2571:2794 | NORMAL_TEXT]
Ni, Y., Denolle, M. A., Fatland, R., Alterman, N., Lipovsky, B. P., & Knuth, F. (2024). An object storage for distributed acoustic sensing. Seismological Research Letters, 95(1), 499–511. [https://doi.org/10.1785/0220230172](https://doi.org/10.1785/0220230172)

[P00383 | 2794:2795 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00384 | 2795:3088 | NORMAL_TEXT]
Paitz, P., Lindner, N. M. A., Edme, P., Huguenin, P., Hohl, M., Sovilla, B., Walter, F., & Fichtner, A. (2023). Phenomenology of avalanche recordings from distributed acoustic sensing. Journal of Geophysical Research: Earth Surface, 128(5), e2022JF007011. [https://doi.org/10.1029/2022JF007011](https://doi.org/10.1029/2022JF007011)

[P00385 | 3088:3089 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00386 | 3089:3354 | NORMAL_TEXT]
Shi, Q., Williams, E. F., Lipovsky, B. P., Denolle, M. A., Wilcock, W. S. D., Kelley, D. S., & Schoedl, K. (2025). Multiplexed distributed acoustic sensing offshore central Oregon. Seismological Research Letters, 96(2A), 784–800. [https://doi.org/10.1785/0220240460](https://doi.org/10.1785/0220240460)

[P00387 | 3354:3355 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00388 | 3355:3667 | NORMAL_TEXT]
Staley, D. M., Negri, J. A., Kean, J. W., Laber, J. L., Tillery, A. C., & Youberg, A. M. (2017). Prediction of spatially explicit rainfall intensity–duration thresholds for post-fire debris-flow generation in the western United States. Geomorphology, 278, 149–162. [https://doi.org/10.1016/j.geomorph.2016.10.019](https://doi.org/10.1016/j.geomorph.2016.10.019)

[P00389 | 3667:3668 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00390 | 3668:3913 | NORMAL_TEXT]
Trafford, A., Ellwood, R., Wacquier, L., Godfrey, A., Minto, C., Coughlan, M., & Donohue, S. (2022). Distributed acoustic sensing for active offshore shear wave profiling. Scientific Reports, 12, 9691. [https://doi.org/10.1038/s41598-022-13962-z](https://doi.org/10.1038/s41598-022-13962-z)

[P00391 | 3913:3914 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00392 | 3914:4349 | NORMAL_TEXT]
Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., Blomberg, N., Boiten, J.-W., Bonino da Silva Santos, L., Bourne, P. E., Bouwman, J., Brookes, A. J., Clark, T., Crosas, M., Dillo, I., Dumon, O., Edmunds, S., Evelo, C. T., Finkers, R., … Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. Scientific Data, 3, 160018. [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

[P00393 | 4349:4350 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

[P00394 | 4350:4787 | NORMAL_TEXT]
Yanites, B. J., Clark, M., Roering, J. J., West, A. J., Zekkos, D., Baldwin, J. W., Cerovski-Darriau, C., Gallen, S. F., Horton, D. E., Kirby, E., Leshchinsky, B. A., Mason, H. B., Moon, S., Barnhart, K. R., Booth, A. M., Czuba, J. A., McCoy, S., McGuire, L. A., Pfeiffer, A. M., & Pierce, J. L. (2025). Cascading land surface hazards as a nexus in the Earth system. Science, 388(6754), eadp9559. [https://doi.org/10.1126/science.adp9559](https://doi.org/10.1126/science.adp9559)

[P00395 | 4787:4788 | NORMAL_TEXT]
⟦EMPTY PARAGRAPH⟧

