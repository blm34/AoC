import aoc_helper

DAY = 15
YEAR = 2024

dirs = {"^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0),
        "<": (0, -1)}


def parse_input(input_text, part_2):
    grid, moves = input_text.split("\n\n")
    moves = moves.replace("\n", "")
    if part_2:
        grid = grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    grid = [list(line) for line in grid.split("\n")]
    robot = None
    for r in range(len(grid)):
        if robot is not None:
            break
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                robot = (r, c)
                grid[r][c] = "."
                break
    return grid, moves, robot


def make_move(grid, move, robot):
    rob_r, rob_c = robot
    dr, dc = dirs[move]
    rr = rob_r + dr
    cc = rob_c + dc
    while grid[rr][cc] == "O":
        rr += dr
        cc += dc
    if grid[rr][cc] == "#":
        return grid, robot
    elif grid[rr][cc] == ".":
        grid[rr][cc] = 'O'
        grid[rob_r+dr][rob_c+dc] = "."
        return grid, (rob_r + dr, rob_c + dc)

# 2028


def make_move_p2(grid, move, robot):
    rob_r, rob_c = robot
    dr, dc = dirs[move]
    rr = rob_r + dr
    cc = rob_c + dc
    if grid[rr][cc] == "#":
        return grid, robot
    elif grid[rr][cc] == ".":
        grid[rr][cc] = "@"
        grid[rob_r][rob_c] = "."
        return grid, (rob_r + dr, rob_c + dc)
    else:
        if dr == 0:  # Horizontal move with box
            while True:
                if grid[rr][cc] == "#":
                    return grid, robot
                elif grid[rr][cc] == "[" or grid[rr][cc] == "]":
                    rr += dr
                    cc += dc
                elif grid[rr][cc] == ".":
                    r = rr
                    c = cc
                    while not (r == rob_r and c == rob_c):
                        grid[r][c] = grid[r - dr][c - dc]
                        r -= dr
                        c -= dc
                    grid[rob_r][rob_c] = '.'
                    return grid, (rob_r + dr, rob_c + dc)
        else:  # Vertical move with box
            # Calculate what needs to move
            to_move = set()
            stack = [(rob_r, rob_c)]
            while stack:
                r, c = stack.pop()
                if grid[r][c] == "#":
                    return grid, robot
                elif grid[r][c] == ".":
                    continue
                to_move.add((r, c))
                stack.append((r + dr, c))
                if grid[r+dr][c] == "[":
                    stack.append((r + dr, c + 1))
                elif grid[r+dr][c] == "]":
                    stack.append((r + dr, c - 1))
                elif grid[r+dr][c] == "#":
                    return grid, robot
            # Make the moves
            to_move = sorted(to_move, reverse=dr==1)
            for r, c in to_move:
                grid[r][c], grid[r+dr][c] = grid[r+dr][c], grid[r][c]
            return grid, (rob_r+dr, rob_c)


def gps_score(grid):
    return sum(100 * r + c
               for r in range(len(grid))
               for c in range(len(grid[0]))
               if grid[r][c] == "O" or grid[r][c] == "[")


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    grid, moves, robot = parse_input(input_text, part_2=False)
    for move in moves:
        grid, robot = make_move(grid, move, robot)
    return gps_score(grid)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    grid, moves, robot = parse_input(input_text, part_2=True)
    for move in moves:
        grid, robot = make_move_p2(grid, move, robot)
    return gps_score(grid)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
