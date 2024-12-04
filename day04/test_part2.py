from pathlib import Path

from .part2 import solve


GOAL_SOLUTION = 9


def read_test_lines():
    test_input_path = Path(__file__).parent / "test_input.txt"
    with open(test_input_path, "r") as f:
        lines = f.read().splitlines()
    return lines


def test_solve():
    lines = read_test_lines()
    solution = solve(lines)
    assert solution == GOAL_SOLUTION
