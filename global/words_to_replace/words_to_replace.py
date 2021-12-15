from talon import Context
from user.helper import csv

ctx = Context()

# The setting "dictate.word_map" is used by `actions.dictate.replace_words`
# to rewrite words Talon recognized. Entries in word_map don't change the
# priority with which Talon recognizes some words over others.

header = ["Word", "Replacement"]


def on_ready_and_change(words_to_replace: list[list[str]]):
    global ctx
    ctx.settings["dictate.word_map"] = dict(words_to_replace)


csv.watch("words_to_replace.csv", header, on_ready_and_change)
