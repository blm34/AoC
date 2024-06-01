def print_results(result: 'AocResult', year: int=None, day: int=None, part: int=None):
    output = ""
    if year is not None:
        output += f"{year} "
    if day is not None:
        output += f"{day:02d} "
    if part is not None:
        output += f"Part {part} "
    if output != "":
        output = output.strip() + ": "
    output += f"{result.answer:<10}"
    output += " ✅ " if result.correct else " ❌ "

    time = result.time
    if time is not None:
        output += "Run time: "
        output += f"{1000 * time:.3f} ms" if time < 1 else f"{time:.1f} s"

    print(output)
