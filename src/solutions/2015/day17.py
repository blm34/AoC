import aoc_helper

DAY = 17
YEAR = 2015


def parse_input(input_text):
    L = input_text.split('\n')

    containers = [int(x) for x in L]
    containers.sort()
    return containers


def dp1(remaining, target):
    if target <= 0:
        return int(target == 0)
    total = 0
    for i in range(len(remaining)):
        total += dp1(remaining[i + 1:], target - remaining[i])
    return total


def dp2(used, remaining, target):
    if target == 0:
        return (len(used), 1)
    if target < 0:
        return None
    ans = None
    for i, bucket in enumerate(remaining):
        next_ans = dp2(used + [bucket], remaining[i + 1:], target - bucket)
        if next_ans is None:
            continue
        elif ans is None:
            ans = next_ans
        elif next_ans[0] == ans[0]:
            ans = (ans[0], next_ans[1] + ans[1])
        elif next_ans[0] < ans[0]:
            ans = next_ans
    return ans


def p1(input_text):
    quantity = 150
    containers = parse_input(input_text)
    return dp1(containers, quantity)


def p2(input_text):
    quantity = 150
    containers = parse_input(input_text)
    return dp2([], containers, quantity)[0]


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
