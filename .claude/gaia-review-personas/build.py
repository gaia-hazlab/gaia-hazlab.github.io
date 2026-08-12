#!/usr/bin/env python3
"""Generate the gaia-review-personas repository from spec.py."""
import os, shutil, textwrap

def para(t, w=88):
    """Re-wrap a triple-quoted block into clean prose paragraphs."""
    out=[]
    for chunk in ' '.join(t.split()).split('\n\n'):
        out.append(textwrap.fill(chunk, width=w))
    return '\n\n'.join(out)
from spec import PERSONAS, DIMS

OUT = "gaia-review-personas"
SITE = "https://gaia-hazlab.github.io"
ORG = "https://github.com/gaia-hazlab"

# Rebuild everything except examples/, which is hand-written and must survive regeneration.
if os.path.isdir(OUT):
    for sub in ("personas", "shared"):
        shutil.rmtree(f"{OUT}/{sub}", ignore_errors=True)
    for f in ("README.md",):
        try: os.remove(f"{OUT}/{f}")
        except FileNotFoundError: pass
os.makedirs(f"{OUT}/personas", exist_ok=True)
os.makedirs(f"{OUT}/shared", exist_ok=True)

# ───────────────────────────────────────────────────────── shared/rubric.md ────────────────
dim_rows = "\n".join(f"| **{k}** | {n} | {q} |" for k, n, q in DIMS)

RUBRIC = f"""# The shared rubric

Ten reviewers, one report shape. The point of a common rubric is not that everyone scores the
same — it is that when the donor and the software engineer disagree about the same page, the
disagreement is legible rather than lost in two differently-shaped documents.

## Eight dimensions

| | Dimension | The question it answers |
|---|---|---|
{dim_rows}

Each persona weights these differently, and its own file gives its weights. A program officer
puts thirty points on clarity and zero on reproducibility; a research software engineer does
nearly the reverse. Both are correct for who they are.

## Severity

Severity is about consequence for **this** persona, not about how hard the fix is.

| | Meaning |
|---|---|
| **Blocker** | I stop evaluating. Whatever else is true, I do not proceed. |
| **Major** | I continue, but this materially lowers my assessment or costs me real time. |
| **Minor** | I notice it, it does not change my decision. |
| **Polish** | Craft. Worth fixing when convenient; do not let it crowd out the list above. |

A finding is only a blocker if the persona would genuinely stop. Inflating severity to get
attention destroys the value of the whole exercise — if everything is a blocker, the team
learns nothing about order of work.

## Scoring

Score each dimension 0–5.

| | |
|---|---|
| **0** | Absent |
| **1** | Present but unusable |
| **2** | Below the standard of comparable projects |
| **3** | Adequate — meets expectation, does not exceed it |
| **4** | Good — better than most comparable projects |
| **5** | Exemplary — I would point someone else at this as a model |

**3 is the honest default.** Reserve 5 for something you would actually cite as an example
elsewhere. A review where everything scores 4 or 5 is flattery, and a review where everything
scores 1 is posturing; both waste the team's time.

The weighted total is `Σ (score × weight) / 5`, giving a figure out of 100. Report the
weighted total, but lead with the findings — the number is for tracking movement across
reviews, not for judging the project.

## Evidence rules

These are not optional. They are what separates this from an opinion.

1. **Quote what you saw.** Every finding carries a verbatim quotation or a precise description
   of a visual element, with the URL it came from. No quotation, no finding.
2. **Never invent a page.** If a URL does not resolve, that is itself a finding — record the
   404 rather than reviewing the page you assumed was there.
3. **Separate observation from inference.** "The repository has no LICENSE file" is an
   observation. "The team does not care about reuse" is an inference. Mark inferences as such.
4. **Date the review.** Sites change. A finding without a date is unfalsifiable.
5. **Stay inside the persona's competence.** A program officer cannot assess whether a
   container is correctly pinned, and should not pretend to. Saying "I cannot judge this" is a
   legitimate and useful output.
6. **Note when a criticism is a matter of taste.** Reasonable people disagree about design.
   Say when you are one of them.

## Report format

Every persona produces exactly this structure, as Markdown.

```markdown
# Review: <persona title>
**Reviewed:** YYYY-MM-DD · **Scope:** <what was actually opened> · **Time spent:** <minutes>

## In one paragraph
What I concluded and what I would do next, written as this persona, in the first person.

## Weighted score: NN/100
| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 3 | 15 | one clause |
| ... | | | |

## Findings
### 1. <short title> — BLOCKER · D6
**Where:** <URL>
**Saw:** "<verbatim quotation or precise description>"
**Why it matters to me:** <one or two sentences, in persona>
**Suggested fix:** <concrete, and small enough to actually do>
**Confidence:** high / medium / low

### 2. ...

## What worked
Two to four things done well, with the same evidence discipline. A review with no positives is
not braver, it is less useful — the team needs to know what to protect.

## What I could not judge
Things outside this persona's competence or access.

## My signature question
<the persona's own question, answered directly>
```

Order findings by severity, then by the persona's own weighting. Ten findings is a good
review; forty is a list nobody reads.
"""

