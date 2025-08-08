# GitHub Repository Setup Guide

## Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the details:
   - **Repository name**: `python-quickstart-course`
   - **Description**: `Learn Python the fastest and easiest way possible with interactive lessons and projects`
   - **Visibility**: Public (recommended for open source)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

## Step 2: Push Your Code

After creating the repository, run these commands in your terminal:

```bash
# Navigate to your project directory
cd python-quickstart-course

# Add the GitHub remote
git remote add origin https://github.com/wiradjuri/python-quickstart-course.git

# Push your code to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Verify GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. You should see the workflow running automatically
4. The workflow will:
   - Test your code on multiple Python versions
   - Build the package
   - Create release artifacts

## Step 4: Create Your First Release (v1.0.0)

1. Go to your repository on GitHub
2. Click on "Releases" (on the right side)
3. Click "Create a new release"
4. Fill in:
   - **Tag version**: `v1.0.0`
   - **Release title**: `Python QuickStart Course v1.0.0`
   - **Description**: 
     ```
     🎉 First stable release of Python QuickStart Course!
     
     ## What's New
     - Complete interactive Python learning system
     - Step-by-step lessons with hands-on activities
     - Calculator building project
     - Python cheatsheet and resources
     - Cross-platform support (Windows, Mac, Linux)
     
     ## Quick Start
     1. Download the complete package below
     2. Extract and run the installation script
     3. Start learning: `python quick_start.py`
     
     ## Installation Options
     - **Complete Package**: Download the zip/tar.gz files below
     - **Python Package**: `pip install python-quickstart-course`
     ```
5. Click "Publish release"

## Step 5: Verify Everything Works

After creating the release:

1. **GitHub Actions**: Check that all workflows completed successfully
2. **Release Assets**: Verify that the complete packages were created
3. **Package Installation**: Test installing via pip (may take a few minutes to appear)

## Optional: Set up PyPI Publishing

If you want to publish to PyPI (Python Package Index):

1. Create a PyPI account at [pypi.org](https://pypi.org)
2. Generate an API token in your PyPI account settings
3. In your GitHub repository:
   - Go to Settings → Secrets and variables → Actions
   - Add a new secret named `PYPI_API_TOKEN`
   - Paste your PyPI API token as the value
4. The next release will automatically publish to PyPI!

## Troubleshooting

- **Actions failing**: Check the Actions tab for detailed error logs
- **Permission issues**: Make sure you have write access to the repository
- **Package conflicts**: Ensure the package name is unique on PyPI

## Next Steps

- Share your repository with others
- Add more lessons and projects
- Create documentation
- Set up a project website using GitHub Pages

Happy coding! 🐍✨
