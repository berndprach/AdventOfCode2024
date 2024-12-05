def read_input() -> list[str]:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    return lines


def parse_input(lines: list[str]):
    _required: dict[int, list[int]] = {}
    lines = iter(lines)
    for line in lines:
        if line == "":
            break
        pn1, pn2 = line.split("|")
        _required[int(pn2)] = _required.get(int(pn2), []) + [int(pn1)]
    required: dict[int, set[int]] = {k: set(v) for k, v in _required.items()}

    page_orderings: list[list[int]] = []
    for line in lines:
        page_ordering = [int(v) for v in line.split(",")]
        page_orderings.append(page_ordering)

    return required, page_orderings


def is_ordered(page_ordering: list[int], required) -> bool:
    all_pages = set(page_ordering)
    pages_seen = set()
    for page_number in page_ordering:
        for required_page in required.get(page_number, set()):
            if required_page in all_pages and required_page not in pages_seen:
                return False
        pages_seen.add(page_number)
    return True


def solve(lines: list[str]) -> int:
    required, page_orderings = parse_input(lines)
    solution = 0
    for page_ordering in page_orderings:
        if is_ordered(page_ordering, required):
            solution += page_ordering[len(page_ordering)//2]
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
