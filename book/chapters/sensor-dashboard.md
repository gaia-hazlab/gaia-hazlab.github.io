# Sensor Dashboard

Interactive geospatial visualization of hazard monitoring sensors and layers across Washington State.

## Overview

The Sensor Dashboard provides a unified interface to explore and analyze:

- **Seismic Monitoring Stations**: Real-time earthquake detection and ground motion sensors from the Pacific Northwest Seismic Network (PNSN)
- **River Gages**: Stream flow and water level monitoring from USGS National Water Information System
- **Meteorological Stations**: Weather and climate monitoring from NOAA, SNOTEL, and other networks
- **Hazard Layers**: Active fault lines, watershed boundaries, and other geospatial features

## Interactive Map

<div style="width: 100%; height: 850px; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; margin: 20px 0;">
    <iframe src="DASHBOARD_URL_PLACEHOLDER" 
            width="100%" 
            height="100%" 
            frameborder="0"
            style="border: none;">
    </iframe>
</div>

**Note**: Replace `DASHBOARD_URL_PLACEHOLDER` with the deployed dashboard URL after deployment to Cloud Run, Heroku, or PythonAnywhere.

## Features

### Sensor Networks

- **Seismic Stations** (red markers): Broadband seismometers and strong motion accelerometers
- **River Gages** (blue markers): Streamflow, stage height, and water quality sensors
- **Met Stations** (green markers): Temperature, precipitation, snow depth, and wind measurements

### Hazard Layers

- **Active Faults** (red lines): Major fault zones including Seattle Fault, Southern Whidbey Island Fault, and Cascadia Subduction Zone
- **Watersheds** (cyan polygons): HUC-12 watershed boundaries for hydrological analysis

### Controls

- Toggle individual sensor networks and layers on/off
- Click markers for detailed station information
- Zoom and pan to explore specific regions
- Refresh data to get latest updates

## Data Sources

All sensor metadata is stored in the repository at [`website/data/`](https://github.com/gaia-hazlab/gaia-hazlab.github.io/tree/main/website/data) and automatically updated monthly via GitHub Actions.

### Seismic Data
- **Source**: [Pacific Northwest Seismic Network](https://pnsn.org)
- **Networks**: UW (University of Washington), CC (Canadian National Seismic Network)
- **Update Frequency**: Monthly

### River Gage Data
- **Source**: [USGS National Water Information System](https://waterdata.usgs.gov/nwis)
- **Coverage**: Major rivers and streams in Washington State
- **Update Frequency**: Monthly

### Meteorological Data
- **Sources**: NOAA, SNOTEL (Snow Telemetry), National Park Service
- **Variables**: Temperature, precipitation, snow depth, wind speed/direction
- **Update Frequency**: Monthly

### Hazard Layers
- **Faults**: [USGS Quaternary Fault and Fold Database](https://www.usgs.gov/natural-hazards/earthquake-hazards/faults)
- **Watersheds**: [USGS Watershed Boundary Dataset](https://www.usgs.gov/national-hydrography/watershed-boundary-dataset)

## Technical Architecture

The dashboard is built with:

- **Frontend**: [Plotly Dash](https://dash.plotly.com/) - Python web application framework
- **Mapping**: [Plotly Scattermapbox](https://plotly.com/python/scattermapbox/) with OpenStreetMap tiles
- **Data Storage**: JSON and GeoJSON files hosted on GitHub Pages
- **Deployment**: Google Cloud Run (or Heroku/PythonAnywhere)
- **Updates**: Monthly automated data refresh via GitHub Actions

## Use Cases

### Research Applications

1. **Multi-Hazard Monitoring**: Correlate seismic, hydrological, and meteorological data
2. **Site Selection**: Identify sensor gaps and plan new monitoring stations
3. **Event Response**: Quickly assess sensor coverage during hazard events
4. **Data Discovery**: Find relevant sensors for specific study areas

### Educational Applications

1. **Hazard Awareness**: Visualize fault locations relative to populated areas
2. **Watershed Analysis**: Understand drainage patterns and river networks
3. **Climate Monitoring**: Explore elevation-dependent climate variables
4. **Infrastructure Planning**: Assess sensor density for critical infrastructure

## API and Programmatic Access

Sensor data can be accessed programmatically:

```python
import requests
import pandas as pd

# Fetch seismic station data
url = "https://gaia-hazlab.github.io/website/data/sensors/seismic_stations.json"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data['stations'])
print(df.head())
```

See [DataHub](datahub.md) for more examples of programmatic data access.

## Future Enhancements

- **Real-time Data Streams**: Live sensor readings and event notifications
- **Time Series Visualization**: Historical data plots for selected stations
- **3D Terrain View**: Elevation-aware visualization with DEM integration
- **Advanced Filtering**: Filter by sensor type, date range, data availability
- **Download Options**: Export filtered sensor lists and spatial layers
- **Mobile Support**: Responsive design for field use

## Related Chapters

- [DataHub](datahub.md) - Data formats and access methods
- [HazEvalHub](hazevalhub.md) - Evaluation frameworks using sensor data
- [Use Cases](wa-2025-stehekin.md) - Examples of sensor data in action

## Feedback

Found an issue or have a suggestion? Open an issue on [GitHub](https://github.com/gaia-hazlab/gaia-hazlab.github.io/issues).
