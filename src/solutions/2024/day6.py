import aoc_helper

DAY = 6
YEAR = 2024

DIRECTIONS = [(-1, 0),
              (0, 1),
              (1, 0),
              (0, -1)]


def get_start(G):
    for r in range(len(G)):
        if '^' in G[r]:
            guard_r = r
            guard_c = G[r].index('^')
            return guard_r, guard_c


def get_visited(G):
    R = len(G)
    C = len(G[0])

    guard_r, guard_c = get_start(G)

    direction_index = 0

    visited = set()
    while 0 <= guard_r < R and 0 <= guard_c < C:
        visited.add((guard_r, guard_c))

        for _ in range(2):
            dr, dc = DIRECTIONS[direction_index]
            if 0 <= guard_r + dr < R and 0 <= guard_c + dc < C:
                if G[guard_r + dr][guard_c + dc] == '#':
                    direction_index = (direction_index + 1) % 4
                else:
                    break
            else:
                break

        dr, dc = DIRECTIONS[direction_index]
        guard_r += dr
        guard_c += dc

    return visited


def p1(input_text):
    G = input_text.split('\n')

    visited = get_visited(G)
    return len(visited)


def get_jumps(G) -> list[list[list[tuple[int, int]]]]:
    R = len(G)
    C = len(G[0])
    jumps = [[[(None, None) for direction in range(4)] for c in range(C)] for r in range(R)]

    for r in range(R):
        for c in range(C):
            for d in range(4):
                guard_r, guard_c = r, c
                while True:
                    dr, dc = DIRECTIONS[d]
                    if 0 <= guard_r + dr < R and 0 <= guard_c + dc < C:
                        if G[guard_r + dr][guard_c + dc] == '#':
                            jumps[r][c][d] = (guard_r, guard_c)
                            break
                    else:
                        jumps[r][c][d] = (guard_r + dr, guard_c + dc)
                        break

                    guard_r += dr
                    guard_c += dc
    return jumps


def p2(input_text):
    G = input_text.split('\n')
    R = len(G)
    C = len(G[0])

    path = get_visited(G)
    start_r, start_c = get_start(G)

    next_pos = get_jumps(G)

    loops = 0
    for r_obstacle, c_obstacle in path - {(start_r, start_c)}:
        guard_r, guard_c = start_r, start_c
        direction_index = 0

        visited = set()
        first_move = True
        while 0 <= guard_r < R and 0 <= guard_c < C:
            if (guard_r, guard_c, direction_index) in visited:
                loops += 1
                break

            if not first_move:
                visited.add((guard_r, guard_c, direction_index))
                direction_index = (direction_index + 1) % 4
            first_move = False
            next_r, next_c = next_pos[guard_r][guard_c][direction_index]

            if guard_r == next_r:
                if guard_r == r_obstacle and next_c <= c_obstacle < guard_c:
                    guard_c = c_obstacle + 1
                elif guard_r == r_obstacle and guard_c < c_obstacle <= next_c:
                    guard_c = c_obstacle - 1
                else:
                    guard_c = next_c

            elif guard_c == next_c:
                if guard_c == c_obstacle and next_r <= r_obstacle < guard_r:
                    guard_r = r_obstacle + 1
                elif guard_c == c_obstacle and guard_r < r_obstacle <= next_r:
                    guard_r = r_obstacle - 1
                else:
                    guard_r = next_r
    return loops


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
