import re

from day03.part1 import read_input


def solve(lines: list[str]) -> int:
    text = "".join(lines)
    pattern = r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))"
    matches = re.findall(pattern, text)

    solution = 0
    is_on = True
    for match in matches:
        print(match)
        if match[0] == "do()":
            is_on = True
        elif match[0] == "don't()":
            is_on = False
        elif is_on:
            solution += int(match[1]) * int(match[2])
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
