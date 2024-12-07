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


@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    ips = parse_input(input_text)
    count = 0
    for ip in ips:
        count += supports_tls(ip)
    return count


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    ips = parse_input(input_text)
    count = 0
    for ip in ips:
        count += supports_ssl(ip)
    return count


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
