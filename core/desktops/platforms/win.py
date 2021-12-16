from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
"""


@ctx.action_class("user")
class Actions:
    def desktop_next():
        actions.key("super-ctrl-right")

    def desktop_previous():
        actions.key("super-ctrl-left")

    def desktop_show():
        actions.key("super-tab")
