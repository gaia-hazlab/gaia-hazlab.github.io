"""Build the static STAC catalog behind the dashboard mockup.

Mockup only (proposal in project_coordination/10-dashboard-stac.md). Writes, under
website/mockups/dashboard-stac/:

  stac/catalog.json                     root catalog, one child per project
  stac/<project>/collection.json        one collection per project (extent, 3D viewer link)
  stac/<project>/<layer>/<layer>.json   one item per map layer
  data/<project>/*.geojson              layers derived here (Cascadia, Rainier only)

Inputs are local copies of two public pages, passed as arguments:

  cascadia_html   https://denolle-lab.github.io/cascadia_obs_ensemble/  (Atlas built 2026-11-22)
  rainier_index   https://denolle-lab.github.io/mt-rainier-source-simulation/gfdb/recip_1km_v1/index.json

Usage:
  python scripts/mockup/build_dashboard_stac.py <cascadia_html> <rainier_index> <fetched YYYY-MM-DD>

Standard library only. Rendering hints use two published STAC extensions (render, web-map-links);
menu grouping and vector styling use `gaia:` fields, which would need their own schema if adopted.
"""

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "website" / "mockups" / "dashboard-stac"
STAC_VERSION = "1.1.0"
EXT_RENDER = "https://stac-extensions.github.io/render/v2.0.0/schema.json"
EXT_WML = "https://stac-extensions.github.io/web-map-links/v1.2.0/schema.json"
CAT = "https://raw.githubusercontent.com/gaia-hazlab/catalog/refs/heads/main"
S3 = "https://gaia-hazlab-map-data.s3.us-west-2.amazonaws.com"
GIBS = "https://gibs.earthdata.nasa.gov/wms/epsg3857/best/wms.cgi"
COG_TYPE = "image/tiff; application=geotiff; profile=cloud-optimized"
GEOJSON = "application/geo+json"


def box(b):
    w, s, e, n = b
    return {"type": "Polygon", "coordinates": [[[w, s], [e, s], [e, n], [w, n], [w, s]]]}


def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1) + "\n")


def item(pid, lid, title, bbox, group, sub, *, start, end, assets=None, links=(), style=None,
         on=False, renders=None, disabled=None, provider=None):
    """One map layer as a STAC item. `disabled` is a reason string for layers not yet published."""
    exts = []
    if renders:
        exts.append(EXT_RENDER)
    if any(l["rel"] in ("xyz", "wms") for l in links):
        exts.append(EXT_WML)
    props = {"title": title, "datetime": None, "start_datetime": start, "end_datetime": end,
             "gaia:group": group, "gaia:subgroup": sub, "gaia:on": on}
    if style:
        props["gaia:style"] = style
    if renders:
        props["renders"] = renders
    if disabled:
        props["gaia:status"] = disabled
    if provider:
        props["providers"] = [{"name": provider, "roles": ["producer"]}]
    return {
        "type": "Feature", "stac_version": STAC_VERSION, "stac_extensions": exts,
        "id": lid, "collection": pid, "bbox": bbox, "geometry": box(bbox), "properties": props,
        "links": [
            {"rel": "collection", "href": "../collection.json", "type": "application/json"},
            {"rel": "parent", "href": "../collection.json", "type": "application/json"},
            {"rel": "root", "href": "../../catalog.json", "type": "application/json"},
            *links,
        ],
        "assets": assets or {},
    }


def geojson_asset(href, title):
    return {"data": {"href": href, "type": GEOJSON, "title": title, "roles": ["data"]}}


def cog_asset(href, title):
    return {"data": {"href": href, "type": COG_TYPE, "title": title, "roles": ["data"]}}


