from .part2 import solve
from .test_part1 import read_test_lines

GOAL_SOLUTION = 123


def test_solve():
    lines = read_test_lines()
    solution = solve(lines)
    assert solution == GOAL_SOLUTION
