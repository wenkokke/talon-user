tag: user.line_commands
-
jump <number>:
  edit.jump_line(number)

jump <number> head:
  edit.jump_line(number)
  edit.line_start()

jump <number> tail:
  edit.jump_line(number)
  edit.line_end()

clear line <number>:
  edit.jump_line(number)
  edit.select_line(number)
  edit.delete()

clear line <number> until <number>:
    edit.select_lines(number_1, number_2)
    edit.delete()

copy line <number>:
    edit.select_lines(number, number)
    edit.copy()

copy line <number> until <number>:
    edit.select_lines(number_1, number_2)
    edit.copy()

cut line <number>:
    edit.select_lines(number, number)
    edit.cut()

cut line <number> until <number>:
    edit.select_lines(number_1, number_2)
    edit.cut()

paste over line <number> until <number>:
    edit.select_lines(number_1, number_2)
    edit.paste()

take line <number>:
    edit.select_lines(number, number)

take line <number> until <number>:
    edit.select_lines(number_1, number_2)

tab line <number>:
    edit.jump_line(number)
    edit.indent_more()

tab line <number> until <number>:
    edit.select_lines(number_1, number_2)
    edit.indent_more()

retab line <number>:
    edit.select_lines(number, number)
    edit.indent_less()

retab line <number> until <number>:
    edit.select_lines(number_1, number_2)
    edit.indent_less()

drag line <number> up:
    edit.select_lines(number, number)
    edit.line_swap_up()

drag line <number> until <number> up:
    edit.select_lines(number_1, number_2)
    edit.line_swap_up()

drag line <number> down:
    edit.select_lines(number, number)
    edit.line_swap_down()

drag line <number> until <number> down:
    edit.select_lines(number_1, number_2)
    edit.line_swap_down()