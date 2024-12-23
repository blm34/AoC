from collections import defaultdict

import aoc_helper

DAY = 23
YEAR = 2024


def bron_kerbosch(graph, r=set(), p=None, x=set()):
    if p is None:
        p = set(graph.keys())

    if not p and not x:
        yield r
    else:
        u = next(iter(p | x))
        for v in p - graph[u]:
            yield from bron_kerbosch(graph, r | {v}, p & graph[v], x & graph[v])
            p.remove(v)
            x.add(v)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    p1 = 0
    lines = input_text.split('\n')
    graph = defaultdict(lambda: set())
    for line in lines:
        node1, node2 = line.split("-")
        graph[node1].add(node2)
        graph[node2].add(node1)
        common_neighbours = graph[node1] & graph[node2]
        if node1[0] == 't' or node2[0] == 't':
            p1 += len(common_neighbours)
        else:
            p1 += len([node3 for node3 in common_neighbours if node3[0] == 't'])

    fully_connected_sub_graphs = list(bron_kerbosch(graph))
    largest_fully_connected_sub_graph = max(fully_connected_sub_graphs, key=len)
    p2 = ','.join(sorted(largest_fully_connected_sub_graph))
    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
