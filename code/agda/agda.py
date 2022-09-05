from talon import Context, Module, actions

from user.util import csv

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.agda_forced
tag: user.auto_lang
and code.language: agda
"""

# support for #user.code_function
# csv.register_spoken_forms(
#     csv_file="code/agda/functions.csv",
#     ctx=ctx,
#     list_name="user.code_function",
#     value_name="Function",
# )

# support for #user.code_library
# csv.register_spoken_forms(
#     csv_file="code/agda/libraries.csv",
#     ctx=ctx,
#     list_name="user.code_library",
#     value_name="Library",
# )

# support for #user.code_operator
# csv.register_spoken_forms(
#     csv_file="code/agda/operators.csv",
#     ctx=ctx,
#     list_name="user.code_operator",
#     value_name="Operator",
# )

# support for #user.code_type
# csv.register_spoken_forms(
#     csv_file="code/agda/types.csv",
#     ctx=ctx,
#     list_name="user.code_type",
#     value_name="Type",
# )


@mod.action_class
class AgdaActions:
    def agda_insert_library_qualified_letter(library: str) -> str:
        """Abbreviate module name using a single letter, e.g., Data.Map -> M."""
        return library.split(".")[-1][0]

    def agda_insert_library_qualified_word(library: str) -> str:
        """Abbreviate module name using a single word, e.g., Data.Map -> Map."""
        return library.split(".")[-1]


@ctx.action_class("user")
class TypeActions:
    def insert_type(code_type: str):
        """Insert <code_type>"""
        actions.insert(f"{code_type} ")

    def insert_function(code_function: str):
        """Insert <code_function>"""
        actions.insert(f"{code_function} ")

    def insert_library(code_library: str):
        """Insert <code_library>"""
        actions.insert(code_library)
