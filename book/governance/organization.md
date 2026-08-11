---
title: The organisation, and how work joins it
short_title: Organisation
description: What the gaia-hazlab GitHub organisation holds, how repositories are tagged, and the five levels at which outside software can join GAIA.
---

## What the organisation holds

The [`gaia-hazlab`](https://github.com/gaia-hazlab) organisation does four different jobs,
and keeping them distinct is what determines whether it stays maintainable.

**How the project runs.** The website and this book, which also carry the coordination
documents and the published weekly digests; a private `notes` repository holding meeting
notes and the redacted Slack archive; and `metrics-observatory`, which produces the
dashboard.

**Software we maintain.** Workflow templates that pass their own tests, container images,
the evaluation library behind HazEvalHub, and the research agents. These carry a real
commitment: if it is here, we keep it working.

**Software we only point to.** A curated index of community tools — ObsPy, SeisBench,
NoisePy, MTUQ, MintPy, ISCE3, RioXarray and others — that a GAIA user is likely to need.
An entry is a recommendation and a link. It is explicitly *not* a maintenance promise.

**The science.** Use-case repositories and the chapters that describe them.

The third category is what keeps the first two sustainable. Without a place to point at
things, an infrastructure project drifts toward absorbing them, and inherits maintenance for
code it did not write and cannot fix.

## How repositories are tagged

:::{note} Proposed — not yet ratified
This taxonomy is a proposal awaiting a numbered decision. Until it is ratified, repository
topics may not match what is described here.
:::

Every public repository carries four GitHub topics, so the taxonomy is machine-readable and
the [Metrics Observatory](https://github.com/gaia-hazlab/metrics-observatory) can count
against it without anyone maintaining a list by hand.

| Axis | Values | Rule |
|---|---|---|
| Umbrella | `gaia` | Every repository |
| Category | `gaia-coordination` · `gaia-template` · `gaia-container` · `gaia-agent` · `gaia-eval` · `gaia-science` | Exactly one |
| Relationship | `gaia-core`, or `gaia-level-1` … `gaia-level-4` | Exactly one |
| Maturity | `gaia-stable` · `gaia-incubating` · `gaia-archived` | Exactly one |

**Category** says what a repository *is*. **Relationship** says how it came to be here —
`gaia-core` for work built by the project, or a level from the ladder below for software that
joined from outside. **Maturity** exists because a list of repositories is not a
recommendation: without it, a newcomer cannot tell established work from an experiment.

Existing repositories are tagged, never renamed — renaming breaks clones, bookmarks and any
URL already printed in a paper or proposal. New *software products* follow a naming
convention (`gaia-template-datacube`, `gaia-container-noisepy`, `gaia-agent-translator`),
while science and coordination repositories keep descriptive names, since those are the ones
most likely to be cited.

## How outside work joins GAIA

Five levels of relationship. Each is a larger commitment by us than the one before, so each
is agreed rather than assumed. A group choosing to stay at level 0 indefinitely is a success,
not a failure.

| | Level | What it means | What GAIA commits to |
|---|---|---|---|
| 0 | **Listed** | A line in the index, proposed by anyone through a pull request | Curation, and a link check |
| 1 | **Containerised** | We publish a tested image; the software stays with its authors and is never forked | Scheduled rebuilds, CI on the image |
| 2 | **Demonstrated** | A template repository shows a complete workflow using it | Keeping that template passing |
| 3 | **Benchmarked** | It becomes a task or baseline in the evaluation hub | Maintaining the task and its held-out data |
| 4 | **Adopted** | The repository moves into the organisation | Long-term maintenance — requires a named maintainer and a numbered decision |

Levels 1–3 each correspond to something we already count — containers, templates and
evaluation tasks are all reported metrics — which keeps the ladder honest rather than
decorative.

If you maintain a tool and want it listed, that is level 0 and it needs nobody's permission
beyond a pull request. See the [FAQ](./faq.md) for what a good entry looks like.

## What we learned from SCOPED

The container registry built for [SCOPED](https://github.com/SeisSCOPED) is the closest
precedent available to us, and four things carry over.

**A small base image with thin layers above it.** SCOPED's base held minimum dependencies,
with separate layers adding what HPC work (MPI) or cloud work (provider CLIs) required. We
inherit that structure rather than building one image per situation.

**One repository per tool.** NoisePy, MTUQ and ELEP each had their own, maintained by people
who knew the software. This scales, and it puts maintenance where the knowledge is.

**Pinned dependencies, rather than containers as such, produced reproducibility.** Workshop
material from years ago still runs because versions were fixed. The container was the
delivery mechanism; the pinning was the guarantee.

**Image size and teaching materials pull in different directions.** HPC favours small
images; teaching benefits from notebooks and test data travelling with the image. SCOPED
documented this trade-off but left it to each project. The lesson we take is to settle it at
the outset — two tags per tool, a lean image and a teaching image, rather than one
compromise image that serves neither well.

What SCOPED lacked, and what the index is meant to supply, was a way for a newcomer to tell
established work from experiment. A repository list is not a recommendation; a curated index
is.
