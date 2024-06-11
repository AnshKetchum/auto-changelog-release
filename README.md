# Repo-Experience

A continuous experiment testing various features the devops team can use with their daily workflow.

https://github.com/marketplace/actions/automated-releases

## Automatic Release: 

### Github Actions Setup
The sample Github actions below watches for changes on the VERSION.txt and triggers a release when `VERSION.txt` is changed.

```yaml
# Create a GitHub Actions workflow YAML file (e.g., main.yml) in the .github/workflows directory
# This workflow will run only on the main branch

name: Automatically Publish Release

on:
  pull_request:
    paths:
      - 'VERSION.txt'
    branches:
      - main
  push:
    paths:
      - 'VERSION.txt'
    branches:
      - main

jobs:
  set-secret-and-run-python:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Automated Releases
        uses: AnshKetchum/auto-changelog-release@alpha-1
        with: 
          GIT_PERSONAL_ACCESS_TOKEN: ${{ secrets.REPOSITORY_TOKEN }}
```

### Daily Setup 

1. Maintain a `CHANGELOG.md` file

2. Highlight your latest release by wrapping your entry with the following: 

--LATEST--
YOUR CHANGELOG HERE
--LATEST--

3. Highlight your description by wrapping the description inside with the following:

--DESCRIPTION--
YOUR DESCRIPTION HERE
--DESCRIPTION--

Example: 

```
--LATEST--
## [1.20.0]
--DESCRIPTION--
- Removed unnecessary log statements from the GCC toolchain from popping up on Windows
--DESCRIPTION--
--LATEST--
```

### Execution

In a `.env` file, add a personal access token from Github. 
```
GITHUB_PERSONAL_ACCESS_TOKEN=<YOUR_PERSONAL_ACCESS_TOKEN>
```

1. Install the requirements. `pip install -r requirements.txt`
2. Run the python code. `python create_release.py`
