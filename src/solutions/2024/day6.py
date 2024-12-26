import aoc_helper

DAY = 6
YEAR = 2024

DIRECTIONS = [(-1, 0),
              (0, 1),
              (1, 0),
              (0, -1)]


def get_start(grid):
    for r in range(len(grid)):
        if '^' in grid[r]:
            return r, grid[r].index("^")


def original_path(grid):
    height = len(grid)
    width = len(grid[0])

    r, c = get_start(grid)
    d = 0
    dr, dc = DIRECTIONS[d]

    yield r, c, d

    while 0 <= r + dr < height and 0 <= c + dc < width:
        if  grid[r+dr][c+dc] == "#":
            d = (d+1) % 4
            dr, dc = DIRECTIONS[d]
        else:
            r += dr
            c += dc
            yield r, c, d


def get_jumps(grid) -> list[list[list[tuple[int, int, int]]]]:
    height = len(grid)
    width = len(grid[0])
    jumps = [[[None for direction in range(4)] for c in range(width)] for r in range(height)]

    # Find index for each obstacle in each row and col
    rows = [[] for _ in range(height)]
    cols = [[] for _ in range(width)]

    for r in range(height):
        for c in range(width):
            if grid[r][c] == "#":
                rows[r].append(c)
                cols[c].append(r)

    # Calculate jumps in each row
    for r in range(height):
        for obs1, obs2 in zip([-2] + rows[r], rows[r] + [width + 1]):
            for c in range(max(0, obs1 + 1), min(width, obs2)):
                jumps[r][c][1] = (r, obs2 - 1, 2)
                jumps[r][c][3] = (r, obs1 + 1, 0)

    # Calculate jumps in each col
    for c in range(width):
        for obs1, obs2 in zip([-2] + cols[c], cols[c] + [height + 1]):
            for r in range(max(0, obs1 + 1), min(height, obs2)):
                jumps[r][c][0] = (obs1 + 1, c, 1)
                jumps[r][c][2] = (obs2 - 1, c, 3)

    return jumps


def loop_finder(jumps, guard_r, guard_c, guard_d, obs_r, obs_c, height, width):
    visited = set()

    while 0 <= guard_r < height and 0 <= guard_c < width:
        if guard_d == 0:
            if (guard_r, guard_c) in visited:
                return 1
            visited.add((guard_r, guard_c))

        next_r, next_c, guard_d = jumps[guard_r][guard_c][guard_d]

        if obs_r == guard_r == next_r:
            if next_c <= obs_c < guard_c:
                guard_c = obs_c + 1
            elif guard_c < obs_c <= next_c:
                guard_c = obs_c - 1
            else:
                guard_r = next_r
                guard_c = next_c

        elif obs_c == guard_c == next_c:
            if next_r <= obs_r < guard_r:
                guard_r = obs_r + 1
            elif guard_r < obs_r <= next_r:
                guard_r = obs_r - 1
            else:
                guard_r = next_r
                guard_c = next_c

        else:
            guard_r = next_r
            guard_c = next_c

    return 0


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    grid = input_text.splitlines()
    height = len(grid)
    width = len(grid[0])

    jumps = get_jumps(grid)

    original_path_generator = original_path(grid)
    prev_r, prev_c, prev_d = next(original_path_generator)

    p1_path = {(prev_r, prev_c)}
    loops = 0

    for guard_r, guard_c, guard_d in original_path_generator:
        if (guard_r, guard_c) not in p1_path:
            p1_path.add((guard_r, guard_c))
            loops += loop_finder(jumps, prev_r, prev_c, prev_d, guard_r, guard_c, height, width)
        prev_r, prev_c, prev_d = guard_r, guard_c, guard_d

    return len(p1_path), loops


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
