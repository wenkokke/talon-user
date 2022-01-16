# Formatted code phrase: "camel hello there" -> helloThere
<user.formatted_code>$:
    insert(formatted_code)
<user.formatted_code> over:
    insert(formatted_code)

# Formatted prose phrase: "sentence hello there" -> Hello there
<user.formatted_prose>$:
    auto_insert(formatted_prose)
<user.formatted_prose> over:
    auto_insert(formatted_prose)

# Formatted word: "word hello" -> hello
<user.formatted_word>:
    auto_insert(formatted_word)

# Reformat
# <user.formatters> format this:
#     user.reformat_selection(formatters)
# <user.formatters> format last:
#     user.reformat_last(formatters)
# <user.formatters> format line:
#     edit.select_line()
#     user.reformat_selection(formatters)
# <user.formatters> format word:
#     edit.select_word()
#     user.reformat_selection(formatters)



# Abbreviated word: brief application -> app
<user.abbreviation>:
    "{abbreviation}"

# Delete last
chuck last:
    user.history_clear_last_phrase()