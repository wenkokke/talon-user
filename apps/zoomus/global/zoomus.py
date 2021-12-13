from typing import Callable
from talon import Module, actions, app


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


# Hooks


def talon_sleep_on_zoomus_unmute(resp: str) -> None:
    """Sleeps Talon when zoom unmutes.

    Note:
        This only triggers when Talon unmutes Zoom.
    """
    if "-mute" in resp:
        actions.user.talon_sleep()


def zoomus_mute_on_talon_wake(resp: str) -> None:
    """Mutes Zoom when Talon wakes.

    Note:
        This does not trigger if Talon is woken up via the menu.
    """
    if "-sleep" in resp:
        actions.user.zoomus_mute()


def on_ready() -> None:
    actions.user.talon_add_mode_hook(zoomus_mute_on_talon_wake)
    actions.user.zoomus_add_hook(talon_sleep_on_zoomus_unmute)


app.register("ready", on_ready)
