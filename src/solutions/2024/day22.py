from collections import defaultdict

import aoc_helper

DAY = 22
YEAR = 2024


def iterate(num, iters):
    for _ in range(iters):
        num = step(num)
    return num


def step(num):
    num = (num ^ (num * 64)) & 0xffffff
    num = (num ^ (num // 32))
    num = (num ^ (num * 2048)) & 0xffffff
    return num


def get_best_sequence(nums):
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
    return max(totals.values())


def p1(input_text):
    nums = map(int, input_text.split('\n'))
    return sum(iterate(num, 2000) for num in nums)


def p2(input_text):
    nums = map(int, input_text.split('\n'))
    return get_best_sequence(nums)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
