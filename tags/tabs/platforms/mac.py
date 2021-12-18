from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("app")
class TabActions:
    def tab_close():
        actions.key("cmd-w")

    def tab_next():
        actions.key("cmd-shift-]")

    def tab_open():
        actions.key("cmd-t")

    def tab_previous():
        actions.key("cmd-shift-[")

    def tab_reopen():
        actions.key("cmd-shift-t")
