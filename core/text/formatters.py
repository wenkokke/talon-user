import re
from itertools import chain, repeat
from typing import Any, Callable, Generator, Iterable, Optional, Sequence, Union

from talon import Context, Module, actions, imgui, ui
from talon.grammar.vm import Capture

mod = Module()
ctx = Context()


# ImmuneString: text which is immune to formatting


class ImmuneString(object):
    """Wrapper that makes a string immune from formatting."""

    def __init__(self, string):
        self.string = string


@mod.capture(rule="({user.key_symbol_immune} | <user.number_prefix>)")
def immune_string(m) -> ImmuneString:
    return ImmuneString(str(m[0]))


# Formatter: a generic class for formatters

Chunk = Union[str, ImmuneString]
StringFormatter = Callable[[str], str]


class Formatter(object):
    @staticmethod
    def from_description(formatter_names: str) -> "Formatter":
        global FORMATTERS_DICT
        formatter = Formatter()
        for formatter_name in formatter_names.split(","):
            formatter += FORMATTERS_DICT[formatter_name]
        return formatter

    def __init__(
        self,
        delimiter: Optional[str] = None,
        chunks_formatters: Sequence[Sequence[Optional[StringFormatter]]] = [(None,)],
        string_formatters: Sequence[StringFormatter] = (),
    ):
        self.__delimiter = delimiter
        self.chunks_formatters = tuple(map(tuple, chunks_formatters))
        self.string_formatters = tuple(string_formatters)

    def __repr__(self):
        result = "{\n"
        result += f"  delimiter = '{self.delimiter()}',\n"
        longest_chunks_formatter = max(map(len, self.chunks_formatters))
        for i in range(0, longest_chunks_formatter - 1):
            sample = "sample"
            for chunk_formatter in self.chunk_formatters(i):
                if chunk_formatter:
                    sample = chunk_formatter(sample)
            result += f"  chunk_formatter({i}, 'sample') = '{sample}',\n"
        for i, string_formatter in enumerate(self.string_formatters):
            sample = "sample"
            if string_formatter:
                sample = string_formatter(sample)
            result += f"  string_formatter({i}, 'sample') = '{sample}',\n"
        result += "}"
        return result

    @staticmethod
    def pick_delimiter(delimiter1: Optional[str], delimiter2: Optional[str]):
        if delimiter1 is None:
            return delimiter2
        else:
            return delimiter1

    def __add__(self, other: "Formatter") -> "Formatter":
        return Formatter(
            Formatter.pick_delimiter(other.__delimiter, self.__delimiter),
            other.chunks_formatters + self.chunks_formatters,
            other.string_formatters + self.string_formatters,
        )

    def delimiter(self) -> str:
        return " " if self.__delimiter is None else self.__delimiter

    def string_formatter(self, string: str) -> str:
        for string_formatter in self.string_formatters:
            string = string_formatter(string)
        return string

    def chunk_formatters(self, i: int) -> Iterable[Optional[StringFormatter]]:
        for chunks_formatter in self.chunks_formatters:
            i_or_last = min(i, len(chunks_formatter) - 1)
            yield chunks_formatter[i_or_last]

    def __call__(self, chunks: Sequence[Chunk]):
        formatted_string = ""
        shifted_chunks = chain(chunks[1:], [None])
        i = 0
        for curr_chunk, next_chunk in zip(chunks, shifted_chunks):
            curr_chunk_is_last = next_chunk is None
            curr_chunk_is_immune = isinstance(curr_chunk, ImmuneString)
            next_chunk_is_immune = isinstance(next_chunk, ImmuneString)

            if curr_chunk_is_immune:
                formatted_string += curr_chunk.string
            else:
                for chunk_formatter in self.chunk_formatters(i):
                    if chunk_formatter:
                        curr_chunk = chunk_formatter(curr_chunk)
                i += 1  # increment i only when chunk is not immune
                formatted_string += curr_chunk
                if not (curr_chunk_is_last or next_chunk_is_immune):
                    formatted_string += self.delimiter()

        return self.string_formatter(formatted_string)


# Helper functions for building formatters


def FormatTopLevel(prefix: str = "", suffix: str = "") -> Formatter:
    return Formatter(string_formatters=(lambda text: f"{prefix}{text}{suffix}",))


def FormatChunk(chunks_formatters: list[Optional[StringFormatter]]) -> Formatter:
    return Formatter(chunks_formatters=[chunks_formatters])


