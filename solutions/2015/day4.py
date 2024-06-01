import aoc_helper
import sys
from hashlib import md5

p1 = 0
p2 = 0

text = aoc_helper.read_input(sys.argv[1])

num = 0
while True:
    num += 1
    string = text + str(num)
    md5_hash = md5(string.encode('utf-8')).hexdigest()
    if not p1 and md5_hash[:5] == '00000':
        p1 = num
    if md5_hash[:6] == '000000':
        p2 = num
        break

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 254575
assert p2 == 1038736
