import re
from collections import defaultdict

import aoc_helper

DAY = 10
YEAR = 2016


def parse_input(input_text):
    L = input_text.split('\n')
    locs = defaultdict(list)
    instructions = dict()
    for line in L:
        if line.startswith('value'):
            match = re.search(r"^value (\d+) goes to (bot \d+)$", line)
            loc = match.group(2)
            val = int(match.group(1))
            locs[loc].append(val)
        elif line.startswith('bot'):
            match = re.search(r"^(bot \d+) gives low to ((bot|output) \d+) and high to ((bot|output) \d+)$", line)
            frm = match.group(1)
            low_to = match.group(2)
            high_to = match.group(4)
            instructions[frm] = (low_to, high_to)
    return locs, instructions


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    locs, instructions = parse_input(input_text)
    while True:
        for loc in locs:
            if len(locs[loc]) == 2:
                if locs[loc][0] > locs[loc][1]:
                    locs[loc].reverse()
                if locs[loc] == [17, 61]:
                    return int(loc.split()[1])
                locs[instructions[loc][0]].append(locs[loc][0])
                locs[instructions[loc][1]].append(locs[loc][1])
                locs[loc] = []
                break


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    locs, instructions = parse_input(input_text)
    complete = False
    while not complete:
        complete = True
        for loc in locs:
            if len(locs[loc]) == 2:
                complete = False
                if locs[loc][0] > locs[loc][1]:
                    locs[loc].reverse()
                locs[instructions[loc][0]].append(locs[loc][0])
                locs[instructions[loc][1]].append(locs[loc][1])
                locs[loc] = []
                break
    return aoc_helper.prod(locs[f'output {i}'][0] for i in range(3))


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
