
def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    return [int(v) for v in lines[0].split(" ")]


def step(n):
    if n == 0:
        return [1]
    if len(str(n)) % 2 == 0:
        n_str = str(n)
        s = len(n_str)
        s1_str, s2_str = n_str[:s//2], n_str[s//2:]
        return [int(s1_str), int(s2_str)]
    return [n*2024]


def eventual_count(n, number_of_steps, cache):
    s = number_of_steps
    if s == 0:
        return 1
    if (n, s) in cache:
        return cache[(n, s)]
    next_numbers = step(n)
    count = 0
    for next_number in next_numbers:
        count += eventual_count(next_number, s-1, cache)
    cache[(n, s)] = count
    return count


def solve(lines: list[str]) -> int:
    initial_stones = parse_input(lines)
    cache = {}
    return sum(eventual_count(n, 25, cache) for n in initial_stones)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
