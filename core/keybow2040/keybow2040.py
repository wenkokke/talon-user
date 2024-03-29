from subprocess import run

from talon import Module, actions, app

# Path to the SetLEDs executable
# <https://github.com/damieng/setledsmac>
SETLEDS = "/usr/local/bin/setleds"


mod = Module()


@mod.action_class
class KeybowActions:
    def keybow2040_set_talon_led(state: bool):
        """ """
        global SETLEDS
        if state:
            run(f'{SETLEDS} +caps -name "Keybow 2040"', shell=True)
        else:
            run(f'{SETLEDS} -caps -name "Keybow 2040"', shell=True)

    def keybow2040_set_zoom_led(state: bool):
        """ """
        global SETLEDS
        if state:
            run(f'{SETLEDS} +num -name "Keybow 2040"', shell=True)
        else:
            run(f'{SETLEDS} -num -name "Keybow 2040"', shell=True)


def on_ready():
    actions.user.keybow2040_set_talon_led(True)


app.register("ready", on_ready)
