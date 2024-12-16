from part1 import parse_input, read_input, neighbours


def solve(lines: list[str]) -> int:
    height = parse_input(lines)
    starting_positions = [p for p, h in height.items() if h == 0]
    return sum(get_trail_rating(p, height) for p in starting_positions)


def get_trail_rating(starting_positions, height):
    current_positions = [starting_positions]
    for h in range(1, 10):
        candidates = [n for p in current_positions for n in neighbours(p)]
        current_positions = [p for p in candidates if height.get(p, None) == h]
    return len(current_positions)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
