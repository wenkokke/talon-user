from pathlib import Path
from user.util import applescript
from talon import Context, actions
from talon.mac import applescript

ctx = Context()
ctx.matches = r"""
os: mac
app: firefox
"""


def firefox_run_applescript(name: str) -> None:
    """Runs one of the AppleScript scripts in the AppleScript subdirectory."""
    APPLESCRIPT_DIR = (Path(__file__).parent / "applescript").resolve()
    return applescript.run(APPLESCRIPT_DIR, name)


@ctx.action_class("browser")
class BrowserActions:
    def address() -> str:
        applescript.run(
            r"""
            tell application "System Events"
                try
                    tell application process "Firefox"
                    return value of UI element 1 of combo box 1 of toolbar "Navigation" of first group of front window
                    end tell
                on error
                    return ""
                end try
            end tell
            """
        )

    def bookmark():
        actions.key("cmd-shift-d")

    def bookmark_tabs():
        actions.key("cmd-shift-d")

    def bookmarks():
        actions.key("cmd-alt-b")

    def bookmarks_bar():
        actions.key("cmd-shift-b")

    def focus_address():
        actions.key("cmd-l")

    def focus_page():
        actions.browser.focus_address()
        actions.key("f6")

    def focus_search():
        actions.key("cmd-k")

    def go(url: str):
        actions.browser.focus_address()
        actions.insert(url)
        actions.edit.enter()

    def go_back():
        actions.key("cmd-[")

    def go_blank():
        actions.browser.go("about:blank")

    def go_forward():
        actions.key("cmd-]")

    def go_home():
        actions.key("alt-home")

    def open_private_window():
        actions.key("cmd-shift-p")

    def reload():
        actions.key("cmd-r")

    def reload_hard():
        actions.key("cmd-shift-r")

    def show_clear_cache():
        actions.key("cmd-shift-delete")

    def show_downloads():
        actions.key("cmd-j")

    def show_extensions():
        actions.key("cmd-shift-a")

    def show_history():
        actions.key("cmd-shift-h")

    def submit_form():
        actions.key("enter")

    def title() -> str:
        applescript.run(
            r"""
            try
                tell application "Firefox"
                    return name of front window
                end tell
            on error
                return ""
            end try
            """
        )

    def toggle_dev_tools():
        actions.key("cmd-alt-i")
