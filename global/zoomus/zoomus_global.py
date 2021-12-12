from typing import Callable
from talon import Module


ZOOMUS_HOOKS = []


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

    def zoomus_add_hook(cb: Callable[[str], None]) -> None:
        """Add a hook which runs whenever Talon changes the Zoom mute status."""
        global ZOOMUS_HOOKS
        ZOOMUS_HOOKS.append(cb)

    def zoomus_run_hooks(resp: str) -> None:
        """Runs all the Zoom hooks."""
        global ZOOMUS_HOOKS
        for cb in ZOOMUS_HOOKS:
            cb(resp)

    def zoomus_clear_hooks() -> None:
        """Removes all existing Zoom hooks."""
        global ZOOMUS_HOOKS
        ZOOMUS_HOOKS.clear()
