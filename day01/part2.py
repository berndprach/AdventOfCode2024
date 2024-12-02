from collections import Counter

from day01.part1 import read_input, parse_lines


def solve(lines: list[str]) -> int:
    list1, list2 = parse_lines(lines)
    list2_counts = Counter(list2)
    solution = sum([n * list2_counts[n] for n in list1])
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
