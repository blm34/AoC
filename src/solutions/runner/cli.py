import argparse
from datetime import datetime


def pos_int(num):
    try:
        num = int(num)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{num}' not a valid integer")

    if num <= 0:
        raise argparse.ArgumentTypeError(f"Repeats must be at least 1 ({num} not valid)")

    return num


def year_type(year):
    try:
        year = int(year)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Year must be an integer. '{year}' not valid.")

    if year < 2015:
        raise argparse.ArgumentTypeError(f"Year must be at least 2015. {year} is too early.")

    latest_year = datetime.now().year
    if datetime.now().month < 12:
        latest_year -= 1

    if year > latest_year:
        raise argparse.ArgumentTypeError(f"AoC year {year} has not yet started.")

    return year

def day_type(day):
    try:
        day = int(day)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Day must be an integer. '{day}' not valid.")

def parse_args():
    parser = argparse.ArgumentParser(prog="aoc",
                                     description="Run the solutions to the Advent of Code problems. By default run "
                                                 "all problems from all years. Optionally specify year(s) to run or a "
                                                 "day from a year.")

    latest_year = datetime.now().year
    if datetime.now().month < 12:
        latest_year -= 1
    parser.add_argument("-y", "--year",
                        nargs="*",
                        default=list(range(2015, latest_year+1)),
                        type=year_type,
                        help="The year (or years) to run.")

    parser.add_argument("-d", "--day",
                        nargs="?",
                        default=0,
                        type=int,
                        help="The day to run.")

    parser.add_argument("-r", "--repeats",
                        nargs="?",
                        default=1,
                        type=pos_int,
                        help="The number of times to run the solutions for calculating run time.")

    parser.add_argument("-s", "--stars",
                        action="store_true",
                        default=False,
                        help="Show stats on how many stars have been achieved.")

    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        default=False,
                        help="Show individual solutions and solve times as they are run.")

    parser.add_argument("-q", "--quiet",
                        action="store_true",
                        default=False,
                        help="Turn off all unrequested outputs.")

    args = parser.parse_args()
    args.year = sorted(set(args.year))  # Remove duplicates and sort
    validate_args(args)

    return args


def validate_args(args):
    # Cannot be verbose and quiet
    if args.verbose and args.quiet:
        raise argparse.ArgumentTypeError("Cannot run with 'verbose' and 'quiet'.")

    # Year must be specified if day is specified
    if args.day != 0 and len(args.year) > 1:
        raise argparse.ArgumentTypeError(f"Day {args.day} specified, but year not specified.")

    # Cannot show stars stats for a single day
    if args.day != 0 and args.stars:
        raise argparse.ArgumentTypeError("Cannot show star related stats if only running one day")
