from talon import Context, Module
from user.util.numbers import *

mod = Module()
ctx = Context()


@mod.capture(rule=f"{number_word_leading} ([and] {number_word})*")
def number_string(m) -> str:
    """Parses a number phrase, returning that number as a string."""
    return parse_number(list(m))


@ctx.capture("number", rule="<user.number_string>")
def number(m) -> int:
    """Parses a number phrase, returning it as an integer."""
    return int(m.number_string)


@ctx.capture(
    "number_small", rule=f"({alt_digits} | {alt_teens} | {alt_tens} [{alt_digits}])"
)
def number_small(m):
    return int(parse_number(list(m)))


@mod.capture(rule="(numb | number) <user.number_string>")
def number_prefix(m) -> str:
    """Parses a prefixed number phrase, returning that number as a string."""
    return m.number_string


@mod.capture(rule=f"{'|'.join(digits[1:])}")
def digit(m) -> int:
    """Parses a (non zero) digit phrase, returning it as an integer"""
    return digits_map[str(m)]
