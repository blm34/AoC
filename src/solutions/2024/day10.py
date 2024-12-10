import aoc_helper

DAY = 10
YEAR = 2024


core_directions = [(-1, 0),
                   (0, 1),
                   (1, 0),
                   (0, -1)]
# Encode the ability to move in each of the 4 directions in one bit of a four bit integer
directions = [[] for _ in range(16)]
for i in range(16):
    for d, (r, c) in enumerate(core_directions):
        if (2 ** d) & i:
            directions[i].append((r, c))


def parse_input(input_text):
    lines = input_text.split('\n')
    topography = [list(map(int, line)) for line in lines]
    R = len(topography)
    C = len(topography[0])

    moves = [[0 for c in range(C)] for r in range(R)]
    zeros = []
    for r in range(R):
        for c in range(C):
            if topography[r][c] == 0:
                zeros.append((r, c))
            for i, (dr, dc) in enumerate(core_directions):
                rr = r + dr
                cc = c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if topography[r][c] + 1 == topography[rr][cc]:
                        moves[r][c] |= 2**i
    return zeros, moves


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    zeros, moves = parse_input(input_text)

    total = 0
    for r_zero, c_zero in zeros:
        stack = [(0, r_zero, c_zero)]
        seen = set()
        while stack:
            height, r, c = stack.pop()
            if height == 9:
                total += 1
            for dr, dc in directions[moves[r][c]]:
                if (r + dr, c + dc) not in seen:
                    seen.add((r+dr, c+dc))
                    stack.append((height+1, r+dr, c+dc))

    return total


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    zeros, moves = parse_input(input_text)

    total = 0
    for r_zero, c_zero in zeros:
        stack = [(0, r_zero, c_zero)]
        while stack:
            height, r, c = stack.pop()
            if height == 9:
                total += 1
            for dr, dc in directions[moves[r][c]]:
                stack.append((height+1, r+dr, c+dc))
    return total


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
