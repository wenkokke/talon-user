from __future__ import annotations
from itertools import chain, repeat
from typing import Callable
from talon import Module, Context, actions, imgui
import re

mod = Module()
ctx = Context()

mod.mode("help_formatters", "Mode for showing the formatter help gui")


Formatter = Callable[[str], str]

noop = lambda text: text
lower = str.lower
upper = str.upper
capitalize = str.capitalize


def surround(char: str) -> Formatter:
    return lambda text: f"{char}{text}{char}"


def suffix(text_suffix: str) -> Formatter:
    return lambda text: f"{text}{text_suffix}"


def formatter(delimiter: str, *formatters: Formatter) -> Formatter:
    """
    Create a formatter from a delimiter and a list of formatters.

    Each of the formatters will be applied to successive words,
    and the last one will be repeated for the rest of the words.
    """
    formatters = chain(formatters, repeat(formatters[-1]))
    return lambda text: delimiter.join(
        formatter(word) for formatter, word in zip(formatters, text.split())
    )


formatters_dict = {
    "NOOP": noop,
    "TRAILING_PADDING": suffix(" "),
    "ALL_CAPS": upper,
    "ALL_LOWERCASE": lower,
    "DOUBLE_QUOTED_STRING": surround('"'),
    "SINGLE_QUOTED_STRING": surround("'"),
    "REMOVE_FORMATTING": formatter(" ", lower),
    "CAPITALIZE_ALL_WORDS": formatter(" ", capitalize),
    "CAPITALIZE_FIRST_WORD": formatter(" ", capitalize, noop),
    "CAMEL_CASE": formatter("", lower, capitalize),
    "PASCAL_CASE": formatter("", capitalize),
    "SNAKE_CASE": formatter("_", lower),
    "ALL_CAPS_SNAKE_CASE": formatter("_", upper),
    "DASH_SEPARATED": formatter("-", lower),
    "DOT_SEPARATED": formatter(".", lower),
    "SLASH_SEPARATED": formatter("/", lower),
    "DOUBLE_UNDERSCORE": formatter("__", lower),
    "DOUBLE_COLON_SEPARATED": formatter("::", lower),
    "NO_SPACES": formatter("", noop),
}

# This is the mapping from spoken phrases to formatters
mod.list("formatter_code", desc="List of code formatters")
ctx.lists["self.formatter_code"] = {
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

mod.list("formatter_prose", desc="List of prose formatters")
ctx.lists["self.formatter_prose"] = {
    "say": "NOOP",
    "sentence": "CAPITALIZE_FIRST_WORD",
    "dubquote": "DOUBLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD",
    "quote": "SINGLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD",
}


mod.list("formatter_word", desc="List of word formatters")
ctx.lists["self.formatter_word"] = {
    "word": "ALL_LOWERCASE",
    "trot": "TRAILING_PADDING,ALL_LOWERCASE",
    "proud": "CAPITALIZE_FIRST_WORD",
    "leap": "TRAILING_PADDING,CAPITALIZE_FIRST_WORD",
}


@mod.capture(rule="{self.formatter_code}+")
def formatters_code(m) -> str:
    """Return a comma-separated string of formatters, e.g., 'DOUBLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD'."""
    return ",".join(m.formatter_code_list)


@mod.capture(rule="({self.formatter_code} | {self.formatter_prose})+")
def formatters(m) -> str:
    """Return a comma-separated string of formatters e.g. 'SNAKE,DUBSTRING'"""
    return ",".join(m)


@imgui.open()
def gui(gui: imgui.GUI):
    gui.text("Formatters")
    gui.line()
    formatters = {
        **ctx.lists["self.formatter_code"],
        **ctx.lists["self.formatter_prose"],
    }
    for name in sorted(set(formatters)):
        example = actions.user.format_text("one two three", formatters[name])
        gui.text(f"{name.ljust(30)}{example}")
    gui.spacer()
    if gui.button("Hide"):
        actions.user.formatters_help_toggle()


@mod.action_class
class Actions:
    def format_text(text: str, formatters: str) -> str:
        """
        Formats a text according to <formatters>.

        Args:
            formatters: A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        global formatters_dict
        for fmtr in reversed(formatters.split(",")):
            text = formatters_dict[fmtr](text)
        return text

    def formatted_text(text: str, formatters: str) -> str:
        """
        Formats a text according to <formatters>.

        Args:
            formatters: A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        return actions.user.format_text(text, formatters)

    def unformat_text(text: str) -> str:
        """Remove format from text"""
        text = de_string(text)
        text = de_delim(r"[-_.:/](?!\s)+", " ", text)
        text = de_camel(text)
        text = text.lower()
        return text

    def formatters_help_toggle():
        """Toggle list all formatters gui"""
        if gui.showing:
            actions.mode.disable("user.help_formatters")
            gui.hide()
        else:
            gui.show()
            actions.mode.enable("user.help_formatters")


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


def de_camel(text: str) -> str:
    global REGEX_CAMEL_BOUNDARY
    return re.sub(REGEX_CAMEL_BOUNDARY, " ", text)


# NOTE: A delimiter char followed by a blank space is no delimiter.
REGEX_DELIMITER = re.compile(r"[-_.:/](?!\s)+")


def de_delim(text: str) -> str:
    global REGEX_DELIMITER
    return re.sub(r"[-_.:/](?!\s)+", " ", text)


def de_string(text: str) -> str:
    if text.startswith('"') and text.endswith('"'):
        return text[1:-1]
    if text.startswith("'") and text.endswith("'"):
        return text[1:-1]
    return text


# Test unformat_text
# tests = {
#     "say": "hello, I'm ip address 2!",
#     "sentence": "Hello, I'm ip address 2!",
#     "allcaps": "HELLO, I'M IP ADDRESS 2!",
#     "camel": "helloThereIPAddressA2a2",
#     "Pascal": "HelloThereIPAddressA2a2",
#     "snake": "hello_there_ip_address_2",
#     "kebab": "hello-there-ip-address-2",
#     "packed": "hello::there::ip::address::2",
#     "dotted": "hello.there.ip.address.2",
#     "slasher": "hello/there/ip/address/2",
#     "dunder": "hello__there__ip_address__2"
# }
# for key, value in tests.items():
#     text = actions.user.unformat_text(value)
#     print(f"{key.ljust(15)}{value.ljust(35)}{text}")
