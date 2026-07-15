# GAIA Participant Roster — Sheet Schema & Data Placement

> The **`GAIA Roster` Google Sheet** (owned by `gaia.hazlab@`, link-shared) is the
> human-curated master list of everyone touching the project. It is the mirror; **GitHub is
> the system of record** ([01 §1](../01-project-coordination.md)). This doc fixes its
> columns so the Sheet can double as the **M3 "unique institutions"** source and feed the
> People page — without ever leaking personnel data into git.

## 1. Three surfaces, one wall

| Surface | Home | Holds | Who sees it |
|---|---|---|---|
| **Roster — Public tab** | Google Sheet | name, institution, role, thrust, GitHub, website, list-on-web | link-shared (project) |
| **Roster — Private tab** | same Sheet, separate tab | funding status, Slack email, seniority, personal email, start date, notes | Lead PI + coordinator only |
| **Personnel** | **UW SharedDrive** | salaries, offers, candidate names, effort % | access-controlled, never here |

Rule: if a machine must read it → GitHub CSV (synced from the Public tab). If it's
sensitive → SharedDrive. The Sheet is only the hand-edited middle.

## 2. Public tab columns

| Col | Field | Example | Notes / → maps to |
|---|---|---|---|
| A | `name` | Jane Rivera | → `team.json.name` |
| B | `institution` | University of Washington | **M3 unique-institutions key** — keep canonical |
| C | `department` | Earth & Space Sciences | joins with B → `affiliation` |
| D | `role` | PhD Student | → `team.json.role` |
| E | `thrust` | HazEvalHub | primary pillar; matches Slack `#ci*`/`#rc*` |
| F | `ci_expertise` | SAR/InSAR; Cloud | semicolon list |
| G | `geo_expertise` | Seismology | → `team.json.geo_expertise` |
| H | `hazard_focus` | earthquakes, landslides | → `team.json.hazard_focus` |
| I | `github` | jrivera | handle only; → org add + default avatar |
| J | `website` | https://… | optional → `team.json.website` |
| K | `scholar` | https://… | optional |
| L | `orcid` | 0000-… | optional |
| M | `list_on_web` | Yes / Not yet | gates People-page publish |
| N | `onboarded` | 2026-08-01 | date org+Slack+calendar done |
| O | `intake_id` | resp #34 | links back to the Form response row |

## 3. Private tab columns (Lead PI + coordinator only)

| Field | Example | Why private |
|---|---|---|
| `full_email` | jrivera@uw.edu | PII |
| `slack_email` | (if different) | PII |
| `funding_status` | Funded / Unfunded / Partner | budget-sensitive |
| `seniority` | PhD | analytics, not public |
| `institution_pi` | co-PI who owns the subaward | governance |
| `mailing_list_optin` | true / false | consent record ([mailing-list-setup.md](mailing-list-setup.md)) |
| `notes` | "starts Sept; needs UW guest NetID" | operational |

## 4. Sync to git (only the Public tab, only when it feeds the dashboard)

- A gated Action exports the **Public tab → `data/roster.csv`** and, for the People page,
  runs the intake pipeline → `data/team.json`
  ([onboarding-intake-form.md §3](onboarding-intake-form.md)). The **repo CSV is
  canonical** for any metric; the Sheet is the editing surface.
- The Private tab is **never exported**. Keep it a separate tab (not hidden columns) so a
  careless "export whole Sheet" can't spill it.
- **M3 institutions** = distinct non-blank values in column B of `roster.csv`, unioned with
  GitHub org email domains — computed by `collect_github.py`
  ([04 §4](../04-metrics-observatory.md)).

## 5. Seeding

Pre-fill the roster from the current [`data/team.json`](../../data/team.json) (14 members)
so the Sheet starts populated; new people arrive via the intake Form. Keep one row per
person; when someone leaves, set `onboarded` note to "alumni <date>" rather than deleting
(preserves the historical institution count).
