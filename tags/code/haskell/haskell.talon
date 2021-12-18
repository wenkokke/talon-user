tag: user.haskell
tag: user.auto_lang
and code.language: haskell
-
tag(): user.code_function
tag(): user.code_library
tag(): user.code_operator
tag(): user.code_type
settings():
  user.code_function_catchall = "CAMEL_CASE"
  user.code_type_catchall = "PASCAL_CASE"

# special cases for #user.code_type
type list:
  insert("[]")
  edit.left()

# support for #user.code_library
import {user.code_library}:
  insert("import {code_library}")

import qualified {user.code_library}:
  qualified_name = user.haskell_qualified_word(code_library)
  insert("import qualified {code_library} as {qualified_name}")

import {user.code_library} qualified:
  qualified_name = user.haskell_qualified_word(code_library)
  insert("import {code_library} qualified as {qualified_name}")

import qualified {user.code_library} letter:
  qualified_name = user.haskell_qualified_letter(code_library)
  insert("import qualified {code_library} as {qualified_name}")

import {user.code_library} qualified letter:
  qualified_name = user.haskell_qualified_letter(code_library)
  insert("import {code_library} qualified as {qualified_name}")

# equivalent of snippet "data type"
(deaf|define) data type <user.code_type>:
  insert("data {code_type}")
  edit.line_insert_down()
  insert("= ")

add constructor:
  edit.line_insert_down()
  insert("| ")


# equivalent of snippet "generalized data type"
(deaf|define) (gene|generalized) data type <user.code_type>:
  insert("data {code_type} where")
  edit.line_insert_down()
  insert("   :: ")
  edit.left()
  repeat(4)

# equivalent of snippet "new type"
(deaf|define) new type <user.code_type>:
  insert("newtype {code_type} = {code_type} ")

# equivalent of snippet "type alias"
(deaf|define) type alias <user.code_type>:
  insert("type {code_type} = ")

# equivalent of snippet "function"
(funk|function) <user.code_function>:
  insert("{code_function} :: ")
  edit.line_insert_down()
  insert("{code_function} = _")
  edit.up()
  edit.line_end()

# equivalent of snippet "function type"
(funk|function) sig <user.code_function>:
  insert("{code_function} :: ")

# equivalent of snippet "function body"
(funk|function) def <user.code_function>:
  insert("{code_function}  = _")
  edit.left()
  repeat(3)

# equivalent of snippet "annotated expression"
has type:
  insert(" :: ")

# equivalent of snippet "parenthesized expression"
ex par:
  insert("()")
  edit.left()

# equivalent of snippet "lambda"
ex (lam|lambda):
  insert("\\ -> _")
  edit.left()
  repeat(4)

# equivalent of snippet "if"
ex if:
  insert("if ")
  edit.line_insert_down()
  insert("then _")
  edit.line_insert_down()
  insert("else _")
  edit.up()
  edit.up()
  edit.line_end()

# equivalent of snippet "let"
ex let <user.code_function>:
  insert("let")
  edit.line_insert_down()
  insert("{code_function} = _")
  edit.line_insert_down()
  insert("in _")
  edit.up()
  edit.line_end()

# equivalent of snippet "where"
ex where:
  edit.line_insert_down()
  edit.indent_more()
  insert("where")
  edit.line_insert_down()

# language pragma
language pragma:
  insert("{{-# LANGUAGE  #-}}")
  edit.left()
  repeat(3)
