from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag("code_operators_array", desc="Tag for enabling array operator commands")

@mod.action_class
class Actions:

    def code_operator_subscript():
        """Insert subscription operator (e.g., C++ [])"""
