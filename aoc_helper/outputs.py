def print_results(p1, p2, time=None):
    output = f"Part 1: {p1[0]:<10}"
    output += "✅" if p1[1] else "❌"
    output += "\n"

    output += f"Part 2: {p2[0]:<10}"
    output += "✅" if p2[1] else "❌"
    output += "\n"

    if time is not None:
        output += "\nRun time: "
        output += f"{1000 * time:.3f} ms" if time < 1 else f"{time:.1f} s"

    print(output)
