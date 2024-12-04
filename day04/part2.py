from day04.part1 import read_input, parse_input


def generate_patterns():
    for order1 in ["MAS", "SAM"]:
        for order2 in ["MAS", "SAM"]:
            yield {
                (-1, -1): order1[0],
                (0, 0): order1[1],
                (1, 1): order1[2],
                (-1, 1): order2[0],
                (1, -1): order2[2],
            }


def is_match(grid, start, pattern):
    x, y = start
    for (dx, dy), letter in pattern.items():
        pos = x+dx, y+dy
        if pos not in grid or grid[pos] != letter:
            return False
    return True


def solve(lines: list[str]) -> int:
    grid = parse_input(lines)
    count = 0
    for start in grid.keys():
        for pattern in generate_patterns():
            if is_match(grid, start, pattern):
                count += 1
    return count


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
