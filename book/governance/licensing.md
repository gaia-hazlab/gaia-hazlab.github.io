---
title: Licensing
short_title: Licensing
description: Which licence applies to what in GAIA, why, and how to add one. Code is MIT, documents are CC BY 4.0, and a repository without a LICENSE file is a bug.
---

(licensing)=

:::{note}
**Status.** Proposed, awaiting a numbered decision. Until it is ratified in the
[decisions register](decisions.md), individual repositories may not yet match what is described
here — the [licence audit](#licence-audit) below says which.
:::

Everything GAIA publishes is meant to be reusable. That is not a slogan: it is a condition of
the awards, and it is the whole argument for building shared infrastructure rather than
another set of scripts. A repository that cannot legally be reused fails that test no matter
how open it looks.

## The rule

| What it is | Licence |
|---|---|
| Software written by the project | **MIT** |
| Software written by the UW eScience **Scientific Software Engineering Center** | **whatever SSEC used** — currently BSD-3-Clause |
| Documentation, this book, vocabularies, curated indexes, model cards | **CC BY 4.0** |
| Curated data products we generate | **CC BY 4.0**, with upstream terms restated |
| Data we merely redistribute | **upstream terms**, restated |
| Container images | inherit the base image; state it in the image label |

MIT is the default because it is short, permissive, and a facility can adopt MIT code without
a legal review. SSEC-authored code keeps the licence SSEC chose, because it is theirs and
relicensing someone else's work is not ours to do.

Data we redistribute is the row people get wrong. Most of our inputs — USGS gauge records, ASF
products, NASA holdings — are federal and already public domain or subject to their own terms.
We cannot relicense them, and applying a GAIA licence to a repackaged federal dataset asserts
a right we do not have. Restate the upstream terms and say where the data came from.

## Two things worth being precise about

**"More permissive than MIT" usually means something else.** Apache-2.0 is often described
that way; it is not more permissive. It adds an express patent grant and a NOTICE requirement
— more protective, and slightly more paperwork. Genuinely more permissive means 0BSD, CC0 or
the Unlicense, which drop attribution altogether. For a project trying to make its software
citable, dropping attribution works against the goal. Use MIT unless you have a reason you can
state out loud.

**A README claim is not a licence.** Absent a `LICENSE` file, default copyright applies and
nobody may reuse the work, however clearly the README invites them to. The combination of a
confident README and a missing file is worse than a plain omission, because it invites
reliance on a permission that was never granted.

## Licence compatibility, in the one case where it bites

`usgs-gauge-utils` is GPL-3.0 while the rest of the organisation is MIT. GPL is not compatible
in the direction that matters here: pull that code into an MIT repository and the combined
work must be distributed under GPL. Its README already says development moved to
`gaia-data-downloaders`, so the safe response is to archive it rather than copy from it. If a
piece of it is genuinely needed, rewrite rather than paste.

This is the general shape of the problem, not a quirk of one repository. Before vendoring code
from anywhere, check what it is licensed under and whether the result can still ship under
ours.

## The copyright line

New repositories should use:

```
Copyright (c) 2026 GAIA HazLab contributors
```

This is the ordinary pattern for a project spanning several institutions, and it avoids
asserting a legal entity that does not exist. Existing repositories carry five different
variants, most of them the expanded project name, which is a description and not an entity.
Normalising them is a one-line change per file and is tracked separately. SSEC-authored
repositories keep the SSEC copyright line as written.

(licence-audit)=
## Where we actually stand

Audited 9 August 2026, reading the raw files rather than the READMEs.

| | Count of 25 |
|---|---|
| Public repositories with **no `LICENSE` file at all** | **8** |
| Repositories asserting a licence they do not carry | 2 |
| Distinct copyright lines among those that do have one | 5 |

The eight: `awesome-gaia`, `gaia-data-downloaders`, `gaia-translate-QA`, `seis-hydro-2-sed`,
`landlab-debrisflow`, `da-seis-groundfailure`, `shred-landlab-prototypes`,
`mt-rainier-smart-sensing`.

Each has an open issue naming the licence it should carry and how to add it. `awesome-gaia`
takes CC BY 4.0 rather than MIT, since it is a curated list rather than software.

We publish this number rather than fixing it quietly, for the same reason the
[dashboard](how-we-work.md) shows figures below target: a page claiming everything is open, on a
project where a third of the repositories are not, would be worth less than the number.

## Adding a licence

The two-minute route is GitHub's own picker. In the repository: **Add file → Create new
file**, type `LICENSE` as the filename, and a **Choose a license template** button appears.
Pick the licence, let it fill in the year and holder, commit to a branch, open a pull request.

Use the picker rather than pasting text from elsewhere. It writes the canonical wording, which
is what makes GitHub recognise the licence and display it in the repository's About panel. If
the About panel still shows nothing after merging, the file was not recognised — and if GitHub
cannot read it, neither can the tools that count what we publish.

For CC BY 4.0, take the text from
[creativecommons.org](https://creativecommons.org/licenses/by/4.0/legalcode.txt).

Then check three things agree: the `LICENSE` file, the README, and the `license:` field in
`CITATION.cff` if the repository has one. A `CITATION.cff` declaring a licence the repository
does not carry is how the current mess started.

## Licensing and citation are one question

From a user's side, "may I use this?" and "how do I credit it?" are the same conversation. The
licence grants the permission; the [citation](how-we-work.md) machinery makes the credit
possible. Neither works alone — a permissively licensed repository with no `CITATION.cff` gets
used and never cited, which is precisely the invisibility this project exists to argue
against.

## If something here is wrong

Open an issue. Corrections to licensing are as welcome as corrections to science, and the edit
history is public either way.
