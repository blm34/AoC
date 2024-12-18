import heapq

import aoc_helper

DAY = 18
YEAR = 2024

R = C = 71

dirs = ((-1, 0),
        (0, 1),
        (1, 0),
        (0, -1))


def parse_input(input_text):
    lines = input_text.split('\n')
    coords = []
    for line in lines:
        coord = tuple(map(int, line.split(",")))
        coords.append(coord)
    return coords


def make_graph(coords):
    coords = set(coords)
    graph = dict()
    for r in range(R):
        for c in range(C):
            if not (r, c) in coords:
                if (r, c) not in graph:
                    graph[(r, c)] = set()
                for dr, dc in dirs:
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in coords:
                        if (rr, cc) not in graph:
                            graph[(rr, cc)] = set()
                        graph[(r, c)].add((rr, cc))
                        graph[(rr, cc)].add((r, c))
    return graph


def connected(graph):
    seen = set()
    stack = [(0, 0)]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        for adj in graph[node]:
            if adj == (R-1, C-1):
                return True
            if adj not in seen:
                stack.append(adj)
    return False


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
        if r == R-1 and c == C-1:
            return dist
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in coords:
                heapq.heappush(heap, (dist+1, (rr, cc)))


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    coords = parse_input(input_text)

    min_index = 1025
    max_index = len(coords)
    while max_index != min_index:
        index = (max_index + min_index) // 2
        graph = make_graph(coords[:index+1])
        if connected(graph):
            min_index = index + 1
        else:
            max_index = index
    coord = coords[min_index]
    return f"{coord[0]},{coord[1]}"


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
