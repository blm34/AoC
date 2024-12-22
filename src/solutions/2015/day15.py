import aoc_helper

DAY = 15
YEAR = 2015


def parse_input(input_text):
    L = input_text.split('\n')
    properties = []
    for line in L:
        line = line.split(': ')[1]
        properties.append([])
        for p in line.split(', '):
            properties[-1].append(int(p.split()[1]))
    return properties


def score(properties, split):
    """Calculate the score for a recipe"""
    ans = 1
    for p in range(4):
        val = 0
        for i in range(4):
           val += properties[i][p] * split[i] 
        ans *= max(val, 0)
    return ans


def calories(properties, split):
    """Calculate the number of calories for a recipe"""
    ans = 0
    for i in range(4):
        ans += properties[i][4] * split[i]
    return ans


def p1(input_text):
    properties = parse_input(input_text)
    ans = 0
    for i in range(101):
        for j in range(101):
            if i+j > 100:
                break
            for k in range(101):
                if i+j+k > 100:
                    break
                l = 100 - (i+j+k)
                ans = max(ans, score(properties, (i,j,k,l)))
    return ans


def p2(input_text):
    properties = parse_input(input_text)
    ans = 0
    for i in range(101):
        for j in range(101):
            if i+j > 100:
                break
            for k in range(101):
                if i+j+k > 100:
                    break
                l = 100 - (i+j+k)
                if calories(properties, (i,j,k,l)) == 500:
                    ans = max(ans, score(properties, (i,j,k,l)))
    return ans


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
