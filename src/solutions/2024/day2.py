import aoc_helper

DAY = 2
YEAR = 2024


def parse_input(input_text):
    return [tuple(map(int, line.split()))
            for line in input_text.split("\n")]


def safe(report):
    diff = [report[i + 1] - report[i]
            for i in range(len(report) - 1)]
    return (all(-3 <= num <= -1 for num in diff) or
            all(1 <= num <= 3 for num in diff))


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    reports = parse_input(input_text)

    p1 = sum(safe(report) for report in reports)
    p2 = sum(any(safe(report[:i] + report[i+1:])
                 for i in range(len(report)))
             for report in reports)

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
