import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()

GITHUB_API_URL = os.getenv('GITHUB_API_URL', None)
GITHUB_REPOSITORY = os.getenv('GITHUB_REPOSITORY', None)

assert GITHUB_API_URL, "Missing environment variable GITHUB_API_URL"
assert GITHUB_REPOSITORY, "Missing environment variable GITHUB_REPOSITORY"

# Git Enterprise API endpoint for creating a release
GIT_ENTERPRISE_API_URL = f"{GITHUB_API_URL}/api/v3/repos/{GITHUB_REPOSITORY}/releases"

def extract_changelog_info(changelog_content):
    # Define regex patterns for tag, description, and latest sections
    tag_pattern = r"\[(\d+\.\d+\.\d+)\]"
    description_pattern = r"--DESCRIPTION--\n(.*?)\n--DESCRIPTION--"
    latest_pattern = r"--LATEST--\n(.*?)\n--LATEST--"

    # Extract tag, description, and latest sections
    tag_match = re.search(tag_pattern, changelog_content)
    description_match = re.search(description_pattern, changelog_content, re.DOTALL)
    latest_match = re.search(latest_pattern, changelog_content, re.DOTALL)

    if tag_match and description_match and latest_match:
        tag = tag_match.group(1)
        description = description_match.group(1).strip()
        latest = latest_match.group(1).strip()
        return tag.strip(), description.strip(), latest.strip()
    else:
        return None, None, None

# Create a Git Enterprise release
def create_git_enterprise_release(changelog_file):

    # Git Enterprise personal access token (replace with your own token)
    GIT_ENTERPRISE_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN", None)
    assert GIT_ENTERPRISE_TOKEN, "Failed to retrieve Github Access Credentials. Make sure to have a .env file with a variable named GITHUB_PERSONAL_ACCESS_TOKEN with a personal access token from Github."

    # Read the content from the CHANGELOG.md file (replace with actual file path)
    with open("CHANGELOG.md", "r") as changelog_file:
        changelog_content = changelog_file.read()

    # Extract tag, description, and latest sections
    tag_name, description, latest = extract_changelog_info(changelog_content)

    release_name = f"Release {tag_name}"  # Replace with the desired release name
    release_body = f"Release notes:\n{description}"  # Replace with your release notes

    headers = {
        "Authorization": f"Bearer {GIT_ENTERPRISE_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "tag_name": tag_name,
        "target_commitish": "main",  # Replace with your branch name
        "name": release_name,
        "body": release_body,
        "draft": False,
        "prerelease": False,
    }

    response = requests.post(
        GIT_ENTERPRISE_API_URL,
        json=data,
        headers=headers,
    )

    if response.status_code == 201:
        print(f"Release {tag_name} created successfully.")
    else:
        print(f"Error creating release: {response.status_code} - {response.text}")

"""
USER DEFINED PARAMETERS BELOW

Change the variables below to run.

"""
# Call the function to create the Git Enterprise release
owner = "anchaura"
repo = "repo-experience"
filename = 'CHANGELOG.md'
run_release = True

# CODE LOGIC BELOW - NO NEED TO MODIFY
# Automatically create the github release
if run_release:
    create_git_enterprise_release(filename)