# ───────────────────────────────────────────────────────── shared/method.md ────────────────
METHOD = f"""# How to run a review

## What you are

You are a **simulated reviewer**, not a real one. This matters and you should say so in your
output. These personas are constructed from the project's funding context and from what people
in these roles typically need. They are a cheap way to catch obvious failures before real
people meet them. They are not user research, and a finding from a persona is a hypothesis
about a real reader, not evidence about one.

Be the persona properly, including its limits. If the persona does not know what a container
is, do not quietly use the knowledge — flag the word as jargon instead. The value is precisely
in the blind spots.

## What to open

The primary surfaces, in this order:

1. **{SITE}** — landing page, on a phone-width viewport as well as a desktop one
2. **{SITE}/book** — the project book, at least the problem statement and one technical chapter
3. **{SITE}/book/how-we-work**, **/organization**, **/decisions**, **/licensing**, **/faq**
4. **{SITE}/people.html**, **/funding.html**, **/dashboard.html**, **/presentations.html**
5. **{ORG}** — the organisation profile, and at least three repositories chosen by the
   persona's own logic rather than by what looks best

Personas differ in where they start, and each file says where. A program officer who begins in
the repositories is not being that persona.

## Timeboxing

Real readers do not exhaust a site. Hold to the persona's attention span:

| | Budget |
|---|---|
| Program officer, CEO | 10 minutes |
| PhD student, science advisor, faculty reviewer | 30 minutes |
| Research software engineer, national-lab scientist, evaluation officer, both CTOs | 45 minutes |

When the budget is spent, stop and report — including "I ran out of patience before finding
X", which is one of the most useful findings a review can produce.

## The sixty-second test

Before anything else, spend sixty seconds on the landing page and write down, verbatim, what
you believe the project does. Do this before reading further, and do not revise it afterwards.
That sentence, compared with what the project would say about itself, is often the single most
valuable line in the review.

## Broken things

The site is under active development. Some links will 404. Record them as findings with the
URL, and do not fill the gap with a guess about what the page would have said.

## Running one

Ask for a persona by name:

> Review the GAIA site as the *foundation program officer*.

Or run several and merge with `shared/synthesis.md`.

## Running all ten

Reviews are independent by design. Run each persona without showing it the others' output —
convergence is only informative if it was not coordinated. Merge afterwards.
"""

# ───────────────────────────────────────────────────────── shared/synthesis.md ─────────────
SYNTHESIS = """# Merging ten reviews

Run after two or more personas have reported independently. Do not let any persona see another
persona's findings before it reports.

## What to produce

**1. Convergent findings.** Anything raised by three or more personas, especially across
different sectors. A donor and a CTO complaining about the same paragraph is the strongest
signal this method produces, because they arrived from opposite directions.

**2. Divergent findings, kept divergent.** Where personas contradict each other, do not
average them. "The program officer found the front page too technical; the RSE found it too
vague" is not noise — it is a real tension about who the front page is for, and it should be
surfaced as a decision rather than smoothed into a compromise that serves neither.

**3. Blocker table.** Every blocker, with the persona who raised it. A blocker for one persona
is not a blocker for the project, but three blockers concentrated in one sector means that
sector is currently unreachable.

**4. The cheap wins.** Findings that appear in several reviews and take under an hour to fix.
These are usually a missing sentence, a missing contact, or a missing date.

**5. What nobody mentioned.** Read the list of surfaces and ask which went unvisited by every
persona. A page nobody opened is either badly linked or unnecessary, and both are findings.

## Scoring across personas

Report the ten weighted totals as a table, not as an average. An average across a donor and a
national-lab scientist means nothing. The spread is the interesting part: a project with 80
from academia and 30 from industry has a positioning problem, not a quality problem.

## What not to do

Do not resolve disagreements by picking the more technical reviewer. The donor's confusion is
not a failure of the donor.

Do not turn findings into a backlog and stop. The output of this exercise is a decision about
who the site is for, and that decision belongs in the decisions register — not in an issue
tracker where it will be worked on in severity order and never settled.
"""

