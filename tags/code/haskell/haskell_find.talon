tag: user.haskell_forced
and tag: user.find
tag: user.auto_lang
and code.language: haskell
and tag: user.find
-
^hole next$:
  edit.find(" _")
  user.find_close()
  edit.select_none()
  edit.select_word()
