from talon import Module, Context, actions

ctx = Context()
ctx.matches = r"""
tag: terminal
"""

ctx.lists["self.formatter_code_extra"] = {
    'long': "LEADING_DOUBLE_DASH,DASH_SEPARATED,TRAILING_PADDING"
}

mod = Module()
@mod.action_class
class Actions:
    @staticmethod
    def terminal_list_directories():
        """Lists directories"""

    @staticmethod
    def terminal_list_all_directories():
        """Lists all directories including hidden"""

    @staticmethod
    def terminal_change_directory(path: str):
        """Goes to the provided directory"""

    @staticmethod
    def terminal_change_directory_root():
        """Goes to the root of the current drive"""

    @staticmethod
    def terminal_change_directory_home():
        """Goes to the provided directory"""
        actions.user.terminal_change_directory(actions.path.user_home())

    @staticmethod
    def terminal_change_directory_talon_home():
        """Goes to the talon user directory"""
        actions.user.terminal_change_directory(actions.path.talon_home())

    @staticmethod
    def terminal_change_directory_talon_user():
        """Goes to the talon user directory"""
        actions.user.terminal_change_directory(actions.path.talon_user())

    @staticmethod
    def terminal_clear_screen():
        """Clear screen"""

    @staticmethod
    def terminal_run_last():
        """Repeats the last command"""

    @staticmethod
    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""

    @staticmethod
    def terminal_kill_current():
        """Kills the running command"""

    @staticmethod
    def terminal_open_talon_repl():
        """Open the Talon REPL"""

    @staticmethod
    def terminal_open_talon_log():
        """Open the Talon log"""
