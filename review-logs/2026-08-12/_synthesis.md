# Synthesis — ten persona reviews, 2026-08-12

**Reviewed:** the live site at `gaia-hazlab.github.io`, the book, and the `gaia-hazlab` GitHub
organisation · **Reviewers:** ten simulated personas, run independently, none shown another's
findings · **Total findings:** 129, of which 13 blockers

These are simulations. A finding here is a hypothesis about a real reader, not evidence about
one. Where a finding is a checkable fact, it has been verified against the live site or the
GitHub API and is marked **[verified]**; the rest are the personas' judgement.

## The one-line result

The writing is well ahead of the artefacts, and every reviewer who tried to *verify* something
rather than *read* something scored the project lower for it.

That is the whole pattern, and it shows up in the scores rather than in any single finding.

## Scores — spread, not average

| Persona | Sector | Total | Blockers |
|---|---|---:|---:|
| Foundation program officer | Philanthropy | 66 | 1 |
| Faculty panel reviewer | Academia | 65 | 2 |
| Prospective PhD student | Academia | 62 | 0 |
| Foundation science advisor | Philanthropy | 61 | 0 |
| Energy resilience CEO | Industry | 60 | 2 |
| Climate risk CTO | Industry | 59 | 3 |
| Impact evaluation officer | Philanthropy | 57 | 1 |
| National lab scientist | Academia | 56 | 2 |
| Research software engineer | Academia | 50 | 1 |
| Geospatial AI CTO | Industry | 49 | 1 |

Do not average these. The interesting structure is that the ranking tracks **how much of each
persona's weight sits on D5 (reproducibility) and D6 (governance)** almost perfectly. The two
lowest scores belong to the two reviewers who came to check whether something could be used;
the highest belongs to the one who came to read. The prose is doing its job. What the prose
describes cannot yet be picked up and carried away.

This is not a philanthropy-versus-industry positioning problem. It is a single problem —
artefacts lagging claims — that different readers meet at different depths.

## 1. Convergent findings

Ordered by how many independent personas raised them, and by how far apart those personas sit.

### C1. Repositories carry no licence, while the site says they do — 8 of 10 personas [verified]

Raised by both CTOs, the RSE, the national-lab scientist, the PhD student, the faculty
reviewer, the science advisor, and the evaluation officer. This is the strongest signal the
method produced: it converged from philanthropy, academia and industry at once.

Verified against the GitHub API on 2026-08-12: **9 of 26 public repositories carry no LICENSE
file; 14 of 33 including private.** The two counts in the individual reviews (eight, eleven,
fourteen) differ only in scope — the RSE counted repos he would actually adopt, the evaluation
officer counted public ones, the CTO counted the whole org. All three are right.

What makes this a blocker rather than a chore is the contradiction: several READMEs and the
site footer assert MIT while the repository has no LICENSE file. The climate-risk CTO's answer
to his own signature question was that his legal team could not clear this today, and that
roughly a week of file-writing would flip that answer.

Unlicensed and public: `.github`, `awesome-gaia`, `da-seis-groundfailure`,
`gaia-data-downloaders`, `gaia-translate-QA`, `landlab-debrisflow`, `mt-rainier-smart-sensing`,
`seis-hydro-2-sed`, `shred-landlab-prototypes`.

### C2. Present-tense claims about things that do not exist — 8 of 10 personas

ModelHub "holds pre-trained weights"; HazEvalHub "holds the metrics, the validation protocols,
and the held-out data"; both document a `gaia_hazlab` Python API that is not on PyPI and not in
the organisation. The faculty reviewer named a HazEvalHub sentence as the one that would be
embarrassing in three years, and it is a sentence I rewrote yesterday — the plain-voice pass
improved the register while leaving the tense claim intact.

The site's own banner already says "code examples are non-functional placeholders", which the
national-lab scientist and the RSE both read as undermining the pages they would otherwise
trust most. A banner is not a substitute for tense.

### C3. No baseline and no performance number anywhere — 5 of 10 personas

The CEO could not find a single figure and stopped. The faculty reviewer could not construct a
novelty paragraph. Both CTOs asked for a trivial baseline and found none. The evaluation
officer found that not one of thirteen committed targets has a baseline value.

The CEO's signature answer is the sharpest statement of the cost: the sentence he would forward
to his VP of engineering has a hole where the number goes, so the forward does not happen.

