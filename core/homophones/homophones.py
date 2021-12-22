from typing import Dict, Optional, Sequence
from talon import Context, Module, app, imgui, actions, ui
from user.util import csv
import re

# a list of homophones where each line is a comma separated list
# e.g. where,wear,ware
# a suitable one can be found here:
# https://github.com/pimentel/homophones

ctx = Context()
mod = Module()

all_homophones: Dict[str, Sequence[str]] = {}

active_word: Optional[str] = None
active_word_list: Optional[Sequence[str]] = None
active_index: Optional[int] = None


def word_to_key(word: str) -> str:
    return word.lower().strip()


def on_ready_and_change(homophones: tuple[tuple[str]]):
    global all_homophones
    for new_words in homophones:
        for word in new_words:
            key = word_to_key(word)
            old_words = all_homophones.get(key, ())
            all_homophones[key] = sorted((*old_words, *new_words))


csv.watch("homophones.csv", ("Homophones",), on_ready_and_change)


def phones_active() -> bool:
    return (
        active_word is not None
        and active_word_list is not None
        and active_index is not None
    )


def phones_reset():
    global active_word, active_word_list, active_index
    active_word = None
    active_word_list = None
    active_index = None


def phones_cycle(step: int):
    global active_word, active_word_list, active_index
    word = actions.edit.selected_text()
    if word != active_word:
        actions.user.phones_set(word)
    if phones_active():
        active_index = (active_index + step) % len(active_word_list)
        active_word = active_word_list[active_index]
        actions.insert(active_word)
        actions.edit.extend_word_left()


@mod.action_class
class Actions:
    def phones_set(word: str):
        """Get homophones for <word>"""
        global all_homophones, active_word, active_word_list, active_index
        try:
            active_word = word_to_key(word)
            active_word_list = all_homophones.get(active_word, ())
            active_index = active_word_list.index(active_word)
        except ValueError:
            app.notify(f"No homophones for {word}")

    def phones_set_selected():
        """Set the active word to the current selection"""
        word = actions.edit.selected_text()
        if word:
            actions.user.phones_set(word)

    def phones_next():
        """Replace the current selection with the next homophone"""
        phones_cycle(1)

    def phones_previous():
        """Replace the current selection with the previous homophone"""
        phones_cycle(-1)

    def phones_select(number: int) -> str:
        """Selects homophone number <number>"""
        global active_word_list
        if phones_active():
            word = active_word_list[number - 1]
            actions.user.history_add_phrase(word)
            actions.insert(word)
            actions.user.help_hide("phones")


# Help menus


@imgui.open(x=ui.main_screen().x, y=ui.main_screen().y)
def gui(gui: imgui.GUI):
    global active_word, active_word_list
    gui.text("Homophones")
    gui.line()
    if active_word and active_word_list:
        for index, word in enumerate(active_word_list, start=1):
            gui.text(f"Choose {index} {word.strip()}")
    elif active_word:
        gui.text(f"No homophones for '{active_word}'")
    else:
        gui.text(f"No word selected")
    gui.spacer()
    if gui.button("Hide"):
        actions.user.help_hide("phones")


def phones_help_hook(showing: bool):
    if showing:
        actions.user.phones_set_selected()
    else:
        phones_reset()


def on_ready():
    actions.user.help_register("phones", gui, cb=phones_help_hook)


app.register("ready", on_ready)
