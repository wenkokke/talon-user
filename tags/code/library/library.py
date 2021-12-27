from talon import Module, actions

mod = Module()
mod.tag("code_library", desc="Tag which provides a general list for libraries")
mod.list("code_library", desc="List of libraries")

setting_code_library_catch_all = mod.setting(
    name="code_library_catch_all", type=str, default="NOOP"
)


@mod.capture(rule="<user.text>")
def code_library_catch_all(m) -> str:
    return actions.user.format_text(str(m), setting_code_library_catch_all.get())


@mod.action_class
class LibraryActions:
    def insert_library(code_library: str):
        """Insert <code_library>"""
        actions.insert(code_library)
