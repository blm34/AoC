import aoc_helper

DAY = 2
YEAR = 2015


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    ans = 0
    for line in input_text.split('\n'):
        dims = [int(x) for x in line.split('x')]
        areas = [dims[i] * dims[(i + 1) % 3] for i in range(3)]
        ans += 2 * sum(areas) + min(areas)
    return ans


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    ans = 0
    for line in input_text.split('\n'):
        dims = [int(x) for x in line.split('x')]
        volume = aoc_helper.prod(dims)
        min_circ = (sum(dims) - max(dims)) * 2
        ans += volume + min_circ
    return ans


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
