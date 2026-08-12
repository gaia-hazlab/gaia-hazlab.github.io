# Review: National laboratory staff scientist assessing interoperability

**Reviewed:** 2026-08-12 · **Scope:** landing page; `book/` and the chapters datahub, datahub-integration-guide, datahub-inventory, how-we-work, organization, decisions, licensing, faq, research-software, modelhub; dashboard.html, people.html, funding.html, presentations.html; the `gaia-hazlab` GitHub organisation and the repositories `gaia-cli`, `catalog`, `prism-stac`, `geocroissant-hazards`, `gaia-agentic-ai`; one live data round-trip against the catalog GeoJSON · **Time spent:** 45 minutes (budget spent; I stopped)

> **This is a simulated review.** I am a persona constructed for this exercise, not a real
> staff scientist at a real laboratory. Each finding below is a hypothesis about how a reader
> in this role would react, not evidence that one did. Treat it accordingly.

## The sixty-second sentence

Written on the landing page before I read anything else, and not revised:

> *"They build digital twins of the Earth from open multi-sensor data plus AI and cloud
> computing, on top of physical models, to monitor and forecast soil moisture, landslides,
> liquefaction and floods."*

That held up. It is one of the few sixty-second sentences I have written that the rest of the
site did not contradict, and the project deserves credit for it.

## In one paragraph

I came to answer one question in writing: what would it take to depend on this, and what
would break if it went away. I can now answer the first half. The technical layer is more
serious than most university cyberinfrastructure I assess — the DataHub Integration Guide
names STAC 1.1.0, declares CRS and grid explicitly, separates native support from posting
resolution, and defines a four-part provenance statement carried as STAC properties. That is
real interoperability thinking, not a gesture. But I cannot answer the second half at all,
and two of my own stopping conditions are met. Nothing on the site says what happens to any
of this after the award ends, or which institution would hold it. And there is no versioning
story: the data the public dashboard serves comes off a mutable branch pointer, the object
store is laid out under per-person prefixes, and across thirty-three repositories in the
organisation there are zero tags, zero releases and no DOI I can resolve today — against a
book page that claims DOI-archived datasets as a delivery metric and claims RO-Crate
provenance is already shipped with releases that do not exist. My next step would not be a
pilot. It would be an email asking two questions — who holds this in year six, and what is
the immutable identifier for the dataset you want me to consume — and I would not open a
requirements document until I had answers.

## Weighted score: 56/100

| Dim | Score | Weight | Note |
|---|---|---|---|
| D1 Clarity of purpose | 4 | 10 | Sixty-second sentence survived the whole review |
| D2 Credibility of claims | 2 | 15 | Several load-bearing claims describe artefacts I cannot find |
| D3 Navigation and information scent | 3 | 5 | The interoperability material exists but is two clicks below where I looked |
| D4 Visual and accessibility | 3 | 5 | Loads and reads fine; book HTML carries no text without JavaScript |
| D5 Technical depth and reproducibility | 3 | 20 | Strong conventions, no versioned artefacts, code declared non-functional |
| D6 Governance and openness | 3 | 20 | Best governance writing I have read on a project site; nothing ratified, licences inconsistent |
| D7 Activity and durability | 2 | 20 | Very much alive; no stated survival path |
| D8 Relevance to me | 4 | 5 | Squarely the problem I have |

## Findings

### 1. No stated plan for what happens after the award — BLOCKER · D7
**Where:** https://gaia-hazlab.github.io/book/how-we-work/ (and /book/organization/, /book/faq/)
**Saw:** The how-we-work page runs to eight numbered sections and a five-year metric table
("Y1 Y2 Y3 Y4 Y5 … D3 DOI-archived datasets 5 10 20 50 100"), and closes at section 8,
"Changing any of this." There is no section on year six. The FAQ's fifteen questions include
"Who decides what goes into the organisation?" but none asking who holds it afterwards. The
strongest commitment anywhere is on /book/organization/, level 4 of the adoption ladder:
"Long-term maintenance — requires a named maintainer and a numbered decision."
**Why it matters to me:** This is one of my explicit stopping conditions and I am applying it
as written. "Long-term maintenance" delegated to "a named maintainer" is a person, not an
institution — and the whole point of my review process is that a person is not a custodian.
Three universities and a consortium hold three linked awards; none of the four is named as
the entity that would hold the artefacts if the awards ended. I cannot write a dependency
memo that says "and then it is somebody's job."
**Suggested fix:** One short section on how-we-work: for each artefact class (containers,
STAC catalogs, evaluation tasks, the book), name the institution that would host it after the
award and the archive of record (Zenodo community, institutional repository, EarthScope). If
the answer for a class is genuinely "unknown," write that — an honest gap is assessable, a
silence is not.
**Confidence:** high

