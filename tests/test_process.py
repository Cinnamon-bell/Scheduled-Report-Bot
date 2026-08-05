from scheduled_report_bot.process import process_repo_data


def test_process_valid_data():
    data = {
        "full_name": "python/cpython",
        "stargazers_count": 100,
        "forks_count": 50,
        "open_issues_count": 25,
        "watchers_count": 100,
    }

    result = process_repo_data(data)

    assert result["name"] == "python/cpython"
    assert result["stars"] == 100
    assert result["forks"] == 50
    assert result["open_issues"] == 25
    assert result["watchers"] == 100


def test_process_empty_data():
    assert process_repo_data({}) == {}


def test_missing_fields():
    data = {
        "full_name": "python/cpython"
    }

    result = process_repo_data(data)

    assert result["stars"] == 0
    assert result["forks"] == 0
    assert result["open_issues"] == 0
    assert result["watchers"] == 0


def test_missing_name():
    data = {
        "stargazers_count": 75
    }

    result = process_repo_data(data)

    assert result["name"] == "Unknown"
    assert result["stars"] == 75