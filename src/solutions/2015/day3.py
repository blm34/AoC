import aoc_helper

DAY = 3
YEAR = 2015


@aoc_helper.communicator(YEAR, DAY, 1)
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


@aoc_helper.communicator(YEAR, DAY, 2)
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


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
