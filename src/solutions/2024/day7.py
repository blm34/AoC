import aoc_helper

DAY = 7
YEAR = 2024


def parse_input(input_text):
    equations = list()
    for line in input_text.splitlines():
        result, operands = line.split(": ")
        operands = tuple(map(int, operands.split()))
        equations.append((int(result), operands))
    return equations


def valid(target, nums):
    """
    Returns:
        0: if not valid in either part
        1: if valid in parts 1 and 2
        2: if valid in only part 2
    """
    if len(nums) == 1:
        return target == nums[0]

    add = valid(target - nums[-1], nums[:-1])
    if add == 1:
        return 1

    mult = target % nums[-1] == 0 and valid(target // nums[-1], nums[:-1])
    if mult == 1:
        return 1

    if add == 2 or mult == 2:
        return 2

    digits = aoc_helper.digit_count(nums[-1])
    concat = target % (10**digits) == nums[-1] and valid(target // (10**digits), nums[:-1])
    if concat:
        return 2

    return 0


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    equations = parse_input(input_text)
    
    p1 = 0
    p2 = 0

    for equation in equations:
        v = valid(*equation)
        if v == 1:
            p1 += equation[0]
            p2 += equation[0]
        elif v == 2:
            p2 += equation[0]

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
