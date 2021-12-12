step back:
    edit.word_left()

step:
    edit.word_right()

go left:
    edit.left()

go right:
    edit.right()

go up:
    edit.up()

go down:
    edit.down()

head:
    edit.line_start()

tail:
    edit.line_end()

header:
    edit.file_start()

tailor:
    edit.file_end()

# selecting
select line:
    edit.select_line()

select all:
    edit.select_all()

select left:
    edit.extend_left()

select right:
    edit.extend_right()

select up:
    edit.extend_line_up()

select down:
    edit.extend_line_down()

select word:
    edit.select_word()

select word left:
    edit.extend_word_left()

select word right:
    edit.extend_word_right()

take head:
    edit.extend_line_start()

take tail:
    edit.extend_line_end()

take header:
    edit.extend_file_start()

take tailor:
    edit.extend_file_end()

# editing
indent [more]:
    edit.indent_more()

(indent less | out dent):
    edit.indent_less()

# deleting
clear line:
    edit.delete_line()

clear left:
    key(backspace)

clear right:
    key(delete)

clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

clear word:
    edit.delete_word()

clear word left:
    edit.extend_word_left()
    edit.delete()

clear word right:
    edit.extend_word_right()
    edit.delete()

clear way left:
    edit.extend_line_start()
    edit.delete()

clear way right:
    edit.extend_line_end()
    edit.delete()

clear way up:
    edit.extend_file_start()
    edit.delete()

clear way down:
    edit.extend_file_end()
    edit.delete()

clear all:
    edit.select_all()
    edit.delete()

#copy commands
copy all:
    edit.select_all()
    edit.copy()

copy word:
    edit.select_word()
    edit.copy()

copy word left:
    edit.extend_word_left()
    edit.copy()

copy word right:
    edit.extend_word_right()
    edit.copy()

copy line:
    edit.select_line()
    edit.copy()

#cut commands
cut all:
    edit.select_all()
    edit.cut()

cut word:
    edit.select_word()
    edit.cut()

cut word left:
    edit.extend_word_left()
    edit.cut()

cut word right:
    edit.extend_word_right()
    edit.cut()

cut line:
    edit.select_line()
    edit.cut()

