# GAIA HazLab Website

[![Deploy GitHub Pages](https://github.com/gaia-hazlab/gaia-hazlab.github.io/workflows/Deploy%20GitHub%20Pages/badge.svg)](https://github.com/gaia-hazlab/gaia-hazlab.github.io/actions)

This repository contains the source code for the GAIA HazLab (Geophysical AI-driven Integration and Assimilation for Hazard Laboratory) website, hosted on GitHub Pages.

## Overview

GAIA HazLab is a comprehensive platform for hazard assessment using machine learning and geospatial analytics. The website consists of:

- **Splashpage**: A modern landing page at the root (`index.html`)
  - Features funders section with logos from eScience Institute, College of the Environment, and UW Innovation Fund
  - Links to team page and documentation
- **People Page**: Team members with circular portraits (`people.html`)
- **Jupyter Book**: Comprehensive documentation organized into five main chapters:
  1. **Problem Statement**: Research challenges and objectives
  2. **DataHub**: Data repository and management tools
  3. **ModelHub**: Machine learning models for hazard prediction
  4. **HazEvalHub**: Evaluation frameworks and tools
  5. **Resources**: Tutorials, references, and community resources

## Local Development

### Prerequisites

We recommend using [pixi](https://pixi.sh/dev/installation/) for a local development environment

### Setup

1. Clone the repository:
```bash
gh repo clone gaia-hazlab/gaia-hazlab.github.io
cd gaia-hazlab.github.io
```

1. Build the Jupyter Book & preview locally
```bash
pixi run serve
```

## Structure

```
.
├── index.html             # Landing page
├── people.html            # Team members page
├── images/                # Images directory
│   └── team/              # Team member portraits
├── book/                  # Jupyter Book source
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
└── pixi.toml              # Conda environment specification
```

## Adding Team Members

To add team members to the people page:

1. Add portrait photos to `images/team/` directory
   - Format: JPG or PNG
   - Size: At least 300x300px (square)
   - Naming: `firstname-lastname.jpg`

2. Edit `people.html` and add team member entries in the appropriate section (PI, Graduate Students, Undergrads)

3. Update with name, role, description, and contact links

## Deployment

The website is automatically built and deployed to GitHub Pages using GitHub Actions when changes are pushed to the `main` branch.


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
