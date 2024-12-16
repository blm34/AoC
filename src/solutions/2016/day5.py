import hashlib
import itertools

import aoc_helper

DAY = 5
YEAR = 2016


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    password = ""
    hash_start = hashlib.md5(str(input_text).encode('utf-8'))
    for num in itertools.count():
        updated_hash = hash_start.copy()
        updated_hash.update(str(num).encode('utf-8'))
        hash_bytes = updated_hash.digest()
        if (not hash_bytes[0]) and (not hash_bytes[1]) and (not (hash_bytes[2] >> 4)):
            password += hex(hash_bytes[2])[2]
            if len(password) == 8:
                return password


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    password = [None for _ in range(8)]
    hash_start = hashlib.md5(str(input_text).encode('utf-8'))
    for num in itertools.count():
        updated_hash = hash_start.copy()
        updated_hash.update(str(num).encode('utf-8'))
        hash_bytes = updated_hash.digest()
        if (not hash_bytes[0]) and (not hash_bytes[1]) and (not (hash_bytes[2] >> 4)):
            loc = hash_bytes[2] & 15
            val = hash_bytes[3] >> 4
            if loc < 8 and password[loc] is None:
                password[loc] = str(val)
                if all(digit is not None for digit in password):
                    return ''.join(password)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
