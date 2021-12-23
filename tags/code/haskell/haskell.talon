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
  insert("| ")

# special cases for #user.code_type
type list:
  insert("[]")
  edit.left()

# equivalent of snippet "annotated expression"
has type$:
  insert(" :: ")

has type {user.code_type}$:
  insert(" :: {code_type}")

has type <user.code_type>$:
  insert(" :: {code_type}")

has type <user.code_type> over:
  insert(" :: {code_type}")

# support for #user.code_library
module <user.code_library_catch_all>$:
  insert("module {code_library_catch_all} where\n\n")

import <user.code_library>$:
  insert("import {code_library}")

import qualified <user.code_library>$:
  qualified_name = user.haskell_qualified_word(code_library)
  insert("import qualified {code_library} as {qualified_name}")

import <user.code_library> qualified:
  qualified_name = user.haskell_qualified_word(code_library)
  insert("import {code_library} qualified as {qualified_name}")

import qualified <user.code_library> letter:
  qualified_name = user.haskell_qualified_letter(code_library)
  insert("import qualified {code_library} as {qualified_name}")

import <user.code_library> qualified letter:
  qualified_name = user.haskell_qualified_letter(code_library)
  insert("import {code_library} qualified as {qualified_name}")