### 2. No versioning story for data products — BLOCKER · D5
**Where:** https://gaia-hazlab.github.io/dashboard.html and
https://gaia-hazlab.github.io/book/datahub-integration-guide/
**Saw:** The dashboard's page source sets
`const CAT = "https://raw.githubusercontent.com/gaia-hazlab/catalog/refs/heads/main"` and
loads its layers from it (`url:CAT+"/seismic-stations.geojson"`, `…/streamflow-stations.geojson`,
`…/pnw_eq_catalog_2025.geojson`). The integration guide's own migration recipe points readers
at the same construction:
`cat = pystac.Catalog.from_file("https://raw.githubusercontent.com/gaia-hazlab/solus-stac/main/stac/catalog.json")`.
Across the thirty-three repositories in the organisation I found zero git tags and zero
releases (checked `gaia-cli`, `catalog`, `prism-stac`, `geocroissant-hazards`, `gaia-agentic-ai`).
**Why it matters to me:** A URL on a branch head returns different content over time, which is
my definition of not-a-data-product. If I ingest `seismic-stations.geojson` today and my
pipeline behaves differently next month, I have no way to tell whether my code changed or your
data did, and no way to retrieve the version I validated against. This is my second explicit
stopping condition.
**Suggested fix:** Two changes, both small. Serve and document commit-pinned URLs
(`raw.githubusercontent.com/.../<40-char-sha>/...`) rather than `refs/heads/main`, and cut a
tagged release per catalog repository so a citable version exists. The DOI step can follow;
an immutable URL is the part I need first.
**Confidence:** high

### 3. Every data product's canonical location is namespaced to an individual — MAJOR · D7
**Where:** https://gaia-hazlab.github.io/book/datahub-integration-guide/
**Saw:** "Object store — s3://cresst (us-west-2): anonymous read, authenticated write via
obstore (AWS_PROFILE=cresst-user), layout `s3://cresst/{user}/`, formats Zarr / COG /
Parquet." And in the DataHub-ready checklist: "Outputs are cloud-native (COG/Zarr) on
`s3://cresst/{user}/`…"
**Why it matters to me:** *(Observation: the layout is per-user. Inference, and I mark it as
one: this makes every published product's address depend on a person's account name.)* When
that postdoc leaves, either the path is wrong or the path is a stranger's name in my
configuration file. Anonymous read is genuinely good and I want to say so — the access model
is fine; the naming is what fails a custody review.
**Suggested fix:** Keep `{user}/` as the scratch and staging convention, and add a promoted
namespace — `s3://cresst/products/{collection}/{version}/` — that a product moves into when
it becomes something the project stands behind. The checklist item then reads "published
outputs live under products/, not under a username."
**Confidence:** high

### 4. The public metrics dashboard the governance page rests on does not exist at any URL I can find — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/book/how-we-work/
**Saw:** "The public dashboard updates weekly whether or not anyone is watching." · "The
quarterly newsletter to the announce list pastes its numbers directly from `latest.json`." ·
"metrics-observatory, which produces the dashboard" (on /book/organization/). I probed
`https://gaia-hazlab.github.io/latest.json`, `/metrics.html` and `/data/latest.json` — all
404. `https://gaia-hazlab.github.io/dashboard.html` resolves, but it is the sensor map, not
the metrics dashboard. `metrics-observatory` does not appear in the `gaia-hazlab`
organisation's repository listing.
**Why it matters to me:** The entire credibility of sections 1–3 of how-we-work rests on the
claim that these numbers are collected automatically and published including the shortfalls.
That is the most persuasive thing on the site, and I cannot verify a single number of it. A
governance page written in the present tense about an artefact that does not exist yet is the
specific failure mode my review process exists to catch.
**Suggested fix:** Either publish the dashboard and `latest.json` at stable URLs and link both
from how-we-work, or move the whole of sections 1–3 into the future tense with a date
("from Y1Q4 the Observatory will publish …"). Both are honest; the present tense is not.
**Confidence:** high

