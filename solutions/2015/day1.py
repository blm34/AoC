import time

import aoc_helper

DAY = 1
YEAR = 2015
START_TIME = time.time()

@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    ans = 0
    for i, char in enumerate(input_text):
        if char == '(':
            ans += 1
        elif char == ')':
            ans -= 1
    return ans


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    floor = 0
    for i, char in enumerate(input_text):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return i+1


if __name__ == "__main__":
    p1_res = p1()
    p2_res = p2()

    END_TIME = time.time()
    aoc_helper.print_results(p1_res, p2_res, END_TIME - START_TIME)
