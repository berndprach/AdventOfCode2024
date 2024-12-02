def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


Report = list[int]


def parse_lines(lines: list[str]) -> list[Report]:
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> Report:
    return [int(x) for x in line.split(" ")]


def is_safe(report: Report) -> bool:
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    is_strictly_increasing = all(d > 0 for d in differences)
    is_strictly_decreasing = all(d < 0 for d in differences)
    is_monotone = is_strictly_increasing or is_strictly_decreasing

    has_small_difference = all(abs(d) <= 3 for d in differences)

    return is_monotone and has_small_difference


def solve(lines: list[str]) -> int:
    reports = parse_lines(lines)
    return sum(1 for report in reports if is_safe(report))


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
