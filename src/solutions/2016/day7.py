import aoc_helper

DAY = 7
YEAR = 2016


def parse_input(input_text):
    L = input_text.split('\n')
    return L


def supports_tls(ip):
    valid = None
    inside = False
    for i in range(len(ip)-3):
        if ip[i] == '[':
            inside = True
        elif ip[i] == ']':
            inside = False
        elif ip[i] == ip[i+3] != ip[i+1] == ip[i+2]:
            if inside:
                valid = False
            if not inside and valid is None:
                valid = True
    return bool(valid)


def supports_ssl(ip):
    abas = [set(), set()]
    inside = False
    for i in range(len(ip)-2):
        if ip[i] == '[':
            inside = True
        elif ip[i] == ']':
            inside = False
        elif ip[i] == ip[i+2] != ip[i+1]:
            abas[int(inside)].add(ip[i:i+2])
    for aba in abas[0]:
        bab = aba[::-1]
        if bab in abas[1]:
            return True
    return False


def p1(input_text):
    ips = parse_input(input_text)
    count = 0
    for ip in ips:
        count += supports_tls(ip)
    return count


def p2(input_text):
    ips = parse_input(input_text)
    count = 0
    for ip in ips:
        count += supports_ssl(ip)
    return count


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
