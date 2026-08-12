# HazEvalHub — Common Task Framework and leaderboard

> **Execution plan for making HazEvalHub exist.** The taxonomy, metric families and CTF phasing
> live in [03-ai-tools-and-evals.md §3](03-ai-tools-and-evals.md) and are not restated here.
> This document covers what that one does not: the benchmark-integrity rules the leaderboard has
> to satisfy to be worth citing, and the two concrete seed tasks that get us from nothing to a
> defensible v0.5.
>
> Opened in response to the two HazEvalHub blockers in the 2026-08-12 review round
> ([synthesis](../review-logs/2026-08-12/_synthesis.md) C2, D2).

## 1. Why this is urgent rather than merely planned

HazEvalHub is the largest gap between what the site says and what exists.

The book states it "holds the metrics, the validation protocols, and the held-out data that
decide whether a prediction is good enough to act on". There is **no `hazevalhub` repository in
the organisation**. The faculty panel reviewer named that exact sentence as the one that would be
embarrassing in three years. Separately, the geospatial AI CTO — the persona best qualified to
judge a benchmark — made the existing FrugalMind board his blocker, because its own data file
cannot distinguish a hidden-set result from a smoke test, and its scorer sits in a repository
that 404s.

Both reviewers reached the same place from opposite directions: **an evaluation you cannot audit
is worth less than no evaluation at all**, because it spends credibility instead of building it.

The corollary is the good news. The geospatial CTO's answer to "would a result on this benchmark
be worth citing?" was *not today*, and the single change he named — publish the scorer and task
specs, stamp every row with the split that produced it — is a fortnight of work, not a year.

## 2. The standard we are holding ourselves to

Borrowed from the NeurIPS and ICML **Datasets and Benchmarks** track, whose reviewers ask
precisely the questions our CTO persona asked, plus the Common Task Framework discipline that
[03](03-ai-tools-and-evals.md) already commits us to.

A benchmark is citable when all nine hold. Each maps to a finding from the review round.

| # | Rule | Why — and who raised it |
|---|---|---|
| R1 | **The task is fully specified before submissions open** — inputs, outputs, metric, split, and what counts as a valid entry | Prevents the metric being chosen after the results are in |
| R2 | **The test set is hidden and never released**, and the leaderboard says so on every row | The board "may not be the held-out evaluation, and its own data file says so" — CTO blocker |
| R3 | **The scorer is public, deterministic and versioned** | "The scoring code is not public, so the anti-gaming claim cannot be checked" |
| R4 | **A trivial baseline is published first** — majority class, persistence, climatology | "No trivial baseline appears anywhere on the site." Without one, no number means anything |
| R5 | **A strong published baseline is published alongside it** | Gives the skill number a ceiling as well as a floor |
| R6 | **Contamination is addressed explicitly**, in writing, per task | "Pretraining contamination is never mentioned" — see §3.2, where it is our sharpest risk |
| R7 | **Splits are DOI-archived** with a datasheet describing provenance, labelling protocol and known biases | Makes the benchmark reproducible after the award |
| R8 | **The evaluation is separable from the group whose models it scores** | "The benchmark is not separable from the group whose models it scores" |
| R9 | **Every row carries model version, split, date, and cost** | Frugality is a first-class axis per [03 §3.0](03-ai-tools-and-evals.md); the rest is auditability |

### 2.1 R8 is the one we will be tempted to skip

GAIA builds the models and runs the leaderboard. That is normal for a new benchmark and fatal if
left unaddressed. The mitigations, in increasing order of cost:

1. **Declare it.** A conflict-of-interest note on the board, naming which entries are GAIA's.
2. **Separate the roles.** The person who holds the hidden labels is not the person who trains
   the submitted model. With Akash on QuakeXNet, that means someone else holds the test labels.
3. **Invite an external entry before publishing any GAIA result.** AI2 and the Kutz group are
   already named collaborators in [03 §3](03-ai-tools-and-evals.md); one external submission on
   the board at launch is worth more than three internal ones.
4. **Hand custody of the test set to a third party.** The eventual Kaggle-style hosting does this
   structurally; not required for v0.5.

For v0.5, do 1 and 2. Do 3 if the timing allows.

## 3. Seed task A — QuakeXNet multi-class event classification

The first hazard task, and the one with a real result behind it: the QuakeXNet-v3 detector and
the 15-year Mt. Rainier surface-event catalog with Akash Kharita.

### 3.1 The task

Multi-class classification of seismic events (earthquake / surface event / noise / explosion,
final class list to be fixed by the task owner) from waveform windows, scored on a hidden test
set. Inputs, window length, sampling rate, channel set and class definitions are frozen in a task
spec before any submission — R1.

Metrics: per-class precision, recall and F1; macro-F1 as the headline; a confusion matrix
published for every entry. Add the cost axis per R9.

### 3.2 The hidden set — where this task can go wrong

Two routes were proposed. **They are not equivalent, and the difference is the whole scientific
validity of the benchmark.**

**Route 1 — relabel existing curated data.** Cheap and fast. It is also **contaminated**: those
waveforms are in QuakeXNet-v3's training data. A model that has already seen the signal will
score high for reasons that have nothing to do with generalisation, and the leaderboard would be
measuring memorisation. This is exactly the failure R6 exists to prevent, and exactly what the
geospatial CTO said was never mentioned. **Do not build the headline test set this way.**

**Route 2 — pull new events, temporally disjoint.** Choose a cutoff date after the QuakeXNet-v3
training window, and draw the test set only from events after it. Costs a labelling campaign. It
is the only route that produces a number worth citing, and it has a second benefit: a
temporally-forward test set measures the thing operators actually care about, which is whether
the detector still works on next year's data.

