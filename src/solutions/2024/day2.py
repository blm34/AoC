import aoc_helper

DAY = 2
YEAR = 2024


def parse_input(input_text):
    L = input_text.split('\n')
    G = [[int(num) for num in line.split()] for line in L]
    return G


def p1(input_text):
    reports = parse_input(input_text)
    return sum(safe(report) for report in reports)


def p2(input_text):
    reports = parse_input(input_text)
    return sum(any(safe(report[:i] + report[i+1:])
                   for i in range(len(report) + 1))
               for report in reports)


def safe(report):
    diff = [report[i + 1] - report[i]
            for i in range(len(report) - 1)]
    return (all(-3 <= num <= -1 for num in diff) or
            all(1 <= num <= 3 for num in diff))


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
