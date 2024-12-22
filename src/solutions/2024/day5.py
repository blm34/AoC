import re

import aoc_helper

DAY = 5
YEAR = 2024


def ordered(update, rules) -> bool:
    for first, second in rules:
        if first not in update or second not in update:
            continue
        first_index = update.index(first)
        second_index = update.index(second)
        if second_index < first_index:
            return False
    return True


def sort_update(update, rules) -> list[int]:
    valid_rules = []
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            valid_rules.append(rule)

    while not ordered(update, valid_rules):
        for first, second in valid_rules:
            first_index = update.index(first)
            second_index = update.index(second)
            if second_index < first_index:
                update[first_index], update[second_index] = update[second_index], update[first_index]

    return update


def parse_input(input_text):
    rules, updates = input_text.split("\n\n")

    rules = re.findall(r"^(\d+)\|(\d+)$", rules, flags=re.MULTILINE)
    rules = tuple(tuple(map(int, rule)) for rule in rules)

    updates = [list(map(int, update.split(","))) for update in updates.split("\n")]

    return rules, updates


def p1(input_text):
    rules, updates = parse_input(input_text)

    result = 0
    for update in updates:
        if ordered(update, rules):
            middle_index = len(update) // 2
            result += update[middle_index]
    return result


def p2(input_text):
    rules, updates = parse_input(input_text)

    result = 0
    for update in updates:
        if ordered(update, rules):
            continue

        sorted_update = sort_update(update, rules)
        middle_index = len(sorted_update) // 2
        result += sorted_update[middle_index]

    return result


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
