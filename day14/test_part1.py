from pathlib import Path

from part1 import solve, parse_input

GOAL_SOLUTION = 480


def read_test_lines():
    test_input_path = Path(__file__).parent / "test_input.txt"
    with open(test_input_path, "r") as f:
        lines = f.read().splitlines()
    return lines


def test_parsing():
    lines = read_test_lines()
    machines = parse_input(lines)
    assert len(machines) == 4
    assert machines[0].a == (94, 34)
    assert machines[0].b == (22, 67)
    assert machines[0].goal == (8400, 5400)


def test_solve():
    lines = read_test_lines()
    solution = solve(lines)
    print(f"Solution: {solution}")
    assert solution == GOAL_SOLUTION


if __name__ == "__main__":
    test_parsing()
    test_solve()
