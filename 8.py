import Modules
import sys

p1 = 0
p2 = 0

text = Modules.readInput(sys.argv[1]) 
L = text.split('\n')

for line in L:
    # Part 1
    p1 += 2 # For the two quotes on either end
    p2 += 2 # For the two quotes on either end
    i = 0
    while i < len(line):
        if line[i] == '\"': # If " then a \ added for part 2
            p2 += 1
        elif line[i] == '\\': # If \ then a \ added for part 2
            p2 += 1
            if line[i+1] == '\\': # If next char \ then \ removed in part 1 and another added in part 2
                p1 += 1
                p2 += 1
                i += 1
            elif line[i+1] == '\"': # If next char " then \ removed in part 1 and added in part 2
                p1 += 1
                p2 += 1
                i += 1
            elif line[i+1] == 'x': # If next char # then 4 chars become 1 in part 1 and next 3 char irrelevant for part 2
                p1 += 3
                i += 3
        i += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 1350
assert p2 == 2085
