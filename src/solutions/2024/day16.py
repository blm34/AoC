import heapq

import aoc_helper

DAY = 16
YEAR = 2024

dirs = [(-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)]


def parse_input(input_text):
    grid = input_text.split('\n')
    R = len(grid)
    C = len(grid[0])

    start = (R - 2, 1)
    end = (1, C - 2)
    assert grid[start[0]][start[1]] == "S"
    assert grid[end[0]][end[1]] == "E"

    return grid, start, end


def p1(input_text):
    grid, start, end = parse_input(input_text)

    graph = dict()
    nodes_stack = list()

    start_node = (start[0], start[1], 1)
    nodes_stack.append(start_node)
    graph[start_node] = dict()

    while nodes_stack:
        node = nodes_stack.pop()
        r, c, d = node

        # Try rotating right
        dd = (d + 1) % 4
        dr, dc = dirs[dd]
        if grid[r + dr][c + dc] != "#":
            new_node = (r, c, dd)
            graph[node][new_node] = 1000
            if new_node not in graph:
                nodes_stack.append(new_node)
                graph[new_node] = dict()

        # Try rotating left
        dd = (d - 1) % 4
        dr, dc = dirs[dd]
        if grid[r + dr][c + dc] != "#":
            new_node = (r, c, dd)
            graph[node][new_node] = 1000
            if new_node not in graph:
                nodes_stack.append(new_node)
                graph[new_node] = dict()

        # Check if we can move forwards
        dr, dc = dirs[d]
        if grid[r + dr][c + dc] != "#":
            rr = r + dr
            cc = c + dc
            last_d = d
            dist = 1
            seen = {(r, c), (rr, cc)}
            while True:
                valid_moves = list()
                for di, (dr, dc) in enumerate(dirs):
                    if grid[rr + dr][cc + dc] != "#" and (rr + dr, cc + dc) not in seen:
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
                        if new_node not in graph:
                            nodes_stack.append(new_node)
                            graph[new_node] = dict()
                    else:
                        seen.add((rr, cc))
                        dist += 0 if di == last_d else 1000
                        last_d = di
                elif len(valid_moves) > 1:
                    new_node = (rr, cc, last_d)
                    graph[node][new_node] = dist
                    if new_node not in graph:
                        nodes_stack.append(new_node)
                        graph[new_node] = dict()
                    break

    heap = list()
    seen = set()
    heapq.heappush(heap, (0, (start[0], start[1], 1)))
    while heap:
        dist, node = heapq.heappop(heap)
        if node in seen:
            continue
        seen.add(node)
        r, c, d = node
        if (r, c) == end:
            return dist
        for adjacent in graph[node]:
            new_dist = dist + graph[node][adjacent]
            heapq.heappush(heap, (new_dist, adjacent))


def p2(input_text):
    grid, start, end = parse_input(input_text)

    graph = dict()
    paths = dict()
    nodes_stack = list()

    start_node = (start[0], start[1], 1)
    nodes_stack.append(start_node)
    graph[start_node] = dict()
    paths[start_node] = dict()

    while nodes_stack:
        node = nodes_stack.pop()
        r, c, d = node

        # Try rotating right
        dd = (d + 1) % 4
        dr, dc = dirs[dd]
        if grid[r + dr][c + dc] != "#":
            new_node = (r, c, dd)
            graph[node][new_node] = 1000
            if new_node not in graph:
                nodes_stack.append(new_node)
                graph[new_node] = dict()
                paths[new_node] = dict()

        # Try rotating left
        dd = (d - 1) % 4
        dr, dc = dirs[dd]
        if grid[r + dr][c + dc] != "#":
            new_node = (r, c, dd)
            graph[node][new_node] = 1000
            if new_node not in graph:
                nodes_stack.append(new_node)
                graph[new_node] = dict()
                paths[new_node] = dict()

        # Check if we can move forwards
        dr, dc = dirs[d]
        if grid[r + dr][c + dc] != "#":
            rr = r + dr
            cc = c + dc
            last_d = d
            dist = 1
            dists = {(r, c), (rr, cc)}
            while True:
                valid_moves = list()
                for di, (dr, dc) in enumerate(dirs):
                    if grid[rr + dr][cc + dc] != "#" and (rr + dr, cc + dc) not in dists:
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
                        paths[node][new_node] = dists | {end}
                        if new_node not in graph:
                            nodes_stack.append(new_node)
                            graph[new_node] = dict()
                            paths[new_node] = dict()
                    else:
                        dists.add((rr, cc))
                        dist += 0 if di == last_d else 1000
                        last_d = di
                elif len(valid_moves) > 1:
                    new_node = (rr, cc, last_d)
                    graph[node][new_node] = dist
                    paths[node][new_node] = dists
                    if new_node not in graph:
                        nodes_stack.append(new_node)
                        graph[new_node] = dict()
                        paths[new_node] = dict()
                    break

    end_dist = 0
    heap = list()
    dists = dict()
    prevs = dict()
    heapq.heappush(heap, (0, (start[0], start[1], 1), None))
    while len(dists) < len(graph):
        dist, node, prev_node = heapq.heappop(heap)
        if node in dists:
            if dist == dists[node]:
                prevs[node].append(prev_node)
            continue
        else:
            prevs[node] = [prev_node]
            dists[node] = dist
        r, c, d = node
        if (r, c) == end and end_dist == 0:
            end_dist = dist
        for adjacent in graph[node]:
            new_dist = dist + graph[node][adjacent]
            heapq.heappush(heap, (new_dist, adjacent, node))

    stack = [(end[0], end[1], d)
             for d in range(4)
             if dists.get((end[0], end[1], d), None) == end_dist]

    reverse_graph = dict()
    for prev_node in graph:
        for node in graph[prev_node]:
            if node not in reverse_graph:
                reverse_graph[node] = list()
            reverse_graph[node].append(prev_node)

    path = set()
    seen = set()
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        for prev_node in reverse_graph[node]:
            if dists[node] == dists[prev_node] + graph[prev_node][node]:
                if node in paths[prev_node]:
                    path |= paths[prev_node][node]
                stack.append(prev_node)
    return len(path)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
