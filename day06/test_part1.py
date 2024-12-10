from pathlib import Path

from part1 import solve

GOAL_SOLUTION = 41


def read_test_lines():
    test_input_path = Path(__file__).parent / "test_input.txt"
    with open(test_input_path, "r") as f:
        lines = f.read().splitlines()
    return lines


def test_solve():
    lines = read_test_lines()
    solution = solve(lines)
    assert solution == GOAL_SOLUTION


if __name__ == "__main__":
    test_solve()
