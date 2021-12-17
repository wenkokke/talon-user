tag: user.find
-
^scout clipboard$:
    user.find_clipboard()

^scout [<user.text>]$:
    edit.find(text or "")

^scout hide$:
    edit.find("")
    key(escape)

^scout all clipboard$:
    user.find_everywhere_clipboard()

^scout all [<user.text>]$:
    user.find_everywhere(text or "")

^replace [<user.text>]$:
    user.find_replace(text or "")

^replace all [<user.text>]$:
    user.find_replace_everywhere(text or "")

^scout case$:
    user.find_toggle_match_by_case()

^scout word$:
    user.find_toggle_match_by_word()

^scout expression$:
    user.find_toggle_match_by_regex()

^replace case$:
    user.find_replace_toggle_preserve_case()

^scout last$:
    edit.find_previous()

^scout next$:
    edit.find_next()

^replace confirm$:
    user.find_replace_confirm()

^replace confirm all$:
    user.find_replace_confirm_all()

^scout dock [<user.text>] [<user.file_extension>]$:
    text = text or ""
    file_extension = file_extension or ""
    user.find_file(text + file_extension)

^pop <user.text>$:
    edit.find(text)
    key(escape)

^pop dock <user.text> [<user.file_extension>]$:
    user.find_file(text + file_extension)
    sleep(300ms)
    key(enter)