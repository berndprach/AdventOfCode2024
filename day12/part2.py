from part1 import parse_input, read_input, neighbors

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def connected_components(positions):
    positions = set(positions)
    visited = set()
    components = 0
    for position in positions:
        if position in visited:
            continue
        components += 1
        stack = [position]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in neighbors(current):
                if neighbor in positions:
                    stack.append(neighbor)
    return components


def get_measure(start_position, plant, visited):
    area = 0
    perimeter = {d: [] for d in DIRECTIONS}
    stack = [start_position]
    while stack:
        position = stack.pop()
        if position in visited:
            continue
        area += 1
        visited.add(position)
        for direction in DIRECTIONS:
            neighbor = (position[0] + direction[0], position[1] + direction[1])
            if plant.get(neighbor) == plant[start_position]:
                stack.append(neighbor)
            else:
                perimeter[direction].append(neighbor)

    sides = sum(connected_components(nbs) for nbs in perimeter.values())
    return area, sides


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
