from talon import Context, Module

from user.util import csv

mod = Module()

# The list "user.vocabulary" is used to explicitly add words/phrases
# that Talon doesn't recognize. Words in user.vocabulary (or other
# lists and captures) are "command-like" and their recognition is
# prioritized over ordinary words.

mod.list("vocabulary", desc="Additional vocabulary")

ctx = Context()
csv.register_spoken_forms(
    csv_file="additional_words.csv",
    ctx=ctx,
    list_name="user.vocabulary",
    value_name="Word",
)
