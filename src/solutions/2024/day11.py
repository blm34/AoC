from collections import Counter, defaultdict
from functools import cache

import aoc_helper

DAY = 11
YEAR = 2024


@cache
def blink(stone):
    if stone == 0:
        return 1,
    d = len(str(stone))
    if d % 2 == 0:
        return divmod(stone, 10**(d//2))
    return stone * 2024,


def count_new_stones(stones, blinks):
    for _ in range(blinks):
        new_stones = defaultdict(int)
        for stone in stones:
            for new_stone in blink(stone):
                new_stones[new_stone] += stones[stone]
        stones = new_stones
    return stones


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    stones = Counter(map(int, input_text.split()))

    stones = count_new_stones(stones, 25)
    p1 = sum(stones.values())
    stones = count_new_stones(stones, 50)
    p2 = sum(stones.values())

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