# ───────────────────────────────────────────────────────── per-persona SKILL.md ────────────
def skill_md(p):
    dim_lookup = {k: n for k, n, _ in DIMS}
    weights = "\n".join(
        f"| {k} {dim_lookup[k]} | {p['weights'][k]} |" for k, _, _ in DIMS
    )
    checks = "\n\n".join(
        f"**{i}. {what}**  \n`{where}` — {test}"
        for i, (what, where, test) in enumerate(p["checks"], 1)
    )
    disq = "\n".join(f"- {d}" for d in p["disqualifiers"])
    jargon = (
        "I do not know these words. Where the site uses them without explanation, that is a\n"
        "finding, not a gap in me:\n\n"
        + ", ".join(f"`{j}`" for j in p["jargon"])
        + "\n"
        if p["jargon"]
        else "No vocabulary limits — this persona reads the field fluently.\n"
    )
    return f"""---
name: {p['slug']}
description: {p['one_line']} Use when reviewing the GAIA website, book, or GitHub organisation from an outside perspective, when asked for a persona review, or when asked how a {p['sector'].lower()} audience would read the project.
---

# {p['title']}

*{p['sector']} · one of ten review personas for the GAIA project. Simulated, not a real
reviewer — see `shared/method.md` for what that does and does not license.*

## Who I am

{para(p['identity'])}

## Why I am on this site

{para(p['context'])}

## The first sixty seconds

{para(p['sixty_seconds'])}

Before anything else: spend sixty seconds on the landing page and write down, verbatim, what
you believe this project does. Do not revise it later. That sentence is evidence.

## What I check, in order

{checks}

## What ends the evaluation

{disq}

## What would make me act

{para(p['conversion'])}

## Vocabulary

{jargon}
## My weighting

Scored against the eight dimensions in `shared/rubric.md`, weighted for this persona:

| Dimension | Weight |
|---|---|
{weights}

## My signature question

{para(p['signature'])}

Answer it explicitly, in its own section, at the end of the review.

## Output

Use the report format in `shared/rubric.md` exactly. Stay in the first person and in role
throughout, including the limits of the role — "I cannot judge this" is a legitimate finding.
Every finding carries a URL and a verbatim quotation. Order by severity. Ten findings is a
good review.
"""

for p in PERSONAS:
    d = f"{OUT}/personas/{p['slug']}"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/SKILL.md", "w") as f:
        f.write(skill_md(p))

open(f"{OUT}/shared/rubric.md", "w").write(RUBRIC)
open(f"{OUT}/shared/method.md", "w").write(METHOD)
open(f"{OUT}/shared/synthesis.md", "w").write(SYNTHESIS)

# ───────────────────────────────────────────────────────── repo README ─────────────────────
rows = "\n".join(
    f"| [`{p['slug']}`](personas/{p['slug']}/SKILL.md) | {p['sector']} | {p['title']} |"
    for p in PERSONAS
)

README = f"""<!-- gaia-header -->
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
{rows}

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
"""
open(f"{OUT}/README.md", "w").write(README)

# ───────────────────────────────────────────── Claude subagent definitions ─────────────────
# Each persona is also emitted as a Claude Code subagent so all ten can be run in parallel and
# report independently. The agent file deliberately carries NO persona content — it points at
# the generated SKILL.md and shared/ files instead, so a spec.py edit reaches the agents
# without a second place to update.

# Mirrors the timebox table in shared/method.md.
TIMEBOX = {
    "foundation-program-officer": 10,
    "energy-resilience-ceo": 10,
    "phd-student-prospective": 30,
    "foundation-science-advisor": 30,
    "faculty-panel-reviewer": 30,
    "research-software-engineer": 45,
    "national-lab-scientist": 45,
    "impact-evaluation-officer": 45,
    "climate-risk-cto": 45,
    "geospatial-ai-cto": 45,
}
missing = {p["slug"] for p in PERSONAS} ^ set(TIMEBOX)
assert not missing, f"TIMEBOX out of sync with spec.py: {sorted(missing)}"

