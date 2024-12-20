import aoc_helper

DAY = 20
YEAR = 2024

dirs = ((-1, 0),
        (0, 1),
        (1, 0),
        (0, -1))

dirs2 = ((-2, 0),
         (-1, 1),
         (0, 2),
         (1, 1),
         (2, 0),
         (1, -1),
         (0, -2),
         (-1, -1))


def parse_input(input_text):
    grid = input_text.split('\n')
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)
    return grid, start, end


def get_path(grid, start, end):
    path = {start: 0}
    prev = start
    prev_prev = None
    dist = 0
    while prev != end:
        dist += 1
        r, c = prev
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if grid[rr][cc] != "#" and (rr, cc) != prev_prev:
                path[(rr, cc)] = dist
                prev_prev = prev
                prev = (rr, cc)
                break
    return path


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    grid, start, end = parse_input(input_text)
    path = get_path(grid, start, end)

    count = 0
    for (r, c), dist in path.items():
        for dr, dc in dirs2:
            rr = r + dr
            cc = c + dc
            if (rr, cc) in path:
                new_dist = path[(rr, cc)]
                if new_dist - dist - 2 >= 100:
                    count += 1
    return count



@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    grid, start, end = parse_input(input_text)
    path = get_path(grid, start, end)

    count = 0
    for pos1 in path:
        r1, c1 = pos1
        for dr in range(-20, 21):
            for dc in range(-20, 21):
                dist = abs(dr) + abs(dc)
                if dist > 20:
                    continue
                r2 = r1 + dr
                c2 = c1 + dc
                if (r2, c2) in path and path[(r2, c2)] - path[pos1] - dist >= 100:
                    count += 1
    return count


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
