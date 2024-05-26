import time
import aoc_helper
START_TIME = time.time()

text = aoc_helper.read_input("19.txt")

replacements_text, molecule = text.split('\n\n')

replacements = list()
for line in replacements_text.split('\n'):
    m1, m2 = line.split(' => ')
    replacements.append((m1, m2))


def step(molecule, replacements):
    unique = set()
    j = -1
    while j+1 < len(molecule):
        # Find start of next element
        i = j = j+1
        # Find end of element
        while j+1 < len(molecule) and molecule[j+1] == molecule[j+1].lower():
            j += 1
        element = molecule[i:j+1]
        for m1, m2 in replacements:
            if element == m1:
                new_molecule = molecule[:i] + m2 + molecule[j+1:]
                unique.add(new_molecule)
    return unique


def step_count(molecule):
    j = -1
    count = -1
    while j+1 < len(molecule):
        # find start of next element
        i = j = j+1
        # Find end of element
        while j+1 < len(molecule) and molecule[j+1] == molecule[j+1].lower():
            j += 1
        element = molecule[i:j+1]
        if element == 'Rn':
            pass
        elif element == 'Ar':
            pass
        elif element == 'Y':
            count -= 1
        else:
            count += 1
    return count


p1 = len(step(molecule, replacements))
p2 = step_count(molecule)

END_TIME = time.time()
RUN_TIME = END_TIME - START_TIME
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {1000*RUN_TIME:.3f} ms')
