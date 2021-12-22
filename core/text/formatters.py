from __future__ import annotations
from itertools import chain, repeat
from typing import Callable
from talon import Module, Context, actions, app, imgui, ui
import re

# NOTE: This is different from the definition of a camelCase boundary
#       in create_spoken_form: this one splits "IOError" as "IO Error",
#       whereas the other splits it as "I O Error", which is important
#       when creating a spoken form as each capitalized letter should
#       be pronounced separately, but which would reformat "IOError"
#       as i_o_error in snake_case.
REGEX_CAMEL_BOUNDARY = re.compile(
    "|".join(
        (
            r"(?<=[a-z])(?=[A-Z])",
            r"(?<=[A-Z])(?=[A-Z][a-z])",
            r"(?<=[A-Za-z])(?=[0-9])",
            r"(?<=[0-9])(?=[A-Za-z])",
        )
    )
)


# NOTE: A delimiter char followed by a blank space is no delimiter.
REGEX_DELIMITER = re.compile(r"[-_.:/](?!\s)+")

Formatter = Callable[[str], str]

noop: Formatter = lambda text: text
lower: Formatter = str.lower
upper: Formatter = str.upper
capitalize: Formatter = str.capitalize


def alphanum(text: str) -> str:
    return lambda text: re.sub(r"[A-Za-z0-9]", "", text)


def surround(char: str) -> Formatter:
    return lambda text: f"{char}{text}{char}"


def prefix(text_prefix: str) -> Formatter:
    return lambda text: f"{text_prefix}{text}"


def suffix(text_suffix: str) -> Formatter:
    return lambda text: f"{text}{text_suffix}"


def words(
    *formatters: Formatter, delimiter: str = " ", splitter: str = " "
) -> Formatter:
    """
    Create a formatter from a delimiter and a list of formatters.

    Each of the formatters will be applied to successive words,
    and the last one will be repeated for the rest of the words.
    """
    return lambda text: delimiter.join(
        formatter(word)
        for formatter, word in zip(
            chain(formatters, repeat(formatters[-1])), text.split(splitter)
        )
    )


formatters_dict = {
    "NOOP": noop,
    "TRAILING_PADDING": suffix(" "),
    "TRAILING_QUESTION_MARK": suffix("?"),
    "TRAILING_EXCLAMATION_MARK": suffix("!"),
    "LEADING_SINGLE_DASH": prefix("-"),
    "LEADING_DOUBLE_DASH": prefix("--"),
    "ALL_CAPS": upper,
    "ALL_LOWERCASE": lower,
    "DOUBLE_QUOTED_STRING": surround('"'),
    "SINGLE_QUOTED_STRING": surround("'"),
    "REMOVE_FORMATTING": words(lower),
    "CAPITALIZE_ALL_WORDS": words(capitalize),
    "CAPITALIZE_FIRST_WORD": words(capitalize, noop),
    "CAMEL_CASE": words(lower, capitalize, delimiter=""),
    "PASCAL_CASE": words(capitalize, delimiter=""),
    "SNAKE_CASE": words(lower, delimiter="_"),
    "ALL_CAPS_SNAKE_CASE": words(upper, delimiter="_"),
    "DASH_SEPARATED": words(lower, delimiter="-"),
    "DOT_SEPARATED": words(lower, delimiter="."),
    "SLASH_SEPARATED": words(lower, delimiter="/"),
    "DOUBLE_UNDERSCORE": words(lower, delimiter="__"),
    "DOUBLE_COLON_SEPARATED": words(lower, delimiter="::"),
    "NO_SPACES": words(noop, delimiter=""),
    "ALPHANUM": alphanum,
}

mod = Module()
ctx = Context()

# This is the mapping from spoken phrases to formatters
mod.list("formatter_code", desc="List of code formatters")
mod.list(
    "formatter_code_extra",
    desc="List of extra code formatters, meant to be overwritten",
)
mod.list("formatter_prose", desc="List of prose formatters")
mod.list(
    "formatter_prose_extra",
    desc="List of extra prose formatters, meant to be overwritten",
)
mod.list("formatter_word", desc="List of word formatters")

