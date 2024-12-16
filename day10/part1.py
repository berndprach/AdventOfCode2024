
def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    height = {}
    for y, line in enumerate(lines):
        for x, height_str in enumerate(line):
            height[(x, y)] = int(height_str)
    return height


def neighbours(position: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = position
    return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]


def solve(lines: list[str]) -> int:
    height = parse_input(lines)
    starting_positions = [p for p, h in height.items() if h == 0]
    return sum(get_trail_score(p, height) for p in starting_positions)


def get_trail_score(starting_positions, height):
    current_positions = [starting_positions]
    for h in range(1, 10):
        candidates = {n for p in current_positions for n in neighbours(p)}
        current_positions = {p for p in candidates if height.get(p, None) == h}
    return len(current_positions)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
