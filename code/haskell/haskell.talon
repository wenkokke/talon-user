tag: user.haskell_forced
tag: user.auto_lang
and code.language: haskell
-
tag(): user.code_function
tag(): user.code_library
tag(): user.code_operator
tag(): user.code_type

settings():
  user.code_function_catch_all = "CAMEL_CASE"
  user.code_library_catch_all = "CAPITALIZE_ALL_WORDS,DOT_SEPARATED"
  user.code_type_catch_all = "PASCAL_CASE"

# useful commands for adding new cases
add constructor:
  edit.line_insert_down()
  "| "

# special cases for #user.code_type
type list:
  "[]"
  edit.left()

# equivalent of snippet "annotated expression"
has type <user.code_type>$:
  " :: {code_type}"

has type <user.code_type> over:
  " :: {code_type}"
