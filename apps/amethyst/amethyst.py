from talon import Module, actions

mod = Module()

AMETHYST_SCREEN_KEYS = {
    1: "w",
    2: "e",
    3: "r",
    4: "q",
}

@mod.action_class
class AmethystActions:
    @staticmethod
    def amethyst_screen_focus(number: int):
        """Focus screen <number>"""
        global AMETHYST_SCREEN_KEYS
        screen_key = AMETHYST_SCREEN_KEYS[number]
        actions.key(f"alt-shift-{screen_key}")

    @staticmethod
    def amethyst_screen_throw(number: int):
        """Throw focused window to screen <number>"""
        global AMETHYST_SCREEN_KEYS
        screen_key = AMETHYST_SCREEN_KEYS[number]
        actions.key(f"ctrl-alt-shift-{screen_key}")
