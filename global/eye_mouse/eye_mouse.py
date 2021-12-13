from talon import Module
from talon_plugins import eye_mouse

mod = Module()

# The following actions may be of use:
#
# mouse_click(button: int = 0)
#   Press and release a mouse button
# mouse_drag(button: int = 0)
#   Hold down a mouse button
# mouse_move(x: float, y: float)
#   Move mouse to (x, y) coordinate
# mouse_release(button: int = 0)
#   Release a mouse button
# mouse_scroll(y: float = 0, x: float = 0, by_lines: bool = False)
#   Scroll the mouse wheel
# mouse_x() -> float
#   Mouse X position
# mouse_y() -> float
#   Mouse Y position

@mod.action_class
class MouseActions:

    def eye_mouse_wake():
        """Enable the eye tracker mouse."""
        eye_mouse.toggle_control(True)

    def eye_mouse_sleep():
        """Disable the eye tracker mouse."""
        eye_mouse.toggle_control(False)

    def eye_mouse_calibrate():
        """Calibrate the eye tracker mouth."""
        eye_mouse.calib_start()