import aoc_helper

DAY = 2
YEAR = 2016

MOVES = {'U': (0, 1),
         'D': (0, -1),
         'R': (1, 0),
         'L': (-1, 0)}


def parse_input(input_text):
    L = input_text.split('\n')
    return L


def loc_to_num_p1(loc):
    col, row = loc
    return (col + 1) + (1 - row) * 3 + 1


def loc_to_num_p2(loc):
    pad = [['_', '_', '1', '_', '_'],
           ['_', '2', '3', '4', '_'],
           ['5', '6', '7', '8', '9'],
           ['_', 'A', 'B', 'C', '_'],
           ['_', '_', 'D', '_', '_']]
    x, y = loc
    row = 2 - y
    col = 2 + x
    return pad[row][col]


def p1(input_text):
    L = parse_input(input_text)
    loc = (0, 0)
    ans = ""

    for line in L:
        for char in line:
            x = loc[0] + MOVES[char][0]
            y = loc[1] + MOVES[char][1]
            if abs(x) <= 1 and abs(y) <= 1:
                loc = (x, y)

        ans += str(loc_to_num_p1(loc))
    return ans


def p2(input_text):
    L = parse_input(input_text)
    loc = (-2, 0)
    ans = ""

    for line in L:
        for char in line:
            x = loc[0] + MOVES[char][0]
            y = loc[1] + MOVES[char][1]
            if abs(x) + abs(y) <= 2:
                loc = (x, y)

        ans += loc_to_num_p2(loc)
    return ans


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