### 5. Provenance artefacts described as already shipping are not in any repository — MAJOR · D2
**Where:** https://gaia-hazlab.github.io/book/licensing/
**Saw:** In the AI-code disclosure guidance: "the provenance YAML / RO-Crate we already ship
with releases." Also on /book/decisions/, GAIA-D-001 obligates "CITATION.cff in every repo ·
all three award numbers as required fields in the provenance YAML schema."
**Why it matters to me:** There are no releases in the organisation to ship anything with, no
file named `provenance.yaml` anywhere in it, and `CITATION.cff` in two of thirty-three
repositories (`seis-hydro-2-sed`, `geocroissant-hazards`). RO-Crate is exactly the standard I
would want cited and it is the one sentence on the site that would have carried real weight
with my review board — which is why finding nothing behind it costs the project more than
never claiming it would have. "We already ship" is a verifiable claim and it does not verify.
**Suggested fix:** Change "we already ship" to "we will ship" until one release exists with an
RO-Crate in it, then change it back and link that release from the licensing page.
**Confidence:** high

### 6. Eight public repositories have no licence, and one is copyleft against the project's own rule — MAJOR · D6
**Where:** https://gaia-hazlab.github.io/book/licensing/ vs https://github.com/gaia-hazlab
**Saw:** The licensing page states the rule — "Software written by the project — MIT" — and
the reason: "A repository that cannot legally be reused fails that test no matter how open it
looks." In the organisation, the public repositories `seis-hydro-2-sed`,
`gaia-data-downloaders`, `awesome-gaia`, `landlab-debrisflow`, `gaia-translate-QA`,
`mt-rainier-smart-sensing`, `da-seis-groundfailure` and `shred-landlab-prototypes` carry no
LICENSE file. `usgs-gauge-utils` is GPL-3.0, against the same page's "Copyleft … Avoid for
anything meant to be a library." `geocroissant-hazards` reports as NOASSERTION — GitHub
cannot read its licence, which the page itself warns about: "if GitHub cannot read it,
neither can the tools that count what we publish."
**Why it matters to me:** An unlicensed public repository is not reusable by me. My
institution's software review treats absence of a licence as "all rights reserved," so
`seis-hydro-2-sed` — one of the two most-pushed science repositories, updated two days ago —
is off the table regardless of its quality. I note the page's own status banner ("Proposed,
awaiting a numbered decision … individual repositories may not yet match what is described
here"), which is honest, and I am scoring the gap rather than the dishonesty.
**Suggested fix:** Eight LICENSE files is an afternoon. Do that before ratifying the policy —
a ratified policy with eight violations is worse than an unratified one with none.
**Confidence:** high

### 7. Nothing in the decisions register is actually decided — MAJOR · D6
**Where:** https://gaia-hazlab.github.io/book/decisions/
**Saw:** The register's first rule: "Nothing counts as decided until it has a number here."
The index then lists four entries, all with status "proposed" and date "—":
"001 Funding acknowledgment text and mechanics proposed —", "002 System of record: Slack
ephemeral, GitHub durable proposed —", "003 Meeting schedule and the sunset rule proposed —",
"004 Project Google identity proposed —". Each carries "Decided at: kickoff call, 2026-08-__"
with the day left blank.
**Why it matters to me:** The decisions register is the artefact I would cite in my memo as
evidence that this project governs itself in a way I can audit — and by its own definition it
currently records four proposals and zero decisions. I take the point that the project is
weeks old. But the governance pages are written as though the machinery is running, and this
page is where that reads most strangely: the licensing policy, the taxonomy and the openness
policy all say "awaiting a numbered decision," and the register they are waiting on has
issued none.
**Suggested fix:** Ratify 001–004 at the September call, fill in the dates, and put a one-line
status at the top of the index ("4 proposed, 0 active as of 2026-08-12") so a reader knows in
two seconds what state the register is in.
**Confidence:** high

