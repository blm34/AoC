import time
import Modules
import sys
START_TIME = time.time()

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')

def gen_graph(L):
    # Generate a graph where the weight of edges between two people represents the change in happiness if they are sat together
    G = dict()
    for line in L:
        p1, _, sign, num, _, _, _, _, _, _, p2 = line.strip('.').split()

        # Make sure person is in graph
        if p1 not in G:
            G[p1] = dict()

        # Calculate change in happiness
        num = int(num)
        if sign == 'lose':
            num *= -1

        G[p1][p2] = num
    return G

def happiness(G, path):
    # Calculate the change in happiness based off the order of people around the table
    val = 0
    for i in range(len(path)):
        left, person, right = path[i-1], path[i], path[(i+1)%len(path)]
        val += G[person][left]
        val += G[person][right]
    return val

G = gen_graph(L)
p1 = Modules.optimal_hamiltonian(G, happiness, max)

# Add 'me' to the graph
G['me'] = dict()
for person in G:
    if person == 'me':
        continue
    G[person]['me'] = 0
    G['me'][person] = 0

p2 = Modules.optimal_hamiltonian(G, happiness, max)

END_TIME = time.time()
RUN_TIME = round(1000*(END_TIME - START_TIME), 3)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')

assert p1 == 733
assert p2 == 725
