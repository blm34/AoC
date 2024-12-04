import aoc_helper

DAY = 4
YEAR = 2024


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])

    count = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] != 'X':
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    rr, cc = r, c
                    found = True
                    for letter in 'MAS':
                        rr += dr
                        cc += dc
                        if not (0 <= rr < R and 0 <= cc < C) or \
                                G[rr][cc] != letter:
                            found = False
                            break
                    count += found
    return count


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])

    count = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if G[r][c] != 'A':
                continue
            corners = [G[r+dr][c+dc] for dr in (-1, 1) for dc in (-1, 1)]
            if 2 == corners.count('M') == corners.count('S') and corners[0] != corners[3]:
                count += 1
    return count


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