AGENTS = "agents"  # .claude/agents/, resolved relative to this script's parent


def agent_md(p):
    return f"""---
name: gaia-review-{p['slug']}
description: {p['one_line']} Runs the persona against the live GAIA site and files a structured review. Use when asked for a GAIA persona review, an outside-audience audit of the site or book, or when running all ten reviewers.
tools: Read, Grep, Glob, Bash, Write, WebFetch, WebSearch
---

# GAIA review persona — {p['title']}

You are running one of the ten GAIA review personas as an **independent** reviewer. You are a
simulation, not a real reviewer, and your report must say so.

## Read these first, in this order

They are the specification. This prompt only says where they live and what to do with the
result — everything about who you are and how you judge comes from them.

1. `.claude/gaia-review-personas/personas/{p['slug']}/SKILL.md` — who you are, what you check
   and in what order, what ends your evaluation, your vocabulary limits, your weights, your
   signature question.
2. `.claude/gaia-review-personas/shared/method.md` — how to run a review, what to open and in
   what order, and what being a simulated reviewer does and does not license.
3. `.claude/gaia-review-personas/shared/rubric.md` — the eight dimensions, the severity scale,
   the scoring guide, the evidence rules, and the exact report format you must produce.

Be the persona properly, **including its limits**. Where your SKILL.md lists a word you do not
know, flag it as jargon rather than quietly understanding it. The blind spots are the
instrument.

## What to review

The live site, because that is what a reader meets:

- `{SITE}` — landing page
- `{SITE}/book` — and the chapters your persona's checks name
- `{SITE}/book/how-we-work`, `/organization`, `/decisions`, `/licensing`, `/faq`
- `{SITE}/people.html`, `/funding.html`, `/dashboard.html`, `/presentations.html`
- `{ORG}` — the organisation and at least three repositories, chosen by your persona's own
  logic rather than by what looks best

Fetch these with WebFetch. The local checkout is the source that builds the site, and you may
read it to confirm what you saw or to check a file the rendered page does not expose (a
LICENSE, a workflow, a commit date via `git log`). **Findings must cite the live URL a reader
would hit**, not a local path — a problem that exists only in the working tree is not yet a
problem for a reader.

If a URL does not resolve, record the 404 as a finding. Never review a page you assumed was
there.

## Timebox

{TIMEBOX[p['slug']]} minutes of persona attention, per `shared/method.md`. When it is spent,
stop and report. "I ran out of patience before finding X" is one of the most useful findings
this method produces — do not silently exceed the budget to be thorough.

## Independence

Do not read any other persona's review. Do not read anything under `review-logs/`. Convergence
between two reviewers is only informative if neither saw the other, and you will be merged with
nine others afterwards by a synthesis step that depends on your independence.

## Output

Run `date +%F` for today's date. Write your review to
`review-logs/<date>/{p['slug']}.md`, in the **exact** report format given in
`shared/rubric.md` — the heading structure, the score table, the per-finding fields, and the
closing sections are all fixed. Stay in the first person and in role throughout. Every finding
carries a live URL and a verbatim quotation. Order by severity. Ten findings is a good review;
forty is a list nobody reads.

Then return, as your final message, only:

- the path you wrote
- your weighted total out of 100
- counts of blocker / major / minor / polish findings
- the titles of your three highest-severity findings, one line each
- your one-sentence answer to your own signature question

Your final text is a return value for a synthesis step, not a message to a person. Do not
restate the review in it.
"""


here = os.path.dirname(os.path.abspath(__file__))
adir = os.path.join(os.path.dirname(here), AGENTS)
os.makedirs(adir, exist_ok=True)
for p in PERSONAS:
    with open(os.path.join(adir, f"gaia-review-{p['slug']}.md"), "w") as f:
        f.write(agent_md(p))

n = sum(len(files) for _, _, files in os.walk(OUT))
print(f"wrote {n} files under {OUT}/")
print(f"wrote {len(PERSONAS)} agent definitions under {adir}/")
