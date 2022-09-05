from talon import Module

mod = Module()


@mod.action_class
class ZoomUsGlobalActions:
    def zoomus_status() -> str:
        """Check if Zoom is muted."""

    def zoomus_join_meeting(meeting_id: str, pwd: str) -> None:
        """Join a Zoom meeting."""

    def zoomus_toggle() -> None:
        """Mute or unmute Zoom."""

    def zoomus_mute() -> None:
        """Mute or unmute Zoom."""

    def zoomus_unmute() -> None:
        """Mute or unmute Zoom."""
