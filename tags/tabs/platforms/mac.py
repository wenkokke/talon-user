from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
"""


@ctx.action_class("app")
class TabActions:
    @staticmethod
    def tab_close():
        actions.key("cmd-w")

    @staticmethod
    def tab_next():
        actions.key("cmd-shift-]")

    @staticmethod
    def tab_open():
        actions.key("cmd-t")

    @staticmethod
    def tab_previous():
        actions.key("cmd-shift-[")

    @staticmethod
    def tab_reopen():
        actions.key("cmd-shift-t")
