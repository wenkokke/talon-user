from talon import Context, Module, actions

mod = Module()
mod.apps.apple_terminal = """
os: mac
and app.bundle: com.apple.Terminal
"""


ctx = Context()
ctx.matches = r"""
app: apple_terminal
"""


@ctx.action_class("user")
class Actions:

    # support for #terminal
    def terminal_clear_screen():
        actions.key("ctrl-l")

    def terminal_run_last():
        actions.key("up enter")

    def terminal_rerun_search(command: str):
        actions.key("ctrl-r")
        actions.insert(command)

    def terminal_kill_current():
        actions.key("ctrl-c")
        actions.key("enter")
