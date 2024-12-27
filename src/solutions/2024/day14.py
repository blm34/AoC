import aoc_helper

DAY = 14
YEAR = 2024

R = 103
C = 101

def parse_input(input_text):
    input_text = input_text.replace("p=", "").replace("v=", "")
    robots = []
    for line in input_text.splitlines():
        pos, vel = line.split()
        posx, posy = pos.split(",")
        velx, vely = vel.split(",")
        robots.append([int(posx), int(posy), int(velx), int(vely)])

    return robots


@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    robots = parse_input(input_text)

    # Part 1
    quads = [0, 0, 0, 0]

    for x, y, vx, vy in robots:
        x = (x + vx * 100) % C
        if x == C // 2:
            continue
        y = (y + vy * 100) % R
        if y == R // 2:
            continue
        quad_x = int(x > C // 2)
        quad_y = int(y > R // 2)
        quads[quad_x + 2 * quad_y] += 1

    p1 = quads[0] * quads[1] * quads[2] * quads[3]

    # Part 2

    x_vars = []
    y_vars = []

    n = len(robots)

    for time in range(max(R, C)):
        sx = 0
        sxx = 0
        sy = 0
        syy = 0

        for i, robot in enumerate(robots):
            sx += robot[0]
            sxx += robot[0] ** 2
            sy += robot[1]
            syy += robot[1] ** 2

            robots[i][0] = (robots[i][0] + robot[2]) % C
            robots[i][1] = (robots[i][1] + robot[3]) % R

        x_vars.append((sxx / n) - (sx / n) ** 2)
        y_vars.append((syy / n) - (sy / n) ** 2)

    x_offset = x_vars.index(min(x_vars))
    y_offset = y_vars.index(min(y_vars))

    p2 = (x_offset * R * (pow(R, C - 2, C)) +
           y_offset * C * (pow(C, R - 2, R))) % (R * C) # By Chinese remainder theorem

    return p1, p2


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
