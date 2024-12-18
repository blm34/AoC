from datetime import datetime

from aoc_helper import format_time


def show_stars(results, args):
    stars = {year: 0
             for year in args.year}
    print(f"\n{'DAY':>47}")
    print(" " * 10 + ' '.join([f"{day:02d}" for day in range(1, 26)]))
    for i, year in enumerate(args.year):
        if i == len(args.year) // 2:
            line = "YEAR "
        else:
            line = "     "
        line += str(year)
        for day in range(1, 26):
            line += " "
            if results[year][day][0][0].correct:
                line += "*"
                stars[year] += 1
            else:
                line += " "
            if results[year][day][1][0].correct or day == 25 and results[year][day][0][0].correct:
                line += "*"
                stars[year] += 1
            else:
                line += " "
        line += f"  {stars[year]:>2} stars"
        print(line)
    print()

    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day

    available_stars = 0
    for year in args.year:
        if year < current_year:
            available_stars += 50
        elif year == current_year:
            if current_month == 12:
                available_stars += min(50, current_day * 2)
        else:
            assert False

    achieved_stars = sum(stars.values())
    print(f"     Earned {achieved_stars}* out of {available_stars}* ({achieved_stars / available_stars * 100:.1f}%)")


def show_times(results, args):
    avg_times = dict()
    min_times = dict()

    for year in results:
        avg_times[year] = dict()
        min_times[year] = dict()
        for day in results[year]:
            avg_times[year][day] = dict()
            min_times[year][day] = dict()
            for part in (1, 2):
                if results[year][day][part-1][0].correct is True:
                    avg_time = sum(result.time for result in results[year][day][part-1]) / args.repeats
                    min_time = min(result.time for result in results[year][day][part-1])
                    avg_times[year][day][part] = avg_time
                    min_times[year][day][part] = min_time

    total_avg_time = 0
    total_min_time = 0
    parts_solved = 0
    print("\nYEAR DAY PART     AVG TIME     MIN TIME")
    for year in args.year:
        line = f"{year} "
        for day in sorted(avg_times[year].keys()):
            if len(line) != 5:
                line = " " * 5
            line += f"{day:2d}   "
            for part in sorted(avg_times[year][day].keys()):
                parts_solved += 1
                line += f" {part}"
                line = f"{line:>12} "
                avg_time = avg_times[year][day][part]
                total_avg_time += avg_time
                line += f"{format_time(avg_time):>13}"

                min_time = min_times[year][day][part]
                total_min_time += min_time
                line += f"{format_time(min_time):>13}"

                print(line)
                line = ""
    print(f"\n        TOTAL{format_time(total_avg_time):>13}{format_time(total_min_time):>13}")
    print(f"         AVG {format_time(total_avg_time/parts_solved):>13}{format_time(total_min_time/parts_solved):>13}")


