def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    plant = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            plant[(x, y)] = c
    return plant


def neighbors(position):
    x, y = position
    return [(x + dx, y + dy) for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]


def get_measure(start_position, plant, visited):
    area = 0
    perimeter = 0
    stack = [start_position]
    while stack:
        position = stack.pop()
        if position in visited:
            continue
        area += 1
        perimeter += 4
        visited.add(position)
        for neighbor in neighbors(position):
            if plant.get(neighbor) == plant[start_position]:
                perimeter -= 1
                stack.append(neighbor)

    return area, perimeter


def solve(lines: list[str]) -> int:
    plant = parse_input(lines)
    visited = set()
    price = 0
    for position in plant.keys():
        if position in visited:
            continue
        area, perimeter = get_measure(position, plant, visited)
        price += area * perimeter
    return price


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
