from talon import Module

mod = Module()
mod.tag("tabs", desc="Tag for enabling generic tab commands")

# Minimal complete implementation:
#
# app.tab_close()
#   Close the current tab
# app.tab_detach()
#   Move the current tab to a new window
# app.tab_next()
#   Switch to next tab for this window
# app.tab_open()
#   Open a new tab
# app.tab_previous()
#   Switch to previous tab for this window
# app.tab_reopen()
#   Re-open the last-closed tab
