import time

import aoc_helper

DAY = 20
YEAR = 2015
START_TIME = time.time()


def parse_input(input_text):
    return int(input_text)


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    target_presents = parse_input(input_text)
    houses = [0] * (target_presents // 10)
    for elf in range(1, len(houses)):
        for house in range(0, len(houses), elf):
            houses[house] += 10 * elf
        if houses[elf] > target_presents:
            return elf


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    target_presents = parse_input(input_text)
    houses = [0] * (target_presents // 10)
    for elf in range(1, len(houses)):
        for house in range(elf, min(elf * 50 + 1, len(houses)), elf):
            houses[house] += 11 * elf
        if houses[elf] > target_presents:
            return elf


if __name__ == "__main__":
    p1_res = p1()
    p2_res = p2()

    END_TIME = time.time()
    aoc_helper.print_results(p1_res, p2_res, END_TIME - START_TIME)
