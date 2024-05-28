import time

import aoc_helper

START_TIME = time.time()
DAY = 0

p1 = 0
p2 = 0

input_text = aoc_helper.read_input(day=DAY, year=2015)
L = input_text.split('\n')
G = [list(line) for line in L]
R = len(G)
C = len(G[0])



END_TIME = time.time()
aoc_helper.print_results(p1, p2, END_TIME-START_TIME)
