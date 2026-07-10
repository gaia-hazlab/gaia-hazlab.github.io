# Automation Runbook

> The concrete "how" behind the agentic-first plan: every recurring coordination task as
> a GitHub Action, bot, or template. This doc maps 1:1 to files created under
> [`../.github/`](../.github/). **All workflows ship gated off** — they exist, they
> `workflow_dispatch`, but scheduled jobs are skipped until you set
> `vars.ENABLE_AUTOMATION=true` and add the required secrets. Nothing fires on merge.

## 1. Enabling automation (one-time)

1. **Repo variable:** Settings → Secrets and variables → Actions → **Variables** →
   add `ENABLE_AUTOMATION = true`. (Leave unset/`false` to keep everything dormant.)
2. **Secrets** (add only the ones you're ready to use):

   | Secret | Used by | Notes |
   |---|---|---|
   | `SLACK_BOT_TOKEN` | weekly nudge, quarterly survey | Slack app with `chat:write` |
   | `SLACK_STATUS_CHANNEL` | weekly nudge | channel ID for `#weekly-status` |
   | `ZENODO_TOKEN` | metrics, annual archive | Zenodo personal token |
   | `HF_TOKEN` | metrics | Hugging Face read token |
   | `GOOGLE_SA_JSON` | metrics (surveys/calendar) | service-account JSON |
   | `SURVEY_FORM_URL` | quarterly survey | Google Form link |
   | `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` | notes/digest agents | LLM key for summarizers |

   `GITHUB_TOKEN` is provided automatically; the GitHub-only metrics collector needs
   nothing else — start there.
3. **Enable schedules:** GitHub disables scheduled Actions after 60 days of repo
   inactivity — the metrics history commit keeps them warm; check monthly during quiet
   spells.

The gating pattern used in every scheduled job:

```yaml
jobs:
  run:
    if: vars.ENABLE_AUTOMATION == 'true'
    runs-on: ubuntu-latest
```

So a fresh clone with no variable set does nothing on schedule, but any maintainer can
still trigger a manual test run via **Run workflow** (`workflow_dispatch`).

## 2. Boards, labels, issue templates (kickoff, one-time)

- **Project board** "GAIA" (Projects v2): columns *To do / In progress / In review /
  Done*; fields *Thrust* (`rc1…`,`ci1…`), *Milestone*, *Assignee-role*.
- **Labels** (create via `gh label`): `documentation`, `training`, `bug`, `datahub`,
  `modelhub`, `hazevalhub`, `agent`, `container`, `metrics`, `website`, `alaska`,
  `geodesy`, `sar-insar`, `good-first-issue`, `partner`.
- **Issue templates** → [`../.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/):
  `task.yml`, `bug.yml`, `documentation.yml`, plus `config.yml` linking Slack/Discussions.
- **CODEOWNERS** → [`../.github/CODEOWNERS`](../.github/CODEOWNERS): routes reviews by
  area (mirrors the Gmail keyword routing in [01 §5](01-project-coordination.md)).

## 3. Weekly Slack status nudge → `weekly-slack-nudge.yml`

- **Cron:** Mondays 16:00 UTC (`0 16 * * 1`).
- **Does:** posts the weekly-status template link + this week's board summary to
  `#weekly-status`; @-reminds thrust leads.
- **Needs:** `SLACK_BOT_TOKEN`, `SLACK_STATUS_CHANNEL`.
- **Human mirror:** Slackbot recurring message is an acceptable no-Action fallback.

## 4. Quarterly survey → `quarterly-survey.yml`

- **Cron:** 1st of Jan/Apr/Jul/Oct 15:00 UTC (`0 15 1 1,4,7,10 *`).
- **Does:** posts the Google Form survey link to Slack + opens a tracking issue labeled
  `metrics`. Feeds M3 (institutions, disciplines) and M4 (skill gain).
- **Needs:** `SLACK_BOT_TOKEN`, `SURVEY_FORM_URL`.

## 5. Metrics Observatory → `metrics-observatory.yml`

- **Cron:** Sundays 06:00 UTC (`0 6 * * 0`).
- **Does:** runs `scripts/metrics/collect_*.py`, writes `data/metrics/latest.json` +
  `history/YYYY-Www.json`, commits the change (dashboard redeploys via Pages). Mirrors
  the existing knowledge-graph workflow's commit-if-changed pattern.
- **Needs:** `GITHUB_TOKEN` (always); `ZENODO_TOKEN`, `HF_TOKEN`, `GOOGLE_SA_JSON`
  as collectors are added.
- **Start small:** GitHub-only collector first; the job no-ops cleanly if optional
  tokens are absent.
- See [04-metrics-observatory.md](04-metrics-observatory.md) for the data contract.

## 6. Annual metrics DOI archive → `metrics-annual-archive.yml`

- **Cron:** yearly on the award anniversary (set the date when NOA lands), or
  `workflow_dispatch`.
- **Does:** tags `metrics-YYYY`, pushes the metrics history to Zenodo → DOI (counts as a
  D3 dataset). Needs `ZENODO_TOKEN`.

## 7. Meeting-notes & digest agents → `agent-*.yml` (optional, LLM)

- `agent-meeting-notes.yml` (`workflow_dispatch`, input: transcript path/URL): transcript
  → cleaned, anonymized MD summary (accomplishments / decisions / action items / issue
  links) → PR to the **private** `notes` repo. Never auto-merges.
- `agent-status-digest.yml` (cron, monthly): `#weekly-status` export → summary GitHub
  Discussion.
- Both need an LLM key; both are **draft-only, human-approved** ([03 §6](03-ai-tools-and-evals.md)).

## 8. Reuse the proven pattern

The repo already runs [`update-knowledge-graph.yml`](../.github/workflows/update-knowledge-graph.yml)
— scheduled, `workflow_dispatch`, `contents: write`, commit-if-changed, concurrency
group. New workflows follow that exact shape. If `main` is protected against direct
pushes, swap the commit/push step for `peter-evans/create-pull-request` (already noted in
that workflow).

## 9. Deferred / external channels

Some coordination lives outside CI and is documented, not automated here:

- **Gmail routing filters** ([01 §5](01-project-coordination.md)) — configured once in
  the `gaia.ci@gmail.com` account.
- **Google Calendar** — human-entered events; `collect_calendar.py` reads it for D5.
- **Zoom AI companion** — records/transcribes; feeds §7's notes agent.
- **LinkedIn / YouTube** — outreach, manual with a monthly checklist.

## 10. Safety checklist before flipping the switch

- [ ] Secrets added to **repo/org secrets**, never committed.
- [ ] `ENABLE_AUTOMATION` set intentionally (leave off until reviewed).
- [ ] Test each workflow via **Run workflow** (`workflow_dispatch`) before trusting cron.
- [ ] Confirm branch-protection interaction (PR vs direct push) for commit-writing jobs.
- [ ] Outward-facing agents (notes, reports) are draft-only + human-approved.
