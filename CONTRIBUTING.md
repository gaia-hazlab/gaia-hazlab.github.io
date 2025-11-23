# Contributing to GAIA HazLab

Thank you for your interest in contributing to GAIA HazLab! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check if the issue already exists in our [issue tracker](https://github.com/gaia-hazlab/gaia-hazlab.github.io/issues)
2. If not, create a new issue with a clear title and description
3. Include steps to reproduce (for bugs) or use cases (for features)

### Contributing Content

#### Adding to the Jupyter Book

1. Fork the repository
2. Create a new branch for your changes
3. Edit the relevant markdown files in `book/chapters/`
4. Test your changes locally:
   ```bash
   jupyter-book build book
   ```
5. Submit a pull request

#### Adding Tutorials

To add a tutorial to the Resources chapter:

1. Create your tutorial as a Markdown file or Jupyter Notebook
2. Place it in `book/chapters/` or create a subdirectory
3. Update `book/_toc.yml` to include your tutorial
4. Add a reference in `book/chapters/resources.md`

#### Contributing Data

See the [DataHub chapter](book/chapters/datahub.md) for information on contributing datasets.

#### Contributing Models

See the [ModelHub chapter](book/chapters/modelhub.md) for information on contributing models.

### Code Style

- Follow existing formatting conventions
- Use meaningful variable and function names
- Include comments where necessary
- Keep changes focused and minimal

### Documentation

- Update documentation when adding new features
- Ensure all links are working
- Include examples where helpful

### Pull Request Process

1. Ensure your code builds successfully
2. Update the documentation if needed
3. Write a clear pull request description
4. Link any related issues
5. Wait for review from maintainers

## Development Setup

### Prerequisites

- Python 3.8+
- Git

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/gaia-hazlab/gaia-hazlab.github.io.git
   cd gaia-hazlab.github.io
   ```

2. Create environment:
   ```bash
   conda env create -f environment.yml
   conda activate gaia-hazlab
   ```

3. Build the Jupyter Book:
   ```bash
   jupyter-book build book
   ```

4. View locally:
   ```bash
   # Start a local server
   python -m http.server 8000
   # Visit http://localhost:8000
   ```

## Questions?

If you have questions about contributing, feel free to:

- Open an issue
- Start a discussion in our [GitHub Discussions](https://github.com/gaia-hazlab/gaia-hazlab.github.io/discussions)
- Contact the maintainers

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and professional in all interactions.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