### 8. Sensitive-location handling is one parenthesis with no policy behind it — MAJOR · D6
**Where:** https://gaia-hazlab.github.io/book/datahub-inventory/
**Saw:** In §7, Known gaps, risks & sensitivities: "Access sensitivities. OpenTopography
(key), PRISM 800 m (license), SMAP (Earthdata), ERA5 (CDS), Synoptic (token), and some
hazard-inventory locations (withheld) — recorded per-layer in the Limitations column of §1
(there is no separate access column)."
**Why it matters to me:** Everything in that sentence except the last clause is a
credentialing note. "Some hazard-inventory locations (withheld)" is a different kind of thing
entirely — it is the only place the site acknowledges that a hazard inventory can locate
vulnerable people and infrastructure, and it is filed alongside API keys. I do not need a long
policy. I need to know who decides what is withheld, on what criterion, and what a requester
does to get it. Without that, I cannot tell my own review board what happens when GAIA
publishes a liquefaction-susceptibility layer over a populated area.
**Suggested fix:** A short section on the DataHub page — three paragraphs: what gets withheld
(named categories), who decides (a role, and eventually a numbered decision), and how a
qualified requester asks. Cross-link it from §7 rather than leaving it inside a bullet about
API keys.
**Confidence:** medium

### 9. A site-wide banner declares the code non-functional, including on the pages I would trust most — MAJOR · D5
**Where:** every book page, e.g. https://gaia-hazlab.github.io/book/datahub/ and
https://gaia-hazlab.github.io/book/how-we-work/; and the landing page
**Saw:** On the book pages, top and bottom: "📢 Announcement: This is a new website, code
examples are non-functional placeholders!" On the landing page: "📢 Newly relaunched — code
examples are placeholders while we rebuild. Welcome back, partners." Immediately below the
banner, the DataHub page says of its Synoptic snippet: "Export it as SYNOPTIC_TOKEN and the
block below runs as-is".
**Why it matters to me:** My decision rule is that I request one dataset through the documented
path and check that what I get matches what was described. The banner tells me not to bother,
and the page under it tells me the block "runs as-is" — I cannot act on both. (I did run the
round trip anyway; see What worked. The banner was wrong about that path, which is the other
half of the cost: a blanket disclaimer over working material makes the working material
invisible.)
**Suggested fix:** Scope the banner to the pages where it is true, or invert it — mark
individual code blocks as placeholders and let the rest stand. A global disclaimer on a
governance page is confusing in a different way: it reads as if the governance were a
placeholder too.
**Confidence:** high

