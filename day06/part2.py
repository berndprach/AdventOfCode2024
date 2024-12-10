from part1 import read_input, parse_input, get_visited_positions, DIRECTION, \
    move, turn_right

Position = tuple[int, int]


def is_loop(is_empty, initial_position):
    direction = DIRECTION.NORTH
    position = initial_position
    visited: set[tuple[Position, DIRECTION]] = set()
    while position in is_empty.keys():
        if (position, direction) in visited:
            return True
        visited.add((position, direction))
        next_position = move(position, direction)
        if is_empty.get(next_position, True):
            position = next_position
        else:
            direction = turn_right(direction)

    return False


def solve(lines: list[str]) -> int:
    is_empty, starting_position = parse_input(lines)
    visited_positions = get_visited_positions(is_empty, starting_position)

    solution = 0
    for position in visited_positions:
        is_empty[position] = False
        if is_loop(is_empty, starting_position):
            solution += 1
        is_empty[position] = True

    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
