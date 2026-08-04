from fetch import fetch_repo_data
from process import process_repo_data


def main() -> None:
    data = fetch_repo_data("python", "cpython")

    if not data:
        print("No data was retrieved.")
        return

    summary = process_repo_data(data)

    if not summary:
        print("Failed to process data.")
        return

    print(summary)


if __name__ == "__main__":
    main()