def JoinBy(delimiter: str) -> Formatter:
    return Formatter(delimiter=delimiter)


# FORMATTERS_DICT: a dictionary of standard formatters

FORMATTERS_DICT = {
    "NOOP": Formatter(),
    "TRAILING_PADDING": FormatTopLevel(suffix=" "),
    "TRAILING_QUESTION_MARK": FormatTopLevel(suffix="?"),
    "TRAILING_EXCLAMATION_MARK": FormatTopLevel(suffix="!"),
    "LEADING_SINGLE_DASH": FormatTopLevel(prefix="-"),
    "LEADING_DOUBLE_DASH": FormatTopLevel(prefix="--"),
    "DOUBLE_QUOTED_STRING": FormatTopLevel(prefix='"', suffix='"'),
    "SINGLE_QUOTED_STRING": FormatTopLevel(prefix="'", suffix="'"),
    "ALL_UPPERCASE": FormatChunk([str.upper]),
    "ALL_LOWERCASE": FormatChunk([str.lower]),
    "CAPITALIZE_ALL": FormatChunk([str.capitalize]),
    "CAPITALIZE_FIRST": FormatChunk([str.capitalize, None]),
    "CAPITALIZE_REST": FormatChunk([None, str.capitalize]),
    "SNAKE_CASE": JoinBy("_"),
    "DASH_SEPARATED": JoinBy("-"),
    "DOT_SEPARATED": JoinBy("."),
    "SLASH_SEPARATED": JoinBy("/"),
    "DOUBLE_UNDERSCORE": JoinBy("__"),
    "DOUBLE_COLON_SEPARATED": JoinBy("::"),
    "NO_SPACES": JoinBy(""),
}

# Spoken forms: A mapping from spoken phrases to formatters.
#
#   Generally, these come in two forms:
#
#   - formatters_code, formatters_prose, formatters_word:
#     A standard list of formatters, which is available in every setting
#     and is not meant to be overwritten by contexts.
#
#   - formatters_code_extra, formatters_prose_extra:
#     An extra list of formatters, which is usually empty and can be
#     overwritten by contexts.

mod.list("formatter_code", desc="List of code formatters")
FORMATTER_CODE = {
    "upper": "ALL_UPPERCASE",
    "lower": "ALL_LOWERCASE",
    "string": "DOUBLE_QUOTED_STRING",
    "quote": "SINGLE_QUOTED_STRING",
    "title": "CAPITALIZE_ALL,ALL_LOWERCASE",
    "ship": "CAPITALIZE_FIRST",
    "camel": "NO_SPACES,CAPITALIZE_REST,ALL_LOWERCASE",
    "pascal": "NO_SPACES,CAPITALIZE_ALL,ALL_LOWERCASE",
    "snake": "SNAKE_CASE,ALL_LOWERCASE",
    "constant": "SNAKE_CASE,ALL_UPPERCASE",
    "kebab": "DASH_SEPARATED,ALL_LOWERCASE",
    "smash": "NO_SPACES",
}
ctx.lists["self.formatter_code"] = FORMATTER_CODE

mod.list(
    "formatter_code_extra",
    desc="List of extra code formatters, meant to be overwritten",
)

mod.list("formatter_prose", desc="List of prose formatters")
FORMATTER_PROSE = {
    "say": "NOOP",
    "sentence": "CAPITALIZE_FIRST",
}
ctx.lists["self.formatter_prose"] = FORMATTER_PROSE

mod.list(
    "formatter_prose_extra",
    desc="List of extra prose formatters, meant to be overwritten",
)

mod.list("formatter_word", desc="List of word formatters")
FORMATTER_WORD = {
    "word": "NOOP",
    "trot": "TRAILING_PADDING",
    "proud": "CAPITALIZE_FIRST",
    "leap": "CAPITALIZE_FIRST,TRAILING_PADDING",
}
ctx.lists["self.formatter_word"] = FORMATTER_WORD


@mod.capture(rule="({self.formatter_code} | {self.formatter_code_extra})+")
def formatters(m: Capture) -> str:
    """Return a comma-separated string of formatters, e.g., 'DOUBLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD'."""
    return ",".join(m)


@mod.capture(rule="<user.formatters> [lit] <user.chunks>")
def formatted_code(m: Capture) -> str:
    """Return a formatted piece of text, using code formatters."""
    return Formatter.from_description(m.formatters)(m.chunks)


