from talon import Module

mod = Module()
mod.tag("code_library", desc="Tag which provides a general list for libraries")
mod.list("code_library", desc="List of libraries")

setting_code_library_catchall = mod.setting(
    name="code_library_catchall", type=str, default="NOOP"
)


# @mod.capture(rule="<user.text>")