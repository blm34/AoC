from datetime import datetime
import statistics

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
            if results[year][day][0].p1_correct:
                line += "*"
                stars[year] += 1
            else:
                line += " "
            if results[year][day][0].p2_correct or day == 25 and results[year][day][0].p1_correct:
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
    total_avg_time = 0
    total_min_time = 0
    days_solved = 0
    print("\nYEAR DAY     MIN TIME     AVG TIME    (STD DEV)     MEDIAN TIME")
    for year in results:
        line = f"{year} "
        for day in results[year]:
            if results[year][day][0].p1_correct or results[year][day][0].p2_correct is True:
                days_solved += 1
                avg_time = sum(result.time for result in results[year][day]) / args.repeats
                if len(results[year][day]) > 1:
                    std_time = statistics.stdev(result.time for result in results[year][day])
                else:
                    std_time = 0.
                min_time = min(result.time for result in results[year][day])
                median_time = statistics.median(result.time for result in results[year][day])

                line += f"{day:2d}"
                line = f"{line:>7}"

                total_min_time += min_time
                line += f"{format_time(min_time):>14}"

                total_avg_time += avg_time
                line += f"{format_time(avg_time):>13}"

                line += f"{format_time(std_time):>12}"

                line += f"{format_time(median_time):>15}"

                print(line)
                line = ""

    print(f"\n   TOTAL{format_time(total_min_time):>13}{format_time(total_avg_time):>13}")
    if days_solved > 0:
        print(f"    AVG {format_time(total_min_time/days_solved):>13}{format_time(total_avg_time/days_solved):>13}")


