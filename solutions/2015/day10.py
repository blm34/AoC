import aoc_helper

DAY = 10
YEAR = 2015


def las(num):
    """Return the next number in the look-and-see sequence"""
    res = ''
    cur_char = num[0]
    char_count = 0
    for char in num:
        if char == cur_char:
            char_count += 1
        else:
            res += str(char_count) + cur_char
            char_count = 1
            cur_char = char
    res += str(char_count) + cur_char
    return res


def repeat(num, times):
    for _ in range(times):
        num = las(num)
    return num


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    return len(repeat(input_text, 40))


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    return len(repeat(input_text, 50))


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
