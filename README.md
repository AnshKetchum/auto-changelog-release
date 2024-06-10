# Repo-Experience

A continuous experiment testing various features the devops team can use with their daily workflow.


## Automatic Release: 

### Setup 

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