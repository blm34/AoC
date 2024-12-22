import re
import heapq

import aoc_helper

DAY = 25
YEAR = 2015


def parse_input(input_text):
    match = re.search(r"row (\d+), column (\d+)", input_text)
    row = int(match.group(1))
    col = int(match.group(2))
    return row, col


def get_index(row, col):
    diagonal_row = row + col - 1
    first_in_diag_row = diagonal_row * (diagonal_row - 1) // 2 + 1
    return first_in_diag_row + col - 1



def p1(input_text):
    row, col = parse_input(input_text)
    index = get_index(row, col)

    init_val = 20151125
    mul = 252533
    mod = 33554393

    ans = init_val
    for i in range(index-1):
        ans = (ans * mul) % mod

    return ans


def p2(input_text):
    return None


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
