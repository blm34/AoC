from .cli import parse_args
from .runner import run_one_day, run_years
from .stats import show_stars, show_times


def main():
    args = parse_args()

    if args.day != 0:  # Run a single day
        results = run_one_day(args)
    else:  # Run whole years
        results = run_years(args)

    if args.repeats > 1 or args.time:
        show_times(results, args)

    if args.stars:
        show_stars(results, args)


if __name__ == "__main__":
    main()
