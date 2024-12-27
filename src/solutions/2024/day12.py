import aoc_helper

DAY = 12
YEAR = 2024

directions = ((-1, 0),
              (0, 1),
              (1, 0),
              (0, -1))

corners = ((-1, 1),
           (1, 1),
           (1, -1),
           (-1, -1))


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    grid = input_text.splitlines()
    R = len(grid)
    C = len(grid[0])

    p1 = 0
    p2 = 0

    seen = [[False for _ in range(C)] for _ in range(R)]

    for sr in range(R):
        for sc in range(C):
            if seen[sr][sc]:
                continue
            letter = grid[sr][sc]

            area = 0
            perimeter = 0
            double_sides = 0

            stack = [(sr, sc)]
            seen[sr][sc] = True
            while stack:
                r, c = stack.pop()
                area += 1
                # Look for adjacent similar letters
                for dr, dc in directions:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == letter:
                        if not seen[rr][cc]:
                            stack.append((rr, cc))
                            seen[rr][cc] = True
                    else:
                        perimeter += 1

                # Calculate the of current cell on sides
                for dr, dc in corners:
                    rr = r + dr
                    cc = c + dc
                    edges = grid[rr][c] == letter if 0 <= rr < R else 0
                    edges += grid[r][cc] == letter if 0 <= cc < C else 0
                    if edges == 0:
                        double_sides += 2
                    elif edges == 1:
                        corner = grid[rr][cc] == letter if 0 <= rr < R and 0 <= cc < C else 0
                        if corner == 1:
                            double_sides += 1

            p1 += area * perimeter
            p2 += area * (double_sides // 2)

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
