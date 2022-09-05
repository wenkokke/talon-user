from os.path import join

from talon import Context, Module, actions

# NOTE: activating #user.terminal_posix provides support for a portion of #terminal

mod = Module()
mod.tag("terminal_posix", desc="Tag for enabling generic BASH shell commands")

ctx = Context()
ctx.matches = r"""
tag: user.terminal_posix
"""


@ctx.action_class("user")
class Actions:
    def terminal_list_directories():
        actions.insert("ls")
        actions.key("enter")

    def terminal_list_all_directories():
        actions.insert("ls -lAF -G")
        actions.key("enter")

    def terminal_change_directory(path: str):
        actions.insert(f"cd {path}")
        if path:
            actions.key("enter")

    def terminal_change_directory_root():
        actions.user.terminal_change_directory("/")

    def terminal_open_talon_repl():
        actions.insert(join(actions.path.talon_home(), "bin", "repl"))
        actions.key("enter")

    def terminal_open_talon_log():
        actions.insert(join(actions.path.talon_home(), "bin", "tail_log"))
        actions.key("enter")
