from fetch import fetch_repo_data
from process import process_repo_data


def main() -> None:
    data = fetch_repo_data("python", "cpython")
    summary = process_repo_data(data)

    print(summary)


if __name__ == "__main__":
    main()