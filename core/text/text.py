from talon import Module, actions, clip

mod = Module()


@mod.action_class
class Actions:
    def insert_paste(text: str):
        """
        Insert <text> via the clipboard.

        Note:
            Use this action to to insert text with Unicode characters.
            This function modifies the phrase history.
        """
        with clip.revert():
            clip.set_text(text)
            actions.edit.paste()
            actions.sleep("150ms")
        actions.user.history_add_phrase(text, text)

    def insert_string(text: str):
        """
        Insert <text>.

        Note:
            Use actions.user.insert_paste to to insert text with Unicode characters.
            This function modifies the phrase history.
        """
        actions.insert(text)
        actions.user.history_add_phrase(text, text)
