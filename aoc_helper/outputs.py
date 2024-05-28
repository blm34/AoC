def print_results(p1, p2, time):
    print(f'Part 1: {p1}\nPart 2: {p2}')
    
    if time < 1:
        print(f"Run time: {1000 * time:.3f} ms")
    else:
        print(f"Run time: {time:.1f} s")
