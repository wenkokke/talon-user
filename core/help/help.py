from talon import Module, Context, actions

mod = Module()
mod.list("help_menu", desc="")

help_menus = {
    "alphabet": (
        actions.user.help_show_alphabet,
        actions.user.help_hide_alphabet,
        actions.user.help_toggle_alphabet,
    ),
    "context": (
        actions.user.help_show_context,
        actions.user.help_hide_context,
        actions.user.help_toggle_context,
    ),
    "focus": (
        actions.user.help_show_focus,
        actions.user.help_hide_focus,
        actions.user.help_toggle_focus,
    ),
    "formatters": (
        actions.user.help_show_formatters,
        actions.user.help_hide_formatters,
        actions.user.help_toggle_formatters,
    ),
    "history": (
        actions.user.help_show_history,
        actions.user.help_hide_history,
        actions.user.help_toggle_history,
    ),
    "scope": (
        actions.user.help_show_scope,
        actions.user.help_hide_scope,
        actions.user.help_toggle_scope,
    ),
    "search": (
        actions.user.help_show_search,
        actions.user.help_hide_search,
        actions.user.help_toggle_search,
    ),
    "snippet": (
        actions.user.help_show_snippet,
        actions.user.help_hide_snippet,
        actions.user.help_toggle_snippet,
    ),
}

ctx = Context()
ctx.lists["self.help_menu"] = {help_menu: help_menu for help_menu in help_menus.keys()}


@mod.action_class
class HelpActions:
    def help_show(text: str):
        """"""
        global help_menus
        if text in help_menus:
            show, hide, toggle = help_menus[text]
            show()

    def help_hide(text: str):
        """"""
        global help_menus
        if text in help_menus:
            show, hide, toggle = help_menus[text]
            hide()

    def help_toggle(text: str):
        """"""
        global help_menus
        if text in help_menus:
            show, hide, toggle = help_menus[text]
            toggle()

    def help_hide_all():
        """"""
        global help_menus
        for show, hide, toggle in help_menus.values():
            hide()
