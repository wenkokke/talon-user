from talon import Module

mod = Module()
mod.tag("editor_jump", desc="Editor commands which rely on jump-to-line")

# Minimal complete definition:
#
# edit.jump_column(n: int)
#   Move cursor to column <n>
# edit.jump_line(n: int)
#   Move cursor to line <n>

# The following actions have default definitions in terms of jump_line:
#
# edit.select_line(n: int = None)
#   Select entire line <n>, or current line
# edit.select_lines(a: int, b: int)
#   Select entire lines from <a> to <b>
