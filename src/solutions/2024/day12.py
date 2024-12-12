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


def parse_input(input_text):
    L = input_text.split('\n')
    G = [list(line) for line in L]
    R = len(G)
    C = len(G[0])
    return None


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    G = input_text.split('\n')
    R = len(G)
    C = len(G[0])

    seen = [[False for _ in range(C)] for _ in range(R)]
    cost = 0

    for sr in range(R):
        for sc in range(C):
            if seen[sr][sc]:
                continue
            area = 0
            perimeter = 0
            stack = [(sr, sc)]
            seen[sr][sc] = True
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in directions:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[sr][sc]:
                        if not seen[rr][cc]:
                            stack.append((rr, cc))
                            seen[rr][cc] = True
                    else:
                        perimeter += 1
            cost += area * perimeter
    return cost


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    G = input_text.split('\n')
    R = len(G)
    C = len(G[0])

    seen = [[False for _ in range(C)] for _ in range(R)]
    cost = 0

    for sr in range(R):
        for sc in range(C):
            if seen[sr][sc]:
                continue
            letter = G[sr][sc]
            area = 0
            double_sides = 0
            stack = [(sr, sc)]
            seen[sr][sc] = True
            while stack:
                r, c = stack.pop()

                # Look for adjacent similar letters
                for dr, dc in directions:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == letter and not seen[rr][cc]:
                        stack.append((rr, cc))
                        seen[rr][cc] = True

                # Calculate effect of area and sides of current cell
                area += 1
                for dr, dc in corners:
                    rr = r + dr
                    cc = c + dc
                    corner = G[rr][cc] == letter if 0 <= rr < R and 0 <= cc < C else 0
                    edges = G[rr][c] == letter if 0 <= rr < R and 0 <= c < C else 0
                    edges += G[r][cc] == letter if 0 <= r < R and 0 <= cc < C else 0
                    if edges == 2:
                        pass
                    elif edges == 0:
                        double_sides += 2
                    elif edges == corner == 1:
                        double_sides += 1
            cost += area * (double_sides//2)
    return cost


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
