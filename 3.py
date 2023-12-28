import Modules
import sys

text = Modules.readInput(sys.argv[1]) 

move_dict = {
        '^':(0, 1),
        'v':(0, -1),
        '<':(-1, 0),
        '>':(1, 0)
        }

x, y, x1, y1, x2, y2 = 0,0,0,0,0,0

history1 = set((x,y))
history2 = set(((x1, y1), (x2, y2)))

for i, char in enumerate(text):
    dx, dy = move_dict[char]
    x += dx
    y += dy
    history1.add((x, y),)
    if i%2 == 0:
        x1 += dx
        y1 += dy
        history2.add((x1, y1),)
    else:
        x2 += dx
        y2 += dy
        history2.add((x2, y2),)

p1 = len(history1)
p2 = len(history2)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 2592
assert p2 == 2360
