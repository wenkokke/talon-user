from talon import Module, actions

mod = Module()
mod.tag("code_type", desc="Tag which provides a general list for types")
mod.list("code_type", desc="List of types")

setting_code_type_catchall = mod.setting(
    name="code_type_catchall", type=str, default="NOOP"
)


@mod.capture(rule="<user.text>")
def code_type_catchall(m) -> str:
    return actions.user.format_text(str(m), str(setting_code_type_catchall.get()))


@mod.capture(rule="{self.code_type} | <user.code_type_catchall>")
def code_type(m) -> str:
    return str(m)
