# Deployment Guide

This guide explains how to deploy the GAIA HazLab website to GitHub Pages.

## Prerequisites

The repository is already configured with:
- GitHub Actions workflow (`.github/workflows/deploy.yml`)
- Jupyter Book configuration
- All necessary content files

## Enabling GitHub Pages

### Step 1: Configure GitHub Pages

1. Go to your repository on GitHub: `https://github.com/gaia-hazlab/gaia-hazlab.github.io`
2. Click on **Settings** tab
3. In the left sidebar, click on **Pages**
4. Under **Source**, select **GitHub Actions**

### Step 2: Merge to Main

Once the pull request is merged to the `main` branch:
1. GitHub Actions will automatically trigger
2. The workflow will:
   - Build the Jupyter Book
   - Copy the splashpage to the build directory
   - Deploy everything to GitHub Pages
3. Wait a few minutes for the deployment to complete

### Step 3: Access Your Site

Your site will be available at:
- **URL**: `https://gaia-hazlab.github.io`

## Workflow Details

The GitHub Actions workflow (`.github/workflows/deploy.yml`) performs the following:

1. **Build Job**:
   - Checks out the repository
   - Sets up Python 3.11
   - Installs dependencies (`jupyter-book`, `sphinx-design`)
   - Builds the Jupyter Book
   - Copies `index.html` to the build output
   - Uploads the built site as an artifact

2. **Deploy Job** (runs only on main branch):
   - Downloads the built site
   - Deploys to GitHub Pages

## Manual Build (Local Testing)

To build and test locally before deploying:

```bash
# Install dependencies
pip install jupyter-book sphinx-design

# Build the book
jupyter-book build book

# The built site will be in book/_build/html/
# You can view it by starting a local server:
python -m http.server 8000 --directory book/_build/html
```

Then visit `http://localhost:8000` in your browser.

## Updating Content

To update the website:

1. Edit the relevant files:
   - `index.html` - Landing page
   - `book/intro.md` - Introduction
   - `book/chapters/*.md` - Chapter content
   - `book/_config.yml` - Book configuration
   - `book/_toc.yml` - Table of contents

2. Commit and push your changes

3. The site will automatically rebuild and deploy (if on main branch)

## Troubleshooting

### Build Fails

If the GitHub Actions build fails:

1. Check the Actions tab for error messages
2. Test the build locally:
   ```bash
   jupyter-book build book
   ```
3. Fix any errors and commit the changes

### Pages Not Updating

If changes don't appear:

1. Check the Actions tab to ensure the workflow completed
2. Clear your browser cache
3. Wait a few minutes - GitHub Pages can take time to update

### Missing Dependencies

If you see dependency errors:

1. Check that `environment.yml` has all required packages
2. Update the workflow to install any missing dependencies

## Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to the repository root with your domain
2. Configure DNS settings with your domain provider
3. See [GitHub's custom domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

## Monitoring

- **Build Status**: Check the badge in README.md
- **Actions**: Monitor builds in the Actions tab
- **Logs**: Click on workflow runs to see detailed logs

## Support

For issues with deployment:
- Check [GitHub Actions documentation](https://docs.github.com/en/actions)
- Check [Jupyter Book documentation](https://jupyterbook.org)
- Open an issue in the repository
