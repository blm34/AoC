import re

import aoc_helper

DAY = 3
YEAR = 2024


def product(string):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, string)
    return sum(int(match[0]) * int(match[1])
               for match in matches)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    p1 = product(input_text)

    p2_string = re.sub(r"don't\(\).*?do\(\)", " ", input_text, flags=re.DOTALL)
    p2_string = re.sub(r"don't\(\).*", "", p2_string, flags=re.DOTALL)
    p2 = product(p2_string)

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
