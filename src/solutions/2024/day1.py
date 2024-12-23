from collections import Counter

import aoc_helper

DAY = 1
YEAR = 2024


def parse_input(input_text):
    left, right = list(), list()
    for line in input_text.split("\n"):
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    return left, right


def p1(left, right):
    left.sort()
    right.sort()

    distance = 0
    for left_num, right_num in zip(left, right):
        distance += abs(left_num - right_num)

    return distance


def p2(left, right):
    left = Counter(left)
    right = Counter(right)

    return sum(num * left[num] * right[num]
               for num in left)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    left, right = parse_input(input_text)
    return p1(left, right), p2(left, right)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
