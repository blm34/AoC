import re

import aoc_helper

DAY = 1
YEAR = 2024


def parse_input(input_text):
    pattern = r"^(\d+)\s+(\d+)$"
    matches = re.findall(pattern, input_text, re.MULTILINE)
    left, right = list(), list()
    for a, b in matches:
        left.append(int(a))
        right.append(int(b))
    return left, right


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    left, right = parse_input(input_text)

    left.sort()
    right.sort()

    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])

    return distance


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    left, right = parse_input(input_text)

    similarity = 0
    for num in left:
        count = right.count(num)
        similarity += num * count

    return similarity


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
