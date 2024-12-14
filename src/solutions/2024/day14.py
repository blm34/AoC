import re
from statistics import pvariance as variance

import aoc_helper

DAY = 14
YEAR = 2024

R = 103
C = 101


def parse_input(input_text):
    pattern = r"^p=(\d+),(\d+) v=(-?\d+),(-?\d+)$"
    robots = re.findall(pattern, input_text, flags=re.MULTILINE)
    robots = [list(map(int, robot)) for robot in robots]
    return robots


def step(robots, steps=1):
    for i, (x, y, vx, vy) in enumerate(robots):
        robots[i][0] = (x + vx * steps) % C
        robots[i][1] = (y + vy * steps) % R
    return robots


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    robots = parse_input(input_text)

    robots = step(robots, steps=100)

    quads = [0, 0, 0, 0]
    for x, y, _, _ in robots:
        if x == C // 2 or y == R // 2:
            continue
        quad_x = int(x > C // 2)
        quad_y = int(y > R // 2)
        quads[quad_x + 2 * quad_y] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    robots = parse_input(input_text)
    x_vars = []
    y_vars = []
    for time in range(max(R, C)):
        x_vars.append(variance(robot[0] for robot in robots))
        y_vars.append(variance(robot[1] for robot in robots))
        robots = step(robots)
    x_offset = x_vars.index(min(x_vars))
    y_offset = y_vars.index(min(y_vars))

    time = x_offset * R * ((R ** (C - 2)) % C) + y_offset * C * ((C ** (R - 2)) % R)  # By Chinese remainder theorem
    time = time % (R*C)

    return time


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
