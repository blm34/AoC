import aoc_helper

DAY = 1
YEAR = 2017


def parse_input(input_text):
    return [int(num) for num in input_text]


def p1(input_text):
    nums = parse_input(input_text)
    return sum_match_offset(nums, 1)


def p2(input_text):
    nums = parse_input(input_text)
    return sum_match_offset(nums, len(nums)//2)


def sum_match_offset(nums, offset):
    total = 0
    for i in range(len(nums)):
        if nums[i] == nums[(i+offset) % len(nums)]:
            total += nums[i]
    return total


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
