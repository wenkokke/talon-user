from talon import Context
from user.settings import csv

ctx = Context()
ctx.matches = r"""
app: vscode
mode: user.haskell
mode: user.auto_lang 
and code.language: haskell
"""

csv.register(
    csv_file="code/haskell/snippets_vscode.csv",
    list_name="user.code_snippets",
    column_name="Snippet name",
    ctx=ctx,
)

