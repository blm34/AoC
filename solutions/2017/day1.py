import aoc_helper

DAY = 1
YEAR = 2017


def parse_input(input_text):
    return [int(num) for num in input_text]


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    nums = parse_input(input_text)
    return sum_match_offset(nums, 1)


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    nums = parse_input(input_text)
    return sum_match_offset(nums, len(nums)//2)


def sum_match_offset(nums, offset):
    total = 0
    for i in range(len(nums)):
        if nums[i] == nums[(i+offset) % len(nums)]:
            total += nums[i]
    return total


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
