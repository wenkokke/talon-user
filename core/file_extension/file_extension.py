from talon import Context, Module

from user.util import csv

mod = Module()
mod.list("file_extension", desc="List of file extensions")

ctx = Context()
csv.register_spoken_forms(
    csv_file="file_extensions.csv",
    ctx=ctx,
    list_name="user.file_extension",
    value_name="File extension",
)


@mod.capture(rule="dot {user.file_extension}")
def file_extension(m) -> str:
    return f".{m.file_extension}"
