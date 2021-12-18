from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("app")
class WindowActions:
    def window_close():
        actions.key("cmd-w")

    def window_hide():
        actions.key("cmd-m")

    def window_hide_others():
        actions.key("cmd-alt-h")

    def window_next():
        actions.key("cmd-`")

    def window_open():
        actions.key("cmd-n")

    def window_previous():
        actions.key("cmd-shift-`")
