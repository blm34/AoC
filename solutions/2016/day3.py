import re
import heapq

import aoc_helper

DAY = 3
YEAR = 2016


def valid_triangle(sides):
    sides = sorted(sides)
    return sides[0] + sides[1] > sides[2]


def parse_input(input_text):
    pattern = r"\s*(\d+)\s+(\d+)\s+(\d+)"
    match = re.findall(pattern, input_text, re.MULTILINE)
    match = [[int(num) for num in line] for line in match]
    return match


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    all_sides = parse_input(input_text)
    possible = 0
    for sides in all_sides:
        possible += valid_triangle(sides)
    return possible


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    all_sides = parse_input(input_text)
    possible = 0
    for i in range(0, len(all_sides), 3):
        for j in range(3):
            sides = []
            for k in range(3):
                sides.append(all_sides[i + k][j])
            possible += valid_triangle(sides)
    return possible


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
