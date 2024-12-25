import sys


def print_results(result: 'AocResult', year: int, day: int):
    if result.p1_ans is None and result.p2_ans is None:
        return

    p1_ans = result.p1_ans or ""
    p2_ans = result.p2_ans or ""

    output = f"{year} {day:02d} Part 1: {p1_ans:<20}"
    output += " (/) " if result.p1_correct else " (X) "
    output += f"Run time: {format_time(result.time)}"

    if day != 25:
        output += f"\n        Part 2: {p2_ans:<20}"
        output += " (/) " if result.p2_correct else " (X) "

    print(output)


def format_time(time: float) -> str:
    if time > 10:
        output = f"{time:.0f} s"
    elif time > 3:
        output = f"{time:.3f} s"
    elif time > 1:
        output = f"{1e3 * time:.0f} ms"
    elif time > 1e-3:
        output = f"{1e3 * time:.1f} ms"
    elif time > 1e-6:
        output = f"{1e6 * time:.0f} us"
    else:
        output = f"{1e9 * time:.0f} ns"
    return output
