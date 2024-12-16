from part1 import parse_input, read_input, eventual_count


def solve(lines: list[str]) -> int:
    initial_stones = parse_input(lines)
    cache = {}
    return sum(eventual_count(n, 75, cache) for n in initial_stones)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
