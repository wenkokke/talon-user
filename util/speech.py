import re
from user.util import csv

RE_SNAKE = r"(?<![A-Za-z])([A-Z]?[a-z]+)"
RE_CAMEL = r"(?<=[A-Za-z])([A-Z][a-z]*)"
RE_NUM = r"([0-9])"
RE_WORD = re.compile(f"{RE_SNAKE}|{RE_CAMEL}|{RE_NUM}")
DIGITS = csv.read_dict("numbers/digits.csv", key_name="Digit", value_name="Spoken form")
ALPHABET = csv.read_dict("alphabet.csv", key_name="Letter", value_name="Spoken form")
APP_NAME_OVERRIDES = csv.read_dict(
    "app_name_overrides.csv", key_name="Application name", value_name="Spoken form"
)


def create_spoken_form(text: str) -> str:
    """Create a spoken form for an arbitrary string"""
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


assert create_spoken_form("user.get_match1") == "user get match one"
assert create_spoken_form("user.macro_play") == "user macro play"
assert create_spoken_form("BlockingIOError") == "blocking sit odd error"


def create_spoken_form_app(name: str) -> str:
    """Create a spoken form for an application name"""
    global APP_NAME_OVERRIDES
    try:
        return APP_NAME_OVERRIDES[name]
    except KeyError:
        name = name.removesuffix(".exe")
        name = name.split("-")[0]
        name = name.strip()
        name = create_spoken_form(name)
        return name
