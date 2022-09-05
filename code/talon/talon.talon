tag: user.talon
-
tag(): user.code_function
tag(): user.code_operator

# support for dynamic reloading of talon lists
^talon mode reload$: user.talon_mode_reload()

# support for #user.code_library
require {user.code_library}: "tag: {code_library}"

set {user.code_library}: "tag(): {code_library}"