@mod.capture(rule="({self.formatter_prose} | {self.formatter_prose_extra})+")
def formatters_prose(m: Capture) -> str:
    """Return a comma-separated string of formatters, e.g., 'DOUBLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD'."""
    return ",".join(m)


@mod.capture(rule="<user.formatters_prose> [lit] <user.prose>")
def formatted_prose(m: Capture) -> str:
    """Return a formatted piece of text, using prose formatters."""
    return Formatter.from_description(m.formatters_prose)(m.prose.split())


@mod.capture(rule="({self.formatter_word})+")
def formatters_word(m: Capture) -> str:
    """Return a comma-separated string of formatters, e.g., 'DOUBLE_QUOTED_STRING,CAPITALIZE_FIRST_WORD'."""
    return ",".join(m)


@mod.capture(rule="<user.formatters_word> [lit] <user.word>")
def formatted_word(m: Capture) -> str:
    """Return a formatted word, using word formatters."""
    return Formatter.from_description(m.formatters_word)((m.word,))


@mod.action_class
class FormatterActions:
    def format_text(text: str, formatter_names: str) -> str:
        """
        Format <text> using <formatter_names>.

        Args:
            text: The text to format.
            formatter_names: A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        return Formatter.from_description(formatter_names)(text.split(" "))

    def unformat_text(text: str) -> str:
        """
        Remove formatting from <text>.

        Note:
            Some formatting, such as 'NO_SPACES', is irreversible. Therefore, this function is a best effort.

        Args:
            text: The text to remove formatting from.
        """
        text = de_string(text)
        text = de_delim(text)
        text = de_camel(text)
        text = text.lower()
        return text

    def reformat_text(text: str, formatter_names: str) -> str:
        """
        Reformat <text> using <formatters>.

        Note:
            Used by Cursorless.

        Args:
            text: The text to format.
            formatter_names: A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        lines = []
        for line in text.splitlines():
            unformatted = actions.user.unformat_text(line)
            reformatted = actions.user.format_text(unformatted, formatter_names)
            lines.append(reformatted)
        return "\n".join(lines)

    def reformat_selection(formatter_names: str):
        """
        Reformat the current selection using <formatter_names>.

        Args:
            formatter_names(str): A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        selected_text = actions.edit.selected_text()
        if not selected_text:
            return
        selections = []
        for selection in selected_text.splitlines():
            unformatted = actions.user.unformat_text(selection)
            reformatted = actions.user.format_text(unformatted, formatter_names)
            selections.append((unformatted, reformatted))

        if len(selections) == 1:
            ((unformatted, reformatted),) = selections
            actions.insert(reformatted)
            actions.user.history_add_phrase(reformatted, unformatted)
        else:
            unformatted, reformatted = zip(*selections)
            actions.insert("\n".join(unformatted))
            # TODO: no actions.user.history_add_phrase?

    def reformat_last(formatter_names: str):
        """
        Reformats the last phrase using <formatter_names>.

        Args:
            formatter_names: A comma-separated string of formatters, e.g., 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING'.
        """
        last_phrase = actions.user.history_get_last_phrase()
        if not last_phrase:
            return
        last_unformatted = actions.user.history_get_last_unformatted()
        actions.user.history_clear_last_phrase()
        if last_unformatted:
            last_formatted = actions.user.format_text(last_unformatted, formatter_names)
            actions.user.history_add_phrase(last_formatted, last_unformatted)
            actions.insert(last_formatted)
        else:
            last_formatted = actions.user.format_text(last_phrase, formatter_names)
            actions.user.history_add_phrase(last_formatted, last_phrase)
            actions.insert(last_formatted)


# Removing formatting

# NOTE: This is different from the definition of a camelCase boundary
#       in create_spoken_forms: this one splits "IOError" as "IO Error",
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


@imgui.open(x=ui.main_screen().x, y=ui.main_screen().y)
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
        actions.user.help_hide_formatters()


# Help menu

mod.mode(
    "help_formatters",
    desc="A mode which is active if the help GUI for formatters is showing",
)


@mod.action_class
class HelpActions:
    def help_show_formatters():
        """Show help GUI for formatters"""
        if not gui.showing:
            actions.mode.enable("user.help_formatters")
            gui.show()

    def help_hide_formatters():
        """Hide help GUI for formatters"""
        if gui.showing:
            actions.mode.disable("user.help_formatters")
            gui.hide()

    def help_toggle_formatters():
        """Toggle help GUI for formatters"""
        if gui.showing:
            actions.user.help_hide_formatters()
        else:
            actions.user.help_show_formatters()
