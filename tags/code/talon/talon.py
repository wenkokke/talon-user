from talon import Module, Context, registry
from user.util import csv
from user.util.speech import create_spoken_form


ctx = Context()
ctx.matches = r"""
tag: user.talon
tag: user.auto_lang
and code.language: talon
"""

# support for #user.code_operator
csv.register(
    csv_file="code/talon/operators.csv",
    list_name="user.code_operator",
    column_name="Operator",
    ctx=ctx,
)


mod = Module()


@mod.action_class
class TalonActions:
    def talon_mode_reload():
        """Dynamically reload the editor support from the Talon registry."""
        global ctx
        # functions
        code_function = {}
        for action in registry.decls.actions:
            spoken_form = create_spoken_form(action)
            code_function[spoken_form] = action
        ctx.lists["user.code_function"] = code_function
        # libraries
        code_library = {}
        for tag in registry.decls.tags:
            spoken_form = create_spoken_form(tag)
            code_library[spoken_form] = tag
        ctx.lists["user.code_library"] = code_library
