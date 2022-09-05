from talon import Context, Module, actions

from user.util import csv

ctx = Context()
ctx.matches = r"""
tag: user.python_forced
tag: user.auto_lang
and code.language: python
"""

# support for #user.code_data
csv.register_spoken_forms(
    csv_file="code/python/data.csv",
    ctx=ctx,
    list_name="user.code_data",
    value_name="Data",
)

# support for #user.code_exception
csv.register_spoken_forms(
    csv_file="code/python/exceptions.csv",
    ctx=ctx,
    list_name="user.code_exception",
    value_name="Exception",
)

# support for #user.code_function
csv.register_spoken_forms(
    csv_file="code/python/functions.csv",
    ctx=ctx,
    list_name="user.code_function",
    value_name="Function",
)

# support for #user.code_library
csv.register_spoken_forms(
    csv_file="code/python/libraries.csv",
    ctx=ctx,
    list_name="user.code_library",
    value_name="Library",
)

# support for #user.code_operator
csv.register_spoken_forms(
    csv_file="code/python/operators.csv",
    ctx=ctx,
    list_name="user.code_operator",
    value_name="Operator",
)

# support for #user.code_type
csv.register_spoken_forms(
    csv_file="code/python/types.csv",
    ctx=ctx,
    list_name="user.code_type",
    value_name="Type",
)


@ctx.action_class("user")
class TypeActions:
    def insert_function(code_function: str):
        """Insert <code_function>"""
        actions.insert(f"{code_function}()")
        actions.edit.left()
