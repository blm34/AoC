import re

import aoc_helper

DAY = 13
YEAR = 2024


def parse_input(input_text):
    turns_text = input_text.split('\n\n')
    turns = []
    move_pattern = r"^Button (A|B): X\+(\d+), Y\+(\d+)$"
    target_pattern = r"^Prize: X=(\d+), Y=(\d+)$"
    for turn_test in turns_text:
        turn = []
        lines = turn_test.split("\n")
        match = re.match(move_pattern, lines[0])
        turn.append(tuple(map(int, match.groups()[1:])))
        match = re.match(move_pattern, lines[1])
        turn.append(tuple(map(int, match.groups()[1:])))
        match = re.match(target_pattern, lines[2])
        turn.append(tuple(map(int, match.groups())))
        turns.append(turn)
    return turns


def min_tokens(da, db, target):
    det = da[0]*db[1] - db[0]*da[1]
    a_num = target[0]*db[1] - target[1]*db[0]
    b_num = target[1]*da[0] - target[0]*da[1]
    if 0 == a_num%det == b_num%det:
        return a_num//det, b_num//det
    else:
        return 0, 0


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    turns = parse_input(input_text)
    tokens = 0
    for turn in turns:
        a, b = min_tokens(*turn)
        tokens += 3*a + b
    return tokens


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    turns = parse_input(input_text)
    tokens = 0
    for turn in turns:
        turn[2] = (turn[2][0]+10_000_000_000_000, turn[2][1]+10_000_000_000_000)
        a, b = min_tokens(*turn)
        tokens += 3*a + b
    return tokens


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
