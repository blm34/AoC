import aoc_helper

DAY = 4
YEAR = 2024


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    grid = input_text.split("\n")
    R = len(grid)
    C = len(grid[0])

    p1 = 0
    # Check horizontal
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'X':
                for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    rr, cc = r, c
                    found = True
                    for letter in 'MAS':
                        rr += dr
                        cc += dc
                        if not (0 <= rr < R and 0 <= cc < C) or grid[rr][cc] != letter:
                            found = False
                            break
                    p1 += found

    # Part 2
    p2 = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if grid[r][c] == 'A':
                if abs(ord(grid[r-1][c-1]) - ord(grid[r+1][c+1])) == 6 and \
                        abs(ord(grid[r-1][c+1]) - ord(grid[r+1][c-1])) == 6:
                    p2 += 1

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
