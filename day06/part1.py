from enum import Enum


def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


class DIRECTION(Enum):
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)


ORDERED_DIRECTIONS = [
    DIRECTION.NORTH,
    DIRECTION.EAST,
    DIRECTION.SOUTH,
    DIRECTION.WEST
]


def turn_right(current_direction: DIRECTION) -> DIRECTION:
    current_index = ORDERED_DIRECTIONS.index(current_direction)
    new_index = (current_index + 1) % len(ORDERED_DIRECTIONS)
    return ORDERED_DIRECTIONS[new_index]


def move(position: tuple[int, int], direction: DIRECTION) -> tuple[int, int]:
    return position[0] + direction.value[0], position[1] + direction.value[1]


def parse_input(lines: list[str]):
    empty = {}
    position = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            empty[(x, y)] = (char != "#")
            if char == "^":
                position = (x, y)
    return empty, position


def get_visited_positions(is_empty, initial_position):
    visited_positions = set()
    direction = DIRECTION.NORTH
    position = initial_position
    while position in is_empty.keys():
        visited_positions.add(position)
        next_position = move(position, direction)
        if is_empty.get(next_position, True):
            position = next_position
            continue
        direction = turn_right(direction)
    return visited_positions


def solve(lines: list[str]) -> int:
    is_empty, position = parse_input(lines)
    visited_positions = get_visited_positions(is_empty, position)
    return len(visited_positions)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
