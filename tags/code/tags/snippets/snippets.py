# defines placeholder actions and captures for ide-specific snippet functionality
from talon import Module, imgui, registry

mod = Module()
mod.tag("code_snippet", desc="Tag for enabling code snippet-related commands")
mod.list("code_snippet", desc="List of code snippets")


@imgui.open()
def gui(gui: imgui.GUI):
    gui.text("snippets")
    gui.line()
    if "user.code_snippet" in registry.lists:
        function_list = sorted(registry.lists["user.code_snippet"][0].keys())
        if function_list:
            for i, entry in enumerate(function_list):
                gui.text("{}".format(entry, function_list))


@mod.action_class
class Actions:
    def snippet_search(text: str):
        """Triggers the program's snippet search"""

    def snippet_insert(text: str):
        """Inserts a snippet"""

    def snippet_create():
        """Triggers snippet creation"""

    def help_snippet_toggle():
        """Toggles UI for available snippets"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()

    def help_snippet_show():
        """Show UI for available snippets"""
        if not gui.showing:
            gui.show()

    def help_snippet_hide():
        """Hide UI for available snippets"""
        if gui.showing:
            gui.hide()
