from talon import actions, app


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
