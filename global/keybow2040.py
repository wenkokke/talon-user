from talon import actions, app
from subprocess import run
import os

# Path to the SetLEDs executable
# <https://github.com/damieng/setledsmac>
SETLEDS = "/usr/local/bin/setleds"


def set_keybow2040_talon_led(resp: str) -> None:
    if "+sleep" in resp:
        run(f'{SETLEDS} -caps -name "Keybow 2040"', shell=True)
    if "-sleep" in resp:
        run(f'{SETLEDS} +caps -name "Keybow 2040"', shell=True)


def set_keybow2040_zoom_led(resp: str) -> None:
    if "-mute" in resp:
        run(f'{SETLEDS} +num -name "Keybow 2040"', shell=True)
    else:
        run(f'{SETLEDS} -num -name "Keybow 2040"', shell=True)


def on_ready() -> None:
    # actions.user.talon_clear_mode_hooks()
    # actions.user.zoomus_clear_hooks()
    if os.path.isfile(SETLEDS) and os.access(SETLEDS, os.X_OK):
        actions.user.talon_add_mode_hook(set_keybow2040_talon_led)
        actions.user.zoomus_add_hook(set_keybow2040_zoom_led)


app.register("ready", on_ready)
