tag: user.editor_snippets
-

snip {user.snippet}:
  user.snippet_insert(snippet)

snip hunt <user.text>:
  user.snippet_search(text)

snip hunt:
  user.snippet_search("")

snip create:
  user.snippet_create()

snip help:
  user.help_toggle_snippet()
