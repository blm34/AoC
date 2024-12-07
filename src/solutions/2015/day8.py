import aoc_helper

DAY = 8
YEAR = 2015


def parse_input(input_text):
    L = input_text.split('\n')
    return L


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    L = parse_input(input_text)

    ans = 0
    for line in L:
        ans += 2  # For the two quotes on either end
        i = 0
        while i < len(line):
            if line[i] == '\\':  # If \ then a \ added for part 2
                if line[i + 1] == '\\':  # If next char \ then \ removed in part 1 and another added in part 2
                    ans += 1
                    i += 1
                elif line[i + 1] == '\"':  # If next char " then \ removed in part 1 and added in part 2
                    ans += 1
                    i += 1
                elif line[i + 1] == 'x':  # If next char # then 4 chars become 1 in part 1 and next 3 char irrelevant for part 2
                    ans += 3
                    i += 3
            i += 1
    return ans


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    L = parse_input(input_text)
    ans = 0

    for line in L:
        ans += 2  # For the two quotes on either end
        i = 0
        while i < len(line):
            if line[i] == '\"':  # If " then a \ added for part 2
                ans += 1
            elif line[i] == '\\':  # If \ then a \ added for part 2
                ans += 1
                if line[i + 1] == '\\':  # If next char \ then \ removed in part 1 and another added in part 2
                    ans += 1
                    i += 1
                elif line[i + 1] == '\"':  # If next char " then \ removed in part 1 and added in part 2
                    ans += 1
                    i += 1
                elif line[
                    i + 1] == 'x':  # If next char # then 4 chars become 1 in part 1 and next 3 char irrelevant for part 2
                    i += 3
            i += 1
    return ans


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
