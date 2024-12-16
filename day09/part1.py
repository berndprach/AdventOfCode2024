
def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    line = lines[0]
    return [int(character) for character in line]


class BidirectionalIterator:
    def __init__(self, data):
        self.data = data
        self.s = 0
        self.t = len(data) - 1

    def next(self, from_start=True):
        if from_start:
            digit = self.data[self.s]
            self.s += 1
        else:
            digit = self.data[self.t]
            self.t -= 1
        return digit


def solve(lines: list[str]) -> int:
    disk_map = parse_input(lines)
    print(disk_map)

    id_numbers = get_id_numbers(disk_map)
    print(id_numbers)

    new_map = get_new_disk_map(disk_map, id_numbers)
    return get_checksum(new_map)


def get_id_numbers(disk_map):
    id_numbers = []
    for i, length in enumerate(disk_map[::2]):
        id_numbers.extend([i] * length)
    return id_numbers


def get_checksum(disk_map):
    checksum = 0
    for p, id_number in enumerate(disk_map):
        checksum += id_number * p
    return checksum


def get_new_disk_map(disk_map, id_numbers):
    current_is_empty = False
    is_empty = []
    for n in disk_map:
        is_empty.extend([current_is_empty] * n)
        current_is_empty = not current_is_empty

    bi_iter = BidirectionalIterator(id_numbers)
    new_map = []
    for current_is_empty in is_empty[:len(id_numbers)]:
        next_id_number = bi_iter.next(from_start=not current_is_empty)
        new_map.append(next_id_number)
    return new_map


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
