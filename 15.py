import time
import Modules
import sys
START_TIME = time.time()

p1 = 0
p2 = 0

text = Modules.read_input(sys.argv[1])
L = text.split('\n')

# Calculate the score for a recipe
def score(properties, split):
    ans = 1
    for p in range(4):
        val = 0
        for i in range(4):
           val += properties[i][p] * split[i] 
        ans *= max(val, 0)
    return ans

# Calculate the number of calories for a recipe
def calories(properties, split):
    ans = 0
    for i in range(4):
        ans += properties[i][4] * split[i]
    return ans

# Parse input
properties = []
for line in L:
    line = line.split(': ')[1]
    properties.append([])
    for p in line.split(', '):
        properties[-1].append(int(p.split()[1]))

# Loop through all combinations of ingredients
for i in range(101):
    for j in range(101):
        if i+j > 100:
            break
        for k in range(101):
            if i+j+k > 100:
                break
            l = 100 - (i+j+k)
            p1 = max(p1, score(properties, (i,j,k,l)))
            if calories(properties, (i,j,k,l)) == 500:
                p2 = max(p2, score(properties, (i,j,k,l)))

END_TIME = time.time()
RUN_TIME = round(1000*(END_TIME - START_TIME), 3)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')

assert p1 == 18965440
assert p2 == 15862900
