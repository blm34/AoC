import heapq
from collections import defaultdict

import aoc_helper

DAY = 16
YEAR = 2024

dirs = [(-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)]


def parse_input(input_text):
    grid = input_text.splitlines()
    R = len(grid)
    C = len(grid[0])

    start = (R - 2, 1)
    end = (1, C - 2)
    assert grid[start[0]][start[1]] == "S"
    assert grid[end[0]][end[1]] == "E"

    return grid, start, end

def make_graph(grid, start, end):
    graph = defaultdict(dict)
    rgraph = defaultdict(dict)  # Reverse graph

    start_node = (start[0], start[1], 1)
    nodes_stack = [start_node]

    while nodes_stack:
        node = nodes_stack.pop()
        if node in graph:
            continue
        r, c, d = node

        # Try rotating right and left
        for cd in (1, -1):
            dd = (d + cd) % 4
            dr, dc = dirs[dd]
            if grid[r + dr][c + dc] != "#":
                new_node = (r, c, dd)
                graph[node][new_node] = 1000
                rgraph[new_node][node] = 1000
                if new_node not in graph:
                    nodes_stack.append(new_node)

        # Check if we can move forwards
        dr, dc = dirs[d]
        if grid[r + dr][c + dc] == "#":
            continue

        rr = r + dr
        cc = c + dc
        last_d = d
        dist = 1
        while True:
            valid_moves = list()
            backwards_dir = (last_d + 2) % 4
            for di in range(4):
                if backwards_dir == di:
                    continue
                dr, dc = dirs[di]
                if grid[rr + dr][cc + dc] != "#":
                    valid_moves.append((di, dr, dc))
            if len(valid_moves) == 0:
                break
            elif len(valid_moves) == 1:
                di, dr, dc = valid_moves[0]
                rr += dr
                cc += dc
                dist += 1
                if (rr, cc) == end:
                    new_node = (rr, cc, last_d)
                    graph[node][new_node] = dist
                    rgraph[new_node][node] = dist
                    if new_node not in graph:
                        nodes_stack.append(new_node)
                else:
                    dist += 0 if di == last_d else 1000
                    last_d = di
            elif len(valid_moves) > 1:
                new_node = (rr, cc, last_d)
                graph[node][new_node] = dist
                rgraph[new_node][node] = dist
                if new_node not in graph:
                    nodes_stack.append(new_node)
                break
    return graph, rgraph


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    grid, start, end = parse_input(input_text)

    graph, rgraph = make_graph(grid, start, end)

    # Dijkstra
    heap = list()
    dists = dict()
    heapq.heappush(heap, (0, (start[0], start[1], 1)))
    while heap:
        dist, node = heapq.heappop(heap)
        if node in dists:
            continue
        dists[node] = dist
        r, c, d = node
        if (r, c) == end:
            p1 = dist
            end_node = node
            break
        for adjacent in graph[node]:
            new_dist = dist + graph[node][adjacent]
            heapq.heappush(heap, (new_dist, adjacent))

    # Backtrack through graph
    p2 = 0
    nodes = [end_node]
    seen = set()
    while nodes:
        node = nodes.pop()
        if node in seen:
            continue
        seen.add(node)
        p2 += 1
        for adjacent in rgraph[node]:
            if adjacent in dists and dists[adjacent] + graph[adjacent][node] == dists[node]:
                nodes.append(adjacent)
                p2 += graph[adjacent][node] % 1000 - 1

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
