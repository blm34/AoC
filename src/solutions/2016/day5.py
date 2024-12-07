import hashlib

import aoc_helper

DAY = 5
YEAR = 2016


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    password = ""
    num = -1
    while len(password) < 8:
        num += 1
        hash = hashlib.md5(f"{input_text}{num}".encode()).hexdigest()
        if hash[:5] == "00000":
            password += hash[5]
    return password


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    password: list[None | str] = [None for _ in range(8)]
    num = -1
    while any(digit is None for digit in password):
        num += 1
        hash = hashlib.md5(f"{input_text}{num}".encode()).hexdigest()
        if hash[:5] == "00000":
            loc = int(hash[5], 16)
            val = hash[6]
            if loc < 8 and password[loc] is None:
                password[loc] = val
    return ''.join(password)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
