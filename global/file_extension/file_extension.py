from talon import Module, Context
from user.helper import csv

mod = Module()
mod.list("file_extension", desc="List of file extensions")

ctx = Context()

header = ["File extension", "Spoken form"]


def on_ready_and_change(file_ext_list: list[list[str]]):
    global ctx
    file_ext_dict = {}
    for row in file_ext_list:
        try:
            v, k = row
            file_ext_dict[k] = v
        except ValueError:
            (k,) = row
            file_ext_dict[k] = k
    ctx.lists["user.file_extension"] = file_ext_dict


csv.watch("file_extension.csv", header, on_ready_and_change)


@mod.capture(rule="dot {user.file_extension}")
def file_extension(m) -> str:
    return f".{m.file_extension}"
