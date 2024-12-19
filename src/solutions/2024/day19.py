from functools import cache

import aoc_helper

DAY = 19
YEAR = 2024


def parse_input(input_text):
    towels, patterns = input_text.split("\n\n")
    towels = tuple(towels.split(", "))
    patterns = patterns.split("\n")
    return towels, patterns


@cache
def possible_pattern(pattern, towels):
    if pattern == "":
        return True
    for towel in towels:
        if pattern.startswith(towel) and possible_pattern(pattern[len(towel):], towels):
            return True
    return False


@cache
def count_pattern(pattern, towels):
    if pattern == "":
        return 1
    count = 0
    for towel in towels:
        if pattern.startswith(towel):
            count += count_pattern(pattern[len(towel):], towels)
    return count


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    towels, patterns = parse_input(input_text)
    return sum(possible_pattern(pattern, towels) for pattern in patterns)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    towels, patterns = parse_input(input_text)
    return sum(count_pattern(pattern, towels) for pattern in patterns)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
