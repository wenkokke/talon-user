from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: mac
app: firefox
"""


@ctx.action_class("browser")
class BrowserActions:
    @staticmethod
    def bookmark():
        actions.key("cmd-d")

    @staticmethod
    def bookmark_tabs():
        actions.key("cmd-shift-d")

    @staticmethod
    def bookmarks():
        actions.key("cmd-alt-b")
        # action(browser.bookmarks_bar):
        # 	key(ctrl-shift-b)

    @staticmethod
    def focus_address():
        actions.key("cmd-l")
        # action(browser.focus_page):

    @staticmethod
    def go_blank():
        actions.key("cmd-n")

    @staticmethod
    def go_back():
        actions.key("cmd-left")

    @staticmethod
    def go_forward():
        actions.key("cmd-right")

    @staticmethod
    def go_home():
        actions.key("cmd-shift-h")

    @staticmethod
    def open_private_window():
        actions.key("cmd-shift-p")

    @staticmethod
    def reload():
        actions.key("cmd-r")

    @staticmethod
    def reload_hard():
        actions.key("cmd-shift-r")

    @staticmethod
    def reload_hardest():
        actions.browser.reload_hard()

    @staticmethod
    def show_clear_cache():
        actions.key("cmd-shift-delete")

    @staticmethod
    def show_downloads():
        actions.key("cmd-shift-j")

    @staticmethod
    def show_extensions():
        actions.key("cmd-shift-a")

    @staticmethod
    def show_history():
        actions.key("cmd-y")

    @staticmethod
    def toggle_dev_tools():
        actions.key("cmd-alt-i")