def collection(pid, title, description, bbox, interval, view, items, links=()):
    return {
        "type": "Collection", "stac_version": STAC_VERSION, "stac_extensions": [],
        "id": pid, "title": title, "description": description, "license": "other",
        "extent": {"spatial": {"bbox": [bbox]}, "temporal": {"interval": [interval]}},
        "gaia:view": view,
        "links": [
            {"rel": "root", "href": "../catalog.json", "type": "application/json"},
            {"rel": "parent", "href": "../catalog.json", "type": "application/json"},
            *links,
            *[{"rel": "item", "href": f"./{i['id']}/{i['id']}.json", "type": "application/geo+json",
               "title": i["properties"]["title"]} for i in items],
        ],
    }


def feature_collection(features):
    return {"type": "FeatureCollection", "features": features}


def pt(lon, lat, props):
    return {"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]}, "properties": props}


def bbox_of(fc, pad=0.05):
    xs, ys = [], []
    for f in fc["features"]:
        g = f["geometry"]
        coords = [g["coordinates"]] if g["type"] == "Point" else (
            g["coordinates"] if g["type"] == "LineString" else g["coordinates"][0])
        for x, y in coords:
            xs.append(x)
            ys.append(y)
    return [round(min(xs) - pad, 3), round(min(ys) - pad, 3), round(max(xs) + pad, 3), round(max(ys) + pad, 3)]


# ---------------------------------------------------------------- Washington (today's dashboard)
def washington():
    pid, B = "washington", [-126.5, 44.5, -114.5, 50.5]
    t = dict(start="2025-01-01T00:00:00Z", end="2025-12-31T23:59:59Z")
    pts = lambda lid, title, url, color, sub, prov: item(  # noqa: E731
        pid, lid, title, B, "Ground-based sensors", sub, **t, assets=geojson_asset(url, title),
        style={"kind": "points", "color": color}, on=True, provider=prov)
    cog = lambda lid, title, url, sub, rescale, cmap, prov, nodata=None, maxz=None: item(  # noqa: E731
        pid, lid, title, B, "Spatial imagery", sub, **t, assets=cog_asset(url, title), provider=prov,
        renders={"default": {"title": title, "assets": ["data"], "rescale": [rescale], "colormap_name": cmap,
                             **({"nodata": nodata} if nodata else {}),
                             **({"minmax_zoom": [0, maxz]} if maxz else {})}})
    wms = lambda lid, title, layer, prov, dims=None: item(  # noqa: E731
        pid, lid, title, B, "Spatial imagery", "Geological", **t, provider=prov,
        links=[{"rel": "wms", "href": GIBS, "type": "image/png", "title": title, "wms:layers": [layer],
                "wms:transparent": True, **({"wms:dimensions": dims} if dims else {})}])
    arcgis = lambda lid, title, url, color, prov, style: item(  # noqa: E731
        pid, lid, title, B, "Hazards & GIS", "Events & boundaries", **t,
        assets=geojson_asset(url, title), style={"color": color, **style}, provider=prov)
    dnr_fire = ("https://gis.dnr.wa.gov/site3/rest/services/Public_Wildfire/WADNR_PUBLIC_WD_WildFire_Data/"
                "MapServer/0/query?where=YEAR%20%3E%3D%202023%20AND%20ACRES%20%3E%20247&outFields=*&f=geojson")
    dnr_ls = ("https://services.arcgis.com/4x406oNViizbGo13/arcgis/rest/services/"
              "Recently_Reported_Landslides_in_Washington_State/FeatureServer/0/query?"
              "where=WATER_YEAR%20%3D%20'2025-2026'&outFields=*&f=geojson")
    huc8 = ("https://hydro.nationalmap.gov/arcgis/rest/services/wbd/FeatureServer/4/query?where=1%3D1"
            "&geometry=-124%2C45%2C-116%2C49&geometryType=esriGeometryEnvelope&inSR=4326"
            "&spatialRel=esriSpatialRelIntersects&outFields=name&f=geojson")
    items = [
        pts("seismometers", "Seismometers", CAT + "/seismic-stations.geojson", "#FF00BB", "Seismic", "IRIS / EarthScope"),
        pts("infrasound", "Infrasound", CAT + "/infrasound-stations.geojson", "#1A982F", "Seismic", "IRIS / EarthScope"),
        item(pid, "gnss", "GNSS / GPS", B, "Ground-based sensors", "Geodetic", **t, disabled="layer coming soon"),
        pts("precip", "Precipitation", CAT + "/precip-stations.geojson", "#1B04E9", "Meteorology", "Synoptic"),
        pts("snotel", "SNOTEL (snow)", CAT + "/snotel_stations.geojson", "#04E9E9", "Meteorology", "USDA NRCS"),
        pts("streamflow", "Streamflow gauges", CAT + "/streamflow-stations.geojson", "#E9AC04", "Hydrology", "USGS"),
        cog("stageiv", "Stage IV Precip (Dec 2025)", S3 + "/rainfall_4km.tif", "Atmospheric", [0, 700], "viridis", "NOAA Stage IV", nodata="nan"),
        cog("erm", "Max ERM (Dec 2025)", S3 + "/max_erm_4km.tif", "Atmospheric", [0, 3], "plasma", "UW Atmos. Sci.", nodata="nan"),
        cog("solus", "SOLUS100 soil depth", "https://storage.googleapis.com/solus100pub/anylithicdpt_cm_p.tif", "Geological", [0, 200], "gist_earth", "USDA SOLUS100", maxz=11),
        item(pid, "vs30", "USGS Vs30 mosaic", B, "Spatial imagery", "Geological", **t, provider="USGS",
             links=[{"rel": "xyz", "href": "https://earthquake.usgs.gov/arcgis/rest/services/eq/vs30_mosaic/MapServer/tile/{z}/{y}/{x}",
                     "type": "image/png", "title": "USGS Vs30 mosaic"}]),
        wms("aster", "ASTER GDEM color index", "ASTER_GDEM_Color_Index", "NASA GIBS"),
        wms("opera", "OPERA disturbance 2025", "OPERA_L3_DIST-ANN-HLS_Color_Index", "NASA GIBS / OPERA", {"TIME": "2025-01-01"}),
        item(pid, "eq", "2025 earthquake catalog", B, "Hazards & GIS", "Events & boundaries", **t,
             assets=geojson_asset(CAT + "/pnw_eq_catalog_2025.geojson", "2025 earthquake catalog"),
             style={"kind": "events", "color": "#d6604d", "size_by": "magnitude"}, provider="PNSN / USGS ComCat"),
        arcgis("wildfire", "WA DNR wildfires (≥2023)", dnr_fire, "#e2562a", "WA DNR", {"weight": 2, "fill": False, "label": "FIRENAME"}),
        arcgis("landslides", "WA DNR landslides WY2025", dnr_ls, "#c98a2b", "WA DNR", {"kind": "markers", "label": "DAMAGE_DESC"}),
        arcgis("huc8", "Watershed sub-basins (HUC8)", huc8, "#5fa0ff", "USGS WBD", {"weight": 1.5, "fillOpacity": 0.08, "label": "name"}),
    ]
    col = collection(pid, "Washington DataHub", "Colocated seismic, meteorological, hydrological and remote-sensing "
                     "layers across Washington State (today's dashboard, unchanged).", B,
                     ["2025-01-01T00:00:00Z", None], {"center": [47.4, -120.5], "zoom": 7}, items,
                     links=[{"rel": "via", "href": "https://github.com/gaia-hazlab/catalog", "type": "text/html",
                             "title": "Catalog source code"}])
    return pid, col, items, {}


# ---------------------------------------------------------------- Cascadia offshore (catalog v4 Atlas)
def cascadia(html_path, fetched):
    pid = "cascadia-offshore"
    h = Path(html_path).read_text(encoding="utf-8")
    i = h.index("const ATLAS = ") + len("const ATLAS = ")
    A, _ = json.JSONDecoder().raw_decode(h[i:])
    src = {"source": "https://denolle-lab.github.io/cascadia_obs_ensemble/", "atlas_built": A["meta"]["built"],
           "fetched": fetched}
    st = feature_collection([pt(s["lon"], s["lat"], {
        "network": s["net"], "station": s["sta"], "elevation_m": s["elev"], "ocean_bottom": s["sea"],
        "start": s["start"], "end": s["end"], "site": s.get("site", "")}) for s in A["stations"]])
    mt = feature_collection([pt(m["lon"], m["lat"], {
        "event_id": m["id"], "time": m["t"], "depth_km": m["dep"], "magnitude": m["mw"],
        "source": m["src"], "place": m.get("place", "")}) for m in A["tensors"]])
    pl = feature_collection([{"type": "Feature", "properties": {"name": p["name"]},
                              "geometry": {"type": "LineString", "coordinates": p["xy"]}} for p in A["plates"]])
    data = {"stations.geojson": st, "moment-tensors.geojson": mt, "plate-boundaries.geojson": pl}
    B = A["meta"]["region"]
    B = [B[0], B[2], B[1], B[3]]                       # Atlas stores [w, e, s, n]
    t = dict(start="2010-01-01T00:00:00Z", end="2016-12-31T23:59:59Z")
    rel = lambda f: f"../../../data/{pid}/{f}"  # noqa: E731  (item → data, relative)
    n_ev = A["meta"]["events"]["n"]
    items = [
        item(pid, "stations", f"Stations ({len(A['stations'])})", bbox_of(st), "Ground-based sensors",
             "Seismic (onshore + ocean bottom)", **t, assets=geojson_asset(rel("stations.geojson"), "Stations"),
             style={"kind": "points", "color": "#66ccf2"}, on=True, provider="EarthScope / FDSN"),
        item(pid, "events", f"Events, catalog v4 ({n_ev:,})", B, "Earthquakes", "Ensemble deep-learning catalog",
             **t, disabled="inlined in the Atlas page; needs its own file (step 2)"),
        item(pid, "moment-tensors", f"Moment tensors ({len(A['tensors'])})", bbox_of(mt), "Earthquakes",
             "Published solutions", **t, assets=geojson_asset(rel("moment-tensors.geojson"), "Moment tensors"),
             style={"kind": "events", "color": "#e8a33d", "size_by": "magnitude", "size_offset": 2.5}, on=True,
             provider="ANSS / NRCan / SLU"),
        item(pid, "plate-boundaries", "Plate boundaries", bbox_of(pl), "Structure", "Tectonics", **t,
             assets=geojson_asset(rel("plate-boundaries.geojson"), "Plate boundaries"),
             style={"color": "#2a1a4f", "weight": 2, "fill": False, "label": "name"}, on=True),
        item(pid, "slab-faults", "Slab2, CFM faults, bathymetry", B, "Structure", "3D surfaces", **t,
             disabled="3D only: open the Atlas"),
    ]
    col = collection(pid, "Cascadia offshore catalog", "Ensemble deep-learning earthquake catalog offshore "
                     "Cascadia, 2010-2016, with its stations and published moment tensors.", B,
                     [t["start"], t["end"]], {"center": [45.0, -125.25], "zoom": 6}, items,
                     links=[{"rel": "alternate", "href": src["source"], "type": "text/html", "title": "3D Atlas"},
                            {"rel": "via", "href": "https://github.com/Denolle-Lab/cascadia_obs_ensemble",
                             "type": "text/html", "title": "Source repository"}])
    col["gaia:derived_from"] = src
    return pid, col, items, data


# ---------------------------------------------------------------- Mount Rainier (source simulator)
def rainier(index_path, fetched):
    pid = "mt-rainier"
    d = json.loads(Path(index_path).read_text())
    src = {"source": "https://denolle-lab.github.io/mt-rainier-source-simulation/gfdb/recip_1km_v1/index.json",
           "db_id": d["db_id"], "created": d["provenance"]["created"], "fetched": fetched}
    rc = feature_collection([pt(r["lon"], r["lat"], {
        "network": r["net"], "station": r["sta"], "elevation_m": r["elev_m"], "group": r["kind"]})
        for r in d["receivers"]])
    kinds = {"sub": "moment tensor (below surface)", "surf": "force (on surface)"}
    sp = feature_collection([pt(p["lon"], p["lat"], {
        "point_id": p["id"], "kind": kinds.get(p["kind"], p["kind"]), "elevation_m": p["elev_m"],
        "burial_m": p["burial_m"]}) for p in d["points"]])
    ring = d["mesh"]["corners_lonlat"] + [d["mesh"]["corners_lonlat"][0]]
    me = feature_collection([{"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [ring]},
                              "properties": {"name": "SPECFEM3D mesh, 28 x 28 km, 10 Hz",
                                             "bottom_km": d["mesh"]["bottom_km"]}}])
    data = {"receivers.geojson": rc, "source-points.geojson": sp, "mesh.geojson": me}
    B = bbox_of(rc, pad=0.03)
    t = dict(start=d["provenance"]["created"].replace("+00:00", "Z"), end=None)
    rel = lambda f: f"../../../data/{pid}/{f}"  # noqa: E731
    items = [
        item(pid, "receivers", f"Receivers ({len(d['receivers'])})", B, "Simulation", "Stations", **t,
             assets=geojson_asset(rel("receivers.geojson"), "Receivers"),
             style={"kind": "points", "color": "#FF00BB"}, on=True, provider="UW, CC, Z5 networks"),
        item(pid, "source-points", f"Source points ({len(d['points'])})", bbox_of(sp), "Simulation",
             "Green's-function database recip_1km_v1", **t,
             assets=geojson_asset(rel("source-points.geojson"), "Source points"),
             style={"kind": "points", "color": "#6d5bd0"}, on=True),
        item(pid, "mesh", "Simulation mesh footprint", bbox_of(me), "Simulation",
             "Green's-function database recip_1km_v1", **t, assets=geojson_asset(rel("mesh.geojson"), "Mesh"),
             style={"color": "#2a1a4f", "weight": 2, "fillOpacity": 0.05, "label": "name"}, on=True),
        item(pid, "gf-database", "Green's functions (RGF1 binary)", B, "Simulation", "Downloads", **t,
             disabled="not a map layer: used by the simulator"),
    ]
    col = collection(pid, "Mount Rainier source simulations", "Synthetic seismograms at 114 stations around "
                     "Mount Rainier from a 3D Green's-function database (SPECFEM3D, reciprocity).", B,
                     [t["start"], None], {"center": [46.853, -121.76], "zoom": 11}, items,
                     links=[{"rel": "alternate", "href": "https://denolle-lab.github.io/mt-rainier-source-simulation/",
                             "type": "text/html", "title": "3D simulator"},
                            {"rel": "via", "href": "https://github.com/Denolle-Lab/mt-rainier-source-simulation",
                             "type": "text/html", "title": "Source repository"}])
    col["gaia:derived_from"] = src
    return pid, col, items, data


def main():
    cascadia_html, rainier_index, fetched = sys.argv[1:4]
    for sub in ("stac", "data"):
        shutil.rmtree(ROOT / sub, ignore_errors=True)
    projects = [washington(), cascadia(cascadia_html, fetched), rainier(rainier_index, fetched)]
    root = {"type": "Catalog", "stac_version": STAC_VERSION, "id": "gaia-dashboard-mockup",
            "title": "GAIA dashboard (mockup)", "description": "One collection per project; one item per map layer.",
            "links": [{"rel": "root", "href": "./catalog.json", "type": "application/json"}]}
    for pid, col, items, data in projects:
        root["links"].append({"rel": "child", "href": f"./{pid}/collection.json", "type": "application/json",
                              "title": col["title"]})
        write(ROOT / "stac" / pid / "collection.json", col)
        for it in items:
            write(ROOT / "stac" / pid / it["id"] / f"{it['id']}.json", it)
        for name, fc in data.items():
            write(ROOT / "data" / pid / name, fc)
        print(f"{pid}: {len(items)} items, {len(data)} derived files")
    write(ROOT / "stac" / "catalog.json", root)


if __name__ == "__main__":
    main()
