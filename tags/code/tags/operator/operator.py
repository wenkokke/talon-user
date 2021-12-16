from talon import Module, Context
from user.settings import csv

mod = Module()
mod.tag("code_operator", desc="Tag which provides a general list for operators")
mod.list("code_operator", desc="List of operators")

# support for #user.code_operator
ctx = Context()
csv.register(
    csv_file="code/default/operators.csv",
    list_name="user.code_operator",
    column_name="Operator",
    ctx=ctx,
)
