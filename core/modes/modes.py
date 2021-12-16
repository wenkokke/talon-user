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

MODE_CHANGE_HOOKS = []

mod = Module()


@mod.action_class
class Modes:
    """A standard action class for mode changes."""

    @staticmethod
    def toggle_sleep_mode() -> None:
        """Toggle Talon sleep mode."""
        if actions.speech.enabled():
            actions.user.talon_sleep()
        else:
            actions.user.talon_wake()

    @staticmethod
    def talon_add_mode_hook(cb: Callable[[str], None]) -> None:
        """Add a callback to run when Talon enters sleep mode."""
        global MODE_CHANGE_HOOKS
        MODE_CHANGE_HOOKS.append(cb)

    @staticmethod
    def talon_clear_mode_hooks() -> None:
        """Removes all existing mode change hooks."""
        global MODE_CHANGE_HOOKS
        MODE_CHANGE_HOOKS.clear()

    @staticmethod
    def talon_sleep() -> None:
        """Sleep Talon."""
        actions.speech.disable()
        global MODE_CHANGE_HOOKS
        for cb in MODE_CHANGE_HOOKS:
            cb("+sleep")

    @staticmethod
    def talon_wake() -> None:
        """Wake Talon."""
        actions.speech.enable()
        global MODE_CHANGE_HOOKS
        for cb in MODE_CHANGE_HOOKS:
            cb("-sleep")

    @staticmethod
    def talon_command_mode() -> None:
        """Enter command mode."""
        # actions.mode.disable("sleep")
        actions.mode.disable("dictation")
        actions.mode.enable("command")
        global MODE_CHANGE_HOOKS
        for cb in MODE_CHANGE_HOOKS:
            cb("+command,-dictation")

    @staticmethod
    def talon_dictation_mode() -> None:
        """Enter dictation mode."""
        # actions.mode.disable("sleep")
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
        global MODE_CHANGE_HOOKS
        for cb in MODE_CHANGE_HOOKS:
            cb("+dictation,-command,-language")
