# Hazard Layers

This directory contains geospatial layer data for hazard visualization.

## File Structure

- `watersheds.geojson` - Watershed boundaries
- `faults.geojson` - Active fault lines
- `soil_properties.json` - Static soil property metadata

## Data Schema

### Watersheds (GeoJSON)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "id": "HUC_12_code",
        "name": "Watershed Name",
        "area_km2": 1234.5,
        "state": "WA"
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [[...]]
      }
    }
  ]
}
```

### Faults (GeoJSON)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "id": "fault_id",
        "name": "Fault Name",
        "type": "strike-slip",
        "slip_rate_mm_yr": 1.5,
        "last_event": "1872"
      },
      "geometry": {
        "type": "LineString",
        "coordinates": [[...]]
      }
    }
  ]
}
```

### Soil Properties

```json
{
  "layers": [
    {
      "id": "soil_moisture",
      "name": "Soil Moisture",
      "type": "raster",
      "source": "s3://gaia-hazlab-data/layers/soil_moisture.tif",
      "units": "volumetric"
    }
  ]
}
```

## Data Sources

- Watersheds: USGS Watershed Boundary Dataset (WBD)
- Faults: USGS Quaternary Fault and Fold Database
- Soil: USDA SSURGO/STATSGO2
- DEM: USGS 3DEP

## S3 Integration

Larger raster layers (DEMs, soil properties) stored in S3:
- Bucket: `s3://gaia-hazlab-data/layers/`
- Access: Public read
- Format: GeoTIFF, Cloud-Optimized GeoTIFF (COG)
