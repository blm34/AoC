from datetime import datetime
from pathlib import Path
import importlib.util
import sys

from aoc_helper import print_results, AocResult, format_time


def get_file_path(year, day):
    fp = Path(__file__)
    while fp.name != 'AoC':
        fp = fp.parent
    return fp / "src" / "solutions" / str(year) / f"day{day}.py"


def run_one(year: int, day: int, part: int) -> AocResult:
    filepath = get_file_path(year, day)
    if not filepath.is_file():
        return AocResult(None, False, 0)

    # Import the file
    spec = importlib.util.spec_from_file_location(f"day{day}", filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"day{day}"] = module
    spec.loader.exec_module(module)

    if part == 1:
        try:
            result = module.p1()
        except:
            result = AocResult(None, False, 0)
    elif part == 2:
        try:
            result = module.p2()
        except:
            result = AocResult(None, False, 0)
    else:
        raise ValueError(f"{part} is not a valid part")

    return result


def run_all():
    # ToDo Add filter for year
    stars = 0
    total_runtime = 0

    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day

    for year in range(2015, current_year + 1):
        for day in range(1, 26):
            p1_res = run_one(year, day, 1)

            print_results(p1_res, year=year, day=day, part=1)
            stars += 1 if p1_res.correct else 0
            stars += 1 if p1_res.correct and day == 25 else 0
            total_runtime += p1_res.time

            p2_res = run_one(year, day, 2)

            print_results(p2_res, year=year, day=day, part=2)
            stars += 1 if p2_res.correct else 0
            total_runtime += p2_res.time

    max_stars = (current_year - 2015) * 50
    if current_month == 12:
        max_stars += 2 * min(current_day, 25)

    avg_runtime = total_runtime / stars if stars != 0 else 0

    print(f"\nEarned {stars}* out of {max_stars}* ({100 * stars / max_stars:.1f}%)")
    print(f"\nTotal runtime: {format_time(total_runtime)}\nAverage runtime: {format_time(avg_runtime)}")


if __name__ == "__main__":
    run_all()
