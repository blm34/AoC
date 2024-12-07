import re
from collections import defaultdict

import aoc_helper

DAY = 4
YEAR = 2016


def parse_input(input_text):
    pattern = r"^(\w+(-\w+)*)-(\d+)\[(\w{5})\]$"
    rooms = re.findall(pattern, input_text, re.MULTILINE)
    rooms = ((room[0], int(room[2]), room[3]) for room in rooms)
    return rooms


def is_real(room):
    freq = defaultdict(int)
    for char in room[0]:
        if char == '-':
            continue
        freq[char] += 1
    freq = [(-val, key) for key, val in freq.items()]
    freq.sort()
    check_sum = ''.join(vk[1] for vk in freq[:5])
    return check_sum == room[2]


def decrypt_name(encrypted, shift):
    decrypted = ""
    for char in encrypted:
        if char == "-":
            decrypted += " "
        else:
            decrypted += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
    return decrypted


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    rooms = parse_input(input_text)
    total = 0
    for room in rooms:
        if is_real(room):
            total += room[1]
    return total


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    rooms = parse_input(input_text)
    for room in rooms:
        decrypted = decrypt_name(room[0], room[1])
        if decrypted == "northpole object storage":
            return room[1]


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
