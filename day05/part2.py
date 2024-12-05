from day05.part1 import read_input, parse_input, is_ordered


def get_fixed_ordering(page_ordering: list[int], required) -> list[int]:
    new_ordering = []
    all_pages = set(page_ordering)
    pages_added = set()
    q = [page for page in page_ordering]
    i = 0
    while i < len(q):
        page_number = q[i]
        i += 1
        req = required.get(page_number, set())
        if requirements_fulfilled(req, pages_added, all_pages):
            new_ordering.append(page_number)
            pages_added.add(page_number)
        else:
            q.append(page_number)
    return new_ordering


def requirements_fulfilled(required_pages, pages_added: set[int], all_pages):
    for required_page in required_pages:
        if required_page in all_pages and required_page not in pages_added:
            return False
    return True


def solve(lines: list[str]) -> int:
    required, page_orderings = parse_input(lines)
    solution = 0
    for page_ordering in page_orderings:
        if is_ordered(page_ordering, required):
            print(f"Ordered: {page_ordering}")
            continue

        fixed_ordering = get_fixed_ordering(page_ordering, required)
        solution += fixed_ordering[len(fixed_ordering)//2]
        print(f"Fixed ordering: {fixed_ordering}")
    return solution


def main():
    lines = read_input()
    solution = solve(lines)
    print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
