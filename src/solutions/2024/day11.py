from functools import cache

import aoc_helper
from aoc_helper import digit_count

DAY = 11
YEAR = 2024


@cache
def blink(stone):
    if stone == 0:
        return 1,
    d = digit_count(stone)
    if d % 2 == 0:
        return divmod(stone, 10**(d//2))
    return stone * 2024,


@cache
def count_new_stones(stone, blinks):
    if blinks == 0:
        return 1
    new_stones = blink(stone)
    ans = 0
    for new_stone in new_stones:
        ans += count_new_stones(new_stone, blinks-1)
    return ans


def p1(input_text):
    stones = list(map(int, input_text.split()))
    return sum(count_new_stones(stone, 25) for stone in stones)


def p2(input_text):
    stones = list(map(int, input_text.split()))
    return sum(count_new_stones(stone, 75) for stone in stones)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
