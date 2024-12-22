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


def get_path(grid, start, end):
    path_list = [start]
    path_dict = {start: 0}
    r, c = start

    # Find start direction
    for d, (dr, dc) in enumerate(dirs):
        if grid[r + dr][c + dc] != "#":
            r += dr
            c += dc
            path_list.append((r, c))
            path_dict[(r, c)] = 1
            break

    # Find the rest of the path favouring forwards motion
    dist = 2
    while (r, c) != end:
        dr, dc = dirs[d]
        if grid[r + dr][c + dc] != "#":
            r += dr
            c += dc
        else:
            dr, dc = dirs[(d + 1) % 4]
            if grid[r + dr][c + dc] != "#":
                r += dr
                c += dc
                d = (d + 1) % 4
            else:
                dr, dc = dirs[(d - 1) % 4]
                if grid[r + dr][c + dc] != "#":
                    r += dr
                    c += dc
                    d = (d - 1) % 4
                else:
                    assert False
        path_list.append((r, c))
        path_dict[(r, c)] = dist

        dist += 1
    return path_list, path_dict


def get_shortcuts_from_square(path_list, index, max_dist, min_saving):
    shortcuts = set()
    r1, c1 = path_list[index]
    i2 = index + min_saving + 2
    while i2 < len(path_list):
        r2, c2 = path_list[i2]
        dist = abs(r1 - r2) + abs(c1 - c2)
        saving = i2 - index - dist
        if dist <= max_dist and saving >= min_saving:
            steps = max_dist - dist
            for k in range(min(steps+1, len(path_list) - i2)):
                shortcuts.add(path_list[i2 + k])
            i2 += steps + 1
        elif dist <= max_dist:
            i2 += (min_saving + 1 - saving) // 2
        else:
            i2 += dist - max_dist
    return shortcuts


def get_cheat_count(path_list, path_dict, max_cheat_len, min_saving):
    # Find cheats from start square
    cheats = get_shortcuts_from_square(path_list, 0, max_cheat_len, min_saving)
    count = len(cheats)

    # Loop through the rest of the path that could be the start of a cheat
    for t1 in range(1, len(path_list) - min_saving - 2):
        r0, c0 = path_list[t1 - 1]
        r1, c1 = path_list[t1]
        dr1 = r1 - r0
        dc1 = c1 - c0

        for i in range(-max_cheat_len, max_cheat_len+1):
            dri = dr1 * (max_cheat_len - abs(i)) + dc1*i
            dci = dc1 * (max_cheat_len - abs(i)) + dr1*i
            cheats.discard((r0 - dri, c0 - dci))
            r2 = r1 + dri
            c2 = c1 + dci
            if (r2, c2) in path_dict:
                t2 = path_dict[(r2, c2)]
                dist = abs(r2 - r1) + abs(c2 - c1)
                if t2 - t1 - dist >= min_saving:
                    cheats.add((r2, c2))

        for t2 in range(t1+min_saving+1, min(len(path_list), t1+min_saving+max_cheat_len)):
            r2, c2 = path_list[t2]
            if t2 - t1 - abs(r2 - r1) - abs(c2 - c1) < min_saving:
                cheats.discard((r2, c2))

        count += len(cheats)
    return count


def p1(input_text):
    grid, start, end = parse_input(input_text)
    _, path = get_path(grid, start, end)

    count = 0
    for (r, c), dist in path.items():
        for dr, dc in dirs:
            rr = r + dr * 2
            cc = c + dc * 2
            if (rr, cc) in path and path[(rr, cc)] - dist - 2 >= 100:
                count += 1
    return count


def p2(input_text):
    grid, start, end = parse_input(input_text)
    path_list, path_dict = get_path(grid, start, end)
    return get_cheat_count(path_list, path_dict, 20, 100)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
