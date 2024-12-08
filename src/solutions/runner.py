from datetime import datetime
from pathlib import Path
import importlib.util
import sys

from aoc_helper import print_results, AocResult, format_time


def get_module_file_path(year, day):
    fp = Path(__file__)
    while fp.name != 'AoC':
        fp = fp.parent
    return fp / "src" / "solutions" / str(year) / f"day{day}.py"


def run_part(year: int, day: int, part: int) -> AocResult:
    filepath = get_module_file_path(year, day)
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

    print_results(result, year=year, day=day, part=part)
    return result


def run_year(year: int):
    results = {year: {day: dict()
                      for day in range(1, 26)}}

    for day in range(1, 26):
        p1_res = run_part(year, day, 1)
        results[year][day][1] = p1_res

        p2_res = run_part(year, day, 2)
        results[year][day][2] = p2_res

    stars = sum(result.correct
                for day in results[year].values()
                for result in day.values())
    stars += 1 if stars == 49 else 0

    total_run_time = sum(result.time
                         for day in results[year].values()
                         for result in day.values()
                         if result.answer is not None)

    avg_runtime = total_run_time / stars if stars != 0 else 0

    print(f"\nEarned {stars}* out of 50*")
    print(f"\nTotal runtime: {format_time(total_run_time)}\nAverage runtime: {format_time(avg_runtime)}")

    return results


def run_all():
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day

    results = {year: {day: dict()
                      for day in range(1, 26)}
               for year in range(2015, current_year + 1)}

    for year in range(2015, current_year + 1):
        for day in range(1, 26):
            p1_res = run_part(year, day, 1)
            results[year][day][1] = p1_res

            p2_res = run_part(year, day, 2)
            results[year][day][2] = p2_res

    stars = sum(result.correct
                for year in results.values()
                for day in year.values()
                for result in day.values())
    stars += 1 if stars == 49 else 0

    max_stars = (current_year - 2015) * 50
    if current_month == 12:
        max_stars += 2 * min(current_day, 25)

    total_run_time = sum(result.time
                         for year in results.values()
                         for day in year.values()
                         for result in day.values()
                         if result.answer is not None)

    avg_runtime = total_run_time / stars if stars != 0 else 0

    print(f"\nEarned {stars}* out of {max_stars}* ({100 * stars / max_stars:.1f}%)")
    print(f"\nTotal runtime: {format_time(total_run_time)}\nAverage runtime: {format_time(avg_runtime)}")

    return results


if __name__ == "__main__":
    run_year(2024)
    # run_all()
