from importlib import import_module, reload
from datetime import datetime

from aoc_helper import print_results, AocResult


def calculate_day(year: int, day: int, args) -> AocResult:
    try:
        solver = import_module(f"solutions.{year}.day{day}")
        if args.repeats > 1:
            reload(solver)  # Necessary to clear functools.cache
    except ModuleNotFoundError:
        return AocResult(None, False, None, False, 0)

    try:
        result = solver.solve()
    except Exception:
        result = AocResult(None, False, None, False, 0)
    else:
        if args.verbose:
            print_results(result, year, day)

    return result


def run_one_day(args):
    if not args.quiet:
        message = f"Running {args.year[0]} day {args.day}"
        if args.repeats > 1:
            message += f" {args.repeats} times"
        message += "."
        print(message)

    results = list()

    for repeat in range(args.repeats):
        if not args.quiet and args.repeats > 1:
            line = "\n" if args.verbose else ""
            line += f"{datetime.now().strftime('%H:%M:%S')} Repeat {repeat+1}/{args.repeats} ({(repeat+1)/args.repeats*100:.0f}%)"
            print(line)
        result = calculate_day(args.year[0], args.day, args)
        results.append(result)

    return {args.year[0]: {args.day: results}}


def run_years(args):
    if not args.quiet:
        years_str = ', '.join([str(year) for year in args.year])
        message = f"Running years {years_str}"
        if args.repeats > 1:
            message += f" {args.repeats} times"
        message += "."
        print(message)

    results = {year: {day: []
                      for day in range(1, 26)}
               for year in args.year}

    for repeat in range(args.repeats):
        if not args.quiet and args.repeats > 1:
            line = "\n" if args.verbose else ""
            line += f"{datetime.now().strftime('%H:%M:%S')} Repeat {repeat + 1}/{args.repeats} ({(repeat + 1) / args.repeats * 100:.0f}%)"
            print(line)
        for year in args.year:
            for day in range(1, 26):
                result = calculate_day(year, day, args)
                results[year][day].append(result)

    return results
