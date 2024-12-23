import aoc_helper

DAY = None
YEAR = 2024


def parse_input(input_text):
    lines = input_text.split('\n')
    grid = [list(line) for line in lines]
    R = len(grid)
    C = len(grid[0])
    return None


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    lines = input_text.split('\n')
    grid = [list(line) for line in lines]
    R = len(grid)
    C = len(grid[0])
    x = parse_input(input_text)
    p1, p2 = None, None

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