### C4. The metrics dashboard the governance pages rest on does not exist — 5 personas [verified]

`https://gaia-hazlab.github.io/metrics-observatory/` returns **404**, and it is linked from the
book's own table of contents ([`myst.yml:65`](../../myst.yml)). `/dashboard.html` resolves but
publishes no metric value. The evaluation officer made this her blocker: the governance pages
promise public accountability against thirteen metrics, and no metric value is published
anywhere on the site.

### C5. The people page shows no people — 5 personas [verified]

Two personas made this a blocker independently, from opposite ends: the program officer
("a team page without faces reads as an org chart") and the energy CEO. Verified: `people.html`
returns 1,005 characters of visible text with JavaScript disabled and contains no personal
name at all — the roster is injected client-side. The PhD student, who came specifically to
find a student to email, could not find one and said that alone would stop him converting.

### C6. Nothing in the decisions register is decided — 7 personas [verified]

Every decision reads "proposed"; two carry the unfilled placeholder `2026-08-__`. The
governance structure is repeatedly praised as unusually good and then discounted because it has
never been exercised. The evaluation officer put it most precisely: the escalation ladder has
never been climbed.

### C7. The FAQ states something that is false — 3 personas [verified]

[`faq.md:42`](../../book/governance/faq.md) claims every repository ships a `CITATION.cff`.
**Two of 33 do** (`seis-hydro-2-sed`, `geocroissant-hazards`). The climate-risk CTO noted that
this was the one claim he chose to check, which is the worst possible claim to get wrong — it
converts a documentation gap into a credibility problem.

### C8. No releases, no versions, no DOIs — 3 personas

Adoption means pinning a commit hash forever. The national-lab scientist made this a blocker
for a different reason: with data products served off `refs/heads/main` and no tags, there is no
way to cite a version of a dataset, and his signature answer to "what would remain, and who
would hold it" was "some files, and nobody."

### C9. The best documents are unreachable from the site — 3 personas

The DataHub Integration Guide, `pillar-1-soil-reanalysis`, and `modelhub-landslide` were each
praised by the reviewer who found them and named as unreachable by another. The RSE called the
integration guide the best document in the project for him and could not get to it from the
site; the climate-risk CTO ran out of patience before finding it. The science advisor's version
is the most damaging: **the only pages that state technical risk are invisible from the front
door**, so the project's strongest evidence of seriousness never reaches a funder.

### C10. Undefined vocabulary — 5 personas

"Digital twin" (unglossed on the landing page, six of the program officer's thirteen
untranslatable sentences), "agentic", "thrust", "cyberinfrastructure", "reanalysis". The
program officer counted thirteen sentences she would have to translate for a trustee.

### C11. The landing-page counters — 4 personas

"∞ Sensors" [verified] drew a finding from four reviewers, ranging from polish to a credibility
note. The evaluation officer's objection is the substantive one: the counters are undefined,
unrelated to the thirteen committed metrics, and one of them is not a number.

## 2. Divergences, kept divergent

These are not noise to be averaged. Each is a decision about audience that belongs in the
decisions register.

### D1. What is the front page for?

- **Program officer:** too technical, no people, nobody harmed in the story. Wants a first
  screen naming who is hurt and what changes.
- **RSE:** "the website is marketing until proven otherwise" — went straight to the repos and
  judged from there.
- **Science advisor:** the front page hides the good stuff. The risk-stating chapters are the
  strongest asset and cannot be reached from it.
- **Faculty reviewer:** wants prior art and a falsifiable claim, neither of which is a front-page
  element in most projects.

Four readers, four different front pages. This cannot be resolved by adding all four, and
adding all four is the default failure mode. **Decide who the front page is for and let the
other three navigate.**

### D2. Is the benchmark an asset or a liability?

The geospatial AI CTO — the persona most qualified to judge — made the FrugalMind board his
blocker: the published leaderboard may not be the held-out evaluation, its own data file says
so, and the scorer is in a 404 repository. The faculty reviewer independently named the same
prototype's unreachable source as a major finding.

But the science advisor and the evaluation officer both treated the existence of a working
evaluation board as among the project's best evidence. Both readings are correct: it is the
most advanced thing on the site *and* the least defensible as published. Publishing the scorer
converts it from a liability to the strongest asset the project has.

