from talon import Module, registry
from user.helper import csv_list

mod = Module()
mod.list("file_extension", desc="List of file extensions")

csv_list.register("user.file_extension")

@mod.capture(rule="dot {user.file_extension}")
def file_extension(m) -> str:
    return f".{m.file_extension}"

