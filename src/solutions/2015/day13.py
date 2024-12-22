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

def p1(input_text):
    G = parse_input(input_text)
    return aoc_helper.optimal_hamiltonian(G, happiness, max)


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


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
