from talon import Context, Module, actions
from user.util import csv

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.haskell
tag: user.auto_lang
and code.language: haskell
"""

# support for #user.code_function
csv.register(
    csv_file="code/haskell/functions.csv",
    list_name="user.code_function",
    column_name="Function",
    ctx=ctx,
)

# support for #user.code_library
csv.register(
    csv_file="code/haskell/libraries.csv",
    list_name="user.code_library",
    column_name="Library",
    ctx=ctx,
)

# support for #user.code_operator
csv.register(
    csv_file="code/haskell/operators.csv",
    list_name="user.code_operator",
    column_name="Operator",
    ctx=ctx,
)

# support for #user.code_type
csv.register(
    csv_file="code/haskell/types.csv",
    list_name="user.code_type",
    column_name="Type",
    ctx=ctx,
)
@mod.action_class
class UserActions:
    def haskell_qualified_letter(library: str) -> str:
        """Abbreviate module name using a single letter, e.g., Data.Map -> M."""
        return library.split(".")[-1][0]

    def haskell_qualified_word(library: str) -> str:
        """Abbreviate module name using a single word, e.g., Data.Map -> Map."""
        return library.split(".")[-1]

@ctx.action_class("user")
class TypeActions:
    def insert_type(code_type: str):
        """Insert <code_type>"""
        actions.insert(f"{code_type} ")
