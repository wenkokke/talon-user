mode: command
and mode: user.haskell
mode: command
and mode: user.auto_lang
and code.language: haskell
-
tag(): user.code_comment_line
tag(): user.code_comment_block
tag(): user.code_comment_documentation
tag(): user.code_data_bool
tag(): user.code_operators_math_extended

op implies:
  insert(" => ")

op (to | arrow):
  insert(" -> ")

op apply:
  insert(" $ ")

op map:
    insert(" <$> ")

has type:
  insert(" :: ")

make <user.text> dot$:
  constructor_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("{constructor_name}.")

make <user.text>$:
  constructor_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("{constructor_name} ")

var <user.text> dot$:
  variable_name = user.formatted_text(text, "PRIVATE_CAMEL_CASE")
  insert("{variable_name}.")

var <user.text>$:
  variable_name = user.formatted_text(text, "PRIVATE_CAMEL_CASE")
  insert("{variable_name} ")

(deaf | define) data [type] <user.text>:
  type_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("data {type_name}")
  edit.line_insert_down()
  insert("= ")

(deaf | define) type [alias] <user.text>$:
  type_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("type {type_name} = ")

(deaf | define) new type <user.text>$:
  type_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("newtype {type_name} = {type_name} ")

(deaf | define) (funk | function) <user.text>$:
  function_name = user.formatted_text(text, "PRIVATE_CAMEL_CASE")
  insert("{function_name} :: ")
  edit.line_insert_down()
  insert("{function_name} = _")
  edit.up()
  edit.line_end()

(deaf | define) class <user.text>$:
  class_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("class {class_name} where")
  edit.left()
  repeat(5)

(deaf | define) instance <user.text>$:
  instance_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("instance {instance_name} where")
  edit.left()
  repeat(5)

(deaf | define) type family <user.text>$:
  type_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("type family {type_name} ")

(deaf | define) closed type family <user.text>$:
  type_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("type family {type_name} where")
  edit.left()
  repeat(5)

(deaf | define) type instance <user.text>$:
  type_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("type instance {type_name}  = ")
  edit.left()
  repeat(2)

deriving instance <user.text> via <user.text>$:
  instance_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("deriving instance {instance_name}")

deriving instance <user.text>$:
  instance_name = user.formatted_text(text, "PUBLIC_CAMEL_CASE")
  insert("deriving instance {instance_name}")

import [<user.text>]$:
  module_name = user.formatted_text(text or "", "DOT_SEPARATED,CAPITALIZE_ALL_WORDS")
  insert("import {module_name}")

^using:
  insert(" ()")
  edit.left()

^hiding:
  insert(" hiding ()")
  edit.left()

^qualified as [<user.text>]:
  module_name = user.formatted_text(text or "", "DOT_SEPARATED,CAPITALIZE_ALL_WORDS")
  insert(" qualified as {module_name}")

^pragma:
  insert("{{-#  #-}}")
  edit.left()
  repeat(3)

^language pragma:
  insert("{{-# LANGUAGE  #-}}")
  edit.left()
  repeat(3)
