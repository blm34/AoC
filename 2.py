import Modules
import sys
from numpy import prod

p1 = 0
p2 = 0

text = Modules.readInput(sys.argv[1]) 

for line in text.split('\n'):
    dims = [int(x) for x in line.split('x')]
    areas = [dims[i]*dims[(i+1)%3] for i in range(3)]
    volume = prod(dims)
    min_circ = (sum(dims)-max(dims))*2
    p1 += 2 * sum(areas) + min(areas)
    p2 += volume + min_circ

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 1588178
assert p2 == 3783758
