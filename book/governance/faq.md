---
title: FAQ
description: Common questions about joining GAIA, using its software, citing the awards, and finding what was decided and why.
---

## Taking part

**How do I get my tool listed?**
Open a pull request against the index adding one line: name, link, one sentence on what it
does, and a category. That is level 0 on the [participation ladder](./organization.md), and
it needs nobody's permission. A good entry says what the tool is *for* rather than what it
is built with, and points at a repository that has seen a commit in the last two years.

**What does level 2 actually commit GAIA to?**
That a template repository demonstrating a complete workflow with your tool exists and keeps
passing its tests in CI. It does not commit us to maintaining your software, fixing your
bugs, or shipping your releases. Each level is a maintenance promise by us, which is why
levels are agreed rather than assumed.

**Can I use your container images?**
Yes. They are permissively licensed and public. If an image is behind on a dependency or a
base-image security update, open an issue — that is the failure mode we most want reported.

**Do you accept pull requests from outside the project?**
Yes, on any public repository. Repositories tagged `gaia-incubating` change shape without
warning, so check the tag before building something on top.

**I am at a different institution and not funded by GAIA. Can I join the meetings?**
The monthly project-wide update is open, and unsupported collaborators are welcome on Slack
and in the thematic channels. The PI coordination call and anything touching personnel or
budget are not open.

## Citing and acknowledging

**How do I acknowledge GAIA?**
Use the wording on the [charter page](./how-we-work.md) verbatim, citing all three award numbers
regardless of your institution. These are linked collaborative awards, not a prime with
subawards.

**Do I cite the software as well?**
Yes. If a GAIA tool or dataset materially shaped your result, cite its DOI. Every repository
ships a `CITATION.cff`. This is not a courtesy — infrastructure work is chronically invisible
in the citation record, and a project of this kind should not reproduce that.

**Should I offer co-authorship?**
If someone's software or data changed your result rather than merely supporting it, offer.
The authorship policy is a numbered decision; see the
[decisions register](./decisions.md).

## How the project runs

**Who decides what goes into the organisation?**
Levels 0–3 are handled by the relevant thrust lead through the normal pull-request process.
Level 4 — moving a repository into the organisation — requires a named maintainer and a
numbered decision, because it is a long-term maintenance commitment.

**Where do I find what was decided, and why?**
The [decisions register](./decisions.md). Every entry carries its reasoning and the
alternatives that were rejected. If something is not there, it was not decided — it is still
a proposal.

**Are meetings recorded?**
Working meetings are recorded to a private repository for notes only, never published raw.
Personnel and budget discussions are not recorded at all. The monthly public seminar is
recorded, opt-in per speaker. The reasoning is on the [charter page](./how-we-work.md).

**Why is the dashboard showing numbers below target?**
Because hiding them would make the rest of the dashboard worthless. Figures below target stay
visible, and the escalation path for each is written down.

**Is my Slack message going to end up on a public page?**
Only as part of a weekly summary attributed by role, never verbatim and never by name, and
only from an allowlisted set of channels. React `:offrecord:` and the message is removed
before anything reads it — on a thread parent, that removes the whole thread. No explanation
is asked for.

## Documents and tooling

**Why are some documents in Google Docs and others here?**
Documents in Google Docs are open for comment and still changing. Once a decision is
ratified, the version in this book becomes canonical and the Doc is frozen with a pointer.
One source per document; nothing is maintained in two places.

**Can I get these pages as Word documents?**
Yes, and they are generated rather than maintained by hand — a branded reference template and
a Markdown preprocessor live in
[`tools/docx/`](https://github.com/gaia-hazlab/gaia-hazlab.github.io/tree/main/tools/docx).
Generated `.docx` files are deliberately not committed to the repository: they are derivable,
they are binaries, and they would churn on every edit.

**Something here is wrong or out of date.**
Open an issue. Corrections to governance are as welcome as corrections to science, and the
edit history is public either way.
