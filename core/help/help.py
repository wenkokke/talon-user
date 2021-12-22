from typing import Callable, Dict
from talon import Module, Context, actions, imgui


help_guis: Dict[str, imgui.GUI] = {}
help_hooks: Dict[str, Callable[[bool], None]] = {}

mod = Module()
mod.list("help_menu", desc="A list of all available help menus")


ctx = Context()
ctx.lists["user.help_menu"] = {}


def update_help_menu_list():
    global ctx
    ctx.lists["user.help_menu"] = {name: name for name in help_guis.keys()}


@mod.action_class
class HelpActions:
    def help_show(name: str):
        """Show help GUI for <name>"""
        global help_guis, help_hooks
        actions.mode.enable(f"user.help_{name}")
        if name in help_guis and not help_guis[name].showing:
            help_guis[name].show()
            if name in help_hooks:
                help_hooks[name](True)

    def help_hide(name: str):
        """Hide help GUI for <name>"""
        global help_guis, help_hooks
        actions.mode.disable(f"user.help_{name}")
        if name in help_guis and help_guis[name].showing:
            help_guis[name].hide()
            if name in help_hooks:
                help_hooks[name](False)

    def help_toggle(name: str):
        """Toggle help GUI for <name>"""
        global help_guis
        if name in help_guis:
            if help_guis[name].showing:
                actions.user.help_hide(name)
            else:
                actions.user.help_show(name)

    def help_hide_all():
        """Hide all help help_guis"""
        global help_guis
        for name in help_guis.keys():
                actions.user.help_hide(name)

    def help_register(name: str, gui: imgui.GUI, cb: Callable[[bool], None] = None):
        """Register a help GUI"""
        global mod, help_guis, help_hooks
        mod.mode(
            f"help_{name}",
            desc=f"A mode which is active if the help GUI for {name} is showing",
        )
        help_guis[name] = gui
        if cb:
            help_hooks[name] = cb
        update_help_menu_list()
