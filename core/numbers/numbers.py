from functools import cache
from talon import Context, Module
from typing import Union, Iterator
from user.util import csv

DIGITS_MAP = csv.read_spoken_forms("numbers/digits.csv", value_name="Digit", value_type=int)
DIGITS = list(DIGITS_MAP.keys())

TEENS_MAP = csv.read_spoken_forms("numbers/teens.csv", value_name="Teen", value_type=int)
TEENS = list(TEENS_MAP.keys())

TENS_MAP = csv.read_spoken_forms("numbers/tens.csv", value_name="Ten", value_type=int)
TENS = list(TENS_MAP.keys())

# Remove spoken forms for 0 and 10, as these
# are handled via DIGITS_MAP and TEENS_MAP
for spoken_form, number in tuple(TENS_MAP.items()):
    if number in [0, 10]:
        del TENS_MAP[spoken_form]

SCALES = "hundred thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion".split()
SCALES_MAP = {n: 10 ** (3 * (i + 1)) for i, n in enumerate(SCALES[1:])}
SCALES_MAP["hundred"] = 100

NUMBERS_MAP = DIGITS_MAP | TEENS_MAP | TENS_MAP | SCALES_MAP
NUMBERS = list(NUMBERS_MAP.keys())

# NOTE: REV_ORDINALS_MAP maps numbers to spoken forms
REV_ORDINALS_MAP = csv.read_dict("numbers/ordinals.csv", key_name="Ordinal", key_type=int, value_name="Spoken form")
for n in range(1, 100):
    if not n in REV_ORDINALS_MAP:
        tens, ones = divmod(n, 10)
        REV_ORDINALS_MAP[n] = f"{TENS[tens]} {REV_ORDINALS_MAP[ones]}"

ORDINALS_MAP = {spoken_form: n for n, spoken_form in REV_ORDINALS_MAP.items()}
ORDINALS = list(ORDINALS_MAP.keys())
ORDINALS_SMALL = ORDINALS[:20]

def parse_number(l: list[str]) -> str:
    """Parses a list of words into a number/digit string."""
    global SCALES
    l = list(scan_small_numbers(l))
    for scale in SCALES:
        l = parse_scale(scale, l)
    return "".join(str(n) for n in l)


def scan_small_numbers(l: list[str]) -> Iterator[Union[str, int]]:
    """
    Takes a list of number words, yields a generator of mixed numbers & strings.
    Translates small number terms (<100) into corresponding numbers.
    Drops all occurrences of "and".
    Smashes digits onto tens words, eg. ["twenty", "one"] -> [21].
    But note that "ten" and "zero" are excluded, ie:
      ["ten", "three"] -> [10, 3]
      ["fifty", "zero"] -> [50, 0]
    Does nothing to scale words ("hundred", "thousand", "million", etc).
    """
    global DIGITS_MAP, TENS_MAP, SCALES_MAP, NUMBERS_MAP
    # reversed so that repeated pop() visits in left-to-right order
    l = [x for x in reversed(l) if x != "and"]
    while l:
        n = l.pop()
        # fuse tens onto digits, eg. "twenty", "one" -> 21
        if n in TENS_MAP and l and DIGITS_MAP.get(l[-1], 0) != 0:
            d = l.pop()
            yield NUMBERS_MAP[n] + NUMBERS_MAP[d]
        # turn small number terms into corresponding numbers
        elif n not in SCALES_MAP:
            yield NUMBERS_MAP[n]
        else:
            yield n


def parse_scale(scale: str, l: list[Union[str, int]]) -> list[Union[str, int]]:
    """Parses a list of mixed numbers & strings for occurrences of the following
    pattern:

        <multiplier> <scale> <remainder>

    where <scale> is a scale word like "hundred", "thousand", "million", etc and
    multiplier and remainder are numbers or strings of numbers of the
    appropriate size. For example:

        parse_scale("hundred", [1, "hundred", 2]) -> [102]
        parse_scale("thousand", [12, "thousand", 3, 45]) -> [12345]

    We assume that all scales of lower magnitude have already been parsed; don't
    call parse_scale("thousand") until you've called parse_scale("hundred").
    """
    global SCALES_MAP
    scale_value = SCALES_MAP[scale]
    scale_digits = len(str(scale_value))

    # Split the list on the desired scale word, then parse from left to right.
    left, *splits = split_list(scale, l)
    for right in splits:
        # (1) Figure out the multiplier by looking to the left of the scale
        # word. We ignore non-integers because they are scale words that we
        # haven't processed yet; this strategy means that "thousand hundred"
        # gets parsed as 1,100 instead of 100,000, but "hundred thousand" is
        # parsed correctly as 100,000.
        before = 1  # default multiplier
        if left and isinstance(left[-1], int) and left[-1] != 0:
            before = left.pop()

        # (2) Absorb numbers to the right, eg. in [1, "thousand", 1, 26], "1
        # thousand" absorbs ["1", "26"] to make 1,126. We pull numbers off
        # `right` until we fill up the desired number of digits.
        after = ""
        while right and isinstance(right[0], int):
            next = after + str(right[0])
            if len(next) >= scale_digits:
                break
            after = next
            right.pop(0)
        after = int(after) if after else 0

        # (3) Push the parsed number into place, append whatever was left
        # unparsed, and continue.
        left.append(before * scale_value + after)
        left.extend(right)

    return left


