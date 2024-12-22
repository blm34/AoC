import aoc_helper

DAY = 3
YEAR = 2015


def p1(input_text):
    x, y = 0, 0
    history1 = {(x, y)}

    move_dict = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    for i, char in enumerate(input_text):
        dx, dy = move_dict[char]
        x += dx
        y += dy
        history1.add((x, y))
    return len(history1)


def p2(input_text):
    x1, y1, x2, y2 = 0, 0, 0, 0
    history2 = {(x1, y1), (x2, y2)}

    move_dict = {
        '^': (0, 1),
        'v': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    for i, char in enumerate(input_text):
        dx, dy = move_dict[char]
        if i % 2 == 0:
            x1 += dx
            y1 += dy
            history2.add((x1, y1))
        else:
            x2 += dx
            y2 += dy
            history2.add((x2, y2))

    return len(history2)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
