import aoc_helper

DAY = 8
YEAR = 2024


def parse_input(input_text):
    L = input_text.split('\n')
    R = len(L)
    C = len(L[0])

    ants = dict()
    for r in range(R):
        for c in range(C):
            val = L[r][c]
            if val != '.':
                if val not in ants:
                    ants[val] = list()
                ants[val].append((r, c))
    return ants, R, C


def p1(input_text):
    ants, height, width = parse_input(input_text)
    nodes = set()
    for char in ants:
        for i in range(len(ants[char])-1):
            for j in range(i+1, len(ants[char])):
                ant1 = ants[char][i]
                ant2 = ants[char][j]

                dr = ant1[0] - ant2[0]
                dc = ant1[1] - ant2[1]

                if 0 <= ant1[0] + dr < height and 0 <= ant1[1] + dc < width:
                    nodes.add((ant1[0] + dr, ant1[1] + dc))
                if 0 <= ant2[0] - dr < height and 0 <= ant2[1] - dc < width:
                    nodes.add((ant2[0] - dr, ant2[1] - dc))
    return len(nodes)


def p2(input_text):
    ants, height, width = parse_input(input_text)
    nodes = set()
    for char in ants:
        for i in range(len(ants[char])-1):
            for j in range(i+1, len(ants[char])):
                ant1 = ants[char][i]
                ant2 = ants[char][j]

                dr = ant1[0] - ant2[0]
                dc = ant1[1] - ant2[1]

                new_node = ant1
                while 0 <= new_node[0] < height and 0 <= new_node[1] < width:
                    nodes.add(new_node)
                    new_node = (new_node[0] + dr, new_node[1] + dc)

                new_node = ant2
                while 0 <= new_node[0] < height and 0 <= new_node[1] < width:
                    nodes.add(new_node)
                    new_node = (new_node[0] - dr, new_node[1] - dc)

    return len(nodes)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
