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
        output += "Run time: "
        if time > 1:
            output += f"{time:.1f} s"
        elif time > 1e-3:
            output += f"{1e3 * time:.3f} ms"
        else:
            output += f"{1e6 * time:.0f} µs"

    file_stream = sys.stdout if result.correct else sys.stderr
    print(output, file=file_stream)
