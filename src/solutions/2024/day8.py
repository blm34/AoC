from collections import defaultdict

import aoc_helper

DAY = 8
YEAR = 2024


def parse_input(input_text):
    lines = input_text.splitlines()
    height = len(lines)
    width = len(lines[0])

    ants = defaultdict(list)
    for r in range(height):
        for c in range(width):
            val = lines[r][c]
            if val != '.':
                ants[val].append((r, c))
    return ants, height, width


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    ants, height, width = parse_input(input_text)

    p1_nodes = set()
    p2_nodes = set()

    for char in ants:
        for i in range(len(ants[char])-1):
            for j in range(i+1, len(ants[char])):
                ant1 = ants[char][i]
                ant2 = ants[char][j]

                dr = ant1[0] - ant2[0]
                dc = ant1[1] - ant2[1]

                # Part 1
                if 0 <= ant1[0] + dr < height and 0 <= ant1[1] + dc < width:
                    p1_nodes.add((ant1[0] + dr, ant1[1] + dc))
                if 0 <= ant2[0] - dr < height and 0 <= ant2[1] - dc < width:
                    p1_nodes.add((ant2[0] - dr, ant2[1] - dc))

                # Part 2
                new_node = ant1
                while 0 <= new_node[0] < height and 0 <= new_node[1] < width:
                    p2_nodes.add(new_node)
                    new_node = (new_node[0] + dr, new_node[1] + dc)

                new_node = ant2
                while 0 <= new_node[0] < height and 0 <= new_node[1] < width:
                    p2_nodes.add(new_node)
                    new_node = (new_node[0] - dr, new_node[1] - dc)

    return len(p1_nodes), len(p2_nodes)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
