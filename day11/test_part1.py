from pathlib import Path

from part1 import solve, step

GOAL_SOLUTION = 55312


def read_test_lines():
    test_input_path = Path(__file__).parent / "test_input.txt"
    with open(test_input_path, "r") as f:
        lines = f.read().splitlines()
    return lines


def test_step():
    assert step(0) == [1]
    assert step(1) == [2024]
    assert step(12) == [1, 2]


def test_solve():
    lines = read_test_lines()
    solution = solve(lines)
    print(f"Solution: {solution}")
    assert solution == GOAL_SOLUTION


if __name__ == "__main__":
    test_step()
    test_solve()
