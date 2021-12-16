from talon import Context, Module
from user.core import csv

ctx = Context()
ctx.matches = r"""
tag: user.python
tag: user.auto_lang
and code.language: python
"""

# support for #user.code_data
csv.register(
    csv_file="code/python/data.csv",
    list_name="user.code_data",
    column_name="Data",
    ctx=ctx,
)

# support for #user.code_exception
csv.register(
    csv_file="code/python/exceptions.csv",
    list_name="user.code_exception",
    column_name="Exception",
    ctx=ctx,
)

# support for #user.code_function
csv.register(
    csv_file="code/python/functions.csv",
    list_name="user.code_function",
    column_name="Function",
    ctx=ctx,
)

# support for #user.code_library
csv.register(
    csv_file="code/python/libraries.csv",
    list_name="user.code_library",
    column_name="Library",
    ctx=ctx,
)

# support for #user.code_operator
csv.register(
    csv_file="code/python/operators.csv",
    list_name="user.code_operator",
    column_name="Operator",
    ctx=ctx,
)

# support for #user.code_type
csv.register(
    csv_file="code/python/types.csv",
    list_name="user.code_type",
    column_name="Type",
    ctx=ctx,
)