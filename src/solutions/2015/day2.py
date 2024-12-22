import aoc_helper

DAY = 2
YEAR = 2015


def p1(input_text):
    ans = 0
    for line in input_text.split('\n'):
        dims = [int(x) for x in line.split('x')]
        areas = [dims[i] * dims[(i + 1) % 3] for i in range(3)]
        ans += 2 * sum(areas) + min(areas)
    return ans


def p2(input_text):
    ans = 0
    for line in input_text.split('\n'):
        dims = [int(x) for x in line.split('x')]
        volume = aoc_helper.prod(dims)
        min_circ = (sum(dims) - max(dims)) * 2
        ans += volume + min_circ
    return ans


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
