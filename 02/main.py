def is_report_valid(report: list[int]) -> bool:
    max_allowed = 3
    is_increasing = is_decreasing = True
    for i in range(1, len(report)):
        difference = report[i] - report[i - 1]
        if difference == 0 or abs(difference) > max_allowed:
            return False
        if difference > 0:
            is_decreasing = False
        elif difference < 0:
            is_increasing = False
    return is_increasing or is_decreasing


def count_valid_reports(reports: list[list[int]]) -> int:
    valid_count = 0
    for report in reports:
        if is_report_valid(report):
            valid_count += 1
    return valid_count


def is_report_valid_second_part(report: list[int]) -> bool:
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1 :]
        if is_report_valid(new_report):
            return True
    return False


def count_valid_reports_second_part(reports: list[list[int]]) -> int:
    valid_count = 0
    for report in reports:
        if is_report_valid_second_part(report):
            valid_count += 1
    return valid_count


def main() -> None:
    reports = [[int(x) for x in line.split()] for line in open("input.txt").readlines()]
    print(
        f"Part 1: {count_valid_reports(reports)}\n"
        f"Part 2: {count_valid_reports_second_part(reports)}"
    )


if __name__ == "__main__":
    main()
