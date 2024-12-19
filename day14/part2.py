from time import sleep

from part1 import parse_input, read_input


def solve(lines: list[str]) -> int:
    robots = parse_input(lines)

    for i in range(10000):
        # sleep(0.01)
        # print(f"\nStep {i}:")

        x_values = [(r.p[0] + i * r.v[0]) % 101 for r in robots]
        y_values = [(r.p[1] + i * r.v[1]) % 103 for r in robots]

        positions = set(zip(x_values, y_values))
        nb_count = 0
        for x, y in positions:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if (x+dx, y+dy) in positions:
                    nb_count += 1

        if nb_count > 1000:
            print(f"\nStep {i}:")
            for y in range(103):
                row = []
                for x in range(101):
                    row.append("#" if (x, y) in positions else ".")
                print("".join(row))
            sleep(2)
            return i


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
