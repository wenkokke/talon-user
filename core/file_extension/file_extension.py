from talon import Module, Context
from user.util import csv

mod = Module()
mod.list("file_extension", desc="List of file extensions")

ctx = Context()
csv.register(
    csv_file="file_extensions.csv",
    list_name="user.file_extension",
    column_name="File extension",
    ctx=ctx,
)

@mod.capture(rule="dot {user.file_extension}")
def file_extension(m) -> str:
    return f".{m.file_extension}"
