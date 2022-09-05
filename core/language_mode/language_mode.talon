^force {user.lang}$: user.code_set_language_mode(lang)

^clear language mode$:
    user.code_clear_language_mode()
    user.notify("Cleared language modes")