### D3. How much does the empty scaffolding cost?

The PhD student filed **zero blockers** and still would not convert, because his objection is
about the future rather than the present. The two CTOs filed four blockers between them about
the present. A project can be a good bet and an unusable artefact at the same time, and these
reviewers disagree about which fact governs.

## 3. Blocker table

| # | Blocker | Persona | Dim |
|---|---|---|---|
| 1 | Repositories I would use have no LICENSE file | Climate risk CTO | D6 |
| 2 | Repositories I would use have no LICENSE file | RSE | D6 |
| 3 | Data provenance and redistribution terms not stated | Climate risk CTO | D6 |
| 4 | No model performance against a baseline anywhere | Climate risk CTO | D5 |
| 5 | No performance number anywhere on the site | Energy CEO | D2 |
| 6 | No published metric value exists on the site | Impact evaluation officer | D2 |
| 7 | The team page has no team on it | Program officer | D1 |
| 8 | The People page names no people | Energy CEO | D1 |
| 9 | No acknowledgement of any adjacent effort | Faculty reviewer | D2 |
| 10 | HazEvalHub described as holding what it does not hold | Faculty reviewer | D2 |
| 11 | Leaderboard may not be the held-out evaluation | Geospatial AI CTO | D5 |
| 12 | No plan for what happens after the award | National lab scientist | D7 |
| 13 | No versioning story for data products | National lab scientist | D5 |

Concentrated in **D2 (credibility, 5)**, **D6 (governance, 3)** and **D5 (reproducibility, 3)**.
Not one blocker concerns design, writing quality, or navigation. The prose is not the problem.

## 4. The cheap wins

Each appears in several reviews and takes under an hour.

| Fix | Raised by | Effort |
|---|---|---|
| Correct the `CITATION.cff` sentence in the FAQ, or ship the files | 3 | 10 min |
| Fill the two `2026-08-__` placeholder dates in the decisions register | 4 | 10 min |
| Replace "∞ Sensors" with a real count or drop the counter row | 4 | 10 min |
| Add `LICENSE` to the 9 unlicensed public repositories | 8 | ~1 hour |
| Gloss "digital twin" in one sentence on the landing page | 5 | 15 min |
| Fix the 404 favicon typo and the 404 team photo | 2 | 10 min |
| Link the DataHub Integration Guide from the DataHub page's top | 3 | 5 min |
| Name one contactable person who is not a PI | 3 | 15 min |
| Un-404 `/metrics-observatory/` or remove it from the ToC | 5 | 15 min |

Roughly two hours of work clears items raised in twenty-nine findings. None requires a decision.

## 5. What nobody mentioned

Read against the surface list in `shared/method.md`:

- **The hazard chapters** (`hazard-landslides`, `hazard-floods`, `hazard-liquefaction`,
  `hazard-postfire-debris-flows`) drew no findings from any persona. They are draft scaffolds,
  and no reviewer's path reached them. Either they are not yet load-bearing, or they are badly
  linked.
- **`ocean-atmosphere-coupling`** — the strongest prose in the book by my own reading — was
  opened by nobody. It is not in any persona's check list and not reachable from the front page.
- **`/presentations.html`** drew one finding, that it is thin and half-unattributed.
- **The science pillars beyond Pillar 1** went unvisited. Pillar 2 and Pillar 3 appeared in no
  review.

A page nobody opened is either badly linked or unnecessary. Given C9, badly linked is the
likelier reading here, and the same fix serves both.

## 6. What the reviewers praised

Worth protecting, because a remediation plan tends to sand off the good with the bad.

- The **governance writing** — `how-we-work`, `decisions`, `licensing` — was praised by the
  reviewers most hostile to everything else. The national-lab scientist, the RSE and the
  evaluation officer all said the structure is better than comparable projects. Its only defect
  is that it has never been exercised.
- **`pillar-1-soil-reanalysis` and `modelhub-landslide`** were called the project's strongest
  evidence by the science advisor, specifically because they state their own technical risk.
- The **FrugalMind board** is the most advanced artefact on the site and the closest thing to a
  citable result, subject to D2 above.
- The **honesty of the draft admonitions** was noticed favourably by three reviewers, even by
  those who then objected to the present-tense prose elsewhere. The scaffolding is labelled;
  the claims around it are not.
