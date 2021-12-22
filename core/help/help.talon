-

^help hide$:
  user.help_hide_all()

^help {self.help_menu}$:
  user.help_toggle(help_menu)

^help context {user.help_contexts}$:
  user.help_commands_context(help_contexts)

