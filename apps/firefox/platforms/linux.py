from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: linux
app: Firefox
app: firefox
"""


@ctx.action_class("app")
class AppActions:
    @staticmethod
    def tab_next():
        actions.key("ctrl-pagedown")

    @staticmethod
    def tab_previous():
        actions.key("ctrl-pageup")


@ctx.action_class("browser")
class BrowserActions:
    @staticmethod
    def bookmark():
        actions.key("ctrl-d")

    @staticmethod
    def bookmark_tabs():
        actions.key("ctrl-shift-d")

    @staticmethod
    def bookmarks():
        actions.key("ctrl-shift-o")

    @staticmethod
    def bookmarks_bar():
        actions.key("ctrl-b")

    @staticmethod
    def focus_address():
        actions.key("ctrl-l")

    @staticmethod
    def go_blank():
        actions.key("ctrl-n")

    @staticmethod
    def go_back():
        actions.key("alt-left")

    @staticmethod
    def go_forward():
        actions.key("alt-right")

    @staticmethod
    def go_home():
        actions.key("alt-home")

    @staticmethod
    def open_private_window():
        actions.key("ctrl-shift-p")

    @staticmethod
    def reload():
        actions.key("ctrl-r")

    @staticmethod
    def reload_hard():
        actions.key("ctrl-shift-r")

    @staticmethod
    def reload_hardest():
        actions.browser.reload_hard()

    @staticmethod
    def show_clear_cache():
        actions.key("ctrl-shift-del")

    @staticmethod
    def show_downloads():
        actions.key("ctrl-shift-y")

    @staticmethod
    def show_extensions():
        actions.key("ctrl-shift-a")

    @staticmethod
    def show_history():
        actions.key("ctrl-h")

    @staticmethod
    def toggle_dev_tools():
        actions.key("ctrl-shift-i")