**Recommended: Route 2 for the scored hidden set. Route 1 has one legitimate use** — a public
*validation* split for people developing a submission, clearly labelled as
train-adjacent and never used for a leaderboard number.

### 3.3 Labelling protocol

The test set is only as good as its labels, and a datasheet (R7) has to describe how they were
made.

- **At least two independent annotators** per event, with disagreements adjudicated by a third.
- **Publish inter-annotator agreement** (Cohen's or Fleiss' κ). This bounds the achievable score:
  no model should be reported as beating human agreement without comment, and a benchmark whose
  κ is low is measuring label noise.
- **Record class balance**, and report macro-F1 rather than accuracy so a rare class cannot be
  ignored for free.
- **Keep a held-back slice of the test set entirely unused** at launch, as insurance against
  leaderboard overfitting later.
- Annotators are named in the datasheet and credited. This is student-visible work, and the
  PhD-student persona's finding was that student credit is undocumented — this is a concrete
  place to fix that.

### 3.4 Baselines to publish before any submission

| Baseline | Purpose |
|---|---|
| Majority class | The floor. R4 |
| STA/LTA + simple spectral features + logistic regression | A classical, non-deep floor |
| Published QuakeXNet-v3 | The strong reference. R5 |

Publishing QuakeXNet's own number on a test set it has not seen is the honest first act of this
benchmark, whatever the number turns out to be.

### 3.5 Custody

`Akashkharita/pnw_seismic_event_detection` is in a personal namespace, which the national-lab
scientist flagged as a durability risk in its own right. Mirror or move the code into
`gaia-hazlab` under W2's licence rule; the hidden labels live somewhere Akash does not hold if
he intends to submit (R8, mitigation 2).

## 4. Seed task B — FrugalMind agent evaluation

The existing board is the closest thing the project has to a citable result and the least
defensible as published. [03 §3.0](03-ai-tools-and-evals.md) already sets the migration path; the
review round adds what has to happen before it is shown from HazEvalHub rather than merely linked.

- **Publish the scorer.** The source link 404s. This is R3, and it is the single change the CTO
  named as most valuable.
- **Stamp every row** with the split that produced it, the model version and weights, the date,
  and the cost. Today a reader cannot tell a hidden-set result from a smoke test — R2, R9.
- **State the evaluation's size.** The CTO's note that it is very small, and does not say so, is
  cheap to fix and expensive to leave.
- **Report the negative result too.** The headline currently omits that domain skills made most
  local models *worse* on some task classes. Reporting it strengthens the frugality thesis rather
  than weakening it, because it shows the board can detect harm.
- **Move it out of the personal namespace** into `gaia-hazlab`, or mirror it with the canonical
  copy in the org.

**Embed or link?** Embed the board in the HazEvalHub chapter as an iframe, the way the DataHub
chapter embeds the CRESST catalog, with the canonical board remaining a standalone page. A reader
should meet a working evaluation on the HazEvalHub page rather than being sent elsewhere to find
one — that page's entire credibility problem is that it describes an evaluation nobody can see.

## 5. Phasing to v0.5

Aligns with [03 §3.3](03-ai-tools-and-evals.md), which already defines v0.5 as "the first hazard
task with one hidden test set and one baseline". This is how that gets built.

| Step | What | Blocks on |
|---|---|---|
| 0 | Create `gaia-hazlab/hazevalhub`, licensed. The chapter stops describing a hub with no repository | — |
| 1 | Write the task spec for Seed A and freeze it (R1) | Class list from the task owner |
| 2 | Publish the three Seed A baselines on a public validation split (R4, R5) | Step 1 |
| 3 | FrugalMind: publish scorer, stamp rows, move to org (R2, R3, R9) | — runs in parallel |
| 4 | Label the temporally-disjoint Seed A test set (§3.2 Route 2, §3.3 protocol) | Labelling campaign — the long pole |
| 5 | Publish the datasheet and DOI-archive the splits (R7) | Step 4 |
| 6 | Board live with both tasks, conflict-of-interest note, external entry invited (R8) | Steps 3, 5 |

Steps 0–3 need no new data and can start immediately. Step 4 is the critical path and needs
people, so it is the one to schedule at kickoff.

## 6. What the site says in the meantime

W1 of the [remediation plan](08-site-remediation-plan.md) rewrites the HazEvalHub chapter to
match reality:

- The present-tense claim about holding metrics, protocols and held-out data comes out.
- The page says **in progress**, names the owner, and gives the v0.5 date.
- The FrugalMind board stays and is described accurately: a working prototype for agent tasks,
  with its current limits stated.
- The nine rules in §2 go on the page as the standard the hub is being built to. Publishing the
  standard before the benchmark is itself evidence of seriousness, and costs nothing that is not
  already written here.

The last point is worth dwelling on. The reviewers did not punish absence — the PhD student filed
zero blockers against a project he could see was early. They punished the gap between claim and
artefact. A page that says "here is the standard, here is the date, here is who owns it" closes
that gap without shipping a single line of code.

## 7. Open items

### For kickoff — carried to [`kickoff-agenda.md`](kickoff-agenda.md)

1. Who owns HazEvalHub? [03](03-ai-tools-and-evals.md) says "CI / eval leads"; the role is unfilled.
2. Is there budget or student time for the labelling campaign (§3.3)? This is the critical path.
3. Do we invite an external entry — AI2, the Kutz group — before publishing a GAIA result?

### Internal to the eval team

These do not need the kickoff call and should not wait for it.

4. **Custody of the Seed A hidden labels.** If Akash submits, someone else holds the test set
   (§2.1, mitigation 2). Settle it inside the team before the labelling campaign starts, because
   it determines who runs it.
5. Final class list for Seed A, and the temporal cutoff date for the test set (§3.1, §3.2).
