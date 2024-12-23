from collections import defaultdict
from functools import cmp_to_key

import aoc_helper

DAY = 5
YEAR = 2024


def ordered(update, rules) -> bool:
    for i in range(len(update) - 1):
        if update[i+1] not in rules[update[i]]:
            return False
    return True


def sort_update(update, rules) -> list[int]:
    def comparator(first, second):
        if second in rules[first]:
            return 1
        if first in rules[second]:
            return -1
        return 0

    return sorted(update, key=cmp_to_key(comparator))


def parse_input(input_text):
    rules_text, updates = input_text.split("\n\n")

    rules = defaultdict(set)  # key=page, value=set of pages that must come after key
    for rule in rules_text.splitlines():
        first, second = rule.split("|")
        rules[int(first)].add(int(second))

    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]

    return rules, updates


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    rules, updates = parse_input(input_text)

    p1 = 0
    p2 = 0

    for update in updates:
        if ordered(update, rules):
            p1 += update[len(update) // 2]
        else:
            sorted_update = sort_update(update, rules)
            p2 += sorted_update[len(sorted_update) // 2]

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
