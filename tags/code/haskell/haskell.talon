tag: user.haskell
tag: user.auto_lang
and code.language: haskell
-
tag(): user.code_library
tag(): user.code_operator

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
(deaf|define) data type <user.text>:
  type_name = user.format_text(text, "PUBLIC_CAMEL_CASE")
  insert("data {type_name}")
  edit.line_insert_down()
  insert("= ")

# equivalent of snippet "generalized data type"
(deaf|define) (gene|generalized) data type <user.text>:
  type_name = user.format_text(text, "PUBLIC_CAMEL_CASE")
  insert("data {type_name} where")
  edit.line_insert_down()
  insert("   :: ")
  edit.left()
  repeat(4)

# equivalent of snippet "new type"
(deaf|define) new type <user.text>:
  type_name = user.format_text(text, "PUBLIC_CAMEL_CASE")
  insert("newtype {type_name} = {type_name} ")

# equivalent of snippet "type alias"
(deaf|define) type alias <user.text>:
  type_name = user.format_text(text, "PUBLIC_CAMEL_CASE")
  insert("type {type_name} = ")

# equivalent of snippet "function"
(funk|function) <user.text>:
  function_name = user.format_text(text, "PRIVATE_CAMEL_CASE")
  insert("{function_name} :: ")
  edit.line_insert_down()
  insert("{function_name} = _")
  edit.up()
  edit.line_end()

# equivalent of snippet "function type"
(funk|function) sig <user.text>:
  function_name = user.format_text(text, "PRIVATE_CAMEL_CASE")
  insert("{function_name} :: ")

# equivalent of snippet "function body"
(funk|function) def <user.text>:
  function_name = user.format_text(text, "PRIVATE_CAMEL_CASE")
  insert("{function_name}  = _")
  edit.left()
  repeat(3)

# equivalent of snippet "to"
op to:
  insert(" -> ")

# equivalent of snippet "from"
op from:
  insert(" <- ")

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
ex let [<user.text>]:
  function_name = user.format_text(text or "_", "PRIVATE_CAMEL_CASE")
  insert("let")
  edit.line_insert_down()
  insert("{function_name} = _")
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

