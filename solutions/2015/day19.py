import aoc_helper

DAY = 19
YEAR = 2015


def parse_input(input_text):
    replacements_text, molecule = input_text.split('\n\n')

    replacements = list()
    for line in replacements_text.split('\n'):
        m1, m2 = line.split(' => ')
        replacements.append((m1, m2))

    return molecule, replacements

@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    molecule, replacements = parse_input(input_text)
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
    return len(unique)

@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    molecule, _ = parse_input(input_text)
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


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
