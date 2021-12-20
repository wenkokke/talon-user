from talon import Module, actions, imgui, Module, scope, ui

mod = Module()
mod.mode("help_scope", "Mode for showing the scope help gui")

main_screen = ui.main_screen()


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
        actions.user.help_active_context_toggle()


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
class Actions:
    def help_scope_toggle():
        """Toggle help scope gui"""
        if gui.showing:
            actions.mode.disable("user.help_scope")
            gui.hide()
        else:
            actions.mode.enable("user.help_scope")
            gui.show()

    def help_scope_show():
        """Show help scope gui"""
        if not gui.showing:
            actions.mode.enable("user.help_scope")
            gui.show()

    def help_scope_hide():
        """Hide help scope gui"""
        if gui.showing:
            actions.mode.disable("user.help_scope")
            gui.hide()