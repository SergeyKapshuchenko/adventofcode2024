def is_safe(report: list[int]) -> bool:
    min_dif, max_dif = (1, 3) if report[1] > report[0] else (-3, -1)

    for i in range(1, len(report)):
        if not min_dif <= report[i] - report[i - 1] <= max_dif:
            return False

    return True


def is_safe_with_allowed_bad_level(report: list[int]) -> bool:
    combinations = [report[:i] + report[i + 1 :] for i in range(len(report))]
    combinations.append(report)
    return any(is_safe(comb) for comb in combinations)


def count_safe_reports(reports: list[list[int]]) -> int:
    return sum(is_safe(report) for report in reports)


def count_safe_reports_with_allowed_bad_level(reports: list[list[int]]) -> int:
    return sum(is_safe_with_allowed_bad_level(report) for report in reports)


def read_input(file_path: str) -> list[list[int]]:
    with open(file_path) as file:
        return [[int(x) for x in line.split()] for line in file]


if __name__ == "__main__":
    reports = read_input("input.txt")

    # part 1
    print(count_safe_reports(reports))

    # part 2
    print(count_safe_reports_with_allowed_bad_level(reports))
