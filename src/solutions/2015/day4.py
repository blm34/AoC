from hashlib import md5

import aoc_helper

DAY = 4
YEAR = 2015


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    num = 0
    while True:
        num += 1
        string = input_text + str(num)
        md5_hash = md5(string.encode('utf-8')).hexdigest()
        if md5_hash[:5] == '00000':
            return num


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    num = 0
    while True:
        num += 1
        string = input_text + str(num)
        md5_hash = md5(string.encode('utf-8')).hexdigest()
        if md5_hash[:6] == '000000':
            return num


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
