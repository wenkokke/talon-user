from talon import Module, actions

mod = Module()
mod.tag("code_function", desc="Tag which provides a general list for functions")
mod.list("code_function", desc="List of functions")

setting_code_function_catch_all = mod.setting(
    name="code_function_catch_all", type=str, default="NOOP"
)


@mod.capture(rule="<user.text>")
def code_function_catch_all(m) -> str:
    return actions.user.format_text(str(m), str(setting_code_function_catch_all.get()))


@mod.capture(rule="{self.code_function} | <user.code_function_catch_all>")
def code_function(m) -> str:
    return str(m)


@mod.action_class
class FunctionActions:
    def insert_function(code_function: str):
        """Insert <code_function>"""
        actions.insert(code_function)
