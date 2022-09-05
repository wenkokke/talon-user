from talon import Module, actions, app, imgui, registry, ui

mod = Module()
mod.mode(
    "help_search", desc="A mode which is active if the help GUI for search is showing"
)


search_text = None
search_type = None


@imgui.open(x=ui.main_screen().x)
def gui(gui: imgui.GUI):
    gui.text(f"Search - {search_type}: {search_text}")
    gui.line()
    if search_type == "actions":
        gui_actions(gui)
    elif search_type == "commands":
        gui_commands(gui)
    if gui.button("Hide"):
        actions.user.help_search_hide()


def format_context_name(context_name: str):
    splits = context_name.split(".")
    if "talon" in splits[-1]:
        return splits[-2].replace("_", " ")
    return splits[-1].replace("_", " ")


def gui_actions(gui: imgui.GUI):
    actions = filter(lambda a: search_text in a, registry.decls.actions.keys())
    for value in sorted(actions):
        gui.text(value)
    gui.spacer()


def gui_commands(gui: imgui.GUI):
    active_contexts = registry.active_contexts()
    for context_name, context in registry.contexts.items():
        if context in active_contexts:
            commands = list(
                filter(
                    lambda c: search_text in c,
                    map(lambda c: c.rule.rule, context.commands.values()),
                )
            )
            if commands:
                gui.text(f"# {format_context_name(context_name)}")
                for command in sorted(commands):
                    gui.text(command)
                gui.spacer()


@mod.action_class
class HelpActions:
    def help_show_search():
        """Show help GUI for search"""
        if not gui.showing:
            actions.mode.enable("user.help_search")
            gui.show()

    def help_hide_search():
        """Hide help GUI for search"""
        if gui.showing:
            actions.mode.disable("user.help_search")
            gui.hide()

    def help_toggle_search():
        """Toggle help GUI for search"""
        if gui.showing:
            actions.user.help_hide_search()
        else:
            actions.user.help_show_search()

    def help_search_commands(text: str):
        """Show help search GUI with results"""
        global search_text
        search_text = text
        actions.user.help_show("search")

    def help_search_commands(text: str):
        """Show help search GUI with command results"""
        global search_text, search_type
        search_text = text
        search_type = "commands"
        actions.user.help_show("search")

    def help_search_actions(text: str):
        """Show help search GUI with actions results"""
        global search_text, search_type
        search_text = text
        search_type = "actions"
        actions.user.help_show("search")
