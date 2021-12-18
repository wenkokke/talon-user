from talon import Context, actions, clip

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("edit")
class EditActions:
    def copy():
        actions.key("cmd-c")

    def cut():
        actions.key("cmd-x")

    def delete():
        actions.key("backspace")

    def delete_line():
        actions.edit.select_line()
        actions.edit.delete()

    # edit.delete_paragraph()
    #   Delete paragraph under cursor

    # edit.delete_sentence()
    #   Delete sentence under cursor

    def delete_word():
        actions.edit.select_word()
        actions.edit.delete()

    def down():
        actions.key("down")

    # edit.extend_again()
    #   Extend selection again in the same way

    # edit.extend_column(n: int)
    #   Extend selection to column <n>

    def extend_down():
        actions.key("shift-down")

    def extend_file_end():
        actions.key("cmd-shift-down")

    def extend_file_start():
        actions.key("cmd-shift-up")

    def extend_left():
        actions.key("shift-left")

    # edit.extend_line(n: int)
    #   Extend selection to include line <n>

    def extend_line_down():
        actions.key("shift-down")

    def extend_line_end():
        actions.key("cmd-shift-right")

    def extend_line_start():
        actions.key("cmd-shift-left")

    def extend_line_up():
        actions.key("shift-up")

    def extend_page_down():
        actions.key("cmd-shift-pagedown")

    def extend_page_up():
        actions.key("cmd-shift-pageup")

    # edit.extend_paragraph_end()
    #   Extend selection to the end of the current paragraph

    # edit.extend_paragraph_next()
    #   Extend selection to the start of the next paragraph

    # edit.extend_paragraph_previous()
    #   Extend selection to the start of the previous paragraph

    # edit.extend_paragraph_start()
    #   Extend selection to the start of the current paragraph

    def extend_right():
        actions.key("shift-right")

    # edit.extend_sentence_end()
    #   Extend selection to the end of the current sentence

    # edit.extend_sentence_next()
    #   Extend selection to the start of the next sentence

    # edit.extend_sentence_previous()
    #   Extend selection to the start of the previous sentence

    # edit.extend_sentence_start()
    #   Extend selection to the start of the current sentence

    def extend_up():
        actions.key("shift-up")

    def extend_word_left():
        actions.key("shift-alt-left")

    def extend_word_right():
        actions.key("shift-alt-right")

    def file_end():
        actions.key("cmd-down cmd-left")

    def file_start():
        actions.key("cmd-up cmd-left")

    def find(text: str = None):
        actions.key("cmd-f")
        if text:
            actions.insert(text)

    def find_next():
        actions.key("cmd-g")

    def find_previous():
        actions.key("cmd-shift-g")

    def indent_less():
        actions.key("cmd-left delete")

    def indent_more():
        actions.key("cmd-left tab")

    # edit.jump_column(n: int)
    #   Move cursor to column <n>

    # edit.jump_line(n: int)
    #   Move cursor to line <n>

    def jump_line(n: int):
        # This action does nothing, but is used in select_line
        pass

    def left():
        actions.key("left")

    # edit.line_clone()
    #   Create a new line identical to the current line

    def line_down():
        actions.key("down home")

    def line_end():
        actions.key("cmd-right")

    def line_insert_down():
        actions.edit.line_end()
        actions.key("enter")

    def line_insert_up():
        actions.edit.line_start()
        actions.key("enter up")

    def line_start():
        actions.key("cmd-left")

    # edit.line_swap_down()
    #   Swap the current line with the line below

    # edit.line_swap_up()
    #   Swap the current line with the line above

    def line_up():
        actions.key("up cmd-left")

    # edit.move_again()
    #   Move cursor again in the same way

    def page_down():
        actions.key("pagedown")

    def page_up():
        actions.key("pageup")

    # edit.paragraph_end()
    #   Move cursor to the end of the current paragraph

    # edit.paragraph_next()
    #   Move cursor to the start of the next paragraph

    # edit.paragraph_previous()
    #   Move cursor to the start of the previous paragraph

    # edit.paragraph_start()
    #   Move cursor to the start of the current paragraph

    def paste():
        actions.key("cmd-v")

    def paste_match_style():
        actions.key("cmd-alt-shift-v")

    def print():
        actions.key("cmd-p")

    def redo():
        actions.key("cmd-shift-z")

    def right():
        actions.key("right")

    def save():
        actions.key("cmd-s")

    def save_all():
        actions.key("cmd-shift-s")

    def select_all():
        actions.key("cmd-a")

    def select_line(n: int = None):
        # If jump_line is not implemented, this action simply selects the current line.
        if n:
            actions.edit.jump_line(n)
        actions.key("cmd-right cmd-shift-left")

    def select_lines(a: int, b: int):
        # If b is smaller, swap a and b:
        if b < a:
            a, b = b, a
        # If jump_line is not implemented, this action simply selects
        # a number of lines equal to the difference between <a> and <b>.
        actions.edit.select_line(a)
        for _ in range(0, b - a):
            actions.edit.extend_line_down()
        actions.edit.extend_line_end()

    def select_none():
        actions.key("escape")

    # edit.select_paragraph()
    #   Select the entire nearest paragraph

    # edit.select_sentence()
    #   Select the entire nearest sentence

    def select_word():
        actions.edit.right()
        actions.edit.word_left()
        actions.edit.extend_word_right()

    def selected_text() -> str:
        with clip.capture() as s:
            actions.edit.copy()
        try:
            return s.get()
        except clip.NoChange:
            return ""

    # edit.selection_clone()
    #   Insert a copy of the current selection

    # edit.sentence_end()
    #   Move cursor to the end of the current sentence

    # edit.sentence_next()
    #   Move cursor to the start of the next sentence

    # edit.sentence_previous()
    #   Move cursor to the start of the previous sentence

    # edit.sentence_start()
    #   Move cursor to the start of the current sentence

    def undo():
        actions.key("cmd-z")

    def up():
        actions.key("up")

    def word_left():
        actions.key("alt-left")

    def word_right():
        actions.key("alt-right")

    def zoom_in():
        actions.key("cmd-=")

    def zoom_out():
        actions.key("cmd--")

    def zoom_reset():
        actions.key("cmd-0")
