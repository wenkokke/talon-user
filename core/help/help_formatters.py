from __future__ import annotations
from talon import Module, actions, imgui
from user.util.talon import active_list

mod = Module()

mod.mode("help_formatters", "Mode for showing the formatter help gui")

@imgui.open()
def gui(gui: imgui.GUI):
    gui.text("Formatters")
    gui.line()
    formatter_code = active_list("self.formatter_code")
    formatter_prose = active_list("self.formatter_prose")
    formatters = {**formatter_code, **formatter_prose}
    for name in sorted(set(formatters)):
        example = actions.user.format_text("one two three", formatters[name])
        gui.text(f"{name.ljust(30)}{example}")
    gui.spacer()
    if gui.button("Hide"):
        actions.user.formatters_help_hide()

@mod.action_class
class Actions:
    def help_formatters_toggle():
        """Toggle list all formatters gui"""
        if gui.showing:
            actions.mode.disable("user.help_formatters")
            gui.hide()
        else:
            gui.show()
            actions.mode.enable("user.help_formatters")

    def help_formatters_hide():
        """Hide list all formatters gui"""
        if gui.showing:
            actions.mode.disable("user.help_formatters")
            gui.hide()

    def help_formatters_show():
        """Show list all formatters gui"""
        if not gui.showing:
            gui.show()
            actions.mode.enable("user.help_formatters")
