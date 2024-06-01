import aoc_helper
import sys

p1 = 0
p2 = 0

text = aoc_helper.read_input(sys.argv[1])
L = text.split('\n')
G = [list(line) for line in L]
R = len(G)
C = len(G[0])

lights1 = [[False for c in range(1000)] for r in range(1000)]
lights2 = [[0 for c in range(1000)] for r in range(1000)]

for line in L:
    if line.startswith('turn off'):
        ran = line[9:]
        start, end = ran.split(' through ')
        start = [int(num) for num in start.split(',')]
        end = [int(num) for num in end.split(',')]
        for r in range(start[0], end[0]+1):
            for c in range(start[1], end[1]+1):
                lights1[r][c] = False
                lights2[r][c] = max(lights2[r][c]-1, 0)
    elif line.startswith('turn on'):
        ran = line[8:]
        start, end = ran.split(' through ')
        start = [int(num) for num in start.split(',')]
        end = [int(num) for num in end.split(',')]
        for r in range(start[0], end[0]+1):
            for c in range(start[1], end[1]+1):
                lights1[r][c] = True
                lights2[r][c] += 1
    elif line.startswith('toggle'):
        ran = line[7:]
        start, end = ran.split(' through ')
        start = [int(num) for num in start.split(',')]
        end = [int(num) for num in end.split(',')]
        for r in range(start[0], end[0]+1):
            for c in range(start[1], end[1]+1):
                lights1[r][c] = not lights1[r][c]
                lights2[r][c] += 2

p1 = sum(sum(val for val in row) for row in lights1)
p2 = sum(sum(val for val in row) for row in lights2)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 400410
assert p2 == 15343601
