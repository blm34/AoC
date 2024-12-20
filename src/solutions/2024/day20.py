import multiprocessing

import aoc_helper

DAY = 20
YEAR = 2024

dirs = ((-1, 0),
        (0, 1),
        (1, 0),
        (0, -1))

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


def get_path_list(grid, start, end) -> list[tuple[int, int]]:
    path = [None, start]
    while path[-1] != end:
        r, c = path[-1]
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if grid[rr][cc] != "#" and (rr, cc) != path[-2]:
                path.append((rr, cc))
                break
    return tuple(path[1:])


def get_path_dict(grid, start, end) -> dict[tuple[int, int], int]:
    prev_prev = None
    prev = start
    dist = 0
    path = {start: dist}
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


def get_cheat_count(path, max_cheat_len):
    count = 0
    for i1 in range(len(path) - 102):
        i2 = i1 + 102
        r1, c1 = path[i1]
        while i2 < len(path):
            r2, c2 = path[i2]
            dr = abs(r1 - r2)
            dc = abs(c2 - c1)
            if dr + dc <= max_cheat_len:
                saving = i2 - i1 - dr - dc
                if saving >= 100:
                    count += 1
                    i2 += 1
                else:
                    i2 += (100 - saving) // 2
            else:
                i2 += dr + dc - max_cheat_len
    return count


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    grid, start, end = parse_input(input_text)
    path = get_path_dict(grid, start, end)

    count = 0
    for (r, c), dist in path.items():
        for dr, dc in dirs:
            rr = r + dr*2
            cc = c + dc*2
            if (rr, cc) in path:
                new_dist = path[(rr, cc)]
                if new_dist - dist - 2 >= 100:
                    count += 1
    return count



@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    grid, start, end = parse_input(input_text)
    path = get_path_list(grid, start, end)
    return get_cheat_count(path, 20)

if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
