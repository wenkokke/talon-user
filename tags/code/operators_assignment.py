from talon import Context, Module

ctx = Context()
mod = Module()

mod.tag("code_operators_assignment", desc="Tag for enabling assignment commands")

@mod.action_class
class Actions:

    def code_operator_assignment():
        """Insert assignment operator"""

    def code_operator_subtraction_assignment():
        """Insert operator for combined subtraction and assignment"""

    def code_operator_addition_assignment():
        """Insert operator for combined addition and assignment"""

    def code_operator_increment():
        """Insert increment operator"""

    def code_operator_multiplication_assignment():
        """Insert operator for combined multiplication and assignment"""

    def code_operator_division_assignment():
        """Insert operator for combined division and assignment"""

    def code_operator_modulo_assignment():
        """Insert operator for combined modulo and assignment"""

    def code_operator_bitwise_and_assignment():
        """Insert operator for combined logical AND and assignment"""

    def code_operator_bitwise_or_assignment():
        """Insert operator for combined logical OR and assignment"""

    def code_operator_bitwise_exclusive_or_assignment():
        """Insert operator for combined bitwise XOR and assignment"""

    def code_operator_bitwise_left_shift_assignment():
        """Insert operator for combined bitwise left-shift and assignment"""

    def code_operator_bitwise_right_shift_assignment():
        """Insert operator for combined bitwise right-shift and assignment"""
