
import re


def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def solve(lines: list[str]) -> int:
    text = "".join(lines)
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)

    solution = 0
    for match in matches:
        solution += int(match[0]) * int(match[1])
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
