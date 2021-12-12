from talon import Module

mod = Module()
mod.tag("terminal", desc="Tag for enabling generic terminal commands")


@mod.action_class
class Actions:
    # implements the function from generic_terminal.talon for unix shells

    def terminal_list_directories():
        """Lists directories"""

    def terminal_list_all_directories():
        """Lists all directories including hidden"""

    def terminal_change_directory(path: str):
        """Goes to the provided directory"""

    def terminal_change_directory_root():
        """Goes to the root of the current drive"""

    def terminal_change_directory_home():
        """Goes to the provided directory"""

    def terminal_change_directory_talon_user():
        """Goes to the talon user directory"""

    def terminal_clear_screen():
        """Clear screen"""

    def terminal_run_last():
        """Repeats the last command"""

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""

    def terminal_kill_current():
        """Kills the running command"""

    def terminal_open_talon_repl():
        """Open the Talon REPL"""

    def terminal_open_talon_log():
        """Open the Talon log"""
