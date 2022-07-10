from talon import Module, app

mod = Module()


@mod.action_class
class Actions:
    def desktop(number: int):
        """Change the current desktop"""
        app.notify("Not supported on this operating system")

    def desktop_show():
        """Shows the current desktops"""
        app.notify("Not supported on this operating system")

    def desktop_next():
        """Move to next desktop"""
        app.notify("Not supported on this operating system")

    def desktop_last():
        """Move to previous desktop"""
        app.notify("Not supported on this operating system")

    def window_move_desktop_left():
        """Move the current window to the desktop to the left"""
        app.notify("Not supported on this operating system")

    def window_move_desktop_right():
        """Move the current window to the desktop to the right"""
        app.notify("Not supported on this operating system")

    def window_move_desktop(desktop_number: int):
        """Move the current window to a different desktop"""
        app.notify("Not supported on this operating system")