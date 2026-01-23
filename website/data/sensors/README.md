# Sensor Data

This directory contains metadata for various sensor networks used in hazard monitoring.

## File Structure

- `seismic_stations.json` - Seismic monitoring stations
- `river_gages.json` - River and stream gages
- `met_stations.json` - Meteorological stations

## Data Schema

### Seismic Stations

```json
{
  "stations": [
    {
      "id": "station_code",
      "name": "Station Name",
      "network": "Network Code",
      "lat": 47.6062,
      "lon": -122.3321,
      "elevation": 100.0,
      "start_date": "2020-01-01",
      "status": "active",
      "sensor_type": "broadband"
    }
  ]
}
```

### River Gages

```json
{
  "gages": [
    {
      "id": "gage_id",
      "name": "Gage Name",
      "lat": 47.6062,
      "lon": -122.3321,
      "elevation": 50.0,
      "drainage_area_km2": 1234.5,
      "status": "active",
      "agency": "USGS"
    }
  ]
}
```

### Met Stations

```json
{
  "stations": [
    {
      "id": "station_id",
      "name": "Station Name",
      "lat": 47.6062,
      "lon": -122.3321,
      "elevation": 200.0,
      "status": "active",
      "variables": ["temperature", "precipitation", "wind"],
      "agency": "NOAA"
    }
  ]
}
```

## Data Sources

Data is refreshed monthly via GitHub Actions workflow from:
- Seismic: IRIS/FDSN web services
- River: USGS National Water Information System
- Met: NOAA/NWS stations

## S3 Integration (Future)

For larger datasets and shapefiles, data can be fetched from S3:
- Bucket: `s3://gaia-hazlab-data/sensors/`
- Access: Public read