def split_list(value, l: list) -> Iterator:
    """Splits a list by occurrences of a given value."""
    start = 0
    while True:
        try:
            i = l.index(value, start)
        except ValueError:
            break
        yield l[start:i]
        start = i + 1
    yield l[start:]


def ordinal(n):
    """
    Convert an integer into its ordinal representation::
        ordinal(0)   => '0th'
        ordinal(3)   => '3rd'
        ordinal(122) => '122nd'
        ordinal(213) => '213th'
    """
    n = int(n)
    suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    return str(n) + suffix

# ---------- TESTS (uncomment to run) ----------
def test_number(expected, string):
    global SCALES
    l = list(scan_small_numbers(string.split()))
    for scale in SCALES:
        old = l
        l = parse_scale(scale, l)
        if not scale in old:
            assert (
                old == l
            ), "parse_scale should do nothing if the scale does not occur in the list"
    result = "".join(str(n) for n in l)
    assert result == parse_number(string.split())
    assert (
        str(expected) == result
    ), f"parsing {string!r}, expected {expected}, got {result}"


test_number(105000, "one hundred and five thousand")
test_number(1000000, "one thousand thousand")
test_number(1501000, "one million five hundred one thousand")
test_number(1501106, "one million five hundred and one thousand one hundred and six")
test_number(123, "one two three")
test_number(123, "one twenty three")
test_number(104, "ten four")  # borderline, but valid in some dialects
test_number(1066, "ten sixty six")  # a common way of saying years
test_number(1906, "nineteen oh six")  # year
test_number(2001, "twenty oh one")  # year
test_number(2020, "twenty twenty")
test_number(1001, "one thousand one")
test_number(1010, "one thousand ten")
test_number(
    123456, "one hundred and twenty three thousand and four hundred and fifty six"
)
test_number(123456, "one twenty three thousand four fifty six")


# ---------- CAPTURES ----------
mod = Module()
ctx = Context()

RULE_DIGITS = "(" + ("|".join(DIGITS)) + ")"
RULE_NONZERO_DIGITS = "(" + ("|".join(DIGITS[1:])) + ")"
RULE_TEENS = "(" + ("|".join(TEENS)) + ")"
RULE_TENS = "(" + ("|".join(TENS[2:])) + ")"
RULE_ORDINALS = "(" + ("|".join(ORDINALS)) + ")"
RULE_ORDINALS_SMALL = "(" + ("|".join(ORDINALS_SMALL)) + ")"
RULE_NUMBERS_ANY = "(" + "|".join(NUMBERS) + ")"
RULE_NUMBERS_SMALL = f"({RULE_DIGITS}|{RULE_TEENS}|{RULE_TENS} [{RULE_DIGITS}])"
LEADING_WORDS = NUMBERS_MAP.keys() - SCALES_MAP.keys()
RULE_LEADING_NUMBERS = f"({'|'.join(LEADING_WORDS)})"
RULE_NUMBERS = f"{RULE_LEADING_NUMBERS} ([and] {RULE_NUMBERS_ANY})*"

@mod.capture(rule=RULE_NUMBERS)
def number_string(m) -> str:
    """Parses a number phrase, returning that number as a string."""
    return parse_number(list(m))


@ctx.capture("number", rule="<user.number_string>")
def number(m) -> int:
    """Parses a number phrase, returning it as an integer."""
    return int(m.number_string)


@ctx.capture("number_small", rule=RULE_NUMBERS_SMALL)
def number_small(m) -> int:
    return int(parse_number(list(m)))


@mod.capture(rule="(numb|number) <user.number_string>")
def number_prefix(m) -> str:
    """Parses a prefixed number phrase, returning that number as a string."""
    return m.number_string


@mod.capture(rule=RULE_NONZERO_DIGITS)
def digit(m) -> int:
    """Parses a (non zero) digit phrase, returning it as an integer"""
    return DIGITS_MAP[str(m)]


@mod.capture(rule=RULE_ORDINALS)
def ordinals(m) -> int:
    """Returns a single ordinal as a digit"""
    global ORDINALS_MAP
    return int(ORDINALS_MAP[m[0]])


@mod.capture(rule=RULE_ORDINALS_SMALL)
def ordinals_small(m) -> int:
    """Returns a single ordinal as a digit"""
    global ORDINALS_MAP
    return int(ORDINALS_MAP[m[0]])
