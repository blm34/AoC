import hashlib
import itertools

import aoc_helper

DAY = 5
YEAR = 2016


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


def p2(input_text):
    password = [None for _ in range(8)]
    hash_start = hashlib.md5(str(input_text).encode('utf-8'))
    for num in itertools.count():
        updated_hash = hash_start.copy()
        updated_hash.update(str(num).encode('utf-8'))
        hash_bytes = updated_hash.digest()
        if (not hash_bytes[0]) and (not hash_bytes[1]) and (not (hash_bytes[2] >> 4)):
            loc = hash_bytes[2] & 15
            if loc < 8 and password[loc] is None:
                val = hash_bytes[3] >> 4
                password[loc] = hex(val)[2]
                if all(digit is not None for digit in password):
                    return ''.join(password)


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
