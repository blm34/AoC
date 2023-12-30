import time
START_TIME = time.time()

import Modules
import sys

text = Modules.readInput(sys.argv[1]) 

def count_nums(text):
    '''Sum the total of all the nums in a string of text'''
    total = 0
    num = 0
    # Loop through text
    for i in range(len(text)):
        # Check if current char is a digit
        if text[i].isdigit():
            # If it is the first digit check the prev char for negative
            if num == 0:
                neg = False
                if text[i-1] == '-':
                    neg = True
            # Add the new digit to the number
            num = num*10 + int(text[i])
        # If current char not a digit but previous was
        elif num:
            # Add number to total
            if neg:
                num *= -1
            total += num
            # Reset current number to 0
            num = 0
    return total

def remove_red(text):
    '''Remove all objects with a property red'''
    t = list(text)
    i = 0
    while i < len(t)-6:
        # Found a red
        if ''.join(t[i:i+6]) == ':\"red\"':
            # Move back to find start of object
            while t[i] != '{':
                i -= 1
            # Delete entirety of this object by counting the number of { and }
            del t[i]
            count = 1
            while count != 0:
                if t[i] == '{':
                    count += 1
                elif t[i] == '}':
                    count -= 1
                del t[i]
            i -= 1
        # Increment i for the next character
        i += 1
    return ''.join(t)

p1 = count_nums(text)
p2_text = remove_red(text)
p2 = count_nums(p2_text)

END_TIME = time.time()
RUN_TIME = round(1000*(END_TIME - START_TIME), 3)
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
print(f'Run time: {RUN_TIME} ms')

assert p1 == 119433
assert p2 == 68466
