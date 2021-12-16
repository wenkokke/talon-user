from talon import Context, actions

# NOTE: some actions require easy window switcher

ctx = Context()
ctx.matches = r"""
os: linux
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
        # requires easy window switcher or equivalent
        actions.key("win-d alt-tab")

    @staticmethod
    def window_next():
        actions.key("alt-`")

    @staticmethod
    def window_open():
        # requires easy window switcher or equivalent
        actions.key("ctrl-n")

    @staticmethod
    def window_previous():
        actions.key("alt-shift-`")
