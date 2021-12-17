from talon import Context
from user.util import csv

ctx = Context()
ctx.matches = r"""
app: vscode
tag: user.haskell
tag: user.auto_lang
and code.language: haskell
"""

# support for #user.snippets
csv.register(
    csv_file="code/haskell/snippets_vscode.csv",
    list_name="user.snippets",
    column_name="Snippet name",
    ctx=ctx,
)

