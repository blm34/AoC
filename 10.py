import time
START_TIME = time.time()

import Modules
import sys

text = Modules.readInput(sys.argv[1]) 

def las(num):
    '''Return the next number in the look-and-see sequence'''
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

num = text
for _ in range(40):
    num = las(num)
p1 = len(num)

for _ in range(10):
    num = las(num)
p2 = len(num)

END_TIME = time.time()
RUN_TIME = int(1000 * round(END_TIME - START_TIME, 3))
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')

assert p1 == 492982
assert p2 == 6989950
