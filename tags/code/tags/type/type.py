from talon import Module, actions

mod = Module()
mod.tag("code_type", desc="Tag which provides a general list for types")
mod.list("code_type", desc="List of types")

setting_code_type_catch_all = mod.setting(
    name="code_type_catch_all", type=str, default="NOOP"
)


@mod.capture(rule="<user.text>")
def code_type_catch_all(m) -> str:
    return actions.user.format_text(str(m), setting_code_type_catch_all.get())


@mod.capture(rule="{self.code_type} | <user.code_type_catch_all>")
def code_type(m) -> str:
    return str(m)


@mod.action_class
class TypeActions:
    def insert_type(code_type: str):
        """Insert <code_type>"""
        actions.insert(code_type)
