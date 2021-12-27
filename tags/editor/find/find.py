from talon import Module, actions, clip

mod = Module()
mod.tag("editor_find")


@mod.action_class
class Actions:
    def find_close():
        """Close the find dialogue"""
        actions.key("escape")

    def find_file(text: str = None):
        """Find file by file name"""

    def find_clipboard():
        """Find clipboard content in file"""
        actions.edit.find(clip.text())

    def find_everywhere(text: str = None):
        """Find in entire project/all files"""

    def find_everywhere_clipboard():
        """Find clipboard in entire project/all files"""
        actions.user.find_everywhere(clip.text())

    def find_replace(text: str = None):
        """Find and replace in current file/editor"""

    def find_replace_everywhere(text: str = None):
        """Find and replace in entire project/all files"""

    def find_replace_confirm():
        """Confirm replace current"""

    def find_replace_confirm_all():
        """Confirm replace all"""

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""

    def find_replace_toggle_preserve_case():
        """Toggles replace preserve case"""
