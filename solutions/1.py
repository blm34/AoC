import aoc_helper
import sys

p1 = 0
p2 = 0

text = aoc_helper.read_input(sys.argv[1])

for i, char in enumerate(text):
    if char == '(':
        p1 += 1
    elif char == ')':
        p1 -= 1
    if p1 == -1 and not p2:
        p2 = i+1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 280
assert p2 == 1797