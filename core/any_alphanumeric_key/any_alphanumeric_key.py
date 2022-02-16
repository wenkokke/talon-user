from talon import Module

mod = Module()

all_alphanumeric_keys = "|".join([
    "{self.key_alphabet}",
    "{self.key_number}",
    "{self.key_symbol}",
    "<self.greek>",
    "<self.blackboard>",
    "<self.math_script>",
    "<self.math_script_bold>",
    "<self.subscript_digit>",
    "<self.superscript_digit>",
    "<self.unicode_arrow>",
    "<self.unicode_mathematical_operator>",
    "<self.unicode_character>",
])

@mod.capture(rule=f"({all_alphanumeric_keys})")
def any_alphanumeric_key(m) -> str:
    "Any alphanumeric key."
    return str(m)
