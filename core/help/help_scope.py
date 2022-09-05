from talon import Module, actions, imgui, scope, ui

mod = Module()
mod.mode(
    "help_scope", desc="A mode which is active if the help GUI for scope is showing"
)


@imgui.open(x=ui.main_screen().x)
def gui(gui: imgui.GUI):
    gui.text("Scope")
    gui.line()
    gui.spacer()
    gui.text("Modes")
    gui.line()
    for mode in sorted(scope.get("mode")):
        gui.text(mode)
    gui.spacer()
    gui.text("Tags")
    gui.line()
    for tag in sorted(scope.get("tag")):
        gui.text(tag)
    gui.spacer()
    gui.text("Misc")
    gui.line()
    ignore = {"main", "mode", "tag", "exe_path", "class"}
    keys = {*scope.data.keys(), *scope.data["main"].keys()}
    for key in sorted(keys):
        if key not in ignore:
            value = scope.get(key)
            print_value(gui, key, value, ignore)
    gui.spacer()
    if gui.button("Hide"):
        actions.user.help_hide_scope()


def print_value(gui: imgui.GUI, path: str, value, ignore: set[str] = {}):
    if isinstance(value, dict):
        for key in value:
            if key not in ignore:
                p = f"{path}.{key}" if path else key
                print_value(gui, p, value[key])
    elif value:
        gui.text(f"{path}: {format_value(value)}")


def format_value(value):
    if isinstance(value, list) or isinstance(value, set):
        return ", ".join(sorted(value))
    return value


@mod.action_class
class HelpActions:
    def help_show_scope():
        """Show help GUI for scope"""
        if not gui.showing:
            actions.mode.enable("user.help_scope")
            gui.show()

    def help_hide_scope():
        """Hide help GUI for scope"""
        if gui.showing:
            actions.mode.disable("user.help_scope")
            gui.hide()

    def help_toggle_scope():
        """Toggle help GUI for scope"""
        if gui.showing:
            actions.user.help_hide_scope()
        else:
            actions.user.help_show_scope()
