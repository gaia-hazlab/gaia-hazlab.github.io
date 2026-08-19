# Contributing to GAIA HazLab

Thanks for your interest in contributing. This document is for human contributors — AI
coding agents should read [AGENTS.md](AGENTS.md) instead. If you use an AI assistant while
contributing, see [AI Coding Agents](README.md#ai-coding-agents) for what this repo
configures and which tools pick it up.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion for improvement:

1. Check whether it already exists in the
   [issue tracker](https://github.com/gaia-hazlab/gaia-hazlab.github.io/issues)
2. If not, open a new issue using one of the templates — **Bug**, **Documentation / Book
   page**, or **Task**
3. Include steps to reproduce (for bugs) or the use case (for features)

For open-ended questions and async updates, use
[GitHub Discussions](https://github.com/gaia-hazlab/gaia-hazlab.github.io/discussions)
rather than an issue.

### Contributing Content

#### Adding to the Jupyter Book

1. Fork the repository and create a branch
2. Edit or add Markdown (MyST flavor) files under `book/chapters/`
3. Register the page in the `toc:` in [myst.yml](myst.yml) — adding a file alone will not
   put it in the book
4. Preview locally:
   ```bash
   pixi run serve-book
   ```
5. Run the checks below, then open a pull request

Governance and process pages live in `book/governance/` rather than `book/chapters/`.

#### Adding Tutorials

1. Write the tutorial as a Markdown file or Jupyter Notebook
2. Place it under `book/chapters/` (or a subdirectory)
3. Add it to the `toc:` in [myst.yml](myst.yml), under the section it belongs to

#### Editing the Website

The static site lives in `website/`. Team members are data-driven — edit
[website/data/team.json](website/data/team.json) and add portraits to
`website/images/team/`; do not hand-edit the team markup in `index.html` or `people.html`.
See [website/data/README.md](website/data/README.md).

Preview the full assembled site (splashpage plus built book) with:

```bash
pixi run build-all && pixi run serve-all
```

#### Contributing Data

See the [DataHub chapter](book/chapters/datahub.md) for information on contributing
datasets, and [book/chapters/datahub-integration-guide.md](book/chapters/datahub-integration-guide.md)
for the integration process.

#### Contributing Models

See the [ModelHub chapter](book/chapters/modelhub.md) for information on contributing
models.

### Code Style

- Follow existing formatting conventions
- Use meaningful variable and function names
- Include comments where necessary
- Keep changes focused and minimal
- Never hand-edit `_build/` or `website/book/` — both are generated
- Treat `_attic/` as archived; do not build on it

### Documentation

- Update documentation when adding new features
- Ensure all links work
- Include examples where helpful
- Keep `project_coordination/` free of budget figures, personal contact information, and
  unreleased science — it is public. Reference people by role, not name or email.

### Checks Before You Open a PR

```bash
pixi run spellcheck   # codespell (use spellcheck-context to see surrounding lines)
pixi run linkcheck    # check the book for broken links
pixi run build-all    # confirm the book and site build
```

`pixi run zizmor` audits the GitHub Actions workflows; run it if you touched anything in
`.github/workflows/`.

### Pull Request Process

1. Make sure the site builds and the checks above pass
2. Update documentation if needed
3. Write a clear pull request description
4. Link any related issues
5. Disclose material AI assistance — a `Co-Authored-By:` commit trailer or a note in the PR
   description is enough. See
   [AI-assisted code](book/governance/licensing.md#licensing-ai-assisted-and-ai-generated-code).
6. Wait for review. [.github/CODEOWNERS](.github/CODEOWNERS) routes reviewers by path.

## Development Setup

### Prerequisites

We recommend the [GitHub CLI](https://cli.github.com) and
[pixi](https://pixi.sh/dev/installation/) for a local development environment.

### Local Setup

1. Clone the repository:
   ```bash
   gh repo clone gaia-hazlab/gaia-hazlab.github.io
   cd gaia-hazlab.github.io
   ```

2. Build the book and preview locally:
   ```bash
   pixi run serve-book
   ```

`pixi task list` shows every available task. See [README.md](README.md#structure) for the
repository layout and [DEPLOYMENT.md](DEPLOYMENT.md) for how deployment works.

## Questions?

If you have questions about contributing:

- Open an issue
- Start a thread in
  [GitHub Discussions](https://github.com/gaia-hazlab/gaia-hazlab.github.io/discussions)
- Contact the maintainers

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful
and professional in all interactions.

## License

This repository is licensed under the [MIT License](LICENSE), and by contributing you agree
your contributions are released under it.

Project-wide, GAIA's guideline is code under MIT and documentation, book content, and
curated data products under CC BY 4.0 — see
[book/governance/licensing.md](book/governance/licensing.md). That guideline is still
awaiting ratification, so this repository currently carries MIT throughout.
