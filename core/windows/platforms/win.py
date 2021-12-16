from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("app")
class WindowActions:
    @staticmethod
    def window_close():
        actions.key("alt-f4")

    @staticmethod
    def window_hide():
        actions.key("alt-space n")

    @staticmethod
    def window_hide_others():
        actions.key("win-d alt-tab")

    @staticmethod
    def window_next():
        actions.key("alt-`")

    @staticmethod
    def window_open():
        actions.key("ctrl-n")

    @staticmethod
    def window_previous():
        actions.key("alt-shift-`")
