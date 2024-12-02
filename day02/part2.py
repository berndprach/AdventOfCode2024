
from day02.part1 import read_input, parse_lines, Report, is_safe


def is_mostly_safe(report: Report) -> bool:
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[0:i] + report[i+1:]):
            return True

    return False


def solve(lines: list[str]) -> int:
    reports = parse_lines(lines)
    return sum(1 for report in reports if is_mostly_safe(report))


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
