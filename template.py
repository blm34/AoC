import time
import Modules
import sys
START_TIME = time.time()

p1 = 0
p2 = 0

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')
G = [list(line) for line in L]
R = len(G)
C = len(G[0])



END_TIME = time.time()
RUN_TIME = round(1000*(END_TIME - START_TIME), 3)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')
