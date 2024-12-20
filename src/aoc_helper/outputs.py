import sys


def print_results(result: 'AocResult', year: int=None, day: int=None, part: int=None):
    if result.answer is None:
        return

    output = ""
    if year is not None:
        output += f"{year} "
    if day is not None:
        output += f"{day:02d} "
    if part is not None:
        output += f"Part {part} "
    if output != "":
        output = output.strip() + ": "
    output += f"{result.answer:<20}"
    output += " ✅ " if result.correct else " ❌ "

    time = result.time
    if time is not None:
        output += f"Run time: {format_time(time)}"

    file_stream = sys.stdout if result.correct else sys.stderr
    print(output, file=file_stream)


def format_time(time: float) -> str:
    if time > 3:
        output = f"{time:.0f} s"
    elif time > 1:
        output = f"{1e3 * time:.0f} ms"
    elif time > 1e-3:
        output = f"{1e3 * time:.1f} ms"
    elif time > 1e-6:
        output = f"{1e6 * time:.0f} µs"
    else:
        output = f"{1e9 * time:.0f} ns"
    return output
