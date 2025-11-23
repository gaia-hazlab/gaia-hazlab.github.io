# GAIA HazLab Website

[![Deploy GitHub Pages](https://github.com/gaia-hazlab/gaia-hazlab.github.io/workflows/Deploy%20GitHub%20Pages/badge.svg)](https://github.com/gaia-hazlab/gaia-hazlab.github.io/actions)

This repository contains the source code for the GAIA HazLab (Geophysical AI-driven Integration and Assimilation for Hazard Laboratory) website, hosted on GitHub Pages.

## Overview

GAIA HazLab is a comprehensive platform for hazard assessment using machine learning and geospatial analytics. The website consists of:

- **Splashpage**: A modern landing page at the root (`index.html`)
- **Jupyter Book**: Comprehensive documentation organized into five main chapters:
  1. **Problem Statement**: Research challenges and objectives
  2. **DataHub**: Data repository and management tools
  3. **ModelHub**: Machine learning models for hazard prediction
  4. **HazEvalHub**: Evaluation frameworks and tools
  5. **Resources**: Tutorials, references, and community resources

## Local Development

### Prerequisites

- Python 3.8 or higher
- Conda (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/gaia-hazlab/gaia-hazlab.github.io.git
cd gaia-hazlab.github.io
```

2. Create and activate the environment:
```bash
conda env create -f environment.yml
conda activate gaia-hazlab
```

Or using pip:
```bash
pip install jupyter-book sphinx-design
```

3. Build the Jupyter Book:
```bash
jupyter-book build book
```

4. View the site locally:
```bash
# Open book/_build/html/index.html in your browser
```

## Structure

```
.
├── index.html              # Landing page
├── book/                   # Jupyter Book source
│   ├── _config.yml        # Book configuration
│   ├── _toc.yml           # Table of contents
│   ├── intro.md           # Introduction page
│   ├── img/               # Images
│   └── chapters/          # Chapter content
│       ├── problem_statement.md
│       ├── datahub.md
│       ├── modelhub.md
│       ├── hazevalhub.md
│       └── resources.md
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions deployment
└── environment.yml        # Conda environment specification
```

## Building and Deployment

The website is automatically built and deployed to GitHub Pages using GitHub Actions when changes are pushed to the `main` branch.

### Manual Build

To build the Jupyter Book manually:

```bash
jupyter-book build book
```

The built HTML files will be in `book/_build/html/`.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- GitHub: [gaia-hazlab](https://github.com/gaia-hazlab)
- Website: [https://gaia-hazlab.github.io](https://gaia-hazlab.github.io)

## Acknowledgments

- Based on the [UW Hackweek Splashpage Template](https://github.com/uwhackweek/splashpage-template)
- Inspired by the [GeoSMART Website](https://github.com/geo-smart/website-2024)
- Built with [Jupyter Book](https://jupyterbook.org)
