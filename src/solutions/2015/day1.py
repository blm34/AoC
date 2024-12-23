import aoc_helper

DAY = 1
YEAR = 2015


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    floor = 0
    p2 = None
    for i, char in enumerate(input_text):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if p2 is None and floor == -1:
            p2 = i+1
    return floor, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