FORMATTER_CODE = {
    "upper": "ALL_CAPS",
    "lower": "ALL_LOWERCASE",
    "dubstring": "DOUBLE_QUOTED_STRING",
    "string": "SINGLE_QUOTED_STRING",
    "title": "CAPITALIZE_ALL_WORDS",
    "unformat": "REMOVE_FORMATTING",
    "camel": "CAMEL_CASE",
    "pascal": "PASCAL_CASE",
    "snake": "SNAKE_CASE",
    "constant": "ALL_CAPS_SNAKE_CASE",
    "kebab": "DASH_SEPARATED",
    "dotted": "DOT_SEPARATED",
    "slasher": "SLASH_SEPARATED",
    "dunder": "DOUBLE_UNDERSCORE",
    "packed": "DOUBLE_COLON_SEPARATED",
    "smash": "NO_SPACES",
}
ctx.lists["self.formatter_code"] = FORMATTER_CODE

FORMATTER_PROSE = {
    "say": "NOOP",
    "sentence": "CAPITALIZE_FIRST_WORD",
    "query": "CAPITALIZE_FIRST_WORD,TRAILING_QUESTION_MARK",
    "shout": "CAPITALIZE_FIRST_WORD,TRAILING_EXCLAMATION_MARK",
    "dubquote": "CAPITALIZE_FIRST_WORD,DOUBLE_QUOTED_STRING",
    "quote": "CAPITALIZE_FIRST_WORD,SINGLE_QUOTED_STRING",
}
ctx.lists["self.formatter_prose"] = FORMATTER_PROSE

FORMATTER_WORD = {
    "word": "ALL_LOWERCASE",
    "trot": "ALL_LOWERCASE,TRAILING_PADDING",
    "proud": "CAPITALIZE_FIRST_WORD",
    "leap": "CAPITALIZE_FIRST_WORD,TRAILING_PADDING",
}
ctx.lists["self.formatter_word"] = FORMATTER_WORD


@mod.capture(rule="({self.formatter_code} | {self.formatter_code_extra})+")
def formatters_code(m) -> str:
    """Return a comma-separated string of formatters, e.g., 'DOUBLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD'."""
    return ",".join(m)


@mod.capture(
    rule="({self.formatter_code} | {self.formatter_code_extra} | {self.formatter_prose} | {self.formatter_prose_extra})+"
)
def formatters(m) -> str:
    """Return a comma-separated string of formatters e.g. 'SNAKE,DUBSTRING'"""
    return ",".join(m)


@mod.action_class
class Actions:
    def format_text(text: str, formatter_names: str) -> str:
        """
        Formats a text according to <formatters>.

        Args:
            formatters: A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        global formatters_dict
        for formatter_name in reversed(formatter_names.split(",")):
            text = formatters_dict[formatter_name](text)
        return text

    def unformat_text(text: str) -> str:
        """Remove format from text"""
        text = de_string(text)
        text = de_delim(text)
        text = de_camel(text)
        text = text.lower()
        return text


def de_camel(text: str) -> str:
    global REGEX_CAMEL_BOUNDARY
    return re.sub(REGEX_CAMEL_BOUNDARY, " ", text)


def de_delim(text: str) -> str:
    global REGEX_DELIMITER
    return re.sub(REGEX_DELIMITER, " ", text)


def de_string(text: str) -> str:
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1]
    return text


# Help menus


@imgui.open(x=ui.main_screen().x)
def gui(gui: imgui.GUI):
    global FORMATTER_CODE, FORMATTER_PROSE, FORMATTER_WORD
    gui.text("Formatters")
    gui.line()
    formatters = {**FORMATTER_CODE, **FORMATTER_PROSE, **FORMATTER_WORD}
    for name in frozenset(formatters):
        example = actions.user.format_text("one two three", formatters[name])
        gui.text(f"{name.ljust(30)}{example}")
    gui.spacer()
    if gui.button("Hide"):
        actions.user.help_hide("formatters")


app.register("ready", lambda: actions.user.help_register("formatters", gui))
