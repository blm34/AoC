from collections import defaultdict

import aoc_helper

DAY = 3
YEAR = 2017


def parse_input(input_text):
    return int(input_text)


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    target = parse_input(input_text)

    root = 1
    while root * root <= target:
        root += 2
    root -= 2

    x, y = root // 2, -(root // 2)

    num = root * root
    if num == target:
        return abs(x) + abs(y)

    num += 1
    x += 1
    if num == target:
        return abs(x) + abs(y)

    if num + root >= target:
        y += target - num
        return abs(x) + abs(y)
    num += root
    y += root

    if num + root + 1 >= target:
        x -= target - num
        return abs(x) + abs(y)
    num += root + 1
    x -= root + 1

    if num + root + 1 >= target:
        y -= target - num
        return abs(x) + abs(y)
    num += root + 1
    y -= root + 1

    assert num + root >= target
    x += target - num
    return abs(x) + abs(y)


def calc_value(x, y, values):
    val = 0
    assert values[(x, y)] == 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            val += values[(x+dx, y+dy)]
    return val


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    target = parse_input(input_text)

    values = defaultdict(int)
    values[(0, 0)] = 1

    x, y = 0, 0
    direction = 1
    length = 1

    while True:
        for _ in range(length):
            x += direction
            values[(x, y)] = calc_value(x, y, values)
            if values[(x, y)] >= target:
                return values[(x, y)]

        for _ in range(length):
            y += direction
            values[(x, y)] = calc_value(x, y, values)
            if values[(x, y)] >= target:
                return values[(x, y)]

        direction *= -1
        length += 1


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
