from talon import Context, actions
from subprocess import run, check_output
from os.path import dirname, join, realpath, exists, getmtime


ctx = Context()
ctx.matches = r"""
os: mac
"""

APPLESCRIPT_DIR = join(dirname(realpath(__file__)), "applescript")


def zoomus_run_applescript(name: str) -> None:
    """Runs one of the AppleScript scripts in the AppleScript subdirectory."""
    global APPLESCRIPT_DIR
    app_path = join(APPLESCRIPT_DIR, f"{name}.app")
    script_path = join(APPLESCRIPT_DIR, f"{name}.applescript")
    if not exists(app_path) or getmtime(script_path) > getmtime(app_path):
        run(["osacompile", "-o", app_path, script_path])
    resp = check_output(["osascript", app_path])
    resp = resp.decode().strip()
    return resp


@ctx.action_class("user")
class ZoomUsActions:
    def zoomus_status() -> str:
        return zoomus_run_applescript("status")

    def zoomus_join_meeting(meeting_id: str, pwd: str) -> None:
        run(
            f'open "zoommtg://zoom.us/j/join?action=join&confno={meeting_id}&pwd={pwd}"',
            shell=True,
        )

    def zoomus_toggle() -> None:
        resp = zoomus_run_applescript("toggle")
        actions.user.zoomus_run_hooks(resp)

    def zoomus_mute() -> None:
        resp = zoomus_run_applescript("mute")
        actions.user.zoomus_run_hooks(resp)

    def zoomus_unmute() -> None:
        resp = zoomus_run_applescript("unmute")
        actions.user.zoomus_run_hooks(resp)
