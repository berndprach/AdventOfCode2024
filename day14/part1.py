import re
from typing import NamedTuple


def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def integers_in(line: str) -> list[int]:
    return [int(x) for x in re.findall(r"-?\d+", line)]


class Robot(NamedTuple):
    p: tuple[int, int]
    v: tuple[int, int]


def parse_input(lines: list[str]):
    robots = []
    for line in lines:
        p0, p1, v0, v1 = integers_in(line)
        robots.append(Robot((p0, p1), (v0, v1)))
    return robots


def solve(lines: list[str], w=101, h=103) -> int:
    robots = parse_input(lines)
    print(robots)

    q_counts = {(b1, b2): 0 for b1 in [0, 1] for b2 in [0, 1]}
    for r in robots:
        final_x = (r.p[0] + 100 * r.v[0]) % w
        final_y = (r.p[1] + 100 * r.v[1]) % h
        if final_x == w // 2 or final_y == h // 2:
            continue
        q_counts[(final_x < w // 2, final_y < h // 2)] += 1
    print(q_counts)

    solution = 1
    for count in q_counts.values():
        solution *= count
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
