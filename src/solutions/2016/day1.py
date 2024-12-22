import aoc_helper

DAY = 1
YEAR = 2016


def parse_input(input_text):
    steps = input_text.split(', ')
    return [(step[0], int(step[1:])) for step in steps]


def p1(input_text):
    steps = parse_input(input_text)
    loc = [0, 0]
    bearing = 0
    for step in steps:
        if step[0] == 'L':
            bearing = (bearing - 90) % 360
        elif step[0] == 'R':
            bearing = (bearing + 90) % 360
        if bearing == 0:
            loc[1] += step[1]
        elif bearing == 90:
            loc[0] += step[1]
        elif bearing == 180:
            loc[1] -= step[1]
        elif bearing == 270:
            loc[0] -= step[1]
    return abs(loc[0]) + abs(loc[1])


def p2(input_text):
    steps = parse_input(input_text)
    visited = list()
    loc = [0, 0]
    bearing = 0
    for step in steps:
        if step[0] == 'L':
            bearing = (bearing - 90) % 360
        elif step[0] == 'R':
            bearing = (bearing + 90) % 360

        if bearing == 0:
            index = 1
            step_dir = 1
        elif bearing == 90:
            index = 0
            step_dir = 1
        elif bearing == 180:
            index = 1
            step_dir = -1
        elif bearing == 270:
            index = 0
            step_dir = -1

        for _ in range(step[1]):
            loc[index] += step_dir
            if loc in visited:
                return abs(loc[0]) + abs(loc[1])
            visited.append(loc.copy())


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
