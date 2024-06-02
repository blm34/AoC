import aoc_helper

DAY = 16
YEAR = 2015

TARGET = {
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

def parse_input(input_text):
    L = input_text.split("\n")

    aunts = dict()
    for line in L:
        index = line.index(':')
        aunt = int(line[:index].split()[1])

        values = line[index+2:].split(', ')
        values = {x.split(': ')[0]: int(x.split(': ')[1]) for x in values}

        aunts[aunt] = values

    return aunts

@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    aunts = parse_input(input_text)
    for aunt in aunts:
        correct = True
        for k, v in aunts[aunt].items():
            if TARGET[k] != v:
                correct = False
                break
        if correct:
            return aunt


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    aunts = parse_input(input_text)
    for aunt in aunts:
        correct = True
        for k, v in aunts[aunt].items():
            if k in ('cats', 'trees'):
                if v <= TARGET[k]:
                    correct = False
                    break
            elif k in ('pomeranians', 'goldfish'):
                if v >= TARGET[k]:
                    correct = False
                    break
            else:
                if v != TARGET[k]:
                    correct = False
                    break
        if correct:
            return aunt

if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
