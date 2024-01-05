def readInput(file):
    '''
    Opens the given file. Typically an puzzle input

    Parameters
    ----------
    file : str
        The file to open

    Returns
    -------
    str
        String of the file contents
    '''
    with open(f'{file}', 'r') as file:
        text = file.read().strip()
    return text

def gcd(a, b):
    '''
    Calculates the greatest common divisor using the Euclidean algorithm

    Parameters
    ----------
    a : int
        The first number
    b : int
        The second number

    Returns
    -------
    int
        The gcd of a and b
    '''
    while b != 0:
        a, b = b, a%b
    return a

def lcm(nums):
    '''
    Calculates the lowest common multiple of an interable of numbers

    Parameters
    ----------
    nums : iterable
        Iterable containing ints

    Returns
    -------
    int
        The lcd of all the nums
    '''
    ans = 1
    for num in nums:
        ans = ans // gcd(num, ans) * num
    return ans

def dijkstra(G, a, b=None):
    '''
    Perform dijkstra's algorithm to find the shortest path from vertex a to vertex b (if b is None then to all vertices)

    Parameters
    ----------
    G : dict
        A dictionary containing dictionaries for each vertex, each representing an edge e.g. {v1:{v2:3, v3:4}, v2:{v1:3}, v3:{v1:4}}
    a : immutable
        The start node as in the form of its key in G
    b : immutable
        The end node as in the form of its key in G. Delault=None

    Returns
    -------
    int
        The sum of weights from a to b (or a dict of ints if b=None)
    list
        The path from a to b (or a dict of list if b=None)
    '''
    import heapq

    visited = set(a)
    prev_vert_dict = dict()
    dists = dict()
    Q = [] # The 'queue' of vertices to analyse. Made up of tuples of the form (distance, vertex, previous_vertex)
    heapq.heappush(Q, (0, a, None))

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

        # Check if its the destination vertex
        if vert == b:
            # Calculate the entire path in reverse
            path = [b]
            while path[-1] != a:
                path.append(prev_vert_dict[path[-1]])
            path.reverse()
            return dist, path

        # Loop through the neighbouring vertices
        for neigh in G[vert]:
            if neigh in visited:
                continue
            heapq.heappush(Q, (dist+G[vert][neigh], neigh, vert))

    # Dijkstra complete. Now caculate all the paths
    paths = dict()
    for vert in G:
        path = [vert]
        while path[-1] != a:
            path.append(prev_vert_dict[path[-1]])
        path.reverse()
        paths[vert] = path
    return dists, paths

def optimal_hamiltonian(G, eval_func, opt_func):
    pass
