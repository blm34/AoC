import aoc_helper

DAY = 13
YEAR = 2024


def parse_input(input_text):
    turns_text = input_text.split('\n\n')
    turns = []
    for turn_test in turns_text:
        turn = []
        lines = turn_test.splitlines()
        for i, line in enumerate(lines):
            _, line = line.split(": ")
            first, second = line.split(", ")
            turn.append([int(first[2:]), int(second[2:])])
        turns.append(turn)
    return turns


def min_tokens(da, db, target):
    det = da[0]*db[1] - db[0]*da[1]
    a_num = target[0]*db[1] - target[1]*db[0]
    b_num = target[1]*da[0] - target[0]*da[1]
    if 0 == a_num%det == b_num%det:
        return a_num//det, b_num//det
    else:
        return 0, 0


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    turns = parse_input(input_text)

    p1 = 0
    p2 = 0

    for turn in turns:
        a, b = min_tokens(*turn)
        p1 += 3*a + b

        turn[2][0] += 10_000_000_000_000
        turn[2][1] += 10_000_000_000_000
        a, b = min_tokens(*turn)
        p2 += 3*a + b

    return p1, p2

if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
