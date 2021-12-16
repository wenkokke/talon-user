tag: user.python
tag: user.auto_lang
and code.language: python
-
tag(): user.code_operator
tag(): user.code_type

# support for #user.code_type
is type {user.code_type}:
    ": {code_type}"

returns type {user.code_type}:
    "-> {code_type}"
