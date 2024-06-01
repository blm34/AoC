def print_results(result, time=None, year=None, day=None, part=None):
    output = ""
    if year is not None:
        output += f"{year} "
    if day is not None:
        output += f"{day:02d} "
    if part is not None:
        output += f"Part {part} "
    if output != "":
        output = output.strip() + ": "
    output += f"{result[0]:<10}"
    output += " ✅ " if result[1] else " ❌ "

    if time is not None:
        output += "Run time: "
        output += f"{1000 * time:.3f} ms" if time < 1 else f"{time:.1f} s"

    print(output)
