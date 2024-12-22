import re

import aoc_helper

DAY = 8
YEAR = 2016


def parse_input(input_text):
    L = input_text.split('\n')
    return L


def rect(instruction, scrn):
    match = re.findall(r"rect (\d+)x(\d+)", instruction)[0]
    width, height = map(int, match)
    for r in range(height):
        for c in range(width):
            scrn[r][c] = True
    return scrn


def rotate_row(instruction, scrn):
    match = re.findall(r"rotate row y=(\d+) by (\d+)", instruction)[0]
    row, shift = map(int, match)
    row_copy = [scrn[row][c] for c in range(50)]
    for c in range(50):
        scrn[row][(c+shift)%50] = row_copy[c]
    return scrn


def rotate_col(instruction, scrn):
    match = re.findall(r"rotate column x=(\d+) by (\d+)", instruction)[0]
    col, shift = map(int, match)
    col_copy = [scrn[r][col] for r in range(6)]
    for r in range(6):
        scrn[(r+shift)%6][col] = col_copy[r]
    return scrn


def render_screen(instructions):
    scrn = [[False for x in range(50)] for y in range(6)]
    for instruction in instructions:
        if instruction.startswith('rect '):
            scrn = rect(instruction, scrn)
        elif instruction.startswith('rotate row '):
            scrn = rotate_row(instruction, scrn)
        elif instruction.startswith('rotate column '):
            scrn = rotate_col(instruction, scrn)
    return scrn


def p1(input_text):
    instructions = parse_input(input_text)
    screen = render_screen(instructions)

    total = 0
    for row in screen:
        for pix in row:
            total += pix
    return total


def p2(input_text):
    SHOW_PLOTS = False
    instructions = parse_input(input_text)
    screen = render_screen(instructions)

    for r in range(6):
        screen[r] = ['#' if pix else ' ' for pix in screen[r]]
        if SHOW_PLOTS:
            print(''.join(screen[r]))

    #  Be aware some characters maps are unknown - complete if found/needed
    ocr_map = {
        " ##  #  # #  # #### #  # #  # ": "A",
        "###  #  # ###  #  # #  # ###  ": "B",
        " ##  #  # #    #    #  #  ##  ": "C",
        "": "D",
        "#### #    ###  #    #    #### ": "E",
        "#### #    ###  #    #    #    ": "F",
        " ##  #  # #    # ## #  #  ### ": "G",
        "#  # #  # #### #  # #  # #  # ": "H",
        " ###   #    #    #    #   ### ": "I",
        "  ##    #    #    # #  #  ##  ": "J",
        "#  # # #  ##   # #  # #  #  # ": "K",
        "#    #    #    #    #    #### ": "L",
        "": "M",
        "": "N",
        " ##  #  # #  # #  # #  #  ##  ": "O",
        "###  #  # #  # ###  #    #    ": "P",
        "": "Q",
        "###  #  # #  # ###  # #  #  # ": "R",
        " ### #    #     ##     # ###  ": "S",
        "": "T",
        "#  # #  # #  # #  # #  #  ##  ": "U",
        "": "V",
        "": "W",
        "": "X",
        "#   ##   # # #   #    #    #  ": "Y",
        "####    #   #   #   #    #### ": "Z",
    }

    code = ""
    for letter in range(10):
        key = ""
        for row in range(6):
            for col in range(letter*5, (letter+1)*5):
                key += screen[row][col]
        code += ocr_map.get(key, "_")

    if "_" in code:
        print("WARNING OCR failed: print resulting screen and update `ocr_map`")
        return
    return code



@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
