from talon import Context, actions, ui

ctx = Context()
ctx.matches = r"""
os: linux
"""


@ctx.action_class("user")
class Actions:
    def desktop(number: int):
        ui.switch_workspace(number)

    def desktop_next():
        ui.switch_workspace(ui.active_workspace() + 1)

    def desktop_previous():
        ui.switch_workspace(ui.active_workspace() - 1)

    def desktop_show():
        actions.key("super")
