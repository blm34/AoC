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
    topography = [[int(num) for num in line] for line in input_text.splitlines()]
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
                if 0 <= rr < R and 0 <= cc < C and \
                        topography[r][c] + 1 == topography[rr][cc]:
                    moves[r][c] += 2**i
    return zeros, moves


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    zeros, moves = parse_input(input_text)

    p1 = 0
    p2 = 0

    for r_zero, c_zero in zeros:
        stack = [(0, r_zero, c_zero)]
        ends_seen = set()
        while stack:
            height, r, c = stack.pop()
            if height == 9:
                p2 += 1
                if (r, c) not in ends_seen:
                    p1 += 1
                    ends_seen.add((r, c))
            for dr, dc in directions[moves[r][c]]:
                stack.append((height+1, r+dr, c+dc))

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
