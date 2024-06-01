import aoc_helper
import sys

p1 = 0
p2 = 0

text = aoc_helper.read_input("2.txt")

for line in text.split('\n'):
    dims = [int(x) for x in line.split('x')]
    areas = [dims[i]*dims[(i+1)%3] for i in range(3)]
    volume = aoc_helper.prod(dims)
    min_circ = (sum(dims)-max(dims))*2
    p1 += 2 * sum(areas) + min(areas)
    p2 += volume + min_circ

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 1588178
assert p2 == 3783758
