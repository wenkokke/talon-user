from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: linux
and user.running: discord
"""


@ctx.action_class("user")
class UserActions:
    def discord_toggle():
        actions.key("ctrl-shift-m")

    def discord_deafen():
        actions.key("ctrl-shift-d")

    def discord_answer_call():
        actions.key("ctrl-enter")

    def discord_decline_call():
        actions.key("esc")
