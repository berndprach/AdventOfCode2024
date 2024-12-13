
def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    return [parse_line(line) for line in lines]


def parse_line(line: str) -> tuple[int, list[int]]:
    left, right = line.split(": ")
    test_value = int(left)
    remaining_numbers = [int(x) for x in right.split(" ")]
    return test_value, remaining_numbers


def goal_in_results(inputs: list[int], goal: int) -> bool:
    possible_values = [inputs[0]]
    for value in inputs[1:]:
        addition_values = [v + value for v in possible_values]
        multiplication_values = [v * value for v in possible_values]
        possible_values = addition_values + multiplication_values
        possible_values = [v for v in possible_values if v <= goal]
    return goal in possible_values


def solve(lines: list[str]) -> int:
    inputs = parse_input(lines)
    solution = 0
    for goal, inputs in inputs:
        if goal_in_results(inputs, goal):
            solution += goal
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
