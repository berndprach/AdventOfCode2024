def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


WORD = "XMAS"
Grid = dict[tuple[int, int], str]


def parse_input(lines: list[str]) -> Grid:
    grid = {}
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            grid[(x, y)] = character
    return grid


DIRECTIONS = [
    (i, j) for i in {-1, 0, 1} for j in {-1, 0, 1} if (i, j) != (0, 0)
]


def is_match(grid, start, direction, word):
    x, y = start
    dx, dy = direction
    for i, letter in enumerate(word):
        if (x, y) not in grid or grid[(x, y)] != letter:
            return False
        x += dx
        y += dy
    return True


def solve(lines: list[str]) -> int:
    grid = parse_input(lines)
    count = 0
    for start in grid.keys():
        for direction in DIRECTIONS:
            if is_match(grid, start, direction, WORD):
                count += 1
    return count


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
