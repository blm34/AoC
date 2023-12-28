import Modules
import sys

p1 = 0
p2 = 0

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')
G = [list(line) for line in L]
R = len(G)
C = len(G[0])



print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
