import aoc_helper

DAY = 11
YEAR = 2015


def valid(password):
    # Find increasing straight
    straight = False
    for i in range(6):
        if password[i] + 2 == password[i + 1] + 1 == password[i + 2]:
            straight = True
            break
    if not straight:
        return False

    # Check for non-permitted letters
    if 9 in password or 12 in password or 15 in password:
        return False

    # Check for double letters
    doub_let_ind = []
    for i in range(7):
        if password[i] == password[i + 1]:
            doub_let_ind.append(i)
    if len(doub_let_ind) >= 2 and doub_let_ind[-1] - doub_let_ind[0] >= 2:
        return True
    return False


def pass_to_list(password):
    """Turn a password string into a list of numbers for each letter (1-26)"""
    return [ord(char) - 96 for char in password]


def list_to_pass(l):
    """Turn a list of numbers back into a password"""
    return ''.join(chr(num + 96) for num in l)


def increment(password):
    """Find the next password that doesn't contain an invalid letter"""
    i = 7
    while True:
        password[i] += 1
        # If made it an invalid letter, jump to next valid
        if password[i] in (9, 12, 15):
            password[i] += 1
            for j in range(i + 1, 8):
                password[j] = 1
        # If overflow, increase next most significant digit
        if password[i] == 27:
            password[i] = 1
            i -= 1
        else:
            return password


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    password = pass_to_list(input_text)
    while not valid(password):
        password = increment(password)
    p1 = list_to_pass(password)
    password = increment(password)
    while not valid(password):
        password = increment(password)
    p2 = list_to_pass(password)
    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
