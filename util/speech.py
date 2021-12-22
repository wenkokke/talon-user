from talon import app
from user.util import numbers
from user.util import csv
import re

RE_SNAKE = r"(?<![A-Za-z])([A-Z]?[a-z]+)"
RE_CAMEL = r"(?<=[A-Za-z])([A-Z][a-z]*)"
RE_NUM = r"([0-9])"
RE_WORD = re.compile(f"{RE_SNAKE}|{RE_CAMEL}|{RE_NUM}")
DIGITS = {str(k): v for k, v in zip(range(0, 9), numbers.digits)}
ALPHABET = {}


def on_ready_and_change(letters: tuple[tuple[str]]):
    global ALPHABET
    for letter, spoken_form in letters:
        ALPHABET[letter] = spoken_form


csv.watch(
    csv_file="alphabet.csv",
    header=("Letter", "Spoken form"),
    on_success=on_ready_and_change,
)


def create_spoken_form(text: str) -> str:
    global ALPHABET, DIGITS
    chunks = RE_WORD.finditer(text)
    chunks = [m.group(0) for m in chunks]
    chunks = list(map(str.lower, chunks))
    for k, v in enumerate(chunks):
        if v in ALPHABET:
            chunks[k] = ALPHABET[v]
        if v in DIGITS:
            chunks[k] = DIGITS[v]
    spoken_form = " ".join(chunks)
    return spoken_form


def test():
    def create_spoken_form_test(input, expected):
        actual = create_spoken_form(input)
        assert actual == expected, f"Expected '{expected}', found '{actual}'"

    create_spoken_form_test("user.get_match1", "user get match one")
    create_spoken_form_test("user.macro_play", "user macro play")
    create_spoken_form_test("BlockingIOError", "blocking sit odd error")


app.register("ready", test)
