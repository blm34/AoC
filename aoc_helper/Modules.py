import heapq
from numpy import prod as product
from typing import Iterable, Callable


def read_input(file: str) -> str:
    """
    Opens the given file. Typically a puzzle input

    Args:
        file: The file to open

    Returns:
        The contents of the file
    """
    with open(f'input_files\\{file}', 'r') as file:
        text = file.read().strip()
    return text


def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor using the Euclidean algorithm

    Args:
        a: The first number
        b: The second number

    Returns:
        The gcd of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a


def lcm(nums: Iterable[int]) -> int:
    """
    Calculates the lowest common multiple of an iterable of numbers

    Args:
        nums: Iterable of ints of which to find the lowest common multiple

    Returns:
        The lowest common multiple of the ints
    """
    ans = 1
    for num in nums:
        ans = ans // gcd(num, ans) * num
    return ans


def dijkstra(G: dict, start_node, target_node=None):
    """
    Perform dijkstra's algorithm to find the shortest path from vertex a to vertex b (if b is None then to all vertices).

    Args:
        G: A dictionary containing dictionaries for each vertex, each representing an edge e.g. {v1:{v2:3, v3:4}, v2:{v1:3}, v3:{v1:4}}
        start_node: The start node as in the form of its key in G.
        target_node: The end node as in the form of its key in G.

    Returns:
        A tuple containing the sum of weights from a to b, and the path taken. If b==None, a dict with values for each possible b.
    """
    visited = set(start_node)
    prev_vert_dict = dict()
    dists = dict()
    Q = []  # The 'queue' of vertices to analyse. Made up of tuples of the form (distance, vertex, previous_vertex)
    heapq.heappush(Q, (0, start_node, None))

    # Loop for dijkstra - each iteration compute next vertex
    while Q and len(visited) < len(G):
        # Pop next vertex off heap and check it's not already been calculated
        dist, vert, prev_vert = heapq.heappop(Q)
        if vert in visited:
            continue
        visited.add(vert)

        # Save distance and previous vertex in path
        dists[vert] = dist
        prev_vert_dict[vert] = prev_vert

        # Check if it's the destination vertex
        if vert == target_node:
            # Calculate the entire path in reverse
            path = [target_node]
            while path[-1] != start_node:
                path.append(prev_vert_dict[path[-1]])
            path.reverse()
            return dist, path

        # Loop through the neighbouring vertices
        for neigh in G[vert]:
            if neigh in visited:
                continue
            heapq.heappush(Q, (dist + G[vert][neigh], neigh, vert))

    # Dijkstra complete. Now calculate all the paths
    paths = dict()
    for vert in G:
        path = [vert]
        while path[-1] != start_node:
            path.append(prev_vert_dict[path[-1]])
        path.reverse()
        paths[vert] = path
    return dists, paths


def optimal_hamiltonian(G: dict,
                        eval_func: Callable=lambda G, p: sum(G[p[i]][p[i + 1]] for i in range(len(p) - 1)),
                        opt_func: Callable=min):
    """
    Return the hamiltonian path that optimises the value of eval_func performed on the path (default sum of weights) with the optimisations defined by opt_func (default minimum)

    Args:
        G: A dictionary containing dictionaries for each vertex, each representing an edge e.g. {v1:{v2:3, v3:4}, v2:{v1:3}, v3:{v1:4}}
        eval_func: Takes two parameters (G, path) and calculates a score for the path through G (default: sum of weights)
        opt_func: Returns the optimal value from an iterable of ints (default: min)

    Returns:
        The value of eval_func associated with the optimal hamiltonian path
    """
    def dfs(path):
        """
        Recursively perform a depth first search to find all hamiltonian paths
        """
        vert = path[-1]
        if len(path) == len(G):
            return eval_func(G, path)
        return opt_func(dfs(path + [neigh]) for neigh in G[vert] if neigh not in path)

    return opt_func(dfs([start_vert]) for start_vert in G)


def prod(nums: Iterable[int | float]):
    """
    Calculate the product of numbers in an iterable

    Args:
        nums: An iterable containing numbers

    Returns:
        The product of all numbers in nums
    """
    return product(nums)
