from talon import Module

mod = Module()


@mod.capture(rule="({self.key_alphabet} | {self.key_number} | {self.key_symbol})")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)
