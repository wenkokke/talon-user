from talon import Context, Module, actions

ctx = Context()
mod = Module()

# TODO: Could split into numeric, comparison, and logic?

mod.tag("code_operators_math", desc="Tag for enabling mathematical operator commands")

@mod.action_class
class Actions:

    def code_operator_subtraction():
        """Insert operator for subtraction"""

    def code_operator_addition():
        """Insert operator for addition"""

    def code_operator_multiplication():
        """Insert operator for multiplication"""

    def code_operator_exponent():
        """Insert operator for exponent"""

    def code_operator_exponent_integral():
        """Insert operator for integral exponents"""
        actions.code_operator_exponent()

    def code_operator_exponent_fractional():
        """Insert operator for fractional exponents"""
        actions.code_operator_exponent()

    def code_operator_exponent_floating():
        """Insert operator for floating exponents"""
        actions.code_operator_exponent()

    def code_operator_division():
        """Insert operator for division"""

    def code_operator_division_integral():
        """Insert operator for integral division"""
        actions.code_operator_division()

    def code_operator_division_fractional():
        """Insert operator for fractional division"""
        actions.code_operator_division()

    def code_operator_division_floating():
        """Insert operator for floating division"""
        actions.code_operator_division()

    def code_operator_modulo():
        """Insert operator for modulo"""

    def code_operator_modulo_integral():
        """Insert operator for integral modulo"""
        actions.code_operator_modulo()

    def code_operator_modulo_fractional():
        """Insert operator for fractional modulo"""
        actions.code_operator_modulo()

    def code_operator_modulo_floating():
        """Insert operator for floating modulo"""
        actions.code_operator_modulo()

    def code_operator_equal():
        """Insert operator for = comparison"""

    def code_operator_not_equal():
        """Insert operator for ≠ comparison"""

    def code_operator_greater_than():
        """Insert operator for > comparison"""

    def code_operator_greater_than_or_equal_to():
        """Insert operator for ≥ comparison"""

    def code_operator_less_than():
        """Insert operator for < comparison"""

    def code_operator_less_than_or_equal_to():
        """Insert operator for ≤ comparison"""

    def code_operator_and():
        """Insert operator for logical and (e.g., ∧)"""

    def code_operator_or():
        """Insert operator for logical or (e.g., ∨)"""
