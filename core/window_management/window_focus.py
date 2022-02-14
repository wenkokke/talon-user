from talon import Context, Module, app, imgui, ui, actions
from talon.grammar import Phrase
from itertools import *
from user.util.speech import create_spoken_forms_app

import time

mod = Module()
mod.mode("help_focus")
mod.list("running_application", desc="List of running applications")

ctx = Context()
ctx.lists["self.running_application"] = {}


# Monitor running applications
def on_ready_app_launch_or_close():
    """Update list of running applications."""
    app_running = {}
    for app in ui.apps(background=False):
        for spoken_form in create_spoken_forms_app(app.name):
            app_running[spoken_form] = app.name
    ctx.lists["self.running_application"] = app_running


def on_ready():
    on_ready_app_launch_or_close()
    ui.register("app_launch", lambda _: on_ready_app_launch_or_close())
    ui.register("app_close", lambda _: on_ready_app_launch_or_close())


app.register("ready", on_ready)


def get_app(name: str) -> ui.App:

    # fast check
    for app in ui.apps(background=False):
        if app.name == name:
            return app

    # slower check
    name_spoken_forms = set(create_spoken_forms_app(name))
    for app in ui.apps(background=False):
        app_spoken_forms = set(create_spoken_forms_app(app.name))
        if not name_spoken_forms.isdisjoint(app_spoken_forms):
            return app
    raise RuntimeError(f'App not running: "{name}"')


def cycle_windows(app: ui.App, diff: int):
    active = ui.active_window()
    windows = list(
        filter(lambda w: w == active or (not w.hidden and w.title != ""), app.windows())
    )
    current = windows.index(active)
    max = len(windows) - 1
    i = actions.user.cycle(current + diff, 0, max)
    while i != current:
        try:
            actions.user.focus_window(windows[i])
            break
        except:
            i = actions.user.cycle(i + diff, 0, max)


def focus_name(name: str):
    app = get_app(name)
    # Focus next window on same app
    if app == ui.active_app():
        cycle_windows(app, 1)
    # Focus app
    else:
        actions.user.focus_app(app)


@mod.action_class
class Actions:
    def focus_name(name: str, phrase: Phrase = None):
        """Focus application by name"""
        focus_name(name)
        actions.user.help_hide_focus()
        if phrase:
            actions.sleep("200ms")
            actions.user.rephrase(phrase)

    def focus_names(names: list[str], phrases: list[Phrase]):
        """Focus applications by name"""
        for n, p in zip(names, phrases):
            actions.user.focus_name(n, p)

    def focus_index(index: int):
        """Focus application by index"""
        names = list(ctx.lists["user.running_application"].values())
        if index > -1 and index < len(names):
            actions.user.focus_name(names[index])

    def focus_app(app: ui.App):
        """Focus app and wait until finished"""
        app.focus()
        t1 = time.monotonic()
        while ui.active_app() != app:
            if time.monotonic() - t1 > 1:
                raise RuntimeError(f"Can't focus app: {app.name}")
            actions.sleep("50ms")

    def focus_window(window: ui.Window):
        """Focus window and wait until finished"""
        window.focus()

        t1 = time.monotonic()
        while ui.active_window() != window:
            if time.monotonic() - t1 > 1:
                raise RuntimeError(f"Can't focus window: {window.title}")
            actions.sleep("50ms")

    def help_show_focus():
        """Show help GUI for focus"""
        if not gui.showing:
            actions.mode.enable("user.help_focus")
            gui.show()

    def help_hide_focus():
        """Hide help GUI for focus"""
        if gui.showing:
            actions.mode.disable("user.help_focus")
            gui.hide()

    def help_toggle_focus():
        """Toggle help GUI for focus"""
        if gui.showing:
            actions.user.help_hide_focus()
        else:
            actions.user.help_show_focus()


@imgui.open(x=ui.main_screen().x)
def gui(gui: imgui.GUI):
    gui.text("Focus")
    gui.line()
    index = 1
    for name in ctx.lists["self.running_application"]:
        gui.text(f"Focus {index}: {name}")
        index += 1
    gui.spacer()
    if gui.button("Hide"):
        actions.user.help_hide_focus()

