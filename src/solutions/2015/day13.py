import aoc_helper

DAY = 13
YEAR = 2015


def parse_input(input_text):
    L = input_text.split('\n')

    # Generate a graph where the weight of edges between two people represents the change in happiness if they are sat together
    G = dict()
    for line in L:
        p1, _, sign, num, _, _, _, _, _, _, p2 = line.strip('.').split()

        # Make sure person is in graph
        if p1 not in G:
            G[p1] = dict()

        # Calculate change in happiness
        num = int(num)
        if sign == 'lose':
            num *= -1

        G[p1][p2] = num
    return G

def happiness(G, path):
    # Calculate the change in happiness based off the order of people around the table
    val = 0
    for i in range(len(path)):
        left, person, right = path[i-1], path[i], path[(i+1)%len(path)]
        val += G[person][left]
        val += G[person][right]
    return val

@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    G = parse_input(input_text)
    return aoc_helper.optimal_hamiltonian(G, happiness, max)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    G = parse_input(input_text)
    # Add 'me' to the graph
    G['me'] = dict()
    for person in G:
        if person == 'me':
            continue
        G[person]['me'] = 0
        G['me'][person] = 0

    return aoc_helper.optimal_hamiltonian(G, happiness, max)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
