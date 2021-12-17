^help active$:                         user.help_commands_active_toggle()
^help search <user.text>$:             user.help_search(text)
^help context {user.help_contexts}$:   user.help_commands_context(help_contexts)

^help <user.text> commands$:           user.help_search_commands(text)
^help <user.text> actions$:            user.help_search_actions(text)

^help alphabet$:                       user.help_alphabet_toggle()
^help scope$:                          user.help_scope_toggle()
^help (format|formatters)$:            user.help_formatters_toggle()
^help focus$:                          user.help_focus_toggle()

# TODO: use a hook
^help hide$:
  user.help_alphabet_hide()
  user.help_commands_hide()
  user.help_formatters_hide()
  user.help_focus_hide()
  user.help_search_hide()
  user.help_scope_hide()
