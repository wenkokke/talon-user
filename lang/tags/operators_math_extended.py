from talon import Module, actions

mod = Module()

mod.tag("code_operators_math_extended", desc="Tag for enabling typed mathematical operator commands")

@mod.action_class
class Actions:

    def code_operator_exponent_integral():
        """Insert operator for integral exponents"""
        actions.code_operator_exponent()

    def code_operator_exponent_fractional():
        """Insert operator for fractional exponents"""
        actions.code_operator_exponent()

    def code_operator_exponent_floating():
        """Insert operator for floating exponents"""
        actions.code_operator_exponent()

    def code_operator_division_integral():
        """Insert operator for integral division"""
        actions.code_operator_division()

    def code_operator_division_fractional():
        """Insert operator for fractional division"""
        actions.code_operator_division()

    def code_operator_division_floating():
        """Insert operator for floating division"""
        actions.code_operator_division()

    def code_operator_modulo_integral():
        """Insert operator for integral modulo"""
        actions.code_operator_modulo()

    def code_operator_modulo_fractional():
        """Insert operator for fractional modulo"""
        actions.code_operator_modulo()

    def code_operator_modulo_floating():
        """Insert operator for floating modulo"""
        actions.code_operator_modulo()

