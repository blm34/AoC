import time
import Modules
START_TIME = time.time()

p2 = 0

text = Modules.readInput("19.txt")

replacements_text, molecule = text.split('\n\n')

replacements = dict()
backwards_replacements = dict()
for line in replacements_text.split('\n'):
    m1, m2 = line.split(' => ')
    if m1 not in replacements:
        replacements[m1] = list()
    replacements[m1].append(m2)
    if m2 not in backwards_replacements:
        backwards_replacements[m2] = list()
    backwards_replacements[m2].append(m1)


def step(molecule, replacements):
    unique = set()
    i = 0
    j = -1
    while j+1 < len(molecule):
        i = j = j+1
        while j+1 < len(molecule) and molecule[j+1] == molecule[j+1].lower():
            j += 1
        element = molecule[i:j+1]
        if element not in replacements:
            continue
        for rep in replacements[element]:
            new_molecule = molecule[:i] + rep + molecule[j+1:]
            unique.add(new_molecule)
    return unique


p1 = len(step(molecule, replacements))


END_TIME = time.time()
RUN_TIME = END_TIME - START_TIME
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {1000*RUN_TIME:.3f} ms')
