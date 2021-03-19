import datetime

import requests

DEFAULT_URL = 'https://api.github.com/repos'
ERROR_MSG = 'Error, status code:'

UNIQUE_AUTHORS = 'Unique authors'
LAST_COMMITS = 'Commits count for last month'
MOST_ACTIVE_USER = 'The most active committee'


def get_commits_info(owner, repo):
    """Get commits information from repo by GitHub API and save in dict.

    What info get:
        all unique authors of commits;
        number of commits since last month;
        most active committee from repo.

    Args:
        owner (str): Owner of repo on GitHub.
        repo (str): Name of repo of owner.

    Returns:
        None

    """

    url = f'{DEFAULT_URL}/{owner}/{repo}/'
    try:
        info_dict = {
            UNIQUE_AUTHORS: get_unique_authors(url),
            LAST_COMMITS: get_commits_count(url),
            MOST_ACTIVE_USER: get_most_active_committee(url),
        }
    except requests.exceptions.ConnectionError as exc:
        return exc
    else:
        return info_dict


def get_unique_authors(url):
    """Print logins of unique authors of repo.

    Args:
        url (str): /owner/repo.

    Returns:
        tuple: All unique authors of repo.

    """
    response = requests.get(f'{url}commits')
    if response.status_code in (204, 409):
        return 0
    elif response.ok:
        repo_json = response.json()
        unique_authors = set()
        for commit in repo_json:
            unique_authors.add(commit['author']['login'])
        return list(unique_authors)
    else:
        raise requests.exceptions.ConnectionError(f'{ERROR_MSG} {response.status_code}. {response.text}')


def get_commits_count(url):
    """Print number of commits since last month.

    Args:
        url (str): /owner/repo

    Returns:
        int: Number of commits.
        str: Error message and status code.

    """
    last_month = datetime.datetime.now() - datetime.timedelta(days=30)
    response = requests.get(f'{url}commits', params=f'since={last_month}')
    if response.status_code in (204, 409):
        return 0
    elif response.ok:
        return len(response.json())
    else:
        raise requests.exceptions.ConnectionError(f'{ERROR_MSG} {response.status_code}. {response.text}')


def get_most_active_committee(url):
    """Get most active committee from repo

    Args:
        url (str): URL of repo.

    Returns:
        str: Login or error message with status code

    """

    response = requests.get(f'{url}contributors')
    if response.status_code in (204, 409):
        return 0
    elif response.ok:
        most_active_user = response.json()[0]['login']
        return most_active_user
    else:
        raise requests.exceptions.ConnectionError(f'{ERROR_MSG} {response.status_code}. {response.text}')
