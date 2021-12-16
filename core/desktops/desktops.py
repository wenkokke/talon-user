from talon import Module

mod = Module()

@mod.action_class
class Actions:
    def desktop(number: int):
        """Change the current desktop"""

    def desktop_show():
        """Shows the current desktops"""

    def desktop_next():
        """Move to next desktop"""

    def desktop_previous():
        """Move to previous desktop"""

    def window_move_desktop_left():
        """Move the current window to the desktop to the left"""

    def window_move_desktop_right():
        """Move the current window to the desktop to the right"""

    def window_move_desktop(desktop_number: int):
        """Move the current window to a different desktop"""
