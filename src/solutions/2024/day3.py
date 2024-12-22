import re

import aoc_helper

DAY = 3
YEAR = 2024


def product(string):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, string)
    result = 0
    for match in matches:
        result += int(match[0]) * int(match[1])
    return result


def p1(input_text):
    return product(input_text)


def p2(input_text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)"
    matches = re.findall(pattern, input_text)
    result = 0
    active = True
    for match in matches:
        if match[3] == "don't":
            active = False
        elif match[2] == "do":
            active = True
        elif active:
            result += int(match[0]) * int(match[1])
    return result


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
