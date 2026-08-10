---
title: Licensing
short_title: Licensing
description: How GAIA chooses a licence and applies it. Code is MIT, documents and data products are CC BY 4.0, AI-assisted code is licensed like any other code, and a repository without a LICENSE file is a bug.
---

(licensing)=

:::{note}
**Status.** Proposed, awaiting a numbered decision in the
[decisions register](decisions.md). Until it is ratified, individual repositories may not
yet match what is described here.
:::

Everything GAIA publishes is meant to be reusable. That is not a slogan: it is a condition
of the awards and the whole argument for building shared infrastructure. A repository that
cannot legally be reused fails that test no matter how open it looks. These are the project
guidelines for making that reuse legal by default.

## The rule

| What it is | Licence |
|---|---|
| Software written by the project | **MIT** |
| Software written by the UW eScience **Scientific Software Engineering Center** | **whatever SSEC used** — currently BSD-3-Clause |
| Documentation, this book, vocabularies, curated indexes, model cards | **CC BY 4.0** |
| Curated data products we generate | **CC BY 4.0**, with upstream terms restated |
| Data we merely redistribute | **upstream terms**, restated |
| Container images | inherit the base image; state it in the image label |

## How we choose a licence

Our default is **MIT**, and the guiding principle is simple:

> **Choose the least restrictive licence that still requires attribution.**

Least restrictive keeps the software easy to adopt — a facility can pull in MIT code
without a legal review. *Still requires attribution* keeps it **citable**, which is the
outcome this project exists to produce. Licences that drop attribution (0BSD, CC0, the
Unlicense) are "more permissive" in the strict sense but work against citability, so we do
not use them.

Use this to place any licence you are considering:

