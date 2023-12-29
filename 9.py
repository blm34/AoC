import Modules
import sys

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')

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

# Find all hamiltonian paths via dfs and return the shortest and longest
def dfs(graph, path, dist, part2=False):
    vert = path[-1]
    if len(path) == len(graph):
        return dist
    if part2:
        return max(dfs(graph, path+[neigh], dist+graph[vert][neigh], part2) for neigh in graph[vert] if neigh not in path)
    else:
        return min(dfs(graph, path+[neigh], dist+graph[vert][neigh], part2) for neigh in graph[vert] if neigh not in path)

p1 = dfs(graph, ['start'], 0)
p2 = dfs(graph, ['start'], 0, part2=True)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 207
assert p2 == 804
