from talon import Module, Context, actions


mod = Module()
mod.apps.iterm2 = """
os: mac
and app.bundle: com.googlecode.iterm2
"""


ctx = Context()
ctx.matches = r"""
os: mac
and app.bundle: com.googlecode.iterm2
"""


@ctx.action_class("user")
class Actions:

    # support for #terminal

    @staticmethod
    def terminal_clear_screen():
        actions.key("ctrl-l")

    @staticmethod
    def terminal_run_last():
        actions.key("up enter")

    @staticmethod
    def terminal_rerun_search(command: str):
        actions.key("ctrl-r")
        actions.insert(command)

    @staticmethod
    def terminal_kill_current():
        actions.key("ctrl-c")
        actions.key("enter")
