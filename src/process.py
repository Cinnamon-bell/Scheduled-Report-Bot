def process_repo_data(data: dict) -> dict:
    """Extract only the information needed for the report."""

    return {
        "name": data["full_name"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "watchers": data["watchers_count"],
    }