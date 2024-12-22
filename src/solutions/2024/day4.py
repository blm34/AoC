import aoc_helper

DAY = 4
YEAR = 2024


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


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
