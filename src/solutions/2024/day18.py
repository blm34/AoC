import heapq

import aoc_helper

DAY = 18
YEAR = 2024

R = C = 71

dirs = ((-1, 0),
        (0, 1),
        (1, 0),
        (0, -1))


class DisjointUnionSet:
    def __init__(self, size):
        self.rank = [[0 for c in range(size + 2)] for r in range(size + 2)]
        self.parent = [[0 for c in range(size + 2)] for r in range(size + 2)]
        for r in range(size + 2):
            for c in range(size + 2):
                self.parent[r][c] = (r - 1, c - 1)

    def find(self, cell):
        cr, cc = cell
        if self.parent[cr + 1][cc + 1] != cell:
            self.parent[cr + 1][cc + 1] = self.find(self.parent[cr + 1][cc + 1])
        return self.parent[cr + 1][cc + 1]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        xrr, xrc = x_root
        yrr, yrc = y_root
        if self.rank[xrr + 1][xrc + 1] < self.rank[yrr + 1][yrc + 1]:
            self.parent[xrr + 1][xrc + 1] = y_root
        elif self.rank[yrr + 1][yrc + 1] < self.rank[xrr + 1][xrc + 1]:
            self.parent[yrr + 1][yrc + 1] = x_root
        else:
            self.parent[yrr + 1][yrc + 1] = x_root
            self.rank[xrr + 1][yrr + 1] += 1

    def same_set(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        return x_root == y_root


def parse_input(input_text):
    lines = input_text.split('\n')
    coords = []
    for line in lines:
        coord = tuple(map(int, line.split(",")))
        coords.append(coord)
    return coords


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    coords = parse_input(input_text)
    coords = set(coords[:1024])

    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    while True:
        dist, (r, c) = heapq.heappop(heap)
        if (r, c) in coords:
            continue
        coords.add((r, c))
        if r == R - 1 and c == C - 1:
            return dist
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in coords:
                heapq.heappush(heap, (dist + 1, (rr, cc)))


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    coords = parse_input(input_text)

    fallen = set()
    dus = DisjointUnionSet(R)
    for i in range(R):
        # Add bottom and left edges as one set
        dus.union((i, -1), (i + 1, -1))
        fallen.add((i, -1))
        dus.union((R, i - 1), (R, i))
        fallen.add((R, i-1))
        # Add top right edges as another set
        dus.union((-1, i), (-1, i + 1))
        fallen.add((-1, i))
        dus.union((i - 1, C), (i, C))
        fallen.add((i-1, C))
    fallen.add((R, -1))
    fallen.add((R, C-1))
    fallen.add((-1, C))
    fallen.add((R-1, C))

    for r, c in coords:
        fallen.add((r, c))
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if 0 == dr == dc:
                    continue
                if (r+dr, c+dc) in fallen:
                    dus.union((r, c), (r + dr, c + dc))
        if dus.same_set((R, -1), (-1, C)):
            return f"{r},{c}"


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
