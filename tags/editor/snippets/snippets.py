# defines placeholder actions and captures for ide-specific snippet functionality
from talon import Module, actions, imgui, registry, ui

mod = Module()
mod.mode(
    "help_snippets",
    desc="A mode which is active if the help GUI for snippet is showing",
)

mod.tag("editor_snippets", desc="Tag for enabling code snippet-related commands")
mod.list("snippet", desc="List of code snippets")


@imgui.open(x=ui.main_screen().x, y=ui.main_screen().y)
def gui(gui: imgui.GUI):
    gui.text("Snippets")
    gui.line()
    if "user.snippet" in registry.lists:
        function_list = sorted(registry.lists["user.snippet"][0].keys())
        if function_list:
            for i, entry in enumerate(function_list):
                gui.text("{}".format(entry, function_list))


@mod.action_class
class SnippetActions:
    def help_show_snippet():
        """Show help GUI for snippet"""
        if not gui.showing:
            actions.mode.enable("user.help_snippets")
            gui.show()

    def help_hide_snippet():
        """Hide help GUI for snippet"""
        if gui.showing:
            actions.mode.disable("user.help_snippets")
            gui.hide()

    def help_toggle_snippet():
        """Toggle help GUI for snippet"""
        if gui.showing:
            actions.user.help_hide_snippet()
        else:
            actions.user.help_show_snippet()

    def snippet_search(text: str):
        """Triggers the program's snippet search"""

    def snippet_insert(text: str):
        """Inserts a snippet"""

    def snippet_create():
        """Triggers snippet creation"""
