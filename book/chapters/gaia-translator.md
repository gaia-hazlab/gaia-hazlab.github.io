# Gaia Translator

## Overview

The **Gaia Translator** is a research chatbot designed to bridge disciplinary divides across the geosciences. It helps researchers (a) interpret papers outside their primary discipline, (b) discover how their work integrates with adjacent fields, and (c) propose joint-observation strategies — with every answer grounded in cited scientific evidence.

The translator targets nine geoscience disciplines that the GAIA HazLab agenda routinely needs to integrate: hydrology, seismology, geotechnical engineering, geomorphology, atmospheric sciences, ecology, agricultural sciences, near-surface geophysics, and the cross-cutting concepts that bridge them. Its design treats cross-discipline integration as a *first-class object*: the deep bridges between fields (effective stress, diffusion, ambient-field exploitation, data assimilation) are themselves part of the knowledge base, not emergent properties the model is left to infer.

The project is companion infrastructure to the GAIA HazLab DataHub, ModelHub, and HazEvalHub: where DataHub assembles the observational substrate and ModelHub builds predictive models, the Translator builds the human-AI collaboration layer that makes cross-disciplinary integration tractable for researchers, students, and decision-makers.

**Repository**: [gaia-translate-QA](https://github.com/gaia-hazlab/gaia-translate-QA) (open-source under MIT for code / CC-BY-4.0 for content).

## Why a translator is needed

A typical Pacific Northwest hazard cascade — atmospheric river → orographic precipitation → shallow landslide → debris flow → downstream sediment delivery → fluvial habitat impact — is touched by seven of our nine disciplines. The papers that describe it live in seven non-overlapping journal communities, use seven partially incompatible vocabularies, and rarely cite each other. Effective integration today depends on rare individual researchers who have invested years in becoming bilingual.

The Translator is an attempt to scale that bilingualism. It does not replace the deep-collaboration relationships that make integration work; it lowers the activation energy for a researcher in one discipline to seriously engage with a paper, a method, or an observation in another.

## How it works

The Translator is built on a three-layer architecture:

1. **System-prompt summaries** — short, ~350-word per-discipline summaries that the chatbot carries as context at every turn. These give the agent baseline discipline awareness without dominating the context window.
2. **Long-form knowledge cards** — a retrieval corpus of ≤500-word cards, organized into four types: *concept cards* (one per major variable or governing equation), *method cards* (one per measurement technique or dataset), *phenomenon dossiers* (one per real-world phenomenon observable by multiple disciplines), and *translation cards* (one per cross-discipline bridge).
3. **Claude inference** with a structured agent playbook that defines four primary user flows — paper interpretation, cross-discipline integration, vocabulary disambiguation, joint observation — and explicit refusal patterns for forced analogies and fabricated citations.

Every card is independent, ≤500 words, cited with full DOIs, and named in a co-retrieval index that promotes the right neighbors when any card is retrieved.

### Example: effective stress as a deep bridge

A representative translation card, `TC-02`, captures the bridge between hydrology, geotechnical engineering, and seismology through the Terzaghi-Biot effective stress relation σ' = σ − αp. The same equation underlies:

- liquefaction triggering in saturated cohesionless soils (geotechnical engineering),
- pore-pressure-driven shallow landslides (geomorphology + hydrology),
- injection-induced seismicity (seismology + hydrology),
- megathrust fault stability (seismology),
- pumping-induced consolidation and land subsidence (geotechnical engineering + hydrology).

The card names each manifestation, identifies when the analogy holds (saturated, isotropic Biot coefficient, linear-elastic) and breaks (unsaturated requires Bishop effective stress; large strain breaks the elastic framework), and lists the anchor citations on each side. When a reviewer in any single discipline asks about a problem touching the others, the chatbot retrieves this card and the discipline-specific concept cards together.

## Current corpus

As of the v3 release (May 2026), three disciplines have completed v3-card-pattern restructuring:

- **Seismology** — 23 cards (8 concept / 7 method / 5 phenomenon / 3 translation)
- **Geotechnical engineering** — 21 cards (7 / 7 / 4 / 3, including `TC-12` on Vs across depth regimes)
- **Hydrology** — 27 cards (9 / 7 / 5 / 6, including the foundational `TC-01` through `TC-06` cross-cutting bridges)

The remaining five disciplines (geomorphology, atmospheric sciences, ecology, agricultural sciences, near-surface geophysics) are in queue. The repository's [roadmap](https://github.com/gaia-hazlab/gaia-translate-QA/blob/main/docs/roadmap.md) lays out the priority order.

## The HazEvalHub connection: expert evaluation platform

The Translator's evaluation strategy is itself a contribution. A 60-question seed eval set spans the nine disciplines and four query types; a planned expansion to ~300 questions, scored by 15–25 domain-expert reviewers against an 8-criterion rubric (technical accuracy, citation discipline, vocabulary precision, cross-discipline integration, refusal correctness, completeness, presentation, overall usefulness) will produce a citable expert-graded benchmark for LLM-agent evaluation in cross-disciplinary geoscience.

The evaluation infrastructure — Sheets templates, signup forms, kickoff-meeting calibration design, inter-rater reliability methodology — is generic enough to support future GAIA HazLab evaluation exercises beyond the Translator, including coding-agent evaluations and any future model that needs domain-expert judgment in the loop. The data model is documented in the `eval_platform/` directory of the repository.

This expert-grounded evaluation complements the automated benchmarking described in [HazEvalHub](./hazevalhub.md): automated metrics tell us how a model behaves on held-out data; expert evaluation tells us whether the model's behavior is actually useful to a researcher.

## Use case: Nisqually 2001 liquefaction digital twin

The Translator's first applied use case is the [Nisqually 2001 liquefaction digital twin](./wa-2001-2031-nisqually-earthquake.md). Building a useful digital twin requires fluent communication across seismology (ground motion, source physics), geotechnical engineering (CSR / CRR triggering, site response), hydrology (pore-pressure history, water-table position), and near-surface geophysics (Vs profiles, basin amplification). The Translator's seismology + geotechnical engineering + hydrology corpora are designed to make the integration tractable.

## Cross-cutting in the AI agenda

The Translator is one of several GAIA HazLab projects that exploit large language models as research infrastructure. Its specific contribution is to treat cross-disciplinary translation as a *grounded, citable, evaluatable* problem — not a free-form summarization task. The agent's refusal patterns (no forced analogies, no fabricated citations, no surface power-law equivalences) are designed to make it usable in research contexts where fabrication is the single most damaging failure mode.

The Translator complements (and depends on) work from the broader GAIA HazLab team on hazard-specific models — [Yiyu Ni](https://niyiyu.github.io/) on earthquake wavefields, [Morgan Sanger](https://sangermd.github.io/website/) on ground failure modeling, [Akash Kharita](https://gaia-hazlab.github.io/people) on storm and landslide detection, [Manuela Köpfli](https://gaia-hazlab.github.io/people) on hydromechanical data integration — by providing the human-AI collaboration layer that helps these models be jointly used by researchers across disciplines.

## Get involved

We are recruiting domain-expert reviewers across the nine disciplines for the v1 expert evaluation round. Reviewers commit ~5–8 hours over six weeks to score chatbot answers against the 8-criterion rubric, in exchange for named attribution on the Zenodo DOI and co-authorship on the planned methodology paper. See the repository's [`eval_platform/README.md`](https://github.com/gaia-hazlab/gaia-translate-QA/blob/main/eval_platform/README.md) for the signup process and reviewer instructions.

Contributions to the knowledge corpus — new cards, revisions to existing cards, translation of additional cross-discipline bridges — are welcomed via pull request to the [gaia-translate-QA](https://github.com/gaia-hazlab/gaia-translate-QA) repository.

## Resources

- **Repository**: [gaia-translate-QA](https://github.com/gaia-hazlab/gaia-translate-QA)
- **Roadmap**: [docs/roadmap.md](https://github.com/gaia-hazlab/gaia-translate-QA/blob/main/docs/roadmap.md)
- **Eval platform**: [eval_platform/](https://github.com/gaia-hazlab/gaia-translate-QA/tree/main/eval_platform)
- **Card format specification**: [docs/card_format_spec.md](https://github.com/gaia-hazlab/gaia-translate-QA/blob/main/docs/card_format_spec.md)
- **Agent playbook** (reasoning templates, refusal patterns, vocabulary disambiguation): [skills/agent_playbook.md](https://github.com/gaia-hazlab/gaia-translate-QA/blob/main/skills/agent_playbook.md)

## Acknowledgments

This work is part of the GAIA HazLab initiative at the University of Washington, supported by NSF EAR-2346079 and related awards. The card corpus and evaluation set were drafted with Claude Opus and curated by the [Denolle Group](https://denolle-lab.github.io/).
