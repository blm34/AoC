import time

import aoc_helper

START_TIME = time.time()

input_text = aoc_helper.read_input(20, 2015)
target_presents = int(input_text)

houses = [0] * (target_presents // 10)
for elf in range(1, len(houses)):
    for house in range(0, len(houses), elf):
        houses[house] += 10 * elf
    if houses[elf] > target_presents:
        p1 = elf
        break

houses = [0] * (target_presents // 10)
for elf in range(1, len(houses)):
    for house in range(elf, min(elf*50+1, len(houses)), elf):
        houses[house] += 11 * elf
    if houses[elf] > target_presents:
        p2 = elf
        break

END_TIME = time.time()
RUN_TIME = END_TIME - START_TIME
aoc_helper.print_results(p1, p2, END_TIME-START_TIME)
