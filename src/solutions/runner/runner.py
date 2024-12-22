from importlib import import_module, reload
from datetime import datetime

from aoc_helper import print_results, AocResult


def calculate_day(year: int, day: int, args) -> tuple[AocResult, AocResult]:
    try:
        solver = import_module(f"solutions.{year}.day{day}")
        if args.repeats > 1:
            reload(solver)  # Necessary to clear functools.cache
    except ModuleNotFoundError:
        return AocResult(None, False, 0), AocResult(None, False, 0)

    try:
        p1 = solver.p1()
    except Exception:
        p1 = AocResult(None, False, 0)
    else:
        if args.verbose:
            print_results(p1, year, day, 1)

    try:
        p2 = solver.p2()
    except Exception:
        p2 = AocResult(None, False, 0)
    else:
        if args.verbose:
            print_results(p2, year, day, 2)

    return p1, p2


def run_one_day(args):
    if not args.quiet:
        message = f"Running {args.year[0]} day {args.day}"
        if args.repeats > 1:
            message += f" {args.repeats} times"
        message += "."
        print(message)

    p1 = list()
    p2 = list()

    for repeat in range(args.repeats):
        if not args.quiet and args.repeats > 1:
            line = "\n" if args.verbose else ""
            line += f"{datetime.now().strftime('%H:%M:%S')} Repeat {repeat+1}/{args.repeats} ({(repeat+1)/args.repeats*100:.0f}%)"
            print(line)
        result = calculate_day(args.year[0], args.day, args)
        p1.append(result[0])
        p2.append(result[1])

    return {args.year[0]: {args.day: [p1, p2]}}


def run_years(args):
    if not args.quiet:
        years_str = ', '.join([str(year) for year in args.year])
        message = f"Running years {years_str}"
        if args.repeats > 1:
            message += f" {args.repeats} times"
        message += "."
        print(message)

    results = {year: {day: [[], []]
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
                results[year][day][0].append(result[0])
                results[year][day][1].append(result[1])

    return results
