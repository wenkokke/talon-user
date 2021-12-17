from talon import Module, Context
from user.util import csv

mod = Module()

# The list "user.vocabulary" is used to explicitly add words/phrases
# that Talon doesn't recognize. Words in user.vocabulary (or other
# lists and captures) are "command-like" and their recognition is
# prioritized over ordinary words.

mod.list("vocabulary", desc="Additional vocabulary")

ctx = Context()

header = ["Word", "Spoken form"]


def on_ready_and_change(additional_words: list[list[str]]):
    global ctx
    additional_word_dict = {}
    for row in additional_words:
        try:
            v, k = row
            additional_word_dict[k] = v
        except ValueError:
            (k,) = row
            additional_word_dict[k] = k
    ctx.lists["user.vocabulary"] = additional_word_dict


csv.watch("additional_words.csv", header, on_ready_and_change)
