from talon import Module, actions

mod = Module()
mod.tag("code_function", desc="Tag which provides a general list for functions")
mod.list("code_function", desc="List of functions")

setting_code_function_catchall = mod.setting(
    name="code_function_catchall", type=str, default="NOOP"
)


@mod.capture(rule="<user.text>")
def code_function_catchall(m) -> str:
    return actions.user.format_text(str(m), str(setting_code_function_catchall.get()))


@mod.capture(rule="{self.code_function} | <user.code_function_catchall>")
def code_function(m) -> str:
    return str(m)
