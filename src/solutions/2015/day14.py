import aoc_helper

DAY = 14
YEAR = 2015

def parse_input(input_text):
    L = input_text.split('\n')

    reindeer = list()
    for line in L:
        _, _, _, speed, _, _, time, _, _, _, _, _, _, rest, _ = line.split()
        reindeer.append((int(speed), int(time), int(rest)))
    return reindeer

def distance(reindeer, time):
    speed, fly_time, rest_time = reindeer
    dist_per_cycle = fly_time * speed
    complete_cycles = time // (fly_time + rest_time)
    final_cycle_time = time % (fly_time + rest_time)

    d = dist_per_cycle * complete_cycles
    if final_cycle_time >= fly_time:
        d += dist_per_cycle
    else:
        d += final_cycle_time * speed

    return d
    
def p1(input_text):
    reindeers = parse_input(input_text)
    return max(distance(reindeer, 2503) for reindeer in reindeers)

def p2(input_text):
    reindeers = parse_input(input_text)
    points = [0] * len(reindeers)
    for t in range(1, 2503+1):
        dists = [distance(reindeer, t) for reindeer in reindeers]
        winner = dists.index(max(dists))
        points[winner] += 1

    return max(points)

@aoc_helper.communicator(YEAR, DAY)
def solve(input_text):
    return p1(input_text), p2(input_text)


if __name__ == "__main__":
    result = solve()
    aoc_helper.print_results(result, YEAR, DAY)
