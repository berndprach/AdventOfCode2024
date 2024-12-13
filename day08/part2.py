from part1 import parse_input, read_input, same_frequency_pair, is_inside


def get_half_line(p1, p2, size):
    x, y = p1
    dx, dy = p2[0] - x, p2[1] - y
    while is_inside((x, y), size):
        yield x, y
        x, y = x + dx, y + dy


def solve(lines: list[str]) -> int:
    antennas, size = parse_input(lines)

    antinodes = set()
    for p1, p2 in same_frequency_pair(antennas):
        antinodes.update(get_half_line(p1, p2, size))
        antinodes.update(get_half_line(p2, p1, size))

    return len(antinodes)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
