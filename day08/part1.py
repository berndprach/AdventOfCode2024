from itertools import combinations


def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    antennas = {}
    for y, line in enumerate(lines):
        for x, character in enumerate(line):
            if character == ".":
                continue
            antennas[character] = antennas.get(character, []) + [(x, y)]
    return antennas, (len(lines[0]), len(lines))


def goal_in_results(inputs: list[int], goal: int) -> bool:
    possible_values = [inputs[0]]
    for value in inputs[1:]:
        addition_values = [v + value for v in possible_values]
        multiplication_values = [v * value for v in possible_values]
        possible_values = addition_values + multiplication_values
        possible_values = [v for v in possible_values if v <= goal]
    return goal in possible_values


def same_frequency_pair(antennas: dict[str, tuple[int, int]]):
    for f_antennas in antennas.values():
        for pair in combinations(f_antennas, 2):
            yield pair


def get_antinodes(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a1 = 2 * x1 - x2, 2 * y1 - y2
    a2 = 2 * x2 - x1, 2 * y2 - y1
    return a1, a2


def is_inside(p, size):
    return 0 <= p[0] < size[0] and 0 <= p[1] < size[1]


def solve(lines: list[str]) -> int:
    antennas, size = parse_input(lines)

    antinodes = set()
    for p1, p2 in same_frequency_pair(antennas):
        pair_antinodes = get_antinodes(p1, p2)
        antinodes.update(pair_antinodes)

    valid_antinodes = [a for a in antinodes if is_inside(a, size)]
    return len(valid_antinodes)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
