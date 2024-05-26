import aoc_helper
import sys

p1 = 0
p2 = 0

text = aoc_helper.read_input(sys.argv[1])
L = text.split('\n')
G = [list(line) for line in L]
R = len(G)
C = len(G[0])

def nice(string):
    # Constants
    bad_pair = {'ab', 'cd', 'pq', 'xy'}
    vowels = 'aeiou'
    # Checks
    vowel_count = int(string[-1] in vowels)
    double_letter = False
    # Loop through string and check conditions
    for i in range(len(string)-1):
        if string[i:i+2] in bad_pair:
            return False
        if string[i] == string[i+1]:
            double_letter = True
        if string[i] in vowels:
            vowel_count += 1
    return vowel_count >= 3 and double_letter

def nice2(string):
    # Check for a pair that appears twice
    two_pair = False
    for i in range(len(string)-3):
        for j in range(i+2, len(string)-1):
            if string[i] == string[j] and string[i+1] == string[j+1]:
                two_pair = True
                break
        if two_pair:
            break
    # Check for a repeated letter with a gap of 1
    rep_let = False
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            rep_let = True
            break
    return rep_let and two_pair

for string in L:
    p1 += nice(string)
    p2 += nice2(string)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

assert p1 == 238
assert p2 == 69
