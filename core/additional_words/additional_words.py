from talon import Module, Context
from user.util import csv

mod = Module()

# The list "user.vocabulary" is used to explicitly add words/phrases
# that Talon doesn't recognize. Words in user.vocabulary (or other
# lists and captures) are "command-like" and their recognition is
# prioritized over ordinary words.

mod.list("vocabulary", desc="Additional vocabulary")

ctx = Context()
csv.register(
    csv_file="additional_words.csv",
    list_name="user.vocabulary",
    column_name="Word",
    ctx=ctx,
)
