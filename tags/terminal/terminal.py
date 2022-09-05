from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
tag: terminal
"""

ctx.lists["self.formatter_code_extra"] = {
    "long": "LEADING_DOUBLE_DASH,DASH_SEPARATED,TRAILING_PADDING"
}

mod = Module()


@mod.action_class
class Actions:
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
        actions.user.terminal_change_directory(actions.path.user_home())

    def terminal_change_directory_talon_home():
        """Goes to the talon user directory"""
        actions.user.terminal_change_directory(actions.path.talon_home())

    def terminal_change_directory_talon_user():
        """Goes to the talon user directory"""
        actions.user.terminal_change_directory(actions.path.talon_user())

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
