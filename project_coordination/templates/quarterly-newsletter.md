# GAIA Quarterly Newsletter — Template

> The outward-facing quarterly update sent to the **Announce** list
> ([mailing-list-setup.md](mailing-list-setup.md)) and posted on the website. Designed to
> be **near-zero marginal effort**: the metrics block is pasted from the Metrics
> Observatory's `latest.json`, and highlights are rolled up from the three monthly thrust
> reports. One quarterly beat = **survey fires + newsletter ships** (align to the quarterly
> survey so it's one rhythm, not two).

## Cadence & sourcing

| Section | Source | Effort |
|---|---|---|
| Highlights | 3× [monthly-report.md](monthly-report.md) rolled up | 20 min |
| By the numbers | `data/metrics/latest.json` ([04](../04-metrics-observatory.md)) | paste |
| New this quarter | Zenodo/HF/repo releases (auto in metrics) | paste |
| Spotlight | pick one member/result | 15 min |
| What's next | next-quarter milestones from the board | 10 min |
| Events | shared Calendar feed | paste |

Send in the **last week of each project quarter** (Q1 ends Y1 M3, etc.). Draft owned by the
**coordinator/metrics lead**, approved by the Lead PI.

---

## ✂ Template (fill and send)

**Subject:** GAIA HazLab — Quarterly Update — {Quarter}, {Year} (Project Year {N})

**Header image:** site hero (as in the intake form) · **Accent:** UW purple `#4B2E83`

---

### GAIA HazLab — {Quarter} {Year}

*A FAIR, agentic, multi-hazard cyberinfrastructure for real-time geohazard prediction.*

**In this issue:** {one line — the 3 biggest things}

---

#### 🌟 Highlights this quarter
- {milestone hit — artifact shipped with a DOI}
- {science result / integration across thrusts}
- {community / partner / broadening win}

#### 📊 By the numbers *(auto — from `latest.json`, {generated_utc})*

| Metric | Now | Y{N} target | Δ vs. last quarter |
|---|---|---|---|
| CI-template repos passing tests (D1) | {value} | {target} | {+n} |
| Container images (D2) | {value} | {target} | {+n} |
| DOI-archived datasets (D3) | {value} | {target} | {+n} |
| Pulls + downloads (M2, annual) | {value} | {target} | {+n} |
| Unique institutions (M3) | {value} | {target} | {+n} |
| Modalities per study, median (M4) | {value} | {target} | — |

> **Composite score:** {score} · **Under-engaged domains:** {list} — where we're steering
> outreach next quarter. *(This feedback loop is the point of the Observatory.)*

#### 🆕 New this quarter
- **Tools/repos:** {name + link}
- **Datasets (Zenodo):** {name + DOI}
- **Model cards (HF):** {name + link}
- **Tutorials / JupyterBooks:** {name + link}

#### 🔬 Spotlight
{2–3 sentences on one person, result, or partner collaboration. Photo optional.}

#### 📅 Coming up
- {Seminar / thrust sync / hackweek — date + registration}
- {In-person: e.g. AGU Sunday sync}
- {Deadline the community should know}

#### 🎯 Next quarter
- {2–4 planned milestones with the accountable thrust}

---

*You're getting this because you opted into the GAIA Announce list. New here?
[Subscribe]({announce-link}) · Not for you? Unsubscribe below.
Explore: [book]({book-link}) · [dashboard]({dashboard-link}) · [GitHub](https://github.com/gaia-hazlab)*

---

## Automation note

A `scripts/newsletter/draft.py` can pre-fill the **By the numbers** table and **New this
quarter** lists directly from `data/metrics/latest.json` + the prior quarter's `history/`
snapshot, emitting this Markdown with only the human sections ({} placeholders) left to
write — same gated-automation pattern as the collectors ([05](../05-automation-runbook.md)).
Until it exists, paste the six metric rows by hand from the dashboard.
