from part2 import solve
from test_part1 import read_test_lines

GOAL_SOLUTION = 11387


def test_solve():
    lines = read_test_lines()
    solution = solve(lines)
    assert solution == GOAL_SOLUTION


if __name__ == "__main__":
    test_solve()
    print("part2 test passed")
