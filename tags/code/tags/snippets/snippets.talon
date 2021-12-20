tag: user.code_snippet
-

snip {user.code_snippet}:
  user.snippet_insert(code_snippet)

snip hunt <user.text>:
  user.snippet_search(text)

snip hunt:
  user.snippet_search("")

snip create:
  user.snippet_create()

snip help:
  user.help_snippet_toggle()
