from hashlib import md5
import itertools

import aoc_helper

DAY = 4
YEAR = 2015


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    hash_start = md5(input_text.encode('utf-8'))
    for num in itertools.count():
        updated_hash = hash_start.copy()
        updated_hash.update(str(num).encode('utf-8'))
        hash_bytes = updated_hash.digest()
        if (not hash_bytes[0]) and (not hash_bytes[1]) and (not (hash_bytes[2] >> 4)):
            return num


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    hash_start = md5(input_text.encode('utf-8'))
    for num in itertools.count():
        updated_hash = hash_start.copy()
        updated_hash.update(str(num).encode('utf-8'))
        hash_bytes = updated_hash.digest()
        if (not hash_bytes[0]) and (not hash_bytes[1]) and (not hash_bytes[2]):
            return num


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
