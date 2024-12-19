import re
from typing import NamedTuple


def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def integers_in(line: str) -> list[int]:
    return [int(x) for x in re.findall(r"\d+", line)]


class Machine(NamedTuple):
    a: tuple[int, int]
    b: tuple[int, int]
    goal: tuple[int, int]


def parse_input(lines: list[str]):
    line = iter(lines)
    machines = []
    while True:
        try:
            a_move = tuple(integers_in(next(line)))
            b_move = tuple(integers_in(next(line)))
            goal = tuple(integers_in(next(line)))
            machines.append(Machine(a_move, b_move, goal))
            next(line)
        except StopIteration:
            break
    return machines


def find_cheapest_combination(m: Machine):
    a_presses = 0
    a_position = (0, 0)
    best_solution = None
    while a_position[0] < m.goal[0] and a_position[1] < m.goal[1]:
        b_presses = (m.goal[0] - a_position[0]) // m.b[0]
        x_matches = (a_position[0] + b_presses * m.b[0] == m.goal[0])
        y_matches = (a_position[1] + b_presses * m.b[1] == m.goal[1])
        if x_matches and y_matches:
            cost = 3 * a_presses + 1 * b_presses
            if best_solution is None or cost < best_solution:
                best_solution = cost
        a_presses += 1
        a_position = (a_presses * m.a[0], a_presses * m.a[1])
    return best_solution


def solve(lines: list[str]) -> int:
    machines = parse_input(lines)
    solution = 0
    for m in machines:
        print(m)
        cc = find_cheapest_combination(m)
        if cc is not None:
            solution += cc

    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
