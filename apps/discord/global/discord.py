from talon import Module

mod = Module()


@mod.action_class
class DiscordGlobalActions:
    def discord_status() -> str:
        """Check if Discord is muted."""

    def discord_toggle():
        """Mute or unmute Discord."""

    def discord_mute():
        """Mute Discord."""

    def discord_unmute():
        """Unmute Discord."""

    def discord_deafen():
        """Deafen Discord"""

    def discord_answer_call():
        """Answer incoming Discord call"""

    def discord_decline_call():
        """Decline incoming Discord call"""
