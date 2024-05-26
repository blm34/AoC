import time
import Modules

START_TIME = time.time()

text = Modules.read_input("16.txt")
L = text.split('\n')

target = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

aunts = dict()
for line in L:
    index = line.index(':')
    aunt = int(line[:index].split()[1])

    values = line[index+2:].split(', ')
    values = {x.split(': ')[0]: int(x.split(': ')[1]) for x in values}

    aunts[aunt] = values

for aunt in aunts:
    correct = True
    for k, v in aunts[aunt].items():
        if target[k] != v:
            correct = False
            break
    if correct:
        p1 = aunt

    correct = True
    for k, v in aunts[aunt].items():
        if k in ('cats', 'trees'):
            if v <= target[k]:
                correct = False
                break
        elif k in ('pomeranians', 'goldfish'):
            if v >= target[k]:
                correct = False
                break
        else:
            if v != target[k]:
                correct = False
                break
    if correct:
        p2 = aunt

END_TIME = time.time()
RUN_TIME = round(1000*(END_TIME - START_TIME), 3)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')
