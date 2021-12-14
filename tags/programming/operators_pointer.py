from talon import Context, Module

ctx = Context()
mod = Module()

# TODO: rename this tag to 'code_operators_pointer' for consistency?
mod.tag("code_operators_pointer", desc="Tag for enabling pointer operator commands")

@mod.action_class
class Actions:

    def code_operator_indirection():
        """Insert operator for pointer dereferencing (e.g., C++ *)"""

    def code_operator_address_of():
        """Insert operator for address-of (e.g., C++ &)"""

    def code_operator_structure_dereference():
        """Insert operator for structure dereferencing (e.g., C++ ->)"""
