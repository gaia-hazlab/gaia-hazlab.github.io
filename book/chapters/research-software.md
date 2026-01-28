# Research Software

## Overview

GAIA HazLab leverages a comprehensive ecosystem of research software packages spanning data I/O, AI/ML frameworks, visualization tools, and domain-specific research packages. This page catalogs the key software tools we use and develop to build reproducible, scalable workflows for multi-hazard assessment.

Our goal is to develop a **Research Software Agent** that integrates these tools into cohesive workflows, enabling rapid prototyping, experimentation, and deployment of AI-driven hazard models.

---

## Core Data I/O Packages

Essential packages for reading, writing, and processing geophysical and environmental data.

### ObsPy
**Description**: The seismological observatory in Python
**Use Cases**: Reading seismic waveforms (mseed, SAC), earthquake catalogs, station metadata
**Website**: [https://obspy.org/](https://obspy.org/)
**Key Features**:
- Support for 20+ seismic data formats
- Signal processing (filtering, spectral analysis)
- Event detection and picking
- Integration with seismological data centers (IRIS, GEOFON)

### EarthScope SDK
**Description**: Python SDK for accessing EarthScope (formerly IRIS) seismic data services
**Use Cases**: Downloading waveforms, station metadata, earthquake catalogs
**Website**: [https://earthscope.org/](https://earthscope.org/)
**Key Features**:
- Access to global seismic networks
- Time-series data retrieval
- Event catalog queries
- Integration with ObsPy

### xarray
**Description**: N-dimensional labeled arrays and datasets in Python
**Use Cases**: Climate data, weather forecasts, multi-dimensional gridded data
**Website**: [https://xarray.dev/](https://xarray.dev/)
**Key Features**:
- NetCDF/HDF5/Zarr file support
- Label-based indexing and alignment
- Integration with Dask for parallel computing
- Climate and weather data standards (CF conventions)

### Rasterio
**Description**: Geospatial raster I/O for Python
**Use Cases**: Reading satellite imagery, DEMs, landslide susceptibility maps
**Website**: [https://rasterio.readthedocs.io/](https://rasterio.readthedocs.io/)
**Key Features**:
- GeoTIFF, NetCDF, HDF support
- CRS transformations
- Windowed reading for large files
- Cloud-optimized GeoTIFF support

### GeoPandas
**Description**: Geographic data manipulation in Python
**Use Cases**: Vector data (fault lines, flood zones, landslide inventories)
**Website**: [https://geopandas.org/](https://geopandas.org/)
**Key Features**:
- GeoJSON, Shapefile, GeoPackage support
- Spatial operations (buffer, intersection, union)
- Integration with matplotlib for mapping
- Coordinate reference system transformations

### Pandas
**Description**: Data analysis and manipulation library
**Use Cases**: Tabular data, time series, catalogs, stream gauge data
**Website**: [https://pandas.pydata.org/](https://pandas.pydata.org/)
**Key Features**:
- CSV, Parquet, Excel support
- Time series analysis
- Data cleaning and transformation
- Statistical operations

---

## AI/ML Software Packages

Frameworks for building, training, and deploying machine learning models.

### PyTorch
**Description**: Deep learning framework
**Use Cases**: Neural networks for earthquake detection, AR forecasting, landslide classification
**Website**: [https://pytorch.org/](https://pytorch.org/)
**Key Features**:
- Dynamic computational graphs
- GPU acceleration
- Extensive model zoo
- TorchScript for deployment

### PyTorch Lightning
**Description**: High-level PyTorch interface for research
**Use Cases**: Standardized training loops, multi-GPU training
**Website**: [https://lightning.ai/](https://lightning.ai/)
**Key Features**:
- Simplified training code
- Automatic distributed training
- Built-in logging and checkpointing
- Research-focused architecture

### Hugging Face Transformers
**Description**: State-of-the-art transformer models
**Use Cases**: Foundation models for spatiotemporal forecasting (ACE2)
**Website**: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
**Key Features**:
- Pre-trained models (BERT, GPT, ViT)
- Model hub for sharing
- Training and fine-tuning utilities
- Tokenizers and datasets

**Collaboration**: GAIA HazLab uses ACE2 for atmospheric river forecasting and extreme weather prediction

### scikit-learn
**Description**: Machine learning library for Python
**Use Cases**: Random forests, SVMs, clustering for landslide susceptibility
**Website**: [https://scikit-learn.org/](https://scikit-learn.org/)
**Key Features**:
- Classical ML algorithms
- Model selection and evaluation
- Preprocessing and feature engineering
- Simple, consistent API

---

## Visualization Packages

Tools for creating publication-quality figures, interactive plots, and geospatial visualizations.

### PyGMT
**Description**: Python interface to the Generic Mapping Tools
**Use Cases**: Publication-quality maps, cross-sections, 3D visualizations
**Website**: [https://www.pygmt.org/](https://www.pygmt.org/)
**Key Features**:
- Cartographic projections
- Topography and bathymetry
- Earthquake focal mechanisms
- Publication-ready outputs

### Plotly
**Description**: Interactive graphing library
**Use Cases**: Interactive dashboards, time series exploration, 3D visualizations
**Website**: [https://plotly.com/python/](https://plotly.com/python/)
**Key Features**:
- Interactive plots (zoom, pan, hover)
- 3D scatter and surface plots
- Dash for web applications
- Export to HTML

### Matplotlib
**Description**: Comprehensive plotting library
**Use Cases**: Static plots, subplots, waveform displays
**Website**: [https://matplotlib.org/](https://matplotlib.org/)
**Key Features**:
- Publication-quality figures
- Extensive customization
- Integration with NumPy/Pandas
- Multiple output formats (PNG, PDF, SVG)

### Seaborn
**Description**: Statistical data visualization
**Use Cases**: Distributions, correlations, statistical relationships
**Website**: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
**Key Features**:
- High-level interface to matplotlib
- Built-in themes and color palettes
- Statistical plotting functions
- Integration with Pandas

### Holoviews & Panel
**Description**: Interactive data visualization and dashboards
**Use Cases**: Exploratory data analysis, interactive parameter tuning
**Website**: [https://holoviews.org/](https://holoviews.org/), [https://panel.holoviz.org/](https://panel.holoviz.org/)
**Key Features**:
- Declarative plotting
- Interactive widgets
- Integration with Jupyter
- Deployment to web apps

---

## Research Core Packages

Domain-specific packages developed by the research community for specialized workflows.

### NoisePy
**Description**: Python package for seismic ambient noise cross-correlation
**Use Cases**: Ambient noise tomography, seismic velocity monitoring
**Website**: [https://github.com/noisepy/NoisePy](https://github.com/noisepy/NoisePy)
**Key Features**:
- Parallel processing with MPI
- Cloud-optimized workflows (AWS, Azure)
- Time-dependent velocity monitoring
- Integration with ObsPy

**Developed by**: Denolle Lab ([Marine Denolle](https://denolle-lab.github.io), [Yiyu Ni](https://niyiyu.github.io/), et al.)

### SeisBench
**Description**: Benchmark suite for seismological machine learning
**Use Cases**: Earthquake detection, phase picking, magnitude estimation
**Website**: [https://github.com/seisbench/seisbench](https://github.com/seisbench/seisbench)
**Key Features**:
- Pre-trained models (PhaseNet, EQTransformer, GPD)
- Standardized datasets
- Model evaluation metrics
- PyTorch-based

**Used in**: Strong earthquake detection models (GAIA HazLab)

### PySINDy
**Description**: Sparse Identification of Nonlinear Dynamics
**Use Cases**: Data-driven modeling, reduced-order models, surrogate modeling
**Website**: [https://github.com/dynamicslab/pysindy](https://github.com/dynamicslab/pysindy)
**Key Features**:
- Discover governing equations from data
- Physics-informed machine learning
- Symbolic regression
- Integration with PyTorch/TensorFlow

**Used in**: Reduced-order modeling for landslide dynamics, debris flow

### PySHRED
**Description**: Python package for Shallow Recurrent Decoder (SHRED) models
**Use Cases**: Spatiotemporal forecasting, sensor placement optimization
**Website**: [https://github.com/shervinsahba/pyshred](https://github.com/shervinsahba/pyshred)
**Key Features**:
- Reconstruct spatiotemporal fields from sensors
- Sensor placement optimization
- Integration with PyTorch
- Video and climate data applications

**Used in**: Multi-sensor fusion for hydromechanical modeling

### Landlab
**Description**: Python toolkit for numerical modeling of Earth surface dynamics
**Use Cases**: Landscape evolution, debris flow, erosion modeling, landslide dynamics
**Website**: [https://landlab.github.io/](https://landlab.github.io/)
**Key Features**:
- Component-based modeling framework
- Grid-based and unstructured grids
- Process coupling (hydrology, erosion, landslides)
- Extensive component library
- Comprehensive documentation

**Used in**: Data-driven reduced-order modeling for landscape evolution, debris flow modeling, and landslide susceptibility analysis

### ESMValTool
**Description**: Earth System Model Evaluation Tool
**Use Cases**: Climate model evaluation, multi-model analysis
**Website**: [https://www.esmvaltool.org/](https://www.esmvaltool.org/)
**Key Features**:
- CMIP data preprocessing
- Diagnostic metrics
- Multi-model ensembles
- Reproducible workflows

### rslearn (AI2)
**Description**: Remote sensing machine learning library from Allen Institute for AI
**Use Cases**: SAR processing, change detection, multi-temporal analysis, landslide detection
**Website**: [https://github.com/allenai/rslearn](https://github.com/allenai/rslearn)
**Key Features**:
- Pre-processing pipelines for Sentinel-1/2 SAR imagery
- Foundation models for Earth observation
- Deep learning models for remote sensing tasks
- Multi-temporal change detection
- Integration with cloud platforms (AWS, GCS)
- Fine-tuning capabilities for downstream tasks

**Collaboration**: GAIA HazLab is collaborating with AI2 on landslide detection using rslearn to fine-tune foundation models on SAR imagery and multi-sensor networks ([Akash Kharita](https://gaia-hazlab.github.io/people), Scott Henderson)

---

## Development & Deployment Tools

Supporting tools for research software development, version control, and deployment.

### Jupyter & JupyterLab
**Description**: Interactive computing environment
**Use Cases**: Exploratory analysis, tutorials, reproducible research
**Website**: [https://jupyter.org/](https://jupyter.org/)

### Conda & Mamba
**Description**: Package and environment management
**Use Cases**: Creating reproducible environments, dependency management
**Website**: [https://conda.io/](https://conda.io/), [https://mamba.readthedocs.io/](https://mamba.readthedocs.io/)

### Docker & Singularity
**Description**: Containerization platforms
**Use Cases**: Reproducible computing environments, HPC deployment
**Website**: [https://docker.com/](https://docker.com/), [https://sylabs.io/singularity/](https://sylabs.io/singularity/)

### Dask
**Description**: Parallel computing library
**Use Cases**: Large dataset processing, distributed computing
**Website**: [https://dask.org/](https://dask.org/)

### MLflow
**Description**: Machine learning lifecycle management
**Use Cases**: Experiment tracking, model registry, deployment
**Website**: [https://mlflow.org/](https://mlflow.org/)

---

## Research Software Agent Vision

Our vision is to develop an integrated **Research Software Agent** that:

1. **Automates Workflows**: Chain together data loading, preprocessing, model training, and visualization
2. **Enables Reproducibility**: Track dependencies, versions, and compute environments
3. **Facilitates Discovery**: Search and recommend appropriate tools for specific tasks
4. **Provides Templates**: Offer ready-to-use templates for common workflows
5. **Integrates AI**: Use LLMs to generate code, debug issues, and optimize pipelines

---

## Contributing

We welcome contributions of:
- New package recommendations
- Code examples and tutorials
- Integration guides
- Best practices documentation

See our [Contributing Guide](../../CONTRIBUTING.md) for details.

---

## Resources

### Package Ecosystems
- **PyOpenSci**: [https://www.pyopensci.org/](https://www.pyopensci.org/)
- **Pangeo**: [https://pangeo.io/](https://pangeo.io/)
- **Project Pythia**: [https://projectpythia.org/](https://projectpythia.org/)

### Learning Resources
- [Software Carpentry](https://software-carpentry.org/)
- [Research Software Engineering](https://society-rse.org/)
- [FAIR Principles for Research Software](https://www.nature.com/articles/s41597-022-01710-x)

---

## Future Development

We are actively working on:
- **Integration guides** for common workflow patterns
- **Benchmark datasets** for evaluating new tools
- **Performance comparisons** across different packages
- **Cloud-native implementations** for scalable processing
- **Tutorial notebooks** demonstrating best practices

