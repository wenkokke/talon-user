tag: user.multiple_cursors
-
cursor nope:
  user.multi_cursor_undo()

cursor redo:
  user.multi_cursor_redo()

cursor multiple:
  user.multi_cursor_enable()

cursor stop:
  user.multi_cursor_disable()

cursor up:
  user.multi_cursor_add_above()

cursor down:
  user.multi_cursor_add_below()

cursor less:
  user.multi_cursor_select_fewer_occurrences()

breed:
  user.multi_cursor_select_more_occurrences()

breed all:
  user.multi_cursor_select_all_occurrences()

cursor skip:
  user.multi_cursor_skip_occurrence()

cursor lines:
  user.multi_cursor_add_to_line_ends()

