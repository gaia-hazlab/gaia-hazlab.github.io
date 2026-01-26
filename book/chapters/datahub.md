# DataHub

## Overview

We are currently focused on streamlining access to data streams from different agencies for our research projects in Washington State. In particular, we're after precipitation, streamflow, and seismic data.

## Datasets

### In Situ Sensors

:::{iframe} http://[::]:3000/remote-data.html
:width: 100%
Station Catalog
:::

While the above map provides a nice overview, you can use use geojson.io to explore the inventory with more functionality (change basemaps, draw polygons of interest, etc)! https://geojson.io/#id=gist:scottyhq/9eaceb340de48082f6eed2620182a507

Or work with our combined GeoJSON inventory in Python:

```python
import geopandas as gpd
inventory = 'https://gist.githubusercontent.com/scottyhq/9eaceb340de48082f6eed2620182a507/raw/766ec6267e7b5168823ac9671f1e379e47182dab/combined-stations-wa-styled.geojson'
gf = gpd.read_file(inventory)
```

### Remote sensing data

* https://nisar-docs.asf.alaska.edu/availability-overview/
* ...


### Modeling data

* https://agdatacommons.nal.usda.gov/articles/dataset/Data_from_Soil_Landscapes_of_the_United_States_100-meter_SOLUS100_soil_property_maps_project_repository/25033856
* ...


## Programmatic access

Currently we're gathering input from groups on various approaches to data acccess here https://github.com/gaia-hazlab/gaia-hazlab.github.io

### Roadmap

We to create a simple Python client to stage relevant datasets for our research groups which will wrap existing API tools. The client may also facilitate reprojecting datasets to common grids and reference frames for easy analysis and ingestion into ML workflows.
