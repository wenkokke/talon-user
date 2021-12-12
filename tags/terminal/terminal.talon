tag: terminal
-
lisa: 
    user.terminal_list_directories()

lisa all: 
    user.terminal_list_all_directories()

katie [<user.text>]:
    user.terminal_change_directory(text or "")

katie root:
    user.terminal_change_directory_root()

katie home:
    user.terminal_change_directory_home()

katie talon user:
    user.terminal_change_directory_talon_user()

clear screen:
    user.terminal_clear_screen()

run last:
    user.terminal_run_last()

rerun [<user.text>]:
    user.terminal_rerun_search(text or "")

rerun search:
    user.terminal_rerun_search("")

kill current:
    user.terminal_kill_current()

copy paste:
    edit.copy()
    sleep(50ms)
    edit.paste()

talon repel:
    user.terminal_open_talon_repl()

talon log:
    user.terminal_open_talon_log()