### 10. "Agentic" is used on the landing page and throughout the governance chapter without ever being defined — MINOR · D1
**Where:** https://gaia-hazlab.github.io/ and https://gaia-hazlab.github.io/book/how-we-work/
**Saw:** Landing page: "The agentic-AI layer — a cross-disciplinary translator, agentic data
downloaders, and research-software agents." How-we-work §6: "it is the most direct evidence we
can offer that agentic project management does what we claim." How-we-work D5 metric row:
"JupyterBooks + hackweeks (per year)".
**Why it matters to me:** I do not know these words, and flagging that is my job here rather
than quietly inferring. "Agentic data downloaders" tells me nothing about what runs, on whose
credentials, or what it writes — which are the three things my supply-chain review asks about
anything automated that touches our data. "Hackweek" appears in a delivery metric I am being
asked to treat as a commitment, and I could not tell you what would count as delivering one.
**Suggested fix:** One sentence at first use of "agentic" ("a program that plans and executes
multi-step tasks using a language model, under the approval rule in §7") and a glossary entry
for hackweek. The concept is fine; the unexplained adjective is what makes an outside reviewer
discount the whole section.
**Confidence:** high

### 11. The book's HTML contains no readable text without JavaScript — MINOR · D4
**Where:** https://gaia-hazlab.github.io/book/datahub/ (and every other book page)
**Saw:** Fetching the page and stripping tags yields 58 characters of body text; the chapter
content is delivered inside a `window.__remixContext` JSON payload and rendered client-side.
The landing page and `dashboard.html`, by contrast, contain their text in the markup.
**Why it matters to me:** *(Observation. Inference, marked: )* Our archiving and
link-checking tooling reads served HTML, and so do several of the harvesters that would be
asked to index a project like this. A book that only exists after JavaScript runs is harder to
preserve than one that does not — which sits oddly next to a project whose thesis is
durability. I cannot judge the accessibility consequences properly; that is outside my
competence.
**Suggested fix:** If mystmd offers a static-HTML or pre-rendered output mode, use it for the
book. If not, this is worth one line in a decision record so it is a known trade rather than
an accident.
**Confidence:** medium

### 12. `CITATION.cff` exists in two of thirty-three repositories — MINOR · D6
**Where:** https://github.com/gaia-hazlab, against
https://gaia-hazlab.github.io/book/licensing/
**Saw:** The licensing page: "a permissively licensed repository with no CITATION.cff gets
used and never cited, which is precisely the invisibility this project exists to argue
against." GAIA-D-001 obligates "CITATION.cff in every repo." A code search across the
organisation returns two files, in `seis-hydro-2-sed` and `geocroissant-hazards`.
**Why it matters to me:** Small on its own, and I note the decision is only proposed. I record
it because it is the third instance of the same pattern — the documentation describes a
practice in the present tense that the repositories have not adopted yet — and the pattern
matters more to me than any of its instances.
**Suggested fix:** Generate `CITATION.cff` from a template as part of whatever creates a new
GAIA repository, and backfill in one pass.
**Confidence:** high

### 13. A reader doing a sixty-second standards check will not find STAC — POLISH · D3
**Where:** https://gaia-hazlab.github.io/book/datahub/
**Saw:** The only mention of a metadata standard on the DataHub page is inside a sentence
pointing elsewhere: "For the concrete architecture (the `s3://cresst` object store, the static
STAC catalogs, and `gaia-cli`) and a repo-by-repo migration path … see the DataHub
Integration Guide." Neither the integration guide nor the data inventory appears in the book's
table of contents.
**Why it matters to me:** I nearly stopped here. My first-sixty-seconds rule is that a data
layer described without a named metadata standard has not thought about interoperability, and
the DataHub page reads that way until you follow a link that is not in the navigation. The
material behind it is the best thing on the site. This is a placement problem, not a substance
problem, and it is costing you the readers most likely to be impressed.
**Suggested fix:** Put "STAC 1.1.0 · COG · Zarr v3 · EPSG declared per layer" in the DataHub
page's overview paragraph, and add both the integration guide and the data inventory to the
book's table of contents.
**Confidence:** high

## What worked

**The round trip succeeded, and that is worth more to me than the rest of the site.** From
https://gaia-hazlab.github.io/dashboard.html I extracted the layer URL, fetched
`seismic-stations.geojson` unauthenticated, and got 286 kB of valid GeoJSON: 685 features, a
`crs` member present, and per-feature properties including `network`, `station`, `latitude`,
`longitude`, `elevation`, `start_datetime`, `end_datetime`, `is_active` and a link back to the
IRIS station page. What I got matched what the page described. Anonymous read, static files,
no bespoke API to reverse-engineer — this is exactly the access model I want, and I would
point other projects at it. The only thing missing is the version (finding 2) and
dataset-level metadata: no licence, no creator, no date of generation, no statement of the
FDSN query it came from.

