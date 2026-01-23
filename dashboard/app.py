"""
GAIA HazLab Sensor Dashboard
Interactive geospatial visualization of hazard monitoring sensors and layers.

This Dash application displays:
- Seismic monitoring stations
- River and stream gages
- Meteorological stations
- Hazard layers (faults, watersheds)

Data is fetched from GitHub Pages and can be updated monthly via GitHub Actions.
"""

import dash
from dash import dcc, html, Input, Output, State
import plotly.graph_objects as go
import json
import requests
import os
from typing import Dict, List, Any

# Configuration
GITHUB_PAGES_URL = os.getenv(
    'DATA_SOURCE_URL', 
    'https://gaia-hazlab.github.io/website/data'
)
MAPBOX_TOKEN = os.getenv('MAPBOX_TOKEN', '')  # Optional, for satellite/terrain layers

# Initialize Dash app
app = dash.Dash(__name__, title="GAIA HazLab Sensor Dashboard")
server = app.server  # For deployment

# Map style configuration
MAP_STYLE = 'open-street-map' if not MAPBOX_TOKEN else 'mapbox://styles/mapbox/satellite-streets-v11'

def fetch_json_data(url: str) -> Dict[str, Any]:
    """Fetch JSON data from URL with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return {}

def load_sensor_data() -> Dict[str, Any]:
    """Load all sensor data from GitHub Pages."""
    data = {
        'seismic': fetch_json_data(f'{GITHUB_PAGES_URL}/sensors/seismic_stations.json'),
        'river': fetch_json_data(f'{GITHUB_PAGES_URL}/sensors/river_gages.json'),
        'met': fetch_json_data(f'{GITHUB_PAGES_URL}/sensors/met_stations.json'),
        'faults': fetch_json_data(f'{GITHUB_PAGES_URL}/layers/faults.geojson'),
        'watersheds': fetch_json_data(f'{GITHUB_PAGES_URL}/layers/watersheds.geojson')
    }
    return data

def create_map_figure(data: Dict[str, Any], 
                     show_seismic: bool = True,
                     show_river: bool = True,
                     show_met: bool = True,
                     show_faults: bool = True,
                     show_watersheds: bool = True) -> go.Figure:
    """Create Plotly map figure with sensor locations and layers."""
    
    fig = go.Figure()
    
    # Add seismic stations
    if show_seismic and 'stations' in data.get('seismic', {}):
        stations = data['seismic']['stations']
        lats = [s['lat'] for s in stations]
        lons = [s['lon'] for s in stations]
        names = [f"{s['id']}<br>{s['name']}<br>Type: {s['sensor_type']}" for s in stations]
        
        fig.add_trace(go.Scattermapbox(
            lat=lats,
            lon=lons,
            mode='markers',
            marker=dict(size=10, color='red'),
            text=names,
            name='Seismic Stations',
            hoverinfo='text'
        ))
    
    # Add river gages
    if show_river and 'gages' in data.get('river', {}):
        gages = data['river']['gages']
        lats = [g['lat'] for g in gages]
        lons = [g['lon'] for g in gages]
        names = [f"{g['id']}<br>{g['name']}<br>Drainage: {g['drainage_area_km2']:.1f} km²" for g in gages]
        
        fig.add_trace(go.Scattermapbox(
            lat=lats,
            lon=lons,
            mode='markers',
            marker=dict(size=10, color='blue'),
            text=names,
            name='River Gages',
            hoverinfo='text'
        ))
    
    # Add meteorological stations
    if show_met and 'stations' in data.get('met', {}):
        stations = data['met']['stations']
        lats = [s['lat'] for s in stations]
        lons = [s['lon'] for s in stations]
        names = [f"{s['id']}<br>{s['name']}<br>Elev: {s['elevation']:.0f} m" for s in stations]
        
        fig.add_trace(go.Scattermapbox(
            lat=lats,
            lon=lons,
            mode='markers',
            marker=dict(size=10, color='green'),
            text=names,
            name='Met Stations',
            hoverinfo='text'
        ))
    
    # Add fault lines
    if show_faults and data.get('faults', {}).get('features'):
        for feature in data['faults']['features']:
            coords = feature['geometry']['coordinates']
            lats = [c[1] for c in coords]
            lons = [c[0] for c in coords]
            name = feature['properties']['name']
            mag = feature['properties'].get('magnitude', 'unknown')
            
            fig.add_trace(go.Scattermapbox(
                lat=lats,
                lon=lons,
                mode='lines',
                line=dict(width=3, color='darkred'),
                text=f"{name}<br>Max Magnitude: {mag}",
                name=name,
                hoverinfo='text',
                showlegend=False
            ))
    
    # Add watershed polygons
    if show_watersheds and data.get('watersheds', {}).get('features'):
        for feature in data['watersheds']['features']:
            coords = feature['geometry']['coordinates'][0]
            lats = [c[1] for c in coords]
            lons = [c[0] for c in coords]
            name = feature['properties']['name']
            area = feature['properties']['area_km2']
            
            fig.add_trace(go.Scattermapbox(
                lat=lats,
                lon=lons,
                mode='lines',
                line=dict(width=2, color='cyan'),
                fill='toself',
                fillcolor='rgba(0, 255, 255, 0.1)',
                text=f"{name}<br>Area: {area:.1f} km²",
                name=name,
                hoverinfo='text',
                showlegend=False
            ))
    
    # Center map on Washington State
    center_lat = 47.5
    center_lon = -121.5
    
    # Update layout
    fig.update_layout(
        mapbox=dict(
            style=MAP_STYLE,
            accesstoken=MAPBOX_TOKEN if MAPBOX_TOKEN else None,
            center=dict(lat=center_lat, lon=center_lon),
            zoom=6
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        height=700,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255, 255, 255, 0.8)"
        )
    )
    
    return fig

# App layout
app.layout = html.Div([
    html.Div([
        html.H1("GAIA HazLab Sensor Dashboard", 
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '10px'}),
        html.P("Interactive visualization of hazard monitoring sensors and geospatial layers",
               style={'textAlign': 'center', 'color': '#7f8c8d', 'marginBottom': '20px'})
    ]),
    
    # Control panel
    html.Div([
        html.Div([
            html.H4("Sensor Networks", style={'marginBottom': '10px'}),
            dcc.Checklist(
                id='sensor-toggles',
                options=[
                    {'label': ' Seismic Stations', 'value': 'seismic'},
                    {'label': ' River Gages', 'value': 'river'},
                    {'label': ' Met Stations', 'value': 'met'}
                ],
                value=['seismic', 'river', 'met'],
                style={'marginBottom': '20px'},
                labelStyle={'display': 'block', 'marginBottom': '5px'}
            ),
            
            html.H4("Hazard Layers", style={'marginBottom': '10px'}),
            dcc.Checklist(
                id='layer-toggles',
                options=[
                    {'label': ' Fault Lines', 'value': 'faults'},
                    {'label': ' Watersheds', 'value': 'watersheds'}
                ],
                value=['faults', 'watersheds'],
                labelStyle={'display': 'block', 'marginBottom': '5px'}
            ),
            
            html.Hr(style={'marginTop': '20px', 'marginBottom': '20px'}),
            
            html.Button('Refresh Data', id='refresh-button', n_clicks=0,
                       style={'width': '100%', 'padding': '10px', 'backgroundColor': '#3498db', 
                              'color': 'white', 'border': 'none', 'borderRadius': '4px',
                              'cursor': 'pointer'})
        ], style={'padding': '20px', 'backgroundColor': '#ecf0f1', 'borderRadius': '8px'}),
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px'}),
    
    # Map container
    html.Div([
        dcc.Graph(id='sensor-map', config={'displayModeBar': True, 'scrollZoom': True})
    ], style={'width': '78%', 'display': 'inline-block', 'padding': '20px'}),
    
    # Hidden div to store data
    dcc.Store(id='sensor-data-store')
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#ffffff'})

# Callback to load/refresh data
@app.callback(
    Output('sensor-data-store', 'data'),
    Input('refresh-button', 'n_clicks')
)
def load_data(n_clicks):
    """Load sensor data from GitHub Pages."""
    return load_sensor_data()

# Callback to update map
@app.callback(
    Output('sensor-map', 'figure'),
    Input('sensor-data-store', 'data'),
    Input('sensor-toggles', 'value'),
    Input('layer-toggles', 'value')
)
def update_map(data, sensor_toggles, layer_toggles):
    """Update map based on toggle selections."""
    if not data:
        data = load_sensor_data()
    
    show_seismic = 'seismic' in sensor_toggles
    show_river = 'river' in sensor_toggles
    show_met = 'met' in sensor_toggles
    show_faults = 'faults' in layer_toggles
    show_watersheds = 'watersheds' in layer_toggles
    
    return create_map_figure(data, show_seismic, show_river, show_met, 
                            show_faults, show_watersheds)

if __name__ == '__main__':
    # For local development
    app.run_server(debug=True, host='0.0.0.0', port=8050)
