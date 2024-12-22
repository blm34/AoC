import aoc_helper

DAY = 1
YEAR = 2015

def p1(input_text):
    ans = 0
    for i, char in enumerate(input_text):
        if char == '(':
            ans += 1
        elif char == ')':
            ans -= 1
    return ans


def p2(input_text):
    floor = 0
    for i, char in enumerate(input_text):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return i+1


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