**The provenance standard on the integration guide is better than most operational
documentation I read.** "Every layer the DataHub serves must carry a four-part provenance
statement, expressed as STAC properties so it travels with the data" — source, measurement,
resolution, uncertainty — and specifically the insistence on keeping native support distinct
from posting resolution: "a product posted at 9 km must keep its true (coarser) native support
recorded — distinct from the grid it is delivered on — so downstream models can weight it
honestly." The data inventory then carries "Native support" and "Posting resolution" as
separate columns and actually populates them ("~9 km · EASE-2" delivered from "L-band
radiometer ~36 km"). Very few projects do this. Protect it.

**The boundary of responsibility is drawn honestly.** /book/organization/ separates "Software
we maintain … if it is here, we keep it working" from "Software we only point to … An entry is
a recommendation and a link. It is explicitly not a maintenance promise," and gives the reason:
"Without a place to point at things, an infrastructure project drifts toward absorbing them,
and inherits maintenance for code it did not write and cannot fix." That is the correct
instinct and it is rarer than it should be. The adoption ladder makes each level a stated
commitment rather than an assumed one, and the note that "A group choosing to stay at level 0
indefinitely is a success, not a failure" tells me the project has thought about what it is
asking of outsiders.

**Pinned environments, and the right explanation of why.** `pixi.lock` is present in
`gaia-cli`, `catalog`, `prism-stac` and `gaia-agentic-ai`, and /book/organization/ states the
lesson correctly: "Pinned dependencies, rather than containers as such, produced
reproducibility. Workshop material from years ago still runs because versions were fixed. The
container was the delivery mechanism; the pinning was the guarantee." That is the sentence I
would quote to my own group.

## What I could not judge

- **Container images and scheduled rebuilds.** The organisation page commits to "Scheduled
  rebuilds, CI on the image" at level 1 and how-we-work targets 3 container images in Y1. I did
  not find a public registry namespace from the site, and I did not spend budget hunting for
  one. Whether images exist, what base they use, and whether the rebuild schedule runs are all
  open for me.
- **Whether the STAC catalogs validate.** I read the conventions; I did not run `stac-validate`
  against `solus-stac`, `prism-stac` or `landlab-stac`. The integration guide itself flags that
  `precip-stac` has "no STAC JSON yet" and `landlab-stac` assets are "plain GeoTIFF" rather than
  COG, so I expect mixed results.
- **Software supply chain beyond dependency pinning.** No SBOM, no signed artefacts, no
  provenance attestations that I found — but with zero releases there is nothing yet to sign, so
  I record this as not-yet-assessable rather than as a failure.
- **Accessibility.** Contrast, keyboard reach and screen-reader behaviour are outside my
  competence and I did not test them. I noted 6 `alt` attributes in the landing-page markup and
  leave the judgement to a reviewer who can make it.
- **Whether the science is right.** Not my question. The hazard chapters look substantive; I am
  not qualified on landslide physics or liquefaction indices.

## What I ran out of patience before finding

The forty-five minutes went on the DataHub chain and the governance chapter. I never opened
`modelhub`, `hazevalhub` or the hazard pages properly, and I never looked for a data
management plan — which, for an NSF award, exists somewhere and would have answered finding 1
in a sentence. If it is on the site, I did not find it in forty-five minutes, and that is
itself the finding.

## My signature question

*If this project ended tomorrow, what would remain usable, and who would hold it?*

**What would remain usable:** the static STAC catalogs and the GeoJSON station inventories,
because they are plain files in public GitHub repositories under MIT and would keep resolving
for as long as GitHub hosts them; the book, under CC BY 4.0; and the conventions themselves —
the four-part provenance standard and the Landlab field-name vocabulary are ideas, and ideas
survive their authors. **What would not:** anything in `s3://cresst`, because it is an
unfunded object store laid out under individual usernames; the dashboard, which depends on a
branch pointer in one repository plus five live external ArcGIS and Google endpoints; and every
data product, because none of them has a version, a DOI, or an archive of record.

**Who would hold it:** nobody named. Three institutions hold the awards (UW, UAF, EarthScope
Consortium) and the site never says which of them, if any, holds the artefacts. Concretely,
these are the artefacts whose survival currently depends on an individual rather than an
institution:

1. Every product under `s3://cresst/{user}/` — the path *is* a person.
2. The credentials themselves — GAIA-D-004: "Credentials live in a password manager shared by
   the Lead PI and one other person."
3. The project record — how-we-work names the risk itself: "over five years, postdocs and
   students cycle through while the PI is the only continuous thread," and the mitigation is a
   private notes repository plus a weekly digest, both inside an organisation with no named
   institutional owner.
4. The metrics — collected by `metrics-observatory`, a repository I could not find, publishing
   to a `latest.json` that 404s.
5. Every repository lacking a licence, which nobody can legally inherit no matter who holds the
   account.

The project has thought harder about single points of failure than most projects I assess —
it names the PI-as-bottleneck problem in its own words. It has not yet applied that thinking to
its data. That is the gap, and it is a small enough gap to close: an institutional home, a
`products/` namespace, and one tagged release would move this from "interesting to watch" to
"assessable as a dependency."
