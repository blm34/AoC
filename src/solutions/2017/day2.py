import aoc_helper

DAY = 2
YEAR = 2017


def parse_input(input_text):
    L = input_text.split('\n')
    sheet = []
    for line in L:
        sheet.append([int(num) for num in line.split()])
    return sheet


def p1(input_text):
    sheet = parse_input(input_text)
    total = 0
    for row in sheet:
        total += max(row) - min(row)
    return total


def p2(input_text):
    sheet = parse_input(input_text)
    total = 0
    for row in sheet:
        for i in range(len(row)-1):
            for j in range(i+1, len(row)):
                num1, num2 = row[i], row[j]
                if num1 < num2:
                    num1, num2 = num2, num1
                div, mod = divmod(num1, num2)
                if mod == 0:
                    total += div
    return total


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
