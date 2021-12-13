from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("app")
class WindowActions:
    @staticmethod
    def window_close():
        actions.key("cmd-w")

    @staticmethod
    def window_hide():
        actions.key("cmd-m")

    @staticmethod
    def window_hide_others():
        actions.key("cmd-alt-h")

    @staticmethod
    def window_next():
        actions.key("cmd-`")

    @staticmethod
    def window_open():
        actions.key("cmd-n")

    @staticmethod
    def window_previous():
        actions.key("cmd-shift-`")
