from talon import Context, Module, actions, registry
from user.util import csv

mod = Module()

mod.list("lang", desc="List of programming languages.")

header = ("Programming language", "File extension", "Spoken form", "Icon")

ctx = Context()
extension_to_lang = {}
spoken_form_to_lang = {}


for lang, ext, spoken_form, icon in csv.read_rows("languages.csv", header):
    if spoken_form and lang:
        spoken_form_to_lang[spoken_form] = lang
    if lang and ext:
        if not ext in extension_to_lang or extension_to_lang[ext] != lang:
            extension_to_lang[ext] = lang
            mod.tag(lang, desc=f"A tag for the {lang.capitalize()} language mode.")
            mod.tag(
                f"{lang}_forced",
                desc=f"A tag for the {lang.capitalize()} language mode (forced).",
            )
            ctx_lang = Context()
            ctx_lang.matches = f"""
            tag: user.{lang}_forced
            tag: user.auto_lang
            and code.language: {lang}
            """
            ctx_lang.tags = [f"user.{lang}"]
ctx.lists["user.lang"] = spoken_form_to_lang


# Create a mode for the automated language detection. This is active when no lang is forced.
mod.tag("auto_lang")
ctx.tags = ["user.auto_lang"]


@ctx.action_class("code")
class CodeActions:
    def language() -> str:
        global extension_to_lang
        ext = actions.win.file_ext()
        if ext in extension_to_lang:
            return extension_to_lang[ext]
        return ""


@mod.action_class
class Actions:
    def code_set_language_mode(lang: str):
        """Sets the active language mode, and disables extension matching"""
        global ctx
        ctx.tags = [f"user.{lang}_forced"]
        actions.user.notify(f"Enabled {lang} mode")

    def code_clear_language_mode():
        """Clears the active language mode, and re-enables code.language: extension matching"""
        global ctx
        ctx.tags = ["user.auto_lang"]
