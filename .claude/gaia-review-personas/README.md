<!-- gaia-header -->
[![GAIA](https://img.shields.io/badge/GAIA-coordination-4B2E83)](https://github.com/gaia-hazlab)
[![maturity](https://img.shields.io/badge/maturity-incubating-B7A57A)](https://gaia-hazlab.github.io/book/organization)
[![relationship](https://img.shields.io/badge/relationship-core-4B2E83)](https://gaia-hazlab.github.io/book/organization)

Ten review personas that read the GAIA website, book and GitHub organisation the way ten
different outside audiences would, and report against one shared rubric.

Part of [GAIA HazLab](https://gaia-hazlab.github.io) — predictive understanding of
weather-compounded geohazards.
<!-- gaia-header -->

# GAIA review personas

A project funded to build public infrastructure has to be legible to people who were not in
the room when it was proposed. This repository holds ten personas, each written as a skill,
that read the project as a particular kind of outsider and file a structured review.

They exist because the people who build a thing are the worst possible judges of whether it
explains itself.

## The ten

| Skill | Sector | Reads as |
|---|---|---|
| [`phd-student-prospective`](personas/phd-student-prospective/SKILL.md) | Academia | Prospective PhD student choosing a thesis foundation |
| [`research-software-engineer`](personas/research-software-engineer/SKILL.md) | Academia | Research software engineer evaluating adoption |
| [`national-lab-scientist`](personas/national-lab-scientist/SKILL.md) | Academia | National laboratory staff scientist assessing interoperability |
| [`faculty-panel-reviewer`](personas/faculty-panel-reviewer/SKILL.md) | Academia | Senior faculty reading as a panel reviewer would |
| [`foundation-program-officer`](personas/foundation-program-officer/SKILL.md) | Philanthropy | Family foundation program officer and donor advisor |
| [`foundation-science-advisor`](personas/foundation-science-advisor/SKILL.md) | Philanthropy | Foundation science advisor doing technical diligence |
| [`impact-evaluation-officer`](personas/impact-evaluation-officer/SKILL.md) | Philanthropy | Impact and evaluation officer auditing the measurement system |
| [`climate-risk-cto`](personas/climate-risk-cto/SKILL.md) | Climate and energy technology | CTO of a climate-risk analytics company |
| [`energy-resilience-ceo`](personas/energy-resilience-ceo/SKILL.md) | Climate and energy technology | CEO of a grid and energy resilience company |
| [`geospatial-ai-cto`](personas/geospatial-ai-cto/SKILL.md) | Climate and energy technology | CTO of a geospatial AI and foundation-model company |

Four from academia because that is where adoption starts, three from philanthropy because the
project carries philanthropic as well as federal funding, and three from industry because
infrastructure that nobody outside the academy can use is not infrastructure.

## How they work

Every persona scores the same eight dimensions and files the same report shape, but weights
those dimensions differently — a program officer puts thirty points on clarity of purpose and
zero on reproducibility; a research software engineer does close to the reverse. The common
shape is what makes ten reviews comparable; the differing weights are what makes them worth
running separately.

Each persona also carries a **vocabulary limit**. The program officer genuinely does not know
what a concept DOI is, and will flag it as jargon rather than quietly understanding it. That
constraint is the point: the blind spots are the instrument.

- **[`shared/rubric.md`](shared/rubric.md)** — the eight dimensions, the severity scale, the
  scoring guide, the evidence rules, and the report format.
- **[`shared/method.md`](shared/method.md)** — what to open, in what order, and how long to
  spend before giving up, which is itself a finding.
- **[`shared/synthesis.md`](shared/synthesis.md)** — how to merge several reviews without
  averaging away the disagreements, which are the useful part.
- **[`examples/`](examples/)** — worked reviews against the live site, dated. Calibration for
  what the right level of detail and honesty looks like.

## Using them

With an assistant that reads skills, ask for one by name:

> Review the GAIA site as the *foundation program officer*.

Or read the file and do it yourself — each is plain Markdown and works as a briefing note for
a human reviewer. That is the more valuable use: hand `climate-risk-cto/SKILL.md` to an actual
CTO and ask what it got wrong.

Run personas independently and merge afterwards. Convergence between a donor and a CTO is only
informative if neither saw the other's report.

## What these are not

These are **simulations**, and any review produced by one should say so. They are a cheap way
to catch the failures that are obvious from outside and invisible from inside — a missing
contact, an unexplained acronym, a claim in the present tense about something that does not
exist. They are not user research. A finding is a hypothesis about a real reader, not evidence
about one.

The honest use is as a filter before real people are asked for their time, and as a way of
holding a position: if the site cannot survive a sceptical reading by a constructed reviewer,
it will not survive a real one.

## Contributing

The personas are wrong in ways we cannot see from here. If you are one of these people, or you
work with them, tell us where the portrait is off — open an issue or a pull request against
the persona's `SKILL.md`. Corrections from someone who holds the actual job outrank anything
written here.

## Provenance

Written for the GAIA project in August 2026, grounded in the NSF CSSI awards, the CRESST focal
node proposal, and the Jerome and Linda Paros Geohazard Center's support — which is why the
philanthropy personas are three rather than one.

## Licence

CC BY 4.0. These are documents, not software. Adapt them for your own project; the structure
generalises further than the content does.

---

This material is based upon work supported by the U.S. National Science Foundation under Grant
Nos. OAC-2608509, OAC-2608510 and OAC-2608511.
