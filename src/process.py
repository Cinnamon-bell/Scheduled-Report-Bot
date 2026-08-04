def process_repo_data(data: dict) -> dict:
    """Extract useful information from the API response."""

    if not data:
        return {}

    return {
        "name": data.get("full_name", "Unknown"),
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "open_issues": data.get("open_issues_count", 0),
        "watchers": data.get("watchers_count", 0),
    }