from talon import Module, Context, actions


mod = Module()
mod.apps.iterm2 = """
os: mac
and app.bundle: com.googlecode.iterm2
"""


ctx = Context()
ctx.matches = r"""
app: iterm2
"""


@ctx.action_class("user")
class Actions:
    # support for user.terminal

    def terminal_list_directories():
        actions.insert("ls")
        actions.key("enter")

    def terminal_list_all_directories():
        actions.insert("ls -a")
        actions.key("enter")

    def terminal_change_directory(path: str):
        actions.insert("cd {}".format(path))
        actions.key("tab")  # autocomplete
        if path:
            actions.key("enter")

    def terminal_change_directory_root():
        actions.insert("cd /")
        actions.key("enter")

    def terminal_change_directory_home():
        actions.insert("cd")
        actions.key("enter")

    def terminal_change_directory_talon_user():
        actions.insert("cd ~/.talon/user")
        actions.key("enter")

    def terminal_clear_screen():
        actions.key("ctrl-l")

    def terminal_run_last():
        actions.key("up enter")

    def terminal_rerun_search(command: str):
        actions.key("ctrl-r")
        actions.insert(command)

    def terminal_kill_current():
        actions.key("ctrl-c")
        actions.key("enter")

    def terminal_open_talon_repl():
        actions.insert("~/.talon/bin/repl\n")

    def terminal_open_talon_log():
        actions.insert("~/.talon/bin/tail_log\n")
