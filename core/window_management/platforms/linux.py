from talon import Context, actions

# NOTE: some actions require easy window switcher

ctx = Context()
ctx.matches = r"""
os: linux
"""


@ctx.action_class("app")
class WindowActions:
    def window_close():
        actions.key("alt-f4")

    def window_hide():
        actions.key("alt-space n")

    def window_hide_others():
        # requires easy window switcher or equivalent
        actions.key("win-d alt-tab")

    def window_next():
        actions.key("alt-`")

    def window_open():
        # requires easy window switcher or equivalent
        actions.key("ctrl-n")

    def window_previous():
        actions.key("alt-shift-`")
