import Modules
import sys

p1 = 0
p2 = 0

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')

for line in L:
    # Part 1
    p1 += 2 # For the two quotes on either end
    i = 0
    while i < len(line):
        if line[i] == '\\':
            if line[i+1] == '\\':
                p1 += 1
                i += 1
            elif line[i+1] == '\"':
                p1 += 1
                i += 1
            elif line[i+1] == 'x':
                p1 += 3
                i += 3
        i += 1

    # Part 2
    p2 += 2 # For the two quotes on either end
    for char in line:
        if char == '\"':
            p2 += 1
        elif char == '\\':
            p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 1350
assert p2 == 2085
