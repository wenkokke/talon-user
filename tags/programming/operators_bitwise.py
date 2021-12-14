from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag("code_operators_bitwise", desc="Tag for enabling bitwise operator commands")


@mod.action_class
class Actions:

    def code_operator_bitwise_and():
        """Insert operator for bitwise AND"""

    def code_operator_bitwise_or():
        """Insert operator for bitwise OR"""

    def code_operator_bitwise_exclusive_or():
        """Insert operator for bitwise XOR"""

    def code_operator_bitwise_left_shift():
        """Insert operator for bitwise left-shift"""

    def code_operator_bitwise_right_shift():
        """Insert operator for bitwise right-shift"""
