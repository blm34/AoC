import aoc_helper


DAY = 5
YEAR = 2015


def parse_input(input_text):
    L = input_text.split("\n")
    return L


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


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    strings = parse_input(input_text)
    ans = 0
    for string in strings:
        ans += nice(string)
    return ans


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    strings = parse_input(input_text)
    ans = 0
    for string in strings:
        ans += nice2(string)
    return ans


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
