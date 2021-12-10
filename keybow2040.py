from talon import actions, app
from subprocess import run, check_output
import os

# Path to the SetLEDs executable
# <https://github.com/damieng/setledsmac>
SETLEDS = "/usr/local/bin/setleds"


def on_talon_sleep() -> None:
    run(f'{SETLEDS} -caps -name "Keybow 2040"', shell=True)


def on_talon_wake() -> None:
    run(f'{SETLEDS} +caps -name "Keybow 2040"', shell=True)


def on_zoomus_mute_toggle(resp: str) -> None:
    if resp == "unmuted":
        run(f'{SETLEDS} +num -name "Keybow 2040"', shell=True)
    else:
        run(f'{SETLEDS} -num -name "Keybow 2040"', shell=True)


def on_ready() -> None:
    if os.path.isfile(SETLEDS) and os.access(SETLEDS, os.X_OK):
        actions.user.add_enter_sleep_mode_hook(on_talon_sleep)
        actions.user.add_leave_sleep_mode_hook(on_talon_wake)
        actions.user.add_zoomus_mute_toggle_hook(on_zoomus_mute_toggle)


app.register("ready", on_ready)
