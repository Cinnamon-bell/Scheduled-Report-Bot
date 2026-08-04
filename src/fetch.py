import requests


def fetch_repo_data(owner: str, repo: str) -> dict:
    """Fetch repository information from the GitHub API."""

    url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}