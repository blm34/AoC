from collections import defaultdict

import aoc_helper

DAY = 22
YEAR = 2024


def step(num):
    num = (num ^ (num * 64)) & 0xffffff
    num = (num ^ (num // 32))
    num = (num ^ (num * 2048)) & 0xffffff
    return num


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    nums = map(int, input_text.split('\n'))
    p1 = 0

    totals = defaultdict(int)
    for num in nums:
        seen = set()
        sequence = 0
        for i in range(2000):
            last_price = num % 10
            num = step(num)
            sequence = (sequence * 20 + (num % 10 - last_price)) % 20**4
            if i >= 3 and sequence not in seen:
                seen.add(sequence)
                totals[sequence] += num % 10
        p1 += num
    return p1, max(totals.values())


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
