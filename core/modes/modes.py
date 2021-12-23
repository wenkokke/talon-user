from typing import Callable
from talon import Module, actions

# The following built-in actions may be of use:
#
# mode.disable(mode: str)
#   Disable a mode
# mode.enable(mode: str)
#   Enable a mode
# mode.restore()
#   Restore saved modes
# mode.save()
#   Save all active modes
# mode.toggle(mode: str)
#   Toggle a mode

mod = Module()


@mod.action_class
class Modes:
    """A standard action class for mode changes."""

    def toggle_sleep_mode() -> None:
        """Toggle Talon sleep mode."""
        if actions.speech.enabled():
            actions.user.talon_sleep()
        else:
            actions.user.talon_wake()

    def talon_sleep() -> None:
        """Sleep Talon."""
        actions.speech.disable()
        actions.user.keybow2040_set_talon_led(False)

    def talon_wake() -> None:
        """Wake Talon."""
        actions.speech.enable()
        actions.user.zoomus_mute()
        actions.user.keybow2040_set_talon_led(True)

    def talon_command_mode() -> None:
        """Enter command mode."""
        # actions.mode.disable("sleep")
        actions.mode.disable("dictation")
        actions.mode.enable("command")

    def talon_dictation_mode() -> None:
        """Enter dictation mode."""
        # actions.mode.disable("sleep")
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
