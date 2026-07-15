# GAIA Onboarding Intake Form — Spec & Build Guide

> The single Google Form (owned by `gaia.hazlab@`, shared with `mdenolle@uw.edu`) that new
> members fill once. Its responses Sheet is the **raw feed for the people page**
> (`data/team.json`) and the roster. Design goal: **collect exactly the fields the website
> and coordination need — no more — and default the portrait to the GitHub avatar** so most
> people never have to upload a photo.

## 1. Header / background image

Google Forms uses a **header image** (banner) + a theme color, not a full-page background.

- **Header image:** the site hero poster, already public on the site:
  `https://gaia-hazlab.github.io/assets/geophysical_hero_cinematic_loop_15s_poster.png`
  Download it, then in the Form: **🎨 (Customize theme) → Header → Upload image**.
- **Theme color:** UW purple **`#4B2E83`** (the site's `--purple`); text/background: light.
- **Title:** "Join GAIA HazLab — Member Intake" · **Description:** one line + link to the
  book and the coordination README so people know what they're joining.

> I can't upload the header via API (no Forms tool). Either you do the 3 clicks above, or
> open the form logged in as gaia.hazlab and I'll drive the browser to build the whole form
> from this spec.

## 2. Questions (paste-ready)

Types: **SA**=short answer, **P**=paragraph, **MC**=multiple choice (one), **CB**=checkboxes
(many), **DD**=dropdown, **FU**=file upload, **§**=section break. `*`=required.

| # | Question | Type | Options / notes | → maps to |
|---|---|---|---|---|
| — | **Section 1: Who you are** | § | | |
| 1 | Full name * | SA | as it should appear on the website | `name` |
| 2 | Preferred email * | SA | used for Slack + mailing list | `email` |
| 3 | Home institution * | SA | e.g. "University of Washington" | `affiliation` (inst.) |
| 4 | Department / unit | SA | e.g. "Earth & Space Sciences" | `affiliation` (dept) |
| 5 | Role on GAIA * | MC | Lead PI · Co-PI · Senior Personnel · Postdoc · PhD Student · MS Student · Undergrad · Research Scientist/Staff · RSE/Engineer · Collaborator (unfunded) · Partner | `role` |
| 6 | Seniority (career stage) * | MC | Faculty/PI · Research Scientist/Staff · Postdoc · PhD · Masters · Undergrad · Industry/Partner | (roster; seniority analytics) |
| 7 | Funding status * | MC | Funded on GAIA CSSI · Unfunded collaborator · Partner org | roster (private tab) |
| — | **Section 2: Where you fit in the project** | § | | |
| 8 | CSSI pillar(s) you contribute to * | CB | *(confirm exact proposal names)* Research Components (science) · DataHub · ModelHub · HazEvalHub (agents & evals) · Coordination/Broadening · Alaska region · Geodesy/GNSS · SAR/InSAR | thrust tags |
| 9 | Cyberinfrastructure expertise * | CB | **SAR/InSAR** · **Seismic/waveform** · **Cloud/HPC** · **Physics-based modeling** · **ML/AI & agents** · Data engineering/catalogs · Visualization/web · None yet — here to learn | `ai_expertise` + CI routing |
| 10 | Geoscience expertise | SA | free text, e.g. "Seismology; geomorphology" | `geo_expertise` |
| 11 | Hazard focus | SA | e.g. "earthquakes, landslides, floods" | `hazard_focus` |
| — | **Section 3: Accounts to connect** | § | | |
| 12 | GitHub username * | SA | just the handle; we add you to `gaia-hazlab` org | `github` (+ default `photo`) |
| 13 | Email for Slack invite * | SA | defaults to Q2 if same | Slack invite batch |
| 14 | Personal / lab website | SA | optional | `website` |
| 15 | Google Scholar URL | SA | optional | `scholar` |
| 16 | ORCID | SA | optional | `orcid` |
| — | **Section 4: Website profile** | § | "How you'll appear on the People page" | |
| 17 | One-line interest / bio | P | 1–2 sentences, shown on your card | (people page blurb) |
| 18 | Portrait | MC | **"Use my GitHub avatar" (default)** · "I'll upload one" · "No photo" | drives `photo` |
| 19 | Upload portrait (only if Q18 = upload) | FU | square, ≥400px; ⚠ requires Google sign-in, counts against Drive quota | `photo` |
| — | **Section 5: Consent** | § | | |
| 20 | Join the GAIA announce mailing list? * | MC | Yes, subscribe me · No thanks | mailing-list opt-in |
| 21 | OK to list me on the public People page? * | MC | Yes · Not yet | gates people-page publish |

**Portrait default is the win:** if Q18 = "Use my GitHub avatar," the pipeline sets
`photo: https://github.com/<username>.png` — the same pattern already used for Scott,
Nicoleta, Brandon, and Alex in `team.json`. Most people never touch the upload question.

## 3. Form → people page pipeline

```
Google Form  →  responses Sheet (in gaia.hazlab Drive)
      │  (export CSV, or Sheets API read)
      ▼
scripts/people/build_team.py   ← new collector, mirrors the metrics pattern
      │  - split affiliation = "Dept, Institution"
      │  - photo = github avatar unless upload/URL given
      │  - only rows with Q21 = Yes are published
      ▼
data/team.json  →  people.html (js/team-loader.js renders it)
```

- The **private roster tab** (funding status, Slack email, seniority) stays in the Sheet /
  SharedDrive and is **not** copied to `team.json` (which is public in the repo).
- `build_team.py` should be **idempotent** and run behind the same gated-automation flag as
  the metrics collectors ([05 runbook](../05-automation-runbook.md)); until it exists, the
  onboarding lead pastes new members into `team.json` by hand using the field map above.

## 4. Per-person profile template (`profile-template.yaml`)

For anyone we onboard before the form/pipeline is live, or who prefers a PR, fill
[profile-template.yaml](profile-template.yaml) and drop it in — it carries the same fields
as a `team.json` entry.

## 5. Build checklist

- [ ] Create/rename the Form in gaia.hazlab Drive → "GAIA Onboarding Intake"
- [ ] Header image + UW-purple theme (§1)
- [ ] Add all 21 questions with required flags and section breaks (§2)
- [ ] Turn on "Collect email addresses" off (we ask explicitly) / limit to 1 response off
      (external collaborators may not have Google) — **keep it open, no sign-in required**,
      except the optional file-upload question
- [ ] Link the responses Sheet; note its file ID for the future collector
- [ ] Add the Form link to: onboarding-checklist, the website "Join" CTA, and the mailing
      list welcome
