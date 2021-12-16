from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("edit")
class EditActions:
    def copy():
        actions.key("ctrl-c")

    def cut():
        actions.key("ctrl-x")

    def delete():
        actions.key("backspace")

    def delete_line():
        actions.edit.select_line()
        actions.edit.delete()

    def delete_word():
        actions.edit.select_word()
        actions.edit.delete()

    def down():
        actions.key("down")

    def extend_down():
        actions.key("shift-down")

    def extend_file_end():
        actions.key("shift-ctrl-end")

    def extend_file_start():
        actions.key("shift-ctrl-home")

    def extend_left():
        actions.key("shift-left")

    def extend_line_down():
        actions.key("shift-down")

    def extend_line_end():
        actions.key("shift-end")

    def extend_line_start():
        actions.key("shift-home")

    def extend_line_up():
        actions.key("shift-up")

    def extend_page_down():
        actions.key("shift-pagedown")

    def extend_page_up():
        actions.key("shift-pageup")

    def extend_right():
        actions.key("shift-right")

    def extend_up():
        actions.key("shift-up")

    def extend_word_left():
        actions.key("ctrl-shift-left")

    def extend_word_right():
        actions.key("ctrl-shift-right")

    def file_end():
        actions.key("ctrl-end")

    def file_start():
        actions.key("ctrl-home")

    def find(text: str = None):
        actions.key("ctrl-f")
        actions.actions.insert(text)

    def find_next():
        actions.key("f3")

    def indent_less():
        actions.key("home delete")

    def indent_more():
        actions.key("home tab")

    def left():
        actions.key("left")

    def line_down():
        actions.key("down home")

    def line_end():
        actions.key("end")

    def line_insert_up():
        actions.key("home enter up")

    def line_start():
        actions.key("home")

    def line_up():
        actions.key("up home")

    def page_down():
        actions.key("pagedown")

    def page_up():
        actions.key("pageup")

    def paste():
        actions.key("ctrl-v")

    def print():
        actions.key("ctrl-p")

    def redo():
        actions.key("ctrl-y")

    def right():
        actions.key("right")

    def save():
        actions.key("ctrl-s")

    def save_all():
        actions.key("ctrl-shift-s")

    def select_all():
        actions.key("ctrl-a")

    def select_line(n: int = None):
        actions.key("end shift-home")

    def select_none():
        actions.key("right")

    def select_word():
        actions.edit.right()
        actions.edit.word_left()
        actions.edit.extend_word_right()

    def undo():
        actions.key("ctrl-z")

    def up():
        actions.key("up")

    def word_left():
        actions.key("ctrl-left")

    def word_right():
        actions.key("ctrl-right")

    def zoom_in():
        actions.key("ctrl-+")

    def zoom_out():
        actions.key("ctrl--")

    def zoom_reset():
        actions.key("ctrl-0")
