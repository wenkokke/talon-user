from talon import Context, Module, actions

mod = Module()

ctx = Context()
ctx.matches = r"""
mode: user.haskell
mode: user.auto_lang
and code.language: haskell
"""


ctx.lists["user.code_libraries"] = {
    "data map"  : "Data.Map",
    "data list" : "Data.List",
}

@ctx.action_class("user")
class UserActions:

    # support for comment_line

    def code_comment_line_prefix():
        actions.insert("-- ")

    # support for comment_block

    def code_comment_block():
        actions.user.code_comment_block_prefix()
        actions.user.code_comment_block_suffix()

    def code_comment_block_prefix():
        actions.insert("{- ")

    def code_comment_block_suffix():
        actions.insert(" -}")

    # support for comment_documentation

    def code_comment_documentation():
        actions.insert("-- | ")

    # support for data_bool

    def code_insert_true():
        actions.insert("True")

    def code_insert_false():
        actions.insert("False")

    # support for libraries

    def code_import():
        actions.insert("import ")

    def code_insert_library(text: str, selection: str):
        # compute abbreviation: Data.Map -> M
        abbrev = text.split('.')[-1][0]
        if selection == 'qualified-post':
            # import … qualified as …
            actions.insert("import ")
            actions.user.paste(text)
            actions.insert(" qualified as ")
            actions.user.paste(abbrev)
        elif selection == 'qualified':
            # import qualified … as …
            actions.insert("import qualified ")
            actions.user.paste(text)
            actions.insert(" as ")
            actions.user.paste(abbrev)
        else:
            # import …
            actions.insert("import ")
            actions.user.paste(text)

    # support for operators_math

    def code_operator_subtraction():
        actions.insert(" - ")

    def code_operator_addition():
        actions.insert(" + ")

    def code_operator_multiplication():
        actions.insert(" * ")

    def code_operator_exponent():
        actions.insert(" ^ ")

    def code_operator_division():
        actions.insert(" `div` ")

    def code_operator_modulo():
        actions.insert(" `mod` ")

    def code_operator_equal():
        actions.insert(" == ")

    def code_operator_not_equal():
        actions.insert(" /= ")

    def code_operator_greater_than():
        actions.insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.insert(" >= ")

    def code_operator_less_than():
        actions.insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.insert(" <= ")

    def code_operator_and():
        actions.insert(" && ")

    def code_operator_or():
        actions.insert(" || ")

    # support for operators_math (extended)

    def code_operator_exponent_fractional():
        actions.insert(" ^^ ")

    def code_operator_exponent_floating():
        actions.insert(" ** ")

    def code_operator_division_fractional():
        actions.insert(" / ")

    def code_operator_division_floating():
        actions.insert(" / ")

