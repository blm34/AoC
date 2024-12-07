import aoc_helper

DAY = 2
YEAR = 2017


def parse_input(input_text):
    L = input_text.split('\n')
    sheet = []
    for line in L:
        sheet.append([int(num) for num in line.split()])
    return sheet


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    sheet = parse_input(input_text)
    total = 0
    for row in sheet:
        total += max(row) - min(row)
    return total


@aoc_helper.communicator(YEAR, DAY, 2)
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


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
