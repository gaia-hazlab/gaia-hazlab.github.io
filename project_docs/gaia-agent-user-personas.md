# Five representative users of GAIA research agents

*Drafted for the eScience Institute's persona request against the `gaia-data-downloader` community plugin (uw-ssec/rse-plugins).*
*Prepared 8 September 2026.*

## How these were built

The five personas below are composites drawn from the current GAIA-HazLab roster of 24 people
(`website/data/team.json`): seismologists and geodesists, hydrologists and geomorphologists,
SAR specialists at a NASA DAAC, atmospheric scientists, geotechnical engineers, research software
engineers, a state monitoring center, and one computer science undergraduate. The roster spans a
wide range of both domain and software fluency, and the personas are chosen to sample that range
rather than to describe an average member.

The agent they are using is the kind of agent the plugin already implements: one that turns a
stated data need into a configured, runnable download script over CONUS404, HRRR, WRF-CMIP6,
PRISM, Stage IV, USGS streamflow, DAYMET, SRTM, Synoptic stations, and IRIS/EarthScope waveforms.

**Names and biographical details are invented.** No persona should be read as a description of a
specific member of the team; the roster mapping at the end shows which positions each one stands for.

---

## 1. Priya Raghunathan — second-year PhD student working across seismology and hydrology

**Setting.** An R1 Earth sciences department. Her project asks whether seasonal groundwater change
leaves a signature in ambient noise velocity, so she needs waveforms and precipitation and
streamflow over the same catchment and the same three years.

**What she brings.** A solid course in Python and one in signal processing. She has used ObsPy under
supervision. She has never opened a GRIB2 file, does not know what a STAC catalog is, and has no
sense of how large a CONUS404 subset becomes before it is downloaded.

**What she asks the agent.** "Get me hourly precipitation and daily mean temperature over the
Nisqually catchment for 2019 through 2022, on the same grid as my station list." She will express
the region as a place name and the variables in the words her advisor used, which may not match any
variable name in the archive.

**What success looks like.** A script she can read, a directory of files with a manifest that records
the source, version, spatial subset, and access date, and a plot she can show at group meeting the
same afternoon. The provenance matters as much as the data: she will be asked in six months where a
number came from.

**Where she gets stuck.** She cannot tell a plausible wrong answer from a right one. If the agent
silently maps "precipitation" to an accumulation variable when she wanted a rate, or picks the
nearest available grid rather than the one her stations sit on, the error survives into a figure.
Her second problem is disk: an unbounded request fills her laptop and she abandons the tool.

**Implication for the agent.** State the resolved variable name, units, grid, and time convention
back to her before downloading, and estimate the volume. Treat the confirmation step as the main
product for this user.

---

## 2. Tomás Belliveau — mid-career research scientist entering an unfamiliar data type

**Setting.** A soft-money research scientist with fifteen years in one observational method, now
contributing to a multi-hazard project that requires a second one. He described his own AI
experience on the project intake form as "here to learn."

**What he brings.** Deep judgment about his own data, including which artifacts are instrumental and
which are real. In the new archive he has none of that judgment, and he knows it. He writes
competent scripts and dislikes tools that hide what they did.

**What he asks the agent.** "I know what I want physically. Tell me what the equivalent product is
here, and what its known limitations are." He is asking for translation between archive
vocabularies as much as for a download.

**What success looks like.** The agent names the candidate products, says plainly how they differ,
cites the archive documentation, and writes a script whose intermediate steps he can inspect. He
will read the code before running it and will change parts of it.

**Where he gets stuck.** Confident prose about a dataset he cannot verify. One fabricated citation or
one invented processing level ends his trust in the whole tool, and he will say so in a group
meeting. He is also the person most likely to ask a question that falls outside the ten supported
sources, and a vague failure there reads to him as unreliability.

**Implication for the agent.** Distinguish what is supported from what is not, in one sentence,
early. Link to primary documentation for every claim about a product's content.

---

## 3. Dana Okonkwo — research software engineer at a data facility

**Setting.** A cloud data platform serving analysis-ready Earth observation products. Dana maintains
pipelines other people depend on and reviews pull requests for a shared library.

**What she brings.** Fluency in the whole stack: STAC, Zarr, Dask, xarray, cloud credentials,
CI. She does not need help downloading anything. She uses the agent to remove the first two hours
from a task she already understands, and she evaluates its output the way she evaluates a
contributor's first PR.

**What she asks the agent.** "Write the fetch layer for this workflow: chunked, resumable, cached,
with pinned dependencies and no credentials in the file." Later: "Add a new source to the plugin and
give me the tests."

**What success looks like.** Code she would merge. Pinned versions, retries with backoff, an
explicit cache directory, credentials read from the environment, and a failure that names the
missing granule rather than raising a bare exception. She is also the person who extends the plugin
itself, so she wants the download-script-dev path documented as carefully as the user-facing one.

