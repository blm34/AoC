import time
import Modules
from copy import deepcopy

START_TIME = time.time()

text = Modules.read_input("18.txt")
L = text.split('\n')
G = [list(line) for line in L]
R = len(G)
C = len(G[0])

for r in range(R):
    for c in range(C):
        G[r][c] = 1 if G[r][c] == "#" else 0


def step(grid, part2=False):
    next_grid = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            neighbours = sum(grid[r + dr][c + dc]
                             for dc in (-1, 0, 1)
                             for dr in (-1, 0, 1)
                             if (0 <= r + dr < R and 0 <= c + dc < C) and not (dr == dc == 0))
            if grid[r][c] and neighbours in (2, 3):
                next_grid[r][c] = 1
            elif not grid[r][c] and neighbours == 3:
                next_grid[r][c] = 1

    if part2:
        for r in (0, R - 1):
            for c in (0, C - 1):
                next_grid[r][c] = 1

    return next_grid


def count_alive(grid):
    return sum(sum(row) for row in grid)


grid1 = deepcopy(G)
grid2 = deepcopy(G)

for _ in range(100):
    grid1 = step(grid1)
    grid2 = step(grid2, True)

p1 = count_alive(grid1)
p2 = count_alive(grid2)

END_TIME = time.time()
RUN_TIME = END_TIME - START_TIME

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {1000 * RUN_TIME:.3f} ms')
