# Agentic Data Downloader

:::{note}
**Draft / scaffold.** Part of [GaiaAgent](gaia-agent). Agentic AI for discovering, downloading,
and staging the multi-source hazard data the digital twins consume — wrapping the
[DataHub](datahub) tooling so acquisition is on-demand and provenance-tracked.
:::

## Overview

The agentic downloader turns a natural-language or programmatic data request into a staged,
provenance-tracked dataset on `s3://cresst`, by orchestrating the existing data tooling:

- [`gaia-cli`](https://github.com/gaia-hazlab/gaia-cli) — the staging CLI (`gaia stage …`).
- [`gaia-data-downloaders`](https://github.com/gaia-hazlab/gaia-data-downloaders) — reproducible
  multi-source download recipes (CONUS404, HRRR, PRISM, Stage IV, USGS gauges, …).
- the STAC catalogs ([`solus-stac`](https://github.com/gaia-hazlab/solus-stac),
  [`prism-stac`](https://github.com/gaia-hazlab/prism-stac)) for discovery.

It is driven by the [`gaia-agentic-ai`](https://github.com/gaia-hazlab/gaia-agentic-ai) project,
using shared [`gaia-skills`](https://github.com/gaia-hazlab/gaia-skills) and the
[`gaia-literature-kb`](https://github.com/gaia-hazlab/gaia-literature-kb) knowledge base.

## How it fits

See the [DataHub Integration Guide](datahub-integration-guide) for the provenance standard and
the `s3://cresst` + STAC + `gaia-cli` architecture the downloader automates.

## Open questions & roadmap

## References
