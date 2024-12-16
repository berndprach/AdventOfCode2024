from typing import NamedTuple, Optional

from part1 import parse_input, read_input, get_checksum


class Block(NamedTuple):
    id_number: Optional[int]
    length: int


def extend_disk_map(disk_map):
    block = {}
    starting_positions = []

    current_is_empty = False
    current_id_number = 0
    current_position = 0
    for length in disk_map:
        block_id = None if current_is_empty else current_id_number
        block[current_position] = Block(block_id, length)
        if not current_is_empty:
            starting_positions.append(current_position)

        current_is_empty = not current_is_empty
        if not current_is_empty:
            current_id_number += 1
        current_position += length
    return block, starting_positions


def get_new_disk_map(disk_map):
    block, starting_positions = extend_disk_map(disk_map)

    first_empty = {s: 0 for s in range(1, 10)}
    update_empty_slots(block, first_empty)

    for s in reversed(starting_positions):
        b = block[s]
        new_start = first_empty[b.length]
        if new_start is None or new_start > s:
            continue

        print(f"Moving block {b} from {s} to {new_start}.")
        block[s] = Block(None, b.length)
        if block[new_start].length > b.length:
            new_empty_block = Block(None, block[new_start].length - b.length)
            block[new_start + b.length] = new_empty_block
        block[new_start] = b

        update_empty_slots(block, first_empty)
    return block


def update_empty_slots(block, first_empty):
    for key in list(first_empty.keys()):
        first_empty[key] = next_empty_slot(block, key, first_empty[key])


def next_empty_slot(block, length, previous):
    position = previous
    while position in block.keys():
        b = block[position]
        if b.id_number is None and b.length >= length:
            return position
        position += b.length
    return None


def get_checksum(block):
    checksum = 0
    for p, b in block.items():
        if b.id_number is None:
            continue
        sum_p = p * b.length + b.length * (b.length - 1) // 2
        block_checksum = b.id_number * sum_p
        checksum += block_checksum
    return checksum


def solve(lines: list[str]) -> int:
    disk_map = parse_input(lines)
    new_blocks = get_new_disk_map(disk_map)
    return get_checksum(new_blocks)


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
