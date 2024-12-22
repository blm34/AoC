import aoc_helper

DAY = 5
YEAR = 2017


def parse_input(input_text):
    return [int(num) for num in input_text.split('\n')]


def p1(input_text):
    nums = parse_input(input_text)
    size = len(nums)
    index = 0
    steps = 0

    while 0 <= index < size:
        steps += 1
        nums[index] += 1
        index += nums[index] - 1

    return steps


def p2(input_text):
    nums = parse_input(input_text)
    size = len(nums)
    index = 0
    steps = 0

    while 0 <= index < size:
        steps += 1
        next_index = index + nums[index]
        nums[index] += 1 if nums[index] < 3 else -1
        index = next_index

    return steps


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
