from collections.abc import Iterable
from talon import Module, Context

mod = Module()
ctx = Context()
mod.tag("keys")

alphabet = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split()
digits = "zero one two three four five six seven eight nine ten eleven twelve".split()

mod.list("key_alphabet", desc="The spoken phonetic alphabet")
ctx.lists["self.key_alphabet"] = {
    alphabet[i]: chr(ord("a") + i) for i in range(len(alphabet))
}

mod.list("key_number", desc="All number keys")
ctx.lists["self.key_number"] = {digits[i]: str(i) for i in range(10)}

mod.list("key_function", desc="All function keys")
ctx.lists["self.key_function"] = {f"F {digits[i]}": f"f{i}" for i in range(1, 13)}

mod.list("key_arrow", desc="All arrow keys")
ctx.lists["self.key_arrow"] = {"up", "down", "left", "right"}

mod.list("key_special", desc="All special keys")
ctx.lists["self.key_special"] = {
    "enter": "enter",
    "tab": "tab",
    "delete": "delete",
    "backspace": "backspace",
    "home": "home",
    "end": "end",
    "insert": "insert",
    "escape": "escape",
    "menu": "menu",
    "page up": "pageup",
    "page down": "pagedown",
    "print screen": "printscr",
}

mod.list("key_modifier", desc="All modifier keys")
ctx.lists["self.key_modifier"] = {
    "alt": "alt",
    "control": "ctrl",
    "shift": "shift",
    "super": "super",
}

# Symbols you want available BOTH in dictation and command mode.
mod.list("key_punctuation", desc="Symbols for inserting punctuation into text")
ctx.lists["self.key_punctuation"] = {
    "ampersand": "&",
    "back tick": "`",
    "comma": ",",
    "period": ".",
    "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "asterisk": "*",
    "hash sign": "#",
    "percent sign": "%",
}

# Symbols available in command mode, but NOT during dictation.
mod.list("key_symbol", desc="All symbols from the keyboard")
ctx.lists["self.key_symbol"] = {
    "dot": ".",
    "dash": "-",
    "prime": "'",
    "space": " ",
    "brick": "`",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    "equal": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    "down score": "_",
    "under score": "_",
    "question": "?",
    "snow": "*",
    "single": "'",
    "double": '"',
    "leper": "(",
    "repper": ")",
    "lack": "[",
    "rack": "]",
    "lace": "{",
    "race": "}",
    "langle": "<",
    "wrangle": ">",
    "pound": "#",
    "percy": "%",
    "tangle": "^",
    "amper": "&",
    "pipe": "|",
    "semi": ";",
    "stack": ":",
    "drip": ",",
    "at sign": "@",
    "hash": "#",
}


@mod.capture(rule="{self.key_modifier}+")
def key_modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.key_modifier_list)


@mod.capture(
    rule="( {self.key_alphabet} | {self.key_number} | {self.key_symbol} | {self.key_special} | {self.key_arrow} | {self.key_function} )"
)
def key_unmodified(m) -> str:
    "A single key with no modifiers"
    return str(m)


@mod.capture(rule="spell {self.key_alphabet}+")
def spell(m) -> str:
    """Spell word phoneticly"""
    return "".join(m.key_alphabet_list)


@mod.capture(rule="({self.key_alphabet} | {self.key_number} | {self.key_symbol})")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(rule="{self.key_alphabet}")
def letter(m) -> str:
    """One letter in the alphabet"""
    return str(m)


@mod.capture(rule="{self.key_alphabet}+")
def letters(m) -> str:
    """One or more letters in the alphabet"""
    return "".join(m.key_alphabet_list)
