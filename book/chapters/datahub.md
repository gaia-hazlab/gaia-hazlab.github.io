# DataHub

## Overview

We are working on access first: getting data streams from several agencies into one place for our Washington State projects. We're after precipitation, streamflow, and seismic data. Two products are in progress, a dashboard for visualization and a command-line platform for Python-native queries.

## Datasets

The dashboard below carries static layers plus sensor and event metadata, so a researcher from one discipline can see what else is recording in the same place. Every sensor measures the physical state of the environment; they differ in which part of it they see.

:::{iframe} https://gaia-hazlab.github.io/catalog/
:width: 100%
GAIA CRESST Catalog
:::

The map shows the data streams the project teams are working with. Its only job is to put in-situ stations on the same view as the GIS layers and remote sensing observations; the code that builds it is at [gaia-hazlab/catalog](https://github.com/gaia-hazlab/catalog).

## Analysis

Click a station and you get a link to the provider's landing page, where the data are available through a web interface. Two examples near Stehekin, Washington: [UW/DREAM](https://ds.iris.edu/mda/UW/DREAM) and [STRW1](https://explore.synopticdata.com/STRW1/metadata).

### Programmatic access

We are still gathering input from the groups on how they want to reach the data; that thread is [here](https://github.com/gaia-hazlab/gaia-hazlab.github.io). Most station data is public and served over APIs, so a few lines of Python will get you a time series for whatever window you need:

This needs an API key from Synoptic, [free for academic use](https://synopticdata.com/open-access-program/). Export it as `SYNOPTIC_TOKEN` and the block below runs as-is:

```python
import os

import pandas as pd
import requests

url = "https://api.synopticdata.com/v2/stations/timeseries"
params = {
    "token": os.environ["SYNOPTIC_TOKEN"],
    "stid": "STRW1",          # Stehekin, WA
    "start": "202512010000",  # YYYYMMDDHHMM, UTC
    "end": "202512310000",
}

data = requests.get(url, params=params).json()
df = pd.DataFrame(data["STATION"][0]["OBSERVATIONS"])
```


## Roadmap

We plan to write a small Python client that wraps the existing API tools and stages the datasets each research group needs. It may also handle reprojection onto common grids and reference frames, so that data drop into an analysis or an ML pipeline without a conversion step in between.

For the concrete architecture (the `s3://cresst` object store, the static STAC catalogs, and `gaia-cli`) and a repo-by-repo migration path that aligns our data-prep repositories with the DataHub, see the [DataHub Integration Guide](datahub-integration-guide). It is driven by the data requirements of the [Soil Reanalysis Product](pillar-1-soil-reanalysis).

## Data inventories

Per-hazard inventories catalog every dataset a digital twin uses — raw external products, deterministically derived layers, and model outputs — with sources/APIs, access sensitivity, spatial/temporal resolution, limitations, and the models behind each derived product:

- [Data Inventory](datahub-inventory) — shallow & deep-seated landslide DT (used by the [Landslides](hazard-landslides) hazard page).
