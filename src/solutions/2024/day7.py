import re

import aoc_helper

DAY = 7
YEAR = 2024


def parse_input(input_text):
    L = input_text.split('\n')
    equations = list()
    for line in L:
        match = re.match(r"(\d+):((\s\d+){2,})", line)
        result = int(match.group(1))
        operands = tuple(map(int, match.group(2).split()))
        equations.append((result, operands))
    return equations


def count_digits(num):
    d = 1
    while 10**d < num:
        d += 1
    return d


def valid(target, nums, p2=False):
    if len(nums) == 1:
        return target == nums[0]
    v = valid(target - nums[-1], nums[:-1], p2)
    v = v or (target % nums[-1] == 0 and valid(target // nums[-1], nums[:-1], p2))
    if p2:
        digits = count_digits(nums[-1])
        if target % (10**digits) == nums[-1]:
            v = v or valid(target//(10**digits), nums[:-1], p2)
    return v


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    equations = parse_input(input_text)
    result = 0
    for equation in equations:
        if valid(*equation):
            result += equation[0]
    return result


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    equations = parse_input(input_text)
    result = 0
    for equation in equations:
        if valid(*equation, p2=True):
            result += equation[0]
    return result


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
