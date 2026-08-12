# Review logs

Dated, structured reviews of the GAIA website and book, filed by the ten review personas in
[`.claude/gaia-review-personas/`](../.claude/gaia-review-personas/).

Each round lives in its own dated directory, one file per persona, all against the shared
rubric — eight dimensions, a four-level severity scale, and a fixed report shape. Reviews are
run independently: no persona sees another's findings before filing, because convergence
between a donor and a CTO is only informative if neither was coordinated with the other.

| Round | Personas | Synthesis |
|---|---|---|
| [2026-08-12](2026-08-12/) | 10 | [`_synthesis.md`](2026-08-12/_synthesis.md) |

## What these are, and are not

**These are simulations.** Each persona is constructed from the project's funding context and
from what people in these roles typically need. A finding is a hypothesis about a real reader,
not evidence about one. They are a cheap filter to run before asking real people for their
time — not a substitute for asking them.

Reviews are dated because sites change. A finding here describes the site on the day it was
filed, and says nothing about the site today. Do not edit a filed review to reflect a fix;
file the next round instead.

## Running a round

Each persona is available as a Claude subagent, generated from the same spec as the personas
themselves:

```bash
cd .claude && python3 gaia-review-personas/build.py   # regenerates personas/ and agents/
```

Then invoke `gaia-review-<persona-slug>` for each of the ten, and merge the results with
[`shared/synthesis.md`](../.claude/gaia-review-personas/shared/synthesis.md). Agent definitions
are discovered when a session starts, so a freshly generated agent needs a new session.

## Reading a round

Read the synthesis first, then the individual reviews for the personas whose sector you care
about. The synthesis deliberately preserves disagreements rather than averaging them: where the
program officer found a page too technical and the research software engineer found the same
page too vague, that tension is a decision about audience, not a defect to split the difference
on.

Do not read the ten weighted scores as an average. A project scoring well with academia and
poorly with industry has a positioning problem, not a quality problem, and the spread is what
tells you so.
