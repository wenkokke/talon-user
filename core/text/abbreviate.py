from talon import Context, Module
from user.util import csv

mod = Module()
mod.list("abbreviation", desc="Common abbreviations")

ctx = Context()
csv.register_spoken_forms(
    csv_file="abbreviations.csv",
    ctx=ctx,
    list_name="user.abbreviation",
    value_name="Abbreviation",
)

@mod.capture(rule="brief {self.abbreviation}")
def abbreviation(m) -> str:
    """Abbreviated words"""
    return m.abbreviation
