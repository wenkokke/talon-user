from talon import Context, Module
from user.settings import csv

mod = Module()
mod.list("abbreviation", desc="Common abbreviations")

ctx = Context()
csv.register(
    csv_file="abbreviations.csv",
    list_name="user.abbreviation",
    column_name="Abbreviation",
    ctx=ctx
)

@mod.capture(rule="brief {self.abbreviation}")
def abbreviation(m) -> str:
    """Abbreviated words"""
    return m.abbreviation
