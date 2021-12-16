tag: user.python
tag: user.auto_lang
and code.language: python
-
tag(): user.code_data
tag(): user.code_exception
tag(): user.code_function
tag(): user.code_operator
tag(): user.code_type

# support for #user.code_type
is type {user.code_type}:
    ": {code_type}"

returns type {user.code_type}:
    "-> {code_type}"

# support for #user.code_exception
raise {user.code_exception}:
    "raise {code_exception}"

except {user.code_exception}:
    "except {code_exception}:"

except {user.code_exception} as:
    "except {code_exception} as :"
    edit.left()