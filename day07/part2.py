from part1 import parse_input, read_input


OPERATIONS = [
    lambda x, y: x + y,
    lambda x, y: x * y,
    lambda x, y: int(str(x) + str(y)),
]


def goal_in_results(inputs: list[int], goal: int, operations) -> bool:
    possible_values = [inputs[0]]
    for value in inputs[1:]:
        new_values = []
        for operation in operations:
            new_values += [operation(v, value) for v in possible_values]
        possible_values = [v for v in new_values if v <= goal]
    return goal in possible_values


def solve(lines: list[str]) -> int:
    inputs = parse_input(lines)
    solution = 0
    for goal, inputs in inputs:
        if goal_in_results(inputs, goal, OPERATIONS):
            solution += goal
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
