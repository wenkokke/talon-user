tag: user.haskell
and tag: user.editor_find
-
^hole step$:
    edit.find(" _")
    user.find_close()
    edit.select_none()
    edit.select_word()

^hole moon$:
    edit.find(" _")
    edit.find_previous()
    edit.find_previous()
    user.find_close()
    edit.select_none()
    edit.select_word()
