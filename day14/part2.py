from part1 import parse_input, read_input, Machine

C = 10000000000000


def find_cheapest_combination(m: Machine):
    """
    alpha a[0] + beta b[0] = goal[0]
    alpha a[1] + beta b[1] = goal[1]
    => beta b[0] a[1] - beta b[1] a[0] = goal[0] a[1] - goal[1] a[0]
    => beta = (goal[0] a[1] - goal[1] a[0]) / (b[0] a[1] - b[1] a[0])
    """

    denominator = m.b[0] * m.a[1] - m.b[1] * m.a[0]
    if denominator == 0:
        raise ValueError("This will require some more work!")

    beta = (m.goal[0] * m.a[1] - m.goal[1] * m.a[0]) // denominator
    alpha = (m.goal[0] - beta * m.b[0]) // m.a[0]
    x_matches = (alpha * m.a[0] + beta * m.b[0] == m.goal[0])
    y_matches = (alpha * m.a[1] + beta * m.b[1] == m.goal[1])

    if x_matches and y_matches:
        return 3 * alpha + 1 * beta
    else:
        return None


def solve(lines: list[str]) -> int:
    machines = parse_input(lines)
    for i in range(len(machines)):
        m = machines[i]
        new_goal = (m.goal[0] + C, m.goal[1] + C)
        machines[i] = Machine(m.a, m.b, new_goal)

    solution = 0
    for m in machines:
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
