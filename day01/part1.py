def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_lines(lines: list[str]) -> tuple[list[int], list[int]]:
    list1, list2 = [], []
    for line in lines:
        number_strings = line.split()
        list1.append(int(number_strings[0]))
        list2.append(int(number_strings[1]))

    return list1, list2


def solve(lines: list[str]) -> int:
    list1, list2 = parse_lines(lines)
    list1.sort()
    list2.sort()
    total_difference = 0
    for n1, n2 in zip(list1, list2):
        difference = abs(n1 - n2)
        total_difference += difference
    return total_difference


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