**Where she gets stuck.** Generated code that works once on one machine. Unpinned imports, silent
`except: pass`, hard-coded paths, and a script that re-downloads everything on the second run all
cost her more time than writing it herself would have.

**Implication for the agent.** Treat the maintainer as a first-class user. The quality bar for
generated code is set by this persona, and meeting it also serves everyone above.

---

## 4. Hal Vestergaard — duty scientist at a regional monitoring center

**Setting.** A state seismic and volcano monitoring operation. An event has happened: a magnitude 5.9
offshore, a slope failure reported by a pilot, a volcano with a week of unrest. Hal is on shift and
someone from an emergency management agency will call within the hour.

**What he brings.** Twenty years of operational judgment and no patience. He works under time
pressure, often on a laptop over a poor connection, and everything he says will be quoted.

**What he asks the agent.** "Everything you can get for this box and these six hours: waveforms,
nearby stream gauges, the last precipitation, elevation. Now."

**What success looks like.** Partial results fast, with an explicit account of what is missing and
why. A gap in the record must be reported as a gap. He needs to be able to state, on a call, which
archive each product came from and when it was retrieved.

**Where he gets stuck.** Silence during a long download, and any output that blurs the line between
retrieved data and inference. A dataset the agent describes but cannot actually reach is worse than
no answer, because he will have already told someone it exists.

**Implication for the agent.** Stream progress, return partial results, and separate retrieved
observations from anything the agent computed or assumed. Provenance here is an operational
requirement rather than a courtesy.

---

## 5. Wren Alcott — undergraduate in computer science at a summer hackweek

**Setting.** A one-week data science event, or a capstone with a faculty mentor. Wren writes good
software and has taken no Earth science courses. They joined because agentic systems interest them
and the science problem came with the position.

**What they bring.** Comfort with APIs, notebooks, and version control, and enough curiosity to read
the generated code closely. No physical intuition for the variables, and no idea which of the
returned numbers should look strange.

**What they ask the agent.** "What data would I need to tell whether a hillside is likely to fail?"
The question is upstream of any download, and a good answer shapes the rest of the week.

**What success looks like.** The agent teaches while it works: it names the quantities, explains why
each one is relevant, shows the request it is about to make, and leaves behind a notebook Wren can
modify. By Friday they can defend their choice of dataset to a room.

**Where they get stuck.** An agent that answers so completely that nothing is learned, and cost. A
single careless request against a continental hourly product can exhaust a shared cloud budget or a
laptop disk in an afternoon, and Wren has no way to anticipate that.

**Implication for the agent.** Offer a dry run with a size and cost estimate before any large
transfer, and make the reasoning visible. This persona is also the clearest test of whether the tool
is usable by someone outside the funded team, which matters for the plugin's broader impact claims.

---

## What the five imply together

1. **Provenance is a default, not a flag.** Four of the five need to state later where a number came
   from. A manifest recording source, version, subset, and access time should be written on every run.
2. **Confirm the interpretation before spending.** The step where the agent restates the resolved
   variable, grid, units, and volume serves the novice, the crosser, and the undergraduate at once.
3. **Fail with a name.** Every persona is damaged by a vague failure, and the operational one is
   damaged most.
4. **Say what is out of scope immediately.** Ten sources are supported; requests outside them arrive
   constantly and deserve a direct answer.
5. **Generated code is reviewed by an engineer.** The maintainer persona sets the quality bar, and
   code that clears it is also the code the student can read.

## Roster coverage

| Persona | Roster positions represented | Sources most exercised | Hardest requirement |
|---|---|---|---|
| Priya, PhD student | PhD students in seismology, hydrology, geomorphology, geotechnical engineering (6 of 24) | IRIS waveforms, CONUS404, PRISM, USGS streamflow | Correct variable resolution, volume estimate |
| Tomás, research scientist | Research scientists in DAS, atmospheric science, and senior personnel entering AI work (4 of 24) | Stage IV, HRRR, WRF-CMIP6, DAYMET | Honest cross-archive translation, real citations |
| Dana, research software engineer | Data facility staff and research computing leadership at ASF, EarthScope, eScience (5 of 24) | All, plus the plugin's own extension path | Mergeable code, documented dev workflow |
| Hal, duty scientist | State seismologist, volcano and geodetic monitoring faculty (3 of 24) | IRIS waveforms, Synoptic, USGS streamflow, SRTM | Speed, partial results, explicit gaps |
| Wren, undergraduate | CS undergraduate and CSE-side co-PI's students (2 of 24), plus hackweek participants outside the team | CONUS404, DEM/SRTM, USGS streamflow | Explanation, dry run, cost ceiling |

Faculty PIs and co-PIs are deliberately absent as a separate persona. In practice they use the agent
through one of the five above, most often through Dana's requirements when specifying and through
Priya's when advising.

---

*Plugin capabilities and the list of supported sources are taken from the `gaia-data-downloader`
README as of 8 September 2026. Roster counts are taken from `website/data/team.json` on the same
date and should be refreshed if the team page changes.*
