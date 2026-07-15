# GAIA Shared Google Account — Runbook

> The project-owned account is **`gaia.hazlab@gmail.com`** (consumer/free Gmail, no paid
> Workspace — per [01-project-coordination.md §5](../01-project-coordination.md)). Owning
> the contact list, Calendar, Drive, and Forms in a **neutral account** (not a person) is
> what gives the CSSI multi-institution continuity. This runbook is how the Lead PI (and a
> backup) operate it.

## 0. Password custody (do this first)

- Store the password in the **Lead PI's password manager** (UW-approved: e.g. Bitwarden,
  1Password, or LastPass), in a shared vault/folder named `GAIA-CI` so a **second person**
  (co-PI or coordinator) has emergency access. Never email or Slack the password.
- Turn on **2-Step Verification** on the account and save the **backup codes** into the
  same vault entry. Add the Lead PI's phone as the recovery phone and a co-PI's email as
  recovery email so no single person is a lock-out risk.
- Record in the vault entry: account email, recovery email, recovery phone, and "owned by
  GAIA CSSI — do not repurpose."

## 1. Logging in

1. Open an **incognito/private window** (keeps it separate from your UW Google session)
   or a dedicated Chrome profile named "GAIA".
2. Go to <https://accounts.google.com>, sign in as `gaia.hazlab@gmail.com`.
3. Complete 2FA with the authenticator/backup code.
4. Bookmark, in that profile: Gmail, Calendar, Drive, and the Forms list
   (<https://docs.google.com/forms>).

**Tip:** a dedicated Chrome profile ("GAIA") is less error-prone than incognito for
day-to-day use — you stay logged in and never cross-contaminate with your UW account.

## 2. Forward this account's mail to your work Gmail

Goal: you read/answer GAIA mail from your normal inbox without logging in constantly.

**In `gaia.hazlab@gmail.com`:**
1. Gmail → **⚙ Settings → See all settings → Forwarding and POP/IMAP**.
2. **Add a forwarding address** → enter `mdenolle@uw.edu` → Next → Proceed.
3. Google emails a **confirmation link to `mdenolle@uw.edu`** — open it and confirm.
4. Back in the gaia.hazlab settings, select **"Forward a copy of incoming mail to
   mdenolle@uw.edu"** and choose **"keep Gmail's copy in the Inbox"** (so the shared
   archive stays complete). Save.

**Optional but recommended — reply *as* the shared address from your UW inbox:**
5. In **your UW Gmail** (`mdenolle@uw.edu`): Settings → **Accounts and Import → Send mail
   as → Add another email address** → `gaia.hazlab@gmail.com` → verify via the code Google
   sends. Now you can pick the From: address when replying, so outbound GAIA mail shows the
   project identity, not your personal one.

**Filters (do these in gaia.hazlab, mirrors [01 §5](../01-project-coordination.md)):**
- `subject:(tool OR container OR software)` → label `CI`
- `subject:(hydrology OR seismology OR geodesy OR SAR OR hazards)` → label `RC`
- everything else → label `Lead-PI`
- Set a **canned auto-reply / vacation-style template** that links the coordination repo
  and the book, so first-contact emails get an instant orientation.

> Setting up forwarding, send-as, and filters are **account-settings changes only the Lead
> PI should make** while logged in — they can't (and shouldn't) be automated for you.

## 3. Calendar — create the shared GAIA calendar, then subscribe from your UW calendar

**A. Create the shared calendar (once, in `gaia.hazlab`):**
1. Calendar → left sidebar **"Other calendars" → + → Create new calendar**.
2. Name: **"GAIA CSSI"**, description: "Seminars, thrust syncs, hackweeks, deadlines",
   time zone: America/Los_Angeles → **Create calendar**.
3. Open that calendar's **Settings → Share with specific people / Access permissions**:
   - For broad visibility, tick **"Make available to public → See all event details"**
     (fine for a research seminar calendar), **or**
   - share with each member's email at "See all event details." Give the coordinator and a
     co-PI **"Make changes to events"** so calendar upkeep isn't single-threaded.
4. Copy the calendar's **public URL / iCal address** (Settings → *Integrate calendar*).
   The website events page mirrors this feed.

**B. Add it to your own (UW) Google Calendar:**
- Easiest: while sharing (step 3) it appears automatically under your Other calendars.
- Or subscribe by address: in **your UW Calendar** → Other calendars → **+ → Subscribe to
  calendar** (paste the address) or **From URL** (paste the iCal URL).

**C. Create an event (the standard entry all members use):**
- Title, start/end time + time zone, **type in the title** (`[Talk]`, `[Poster]`,
  `[Seminar]`, `[Deadline]`), location or Meet link, and a **description with a link**
  (slides/issue/registration). Set the event's calendar to **GAIA CSSI**, not your personal
  one. Invite `gaia.hazlab@` contacts or the mailing-list group as needed.

> I can create the **kickoff event** for you via the calendar tool once you tell me the
> date/time and confirm which calendar — but note the tool is currently connected to your
> **UW** account, so I'd create it there and you'd move/copy it, unless you connect the
> gaia.hazlab account to this session.

## 4. What lives in this account's Google Drive

Keep the split from [01 §5.1](../01-project-coordination.md): **GitHub is the system of
record; Google is the human-comfort mirror.** The gaia.hazlab Drive (15 GB, single-owner)
holds only the human-curated, non-machine-read surfaces:

| Folder / file in gaia.hazlab Drive | Purpose | Notes |
|---|---|---|
| **`GAIA Roster` (Google Sheet)** | Contact list + roles + mailing-list opt-in; doubles as M3 "unique institutions" source | Link-shared; synced to repo CSV by an Action when it feeds the dashboard |
| **`GAIA Onboarding Intake` (Form + responses Sheet)** | New-member intake (§ onboarding-intake-form.md) | Responses Sheet is the raw feed for the people page |
| **`Meeting Notes` (Docs, by month)** | Human-readable notes; AI-summarized copy goes to the private `notes` repo | Working copies only |
| **`Slides & Posters` (working copies)** | Drafts before they get a Zenodo/FigShare DOI | Final versions get a **DOI**, not a Drive link |
| **`Templates`** | Google-native copies of the letterhead, slide master, report template | Mirrors of the git templates |

**Never in this Drive:** big data (SAR scenes, cubes, model checkpoints → Zenodo / cloud /
ASF-HyP3), anything a machine must read (→ GitHub), or sensitive personnel data (salaries,
offers, candidate names → **UW SharedDrive**, access-controlled, not here). The 15 GB cap
is a feature: if you're tempted to put big or canonical data here, it belongs elsewhere.

## 5. Backup owner

Designate a **co-PI or the coordinator as secondary operator**: they hold vault access
(§0), are a "Make changes" delegate on the Calendar, and are added as **send-as** on the
account. This removes the Lead PI as a single point of failure for a 5-year award.
