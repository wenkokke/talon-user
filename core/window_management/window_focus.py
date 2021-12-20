from talon import Context, Module, app, imgui, ui, actions
from talon.grammar import Phrase
from itertools import *
from user.util import csv
from user.util.speech import create_spoken_form

import os
import re
import time

mod = Module()
mod.mode("focus")
mod.list("running_application", desc="List of running applications.")

ctx = Context()
ctx.lists["self.running_application"] = {}


# Monitor running applications
def on_app_launch_or_close():
    """Update list of running applications."""
    running_application = {}
    for app in ui.apps(background=False):
        spoken_form = creates_spoken_form_app(app.name)
        if spoken_form:
            running_application[spoken_form] = app.name
        else:
            print(f"Could not pronounce {app.name}")
    ctx.lists["self.running_application"] = running_application


def creates_spoken_form_app(name: str) -> str:
    """Create a spoken form for an application name."""
    global app_name_overrides
    try:
        return app_name_overrides[name]
    except KeyError:
        name = name.removesuffix(".exe")
        name = name.split("-")[0]
        name = name.strip()
        name = create_spoken_form(name)
        return name


def on_ready():
    ui.register("app_launch", lambda _: on_app_launch_or_close())
    ui.register("app_close", lambda _: on_app_launch_or_close())


app.register("ready", on_ready)


# Monitor CSV file with application name overrides
app_name_overrides = {}

header = ("Application name", "Override")


def on_csv_change(apps: list[list[str]]):
    """Update list of application name overrides."""
    global app_name_overrides
    for app_name, app_name_override in apps:
        app_name_overrides[app_name] = app_name_override
    on_app_launch_or_close()


csv.watch("app_name_overrides.csv", header, on_csv_change)


def get_app(name: str) -> ui.App:
    for app in ui.apps(background=False):
        if app.name == name:
            return app
    spoken_form = creates_spoken_form_app(name)
    for app in ui.apps(background=False):
        if creates_spoken_form_app(app.name) == spoken_form:
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
        actions.user.help_focus_hide()
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

    def help_focus_toggle():
        """Shows/hides all running applications"""
        if gui.showing:
            actions.user.help_focus_hide()
        else:
            actions.mode.enable("user.focus")
            gui.show()

    def help_focus_hide():
        """Hides list of running applications"""
        actions.mode.disable("user.focus")
        gui.hide()

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
        actions.user.help_focus_hide()
