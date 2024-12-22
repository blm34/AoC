from pathlib import Path
import json
from dataclasses import dataclass
import time
import re

import requests


def filter_response_text(text: str) -> str:
    main_text_match = re.search(r"<main.*?>(.*?)</main>", text, re.DOTALL)

    if main_text_match:
        main_text = main_text_match.group(1)
    else:
        return text

    one_line_text = re.sub(r"\r\n|\r|\n", " ", main_text)
    clean_text = re.sub("<.*?>", "", one_line_text, re.DOTALL)

    return clean_text


class Communicator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._headers = {
            'User-Agent': ''  # ToDo: Include email and url to github repo where code can be seen here
        }
        self._root_folder = self.get_root_folder()
        self._cookie = self.get_cookie()

    def get_cookie(self):
        filepath = self._root_folder / "cookie.txt"

        if not filepath.exists():
            cookie = input("Cookie file not found. Enter session cookie here: ")
            with open(filepath, 'w') as file:
                file.write(cookie)

        with open(filepath) as file:
            cookie = file.read()

        return {"session": cookie.strip()}

    def get_root_folder(self):
        path = Path().absolute()
        while path.name != "AoC":
            path = path.parent
        return path

    def get_input(self, year: int, day: int):
        """
        Opens the given file. Typically a puzzle input

        Args:
            day: Load the puzzle input for this day.
            year: Load the puzzle input for this year.

        Returns:
            The contents of the file
        """
        filepath = Path.joinpath(self._root_folder, "input_files", f"{year}", f"day{day}.txt")

        if not filepath.parent.exists():
            filepath.parent.mkdir()

        if not filepath.exists():
            puzzle_input = self.download_input(year, day)
            with open(filepath, 'w') as file:
                file.write(puzzle_input)

        with open(filepath, 'r') as file:
            puzzle_input = file.read().strip()

        return puzzle_input

    def download_input(self, year: int, day: int) -> str:
        """
        Download the puzzle input for the given day and year from the advent of code website, and return as a string.

        Args:
            day: Load the puzzle input for this day.
            year: Load the puzzle input for this year.

        Returns:
            The puzzle input for the given day
        """
        r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=self._headers,
                         cookies=self._cookie)
        input_text = r.text

        if "Please log in" in input_text:
            raise ValueError("Cookie in `cookie.txt` not valid - please save your session cookie as text in this file")

        if 'before it unlocks' in input_text:
            raise ValueError(f"This year {year} day {day} is not available yet")

        print(f"Input downloaded:\n{input_text[:100]}\n")
        return input_text

    def check_answer(self, answer, year: int, day: int, level: int) -> bool | None:
        if answer is None:
            return False

        answers_filepath = Path.joinpath(self._root_folder, "answers", f"{year}.json")

        if not answers_filepath.is_file():
            self.create_answers_json(answers_filepath)

        with open(answers_filepath, 'r') as file:
            correct_answers = json.load(file)

        if correct_answers[str(day)][str(level)] is not None:
            return correct_answers[str(day)][str(level)] == answer

        elif self.upload_answer(answer, year, day, level):
            correct_answers[str(day)][str(level)] = answer
            with open(answers_filepath, 'w') as file:
                json.dump(correct_answers, file)
            return True
        else:
            return False

    def upload_answer(self, answer, year: int, day: int, level: int) -> bool:
        if input(f"Part {level}: Submit `{answer}`? (y/n): ").lower() != "y":
            print("Not submitting answer")
            return False

        url = f"https://adventofcode.com/{year}/day/{day}/answer"
        post_data = {'level': level, 'answer': str(answer)}
        response = requests.post(url, headers=self._headers, cookies=self._cookie, data=post_data)

        if response.status_code != 200:
            raise ValueError(f"Answer submission failed.\nStatus code: {response.status_code}\n\nResponse:\n{response.text}")

        print(f"Successfully submitted answer.")

        response_msg = filter_response_text(response.text)

        print(response_msg)

        if "That's the right answer" in response_msg:
            return True
        elif "That's not the right answer" in response_msg:
            if "too low" in response_msg:
                pass  # ToDo: Give custom response for too low answers
            elif "too high" in response_msg:
                pass  # ToDo: Give custom response for too high answers
            return False
        elif "Did you already complete it" in response_msg:
            raise ValueError("Problem already solved, answer should be stored")
        else:
            raise ValueError("Unexpected response message")

    def create_answers_json(self, path: Path):
        answers = {day: {1: None, 2: None} for day in range(1, 26)}
        with open(path, 'w') as file:
            json.dump(answers, file)


@dataclass
class AocResult:
    answer: int | str | None
    correct: bool
    time: float


def communicator(year: int, day: int, level: int):
    def decorator(func):
        comm = Communicator()

        def new_func(input_data=None):
            if input_data is None:
                input_data = comm.get_input(year, day)
            start_time = time.perf_counter()
            answer = func(input_data)
            end_time = time.perf_counter()
            check = comm.check_answer(answer, year, day, level)
            return AocResult(answer=answer, correct=check, time=end_time-start_time)
        return new_func
    return decorator
