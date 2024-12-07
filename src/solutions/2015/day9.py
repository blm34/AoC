import aoc_helper

DAY = 9
YEAR = 2015


def parse_input(input_text):
    L = input_text.split("\n")

    # Generate graph
    graph = dict()
    for line in L:
        loc1, _, loc2, _, dist = line.split()
        for loc in (loc1, loc2):
            if loc not in graph:
                graph[loc] = dict()
        graph[loc1][loc2] = int(dist)
        graph[loc2][loc1] = int(dist)

    # Add a 'start' node that connects to all locations with distance 0
    graph['start'] = {loc:0 for loc in graph}

    return graph

def dfs(graph, path, dist, part2=False):
    """Find all hamiltonian paths via dfs and return the shortest and longest"""
    vert = path[-1]
    if len(path) == len(graph):
        return dist
    if part2:
        return max(dfs(graph, path+[neigh], dist+graph[vert][neigh], part2) for neigh in graph[vert] if neigh not in path)
    else:
        return min(dfs(graph, path+[neigh], dist+graph[vert][neigh], part2) for neigh in graph[vert] if neigh not in path)

@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    graph = parse_input(input_text)
    return dfs(graph, ['start'], 0)

@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    graph = parse_input(input_text)
    return dfs(graph, ['start'], 0, part2=True)

if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
