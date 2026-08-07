# Scheduled Report Bot

A Python automation tool that fetches GitHub repository data, processes it, and generates a daily summary report automatically using GitHub Actions.

## Problem and Target Users

Collecting and checking repository statistics manually is repetitive and time-consuming. The Scheduled Report Bot automates this process by fetching repository information from the GitHub API, processing the data, and generating a readable summary. It is intended for developers, students, and small teams who want an automated way to monitor repository statistics without manually collecting the data.

## Features

- Fetches repository data from the GitHub API.
- Processes and cleans the retrieved data.
- Generates a summary of important repository statistics.
- Runs automatically using GitHub Actions.
- Runs tests automatically using GitHub Actions CI.
- Supports manual workflow execution.
- Uses scheduled execution to run without manual intervention.
- Can be extended to send reports through Discord or email webhooks.

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Scheduled-Report-Bot.git
cd Scheduled-Report-Bot
```

Install the project dependencies using `uv`:

```bash
uv sync
```

Verify that the project works by running the tests:

```bash
uv run pytest
```

Expected result:

```text
4 passed
```

## Usage

Run the application manually with:

```bash
uv run python -m scheduled_report_bot.main
```

The application fetches information about the configured GitHub repository.

For example, the bot can retrieve data such as:

```text
Repository: python/cpython
Stars: 75000
Forks: 35000
Open issues: 12000
Watchers: 75000
```

The data is then processed into a smaller summary that can be used to generate the daily report.

### Example input

The application uses a GitHub repository as its input:

```text
Owner: python
Repository: cpython
```

### Example output

```text
Repository: python/cpython
Stars: 75000
Forks: 35000
Open issues: 12000
Watchers: 75000
```

The exact numbers will change because the data is retrieved from the GitHub API.

## How It Works

The project is divided into several small components. Each function has a single responsibility.

```text
                 GitHub API
                     │
                     ▼
              ┌─────────────┐
              │   fetch.py  │
              │ Fetch data  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │ process.py  │
              │ Clean and   │
              │ process     │
              │ data        │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │   main.py   │
              │ Coordinates │
              │ the process │
              └──────┬──────┘
                     │
                     ▼
              Daily report
                     │
                     ▼
             GitHub Actions
              scheduled run
```

### GitHub Actions

The project contains automated workflows in:

```text
.github/workflows/
```

The CI workflow runs the tests automatically when code is pushed and also runs on a daily schedule.

The workflow can also be started manually using `workflow_dispatch`.

## Project Structure

```text
Scheduled-Report-Bot/
│
├── .github/
│   └── workflows/
│       ├── automation.yml
│       └── ci.yml
│
├── data/
│
├── src/
│   └── scheduled_report_bot/
│       ├── __init__.py
│       ├── fetch.py
│       ├── process.py
│       └── main.py
│
├── tests/
│   └── test_process.py
│
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Tech Stack

- **Python 3.13** – main programming language.
- **Requests** – communicates with the GitHub API.
- **Pytest** – automated testing.
- **uv** – Python dependency and project management.
- **GitHub API** – source of repository information.
- **GitHub Actions** – automated CI and scheduled execution.
- **Git/GitHub** – version control and project hosting.

### Data

The project uses repository information retrieved from the GitHub API.

Any local example or test data used by the project is **synthetic/example data** and does not represent private or real-world business data. The automated tests use controlled data so that the results are predictable and reproducible.

## Testing

The project contains automated tests for the core processing functionality.

Run all tests with:

```bash
uv run pytest
```

The CI workflow also runs these tests automatically after every push and on the configured schedule.

Example:

```text
============================= test session starts =============================
collected 4 items

tests/test_process.py ....                                       [100%]

============================== 4 passed ==============================
```

## Automation

The GitHub Actions workflow is configured to run automatically.

It supports:

- **Push** – runs CI after code is pushed.
- **Pull request** – runs tests for pull requests.
- **Scheduled execution** – runs automatically according to the configured cron schedule.
- **Manual execution** – can be started from the GitHub Actions interface.

This means the pipeline can run unattended without requiring the developer to start it manually.

## Future Improvements

- Generate a more detailed Markdown or HTML report.
- Send reports to Discord using a webhook.
- Send reports by email.
- Track repository statistics over time.
- Add more GitHub repositories to the report.
- Add additional automated tests.

## Screenshot / Example Output

Example console output:

```text
Scheduled Report Bot
--------------------
Repository: python/cpython
Stars: 75000
Forks: 35000
Open issues: 12000
Watchers: 75000

Report generated successfully.
```

The actual values depend on the current information returned by the GitHub API.

## License

This project was created for educational purposes.