| Family | Examples | What it means for reuse | Where we use it |
|---|---|---|---|
| **Permissive** | MIT, BSD-3-Clause, Apache-2.0 | Reuse freely; keep the attribution/licence notice | **MIT** is the default; **BSD-3** for SSEC code; **Apache-2.0** only when you specifically need its patent grant |
| **Public-domain-style** | 0BSD, CC0, Unlicense | Reuse freely, *no* attribution | Avoid — breaks citability |
| **Copyleft** | GPL, LGPL, AGPL, MPL | Derivatives must stay under the same licence | Avoid for anything meant to be a library; never vendor into MIT (see [compatibility](#compatibility)) |
| **Content** | CC BY 4.0 | Attribution, for prose and data rather than code | Docs, this book, curated data products |

A common trap: **Apache-2.0 is not "more permissive" than MIT.** It adds an express patent
grant and a `NOTICE` requirement — more *protective*, and slightly more paperwork. Reach for
it only when the patent grant matters (e.g. code with patentable methods shared with
industry); otherwise MIT is shorter and simpler.

**Data we redistribute is the row people get wrong.** Most inputs — USGS gauge records, ASF
products, NASA holdings — are federal and already public domain or carry their own terms. We
cannot relicense them; stamping a GAIA licence on a repackaged federal dataset asserts a
right we do not have. Restate the upstream terms and say where the data came from.

Resources for picking and checking a licence:

- [choosealicense.com](https://choosealicense.com/) — plain-language chooser (GitHub).
- [OSI approved licences](https://opensource.org/licenses) and the
  [SPDX licence list](https://spdx.org/licenses/) — canonical identifiers to put in
  `CITATION.cff` and package metadata.
- [MIT](https://opensource.org/license/mit) ·
  [BSD-3-Clause](https://opensource.org/license/bsd-3-clause) ·
  [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) ·
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

(compatibility)=
## Compatibility: never mix copyleft into permissive

Before you vendor, copy, or paste code from anywhere, check what it is licensed under and
whether the result can still ship under ours. Copyleft is the case that bites: pull **GPL**
code into an MIT repository and the *combined* work must be distributed under GPL. The
direction is one-way, and it is not negotiable by a README.

The rule: if a needed snippet is copyleft, **rewrite rather than paste**, or depend on it at
arm's length (a separate process/service) rather than linking it in. Archive superseded
copyleft repositories instead of copying from them. See the GNU
[licence compatibility list](https://www.gnu.org/licenses/license-list.html) when in doubt.

## Licensing AI-assisted and AI-generated code

Much GAIA code is drafted with assistants (Claude, ChatGPT, Copilot). That changes what you
should **document**, not what licence applies. The guidelines:

1. **Licence it like any other code — MIT by default.** The assistant is a tool, not an
   author or a rights-holder. Never list a model, "OpenAI", or "Anthropic" as a copyright
   holder, and never add them to the `LICENSE` or the copyright line.
2. **You are allowed to license it.** The major assistants assign their rights in the output
   to you: see the
   [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms) and the
   [OpenAI Terms of Use](https://openai.com/policies/terms-of-use). So releasing
   AI-drafted code under MIT is yours to do.
3. **Understand what copyright actually attaches to.** Under current U.S. Copyright Office
   [guidance on AI](https://www.copyright.gov/ai/), purely machine-generated material may not
   be copyrightable, but the parts a human *directs, selects, edits, integrates, and tests*
   carry human authorship. Practically this changes nothing about the file you ship — license
   the repository normally; the MIT grant lets people reuse it either way.
4. **Disclose material AI assistance — provenance is our ethos.** When a model wrote a
   non-trivial part of a file, say so, lightly and in the place people already look:
   - a commit trailer (`Co-Authored-By:` / a "Generated with …" line),
   - a sentence in the README or methods, and/or
   - the provenance YAML / RO-Crate we already ship with releases.
   This mirrors our reproducibility practice and keeps a **human accountable** for the code —
   the assistant does not own it and cannot be responsible for it.
5. **The compatibility rule still applies.** Assistants can reproduce third-party code, and
   sometimes copyleft snippets, close to verbatim. Do not paste output that looks like it was
   lifted from an incompatible source; review before committing.

> This is project guidance, not legal advice. When a case is genuinely unclear — patents,
> a mixed-licence dependency, third-party data terms — ask before you publish, and note the
> question in the [decisions register](decisions.md).

## The copyright line

New repositories should use:

```
Copyright (c) 2026 GAIA HazLab contributors
```

This is the ordinary pattern for a project spanning several institutions, and it avoids
asserting a legal entity that does not exist. Existing repositories carry five variants, most
of them the expanded project name — a description, not an entity. Normalising them is a
one-line change per file, tracked separately. SSEC-authored repositories keep the SSEC
copyright line as written.

## Adding a licence

The two-minute route is GitHub's own picker. In the repository: **Add file → Create new
file**, type `LICENSE` as the filename, and a **Choose a license template** button appears.
Pick the licence, let it fill in the year and holder, commit to a branch, open a pull
request.

Use the picker rather than pasting text from elsewhere. It writes the canonical wording,
which is what makes GitHub recognise the licence and show it in the About panel. If the About
panel still shows nothing after merging, the file was not recognised — and if GitHub cannot
read it, neither can the tools that count what we publish. For CC BY 4.0, take the text from
[creativecommons.org](https://creativecommons.org/licenses/by/4.0/legalcode.txt).

Then check three things agree: the `LICENSE` file, the README, and the `license:` field in
[`CITATION.cff`](https://citation-file-format.github.io/) if the repository has one. A
`CITATION.cff` declaring a licence the repository does not carry is how the current mess
started.

## Licensing and citation are one question

From a user's side, "may I use this?" and "how do I credit it?" are the same conversation. The
licence grants the permission; the [citation](how-we-work.md) machinery makes the credit
possible. Neither works alone — a permissively licensed repository with no `CITATION.cff` gets
used and never cited, which is precisely the invisibility this project exists to argue
against.

## If something here is wrong

Open an issue. Corrections to licensing are as welcome as corrections to science, and the edit
history is public either way.
