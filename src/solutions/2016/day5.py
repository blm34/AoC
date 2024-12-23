import hashlib
import itertools

import aoc_helper

DAY = 5
YEAR = 2016


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    p1 = ""
    p2 = [None for _ in range(8)]
    hash_start = hashlib.md5(str(input_text).encode('utf-8'))
    for num in itertools.count():
        updated_hash = hash_start.copy()
        updated_hash.update(str(num).encode('utf-8'))
        hash_bytes = updated_hash.digest()
        if (not hash_bytes[0]) and (not hash_bytes[1]) and (not (hash_bytes[2] >> 4)):
            if len(p1) < 8:
                p1 += hex(hash_bytes[2])[2]
            loc = hash_bytes[2] & 15
            if loc < 8 and p2[loc] is None:
                val = hash_bytes[3] >> 4
                p2[loc] = hex(val)[2]
                if all(digit is not None for digit in p2):
                    return p1, ''.join(p2)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
