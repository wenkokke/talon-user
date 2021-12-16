from talon import Module

mod = Module()
mod.apps.firefox = """
os: mac
and app.bundle: org.mozilla.firefox
"""

# Minimal complete definition:
#
# browser.address() -> str
#   Get page URL
# browser.bookmark()
#   Bookmark the current page
# browser.bookmark_tabs()
#   Bookmark all open tabs
# browser.bookmarks()
#   Open the Bookmarks editor
# browser.bookmarks_bar()
#   Toggle the bookmarks bar
# browser.focus_address()
#   Focus address bar
# browser.focus_page()
#   Focus the page body
# browser.focus_search()
#   Focus the search box
# browser.go(url: str)
#   Go to a new URL
# browser.go_back()
#   Go back in the history
# browser.go_blank()
#   Go to a blank page
# browser.go_forward()
#   Go forward in the history
# browser.go_home()
#   Go to home page
# browser.open_private_window()
#   Open a private browsing window
# browser.reload()
#   Reload current page
# browser.reload_hard()
#   Reload current page (harder)
# browser.reload_hardest()
#   Reload current page (hardest)
# browser.show_clear_cache()
#   Show 'Clear Cache' dialog
# browser.show_downloads()
#   Show download list
# browser.show_extensions()
#   Show installed extensions
# browser.show_history()
#   Show recently visited pages
# browser.submit_form()
#   Submit the current form
# browser.title() -> str
#   Get page title
# browser.toggle_dev_tools()
#   Open or close the developer tools


# Maybe support these as well:
#
# Focus Next Link or Input Field: tab
# Focus Previous Link or Input Field: shift-tab
# Go Down a Screen: space
# Go Up a Screen: shift-space
# Go to Bottom of Page: cmd-down
# Go to Top of Page: cmd-up
# Move to Next Frame: F6
# Move to Previous Frame: shift-f6
# Save Focused Link: option-enter
# Quick Find within link-text only: '
# Quick Find: /
# Switch Search Engine: alt-down
# Close Tab: command-W
# Close Window: command-shift-W
# Cycle through Tabs in Recently Used Order: control-tab
# Quit: command-Q
# Go one Tab to the Left: control-page up
# Go one Tab to the Right: control-page down
# Go to Tab 1 to 8: command-1 to 8
# Go to Last Tab: command-9
# Move Tab Left: Ctrl-Shift-Page Up
# Move Tab Right: Ctrl-Shift-Page Down
# Move Tab to start: command-shift-home
# Move Tab to end: command-shift-end
# Mute/Unmute Audio: control-M
# Undo Close Tab: command-shift-T
# Undo Close Window: command-shift-N
