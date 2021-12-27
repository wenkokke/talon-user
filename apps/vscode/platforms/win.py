from talon import Module, Context, actions, ui, ctrl, app

ctx = Context()
ctx.matches = r"""
os: win
app: vscode
"""

@ctx.action_class("win")
class WinActions:
    def filename():
        parts = actions.win.title().split(" - ")
        result = parts[1] if parts[0] == "[Extension Development Host]" else parts[0]
        return result if "." in result else ""

@ctx.action_class("user")
class UserActions:
    # support for #user.editor_find
    def find_replace_confirm():
        """Confirm replace current"""
        actions.key("enter")

    def find_replace_confirm_all():
        """Confirm replace all"""
        actions.key("ctrl-alt-enter")

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""
        actions.key("alt-c")

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""
        actions.key("alt-w")

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""
        actions.key("alt-r")

    def find_replace_toggle_preserve_case():
        """Toggles replace preserve case"""
        actions.key("alt-p")
