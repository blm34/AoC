import aoc_helper

DAY = 20
YEAR = 2015


def parse_input(input_text):
    return int(input_text)


def p1(input_text):
    target_presents = parse_input(input_text)
    houses = [0] * (target_presents // 10)
    for elf in range(1, len(houses)):
        for house in range(0, len(houses), elf):
            houses[house] += 10 * elf
        if houses[elf] > target_presents:
            return elf


def p2(input_text):
    target_presents = parse_input(input_text)
    houses = [0] * (target_presents // 10)
    for elf in range(1, len(houses)):
        for house in range(elf, min(elf * 50 + 1, len(houses)), elf):
            houses[house] += 11 * elf
        if houses[elf] > target_presents:
            return elf


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
