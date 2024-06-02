from datetime import datetime
from pathlib import Path
import importlib.util
import sys

from aoc_helper import print_results

def get_file_path(year, day):
    return Path(str(year)).joinpath(f"day{day}.py")


if __name__ == "__main__":
    stars = 0
    total_runtime = 0

    current_year = datetime.now().year

    for year in range(2015, current_year + 1):
        for day in range(1, 26):
            filepath = get_file_path(year, day)
            if not filepath.is_file():
                continue

            # Import the file
            spec = importlib.util.spec_from_file_location(f"day{day}", filepath)
            module = importlib.util.module_from_spec(spec)
            sys.modules[f"day{day}"] = module
            spec.loader.exec_module(module)

            # Run part 1
            p1_res = module.p1()
            print_results(p1_res, year=year, day=day, part=1)
            stars += p1_res.correct
            total_runtime += p1_res.time

            # Run part 2
            p2_res = module.p2()
            print_results(p2_res, year=year, day=day, part=2)
            stars += p2_res.correct
            total_runtime += p2_res.time

print(f"\nTotal stars: {stars}\nTotal runtime: {total_runtime:.1f} s")


