-
phones this:
    user.phones_set_selected()
    user.help_show("phones")

phones step: user.phones_next()

phones moon: user.phones_previous()

phones last:
    user.history_select_last_phrase()
    user.phones_next()

phones word:
    edit.select_word()
    user.phones_next()
