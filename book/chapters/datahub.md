# DataHub

## Overview

We are currently focused on streamlining access to data streams from different agencies for our research projects in Washington State. In particular, we're after precipitation, streamflow, and seismic data.

## Datasets

:::{iframe} https://gaia-hazlab.github.io/catalog/
:width: 100%
GAIA CRESST Catalog
:::

The above map renders data streams various teams are working with on this project. It is intended purely for visualizing the distribution of in-situ stations in the context of GIS layers and remote sensing observations and is created with code here https://github.com/gaia-hazlab/catalog.

## Analysis

Clicking on stations in the map above will provide links to data provider landing pages from which it is possible to access data via web interfaces. For example, these stations near Stehekin, Washington: https://ds.iris.edu/mda/UW/DREAM or https://explore.synopticdata.com/STRW1/metadata

### Programmatic access

Currently we're gathering input from groups on various approaches to data access here https://github.com/gaia-hazlab/gaia-hazlab.github.io. Most station data is public and provided via APIs, so a little bit of Python code will get you time series to analyze for a time period of interest:

This requires an API key from Synoptic (free for academic use) https://synopticdata.com/open-access-program/

```python
import pandas as pd
import requests
import os

dict(token = TOKEN,
     stid = "STRW1",
     start = "202512010000",
     end = "202512310000")

data = requests.get(url, params=params).json()
df = pd.DataFrame(data['STATION'][0]['OBSERVATIONS'])
```


## Roadmap

We plan to create a simple Python client to stage relevant datasets for our research groups which wraps existing API tools. The client may also facilitate reprojecting datasets to common grids and reference frames for easy analysis and ingestion into ML workflows.
