import aoc_helper

DAY = 6
YEAR = 2015


def parse_input(input_text):
    L = input_text.split("\n")
    return L


def p1(input_text):
    L = parse_input(input_text)
    lights = [[False for c in range(1000)] for r in range(1000)]

    for line in L:
        if line.startswith('turn off'):
            ran = line[9:]
            start, end = ran.split(' through ')
            start = [int(num) for num in start.split(',')]
            end = [int(num) for num in end.split(',')]
            for r in range(start[0], end[0]+1):
                for c in range(start[1], end[1]+1):
                    lights[r][c] = False
        elif line.startswith('turn on'):
            ran = line[8:]
            start, end = ran.split(' through ')
            start = [int(num) for num in start.split(',')]
            end = [int(num) for num in end.split(',')]
            for r in range(start[0], end[0]+1):
                for c in range(start[1], end[1]+1):
                    lights[r][c] = True
        elif line.startswith('toggle'):
            ran = line[7:]
            start, end = ran.split(' through ')
            start = [int(num) for num in start.split(',')]
            end = [int(num) for num in end.split(',')]
            for r in range(start[0], end[0]+1):
                for c in range(start[1], end[1]+1):
                    lights[r][c] = not lights[r][c]

    return sum(sum(val for val in row) for row in lights)


def p2(input_text):
    L = parse_input(input_text)
    lights = [[0 for c in range(1000)] for r in range(1000)]

    for line in L:
        if line.startswith('turn off'):
            ran = line[9:]
            start, end = ran.split(' through ')
            start = [int(num) for num in start.split(',')]
            end = [int(num) for num in end.split(',')]
            for r in range(start[0], end[0] + 1):
                for c in range(start[1], end[1] + 1):
                    lights[r][c] = max(lights[r][c] - 1, 0)
        elif line.startswith('turn on'):
            ran = line[8:]
            start, end = ran.split(' through ')
            start = [int(num) for num in start.split(',')]
            end = [int(num) for num in end.split(',')]
            for r in range(start[0], end[0] + 1):
                for c in range(start[1], end[1] + 1):
                    lights[r][c] += 1
        elif line.startswith('toggle'):
            ran = line[7:]
            start, end = ran.split(' through ')
            start = [int(num) for num in start.split(',')]
            end = [int(num) for num in end.split(',')]
            for r in range(start[0], end[0] + 1):
                for c in range(start[1], end[1] + 1):
                    lights[r][c] += 2

    return sum(sum(val for val in row) for row in lights)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
