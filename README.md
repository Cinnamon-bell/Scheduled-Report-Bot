# Scheduled Report Bot

A Python automation project that fetches data from the GitHub API, processes the information, and generates a daily summary report. The project is automatically executed using GitHub Actions on a schedule or can be run manually.

## Project Brief

The Scheduled Report Bot automates the process of collecting repository statistics from the GitHub API. It retrieves repository information, cleans and processes the data, and generates a daily report containing key metrics such as stars, forks, watchers, and open issues. The report can be stored in the repository, making it easy to track changes over time. As a future enhancement, the report can be delivered automatically to Discord or email using a webhook.

## Features

- Fetch repository data from the GitHub API.
- Process and clean the fetched data.
- Generate a daily summary report.
- Run automatically with GitHub Actions.
- Support manual execution through `workflow_dispatch`.

## Project Structure

```
scheduled-report-bot/
│
├── .github/
│   └── workflows/
│       └── automation.yml
├── data/
├── src/
│   ├── fetch.py
│   ├── process.py
│   └── main.py
├── tests/
├── README.md
├── pyproject.toml
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/scheduled-report-bot.git
cd scheduled-report-bot
```

Install dependencies:

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

## Usage

Run the project manually:

```bash
uv run src/main.py
```

or

```bash
python src/main.py
```

## Automation

The project uses GitHub Actions to:

- run every day on a schedule
- allow manual execution using `workflow_dispatch`
- generate a new report automatically

## Future Improvements

- Send reports to Discord via webhook.
- Send reports by email.
- Add more repository statistics.
- Improve report formatting.

## License

This project was created for educational purposes.