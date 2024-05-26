from pathlib import Path

import browser_cookie3 as bc3
import requests


def read_input(day: int, year: int) -> str:
    """
    Opens the given file. Typically a puzzle input

    Args:
        day: Load the puzzle input for this day.
        year: Load the puzzle input for this year.

    Returns:
        The contents of the file
    """
    filepath = Path.joinpath(Path("..").resolve(), "input_files", f"{day}.txt")

    if not filepath.exists():
        puzzle_input = download_input(day, year)
        with open(filepath, 'w') as file:
            file.write(puzzle_input)

    else:
        with open(filepath, 'r') as file:
            puzzle_input = file.read().strip()

    return puzzle_input


def download_input(day: int, year: int) -> str:
    """
    Download the puzzle input for the given day and year from the advent of code website, and return as a string.

    Args:
        day: Load the puzzle input for this day.
        year: Load the puzzle input for this year.

    Returns:
        The puzzle input for the given day
    """
    cookies = bc3.firefox(domain_name=".adventofcode.com")
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies)
    return r.text

