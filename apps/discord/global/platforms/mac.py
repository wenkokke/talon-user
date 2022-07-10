from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
and user.running: discord
"""


@ctx.action_class("user")
class UserActions:
    def discord_toggle():
        actions.key("cmd-shift-m")

    def discord_deafen():
        actions.key("cmd-shift-d")

    def discord_answer_call():
        actions.key("cmd-enter")

    def discord_decline_call():
        actions.key("esc")
