from talon import actions, app
from subprocess import run, check_output
import os

# Path to the SetLEDs executable
# <https://github.com/damieng/setledsmac>
SETLEDS = "/usr/local/bin/setleds"


def set_keybow2040_talon_led(resp: str) -> None:
    print(f"set_keybow2040_talon_led({resp})")
    if "+sleep" in resp:
        run(f'{SETLEDS} -caps -name "Keybow 2040"', shell=True)
    if "-sleep" in resp:
        run(f'{SETLEDS} +caps -name "Keybow 2040"', shell=True)


def set_keybow2040_zoom_led(resp: str) -> None:
    print(f"set_keybow2040_zoom_led({resp})")
    if "-mute" in resp:
        run(f'{SETLEDS} +num -name "Keybow 2040"', shell=True)
    else:
        run(f'{SETLEDS} -num -name "Keybow 2040"', shell=True)


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


# Due to Talon's hot reloading things can get a little bit confusing
# if you define hooks in multiple files. Therefore, all hooks are
# declared in this file. (Even those that don't directly interact with
# the Keybow 2040.)
def on_ready() -> None:
    actions.user.talon_clear_mode_hooks()
    actions.user.zoomus_clear_hooks()
    if os.path.isfile(SETLEDS) and os.access(SETLEDS, os.X_OK):
        actions.user.talon_add_mode_hook(set_keybow2040_talon_led)
        actions.user.talon_add_mode_hook(zoomus_mute_on_talon_wake)
        actions.user.zoomus_add_hook(set_keybow2040_zoom_led)
        actions.user.zoomus_add_hook(talon_sleep_on_zoomus_unmute)


app.register("ready", on_ready)
