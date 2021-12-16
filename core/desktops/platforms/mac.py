from contextlib import contextmanager
from talon import actions, ctrl, ui, Context

ctx = Context()
ctx.matches = r"""
os: mac
"""


@contextmanager
@staticmethod
def _drag_window_mac(win=None):
    if win is None:
        win = ui.active_window()
    fs = win.children.find(AXSubrole="AXFullScreenButton")[0]
    rect = fs.AXFrame["$rect2d"]
    x = rect["x"] + rect["width"] + 5
    y = rect["y"] + rect["height"] / 2
    ctrl.mouse_move(x, y)
    ctrl.mouse_click(button=0, down=True)
    yield
    actions.sleep(0.1)
    ctrl.mouse_click(button=0, up=True)


@ctx.action_class("user")
class MacActions:
    @staticmethod
    def desktop(number: int):
        # TODO: support more than ten desktops by iterating desktop_next
        if number < 10:
            actions.key("ctrl-{}".format(number))

    @staticmethod
    def desktop_next():
        actions.key("ctrl-right")

    @staticmethod
    def desktop_previous():
        actions.key("ctrl-left")

    @staticmethod
    def desktop_show():
        actions.key("ctrl-up")

    @staticmethod
    def window_move_desktop_left():
        with _drag_window_mac():
            actions.key("ctrl-cmd-alt-left")

    @staticmethod
    def window_move_desktop_right():
        with _drag_window_mac():
            actions.key("ctrl-cmd-alt-right")

    @staticmethod
    def window_move_desktop(desktop_number: int):
        # TODO: should be moved into amethyst support
        if ui.apps(bundle="com.amethyst.Amethyst"):
            actions.key(f"ctrl-alt-shift-{desktop_number}")
        else:
            with _drag_window_mac():
                actions.key(f"ctrl-{desktop_number}")
