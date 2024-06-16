import re
import heapq

import aoc_helper

DAY = None
YEAR = None


def parse_input(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])
    return None


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])
    x = parse_input(input_text)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])
    x = parse_input(input_text)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
