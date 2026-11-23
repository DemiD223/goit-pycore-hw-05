import sys


def parse_log_line(line: str) -> dict:
    """Split a log line into date, time, level and message."""
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        raise ValueError(f"Invalid log line: {line}")
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> list:
    """Read the log file and return a list of parsed log lines."""
    logs = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                logs.append(parse_log_line(line))
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Return only logs with the given level."""
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """Count how many logs there are for each level."""
    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts


def display_log_counts(counts: dict):
    """Print a table with log counts."""
    print(f"{'Рівень логування':<17}| Кількість")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <log_file> [level]")
        return

    try:
        logs = load_logs(sys.argv[1])
    except FileNotFoundError:
        print("File not found")
        return
    except ValueError as error:
        print(error)
        return

    display_log_counts(count_logs_by_level(logs))

    if len(sys.argv) > 2:
        level = sys.argv[2]
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filter_logs_by_level(logs, level):
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()