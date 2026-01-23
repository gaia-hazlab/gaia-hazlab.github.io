# GAIA HazLab Sensor Dashboard

Interactive geospatial visualization dashboard for hazard monitoring sensors and layers using Plotly Dash.

## Features

- **Sensor Networks**: Seismic stations, river gages, meteorological stations
- **Hazard Layers**: Active fault lines, watershed boundaries
- **Interactive Map**: Toggle layers, zoom, pan, hover for details
- **Data Sources**: Fetches from GitHub Pages, monthly updates via GitHub Actions
- **Map Styles**: OpenStreetMap (default), Mapbox satellite (with token)

## Local Development

### Prerequisites

- Python 3.11+
- pip or conda

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Dashboard will be available at `http://localhost:8050`

### Environment Variables

- `DATA_SOURCE_URL`: URL to sensor data (default: `https://gaia-hazlab.github.io/website/data`)
- `MAPBOX_TOKEN`: Optional Mapbox token for satellite/terrain layers

## Deployment

### Option 1: Google Cloud Run (Recommended)

```bash
# Install gcloud CLI
# https://cloud.google.com/sdk/docs/install

# Deploy to Cloud Run
gcloud run deploy gaia-sensor-dashboard \
  --source . \
  --region us-west1 \
  --allow-unauthenticated \
  --set-env-vars DATA_SOURCE_URL=https://gaia-hazlab.github.io/website/data

# With Mapbox token
gcloud run deploy gaia-sensor-dashboard \
  --source . \
  --region us-west1 \
  --allow-unauthenticated \
  --set-env-vars DATA_SOURCE_URL=https://gaia-hazlab.github.io/website/data,MAPBOX_TOKEN=your_token_here
```

Dashboard will be available at the Cloud Run URL (e.g., `https://gaia-sensor-dashboard-xyz.run.app`)

### Option 2: Google App Engine

```bash
# Deploy to App Engine
gcloud app deploy app.yaml

# Set Mapbox token (optional)
gcloud app deploy app.yaml --set-env-vars MAPBOX_TOKEN=your_token_here
```

### Option 3: Heroku

```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Create app
heroku create gaia-sensor-dashboard

# Set environment variables
heroku config:set DATA_SOURCE_URL=https://gaia-hazlab.github.io/website/data

# Deploy
git push heroku main
```

### Option 4: PythonAnywhere

1. Upload files to PythonAnywhere
2. Create a new web app (Flask)
3. Set working directory to dashboard folder
4. Set WSGI file to point to `app.server`
5. Reload web app

## Data Updates

Sensor data is automatically refreshed monthly via GitHub Actions workflow (`.github/workflows/update-sensor-data.yml`).

To manually refresh data, click the "Refresh Data" button in the dashboard.

## Embedding in Website

Add to MyST Markdown:

```markdown
<iframe src="https://your-dashboard-url.com" width="100%" height="800px" frameborder="0"></iframe>
```

Or in HTML:

```html
<div style="width: 100%; height: 800px;">
    <iframe src="https://your-dashboard-url.com" 
            width="100%" 
            height="100%" 
            frameborder="0"
            style="border: none;">
    </iframe>
</div>
```

## Architecture

- **Frontend**: Dash (React-based)
- **Backend**: Flask
- **Data**: JSON from GitHub Pages
- **Map**: Plotly Scattermapbox with OpenStreetMap or Mapbox
- **Deployment**: Cloud Run / App Engine / Heroku / PythonAnywhere

## Data Schema

See `../website/data/sensors/README.md` and `../website/data/layers/README.md` for data format specifications.

## Troubleshooting

### CORS Issues

If fetching data from GitHub Pages fails, ensure:
1. Data files are committed and pushed
2. GitHub Pages is enabled
3. Files are accessible at `https://gaia-hazlab.github.io/website/data/`

### Map Not Displaying

- Check browser console for errors
- Verify `MAPBOX_TOKEN` is set if using Mapbox styles
- Try using `open-street-map` style (no token required)

### Slow Performance

- Enable caching for data requests
- Use Cloud Run with min_instances > 0
- Optimize GeoJSON polygon complexity

## License

Part of the GAIA HazLab project. See main repository LICENSE.

## Contact

For issues or questions, open an issue in the main repository.
