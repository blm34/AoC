import aoc_helper

DAY = 18
YEAR = 2015


def parse_input(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])

    for r in range(R):
        for c in range(C):
            G[r][c] = 1 if G[r][c] == "#" else 0
    return G


def step(grid, part2=False):
    R = len(grid)
    C = len(grid[0])
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


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    grid = parse_input(input_text)
    for _ in range(100):
        grid = step(grid)
    return count_alive(grid)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    grid = parse_input(input_text)
    for _ in range(100):
        grid = step(grid, True)
    return count_alive(grid)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
