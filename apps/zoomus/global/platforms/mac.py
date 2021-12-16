from talon import Context, actions
from pathlib import *
import subprocess
from user.core import applescript


ctx = Context()
ctx.matches = r"""
os: mac
"""


def zoomus_run_applescript(name: str) -> None:
    """Runs one of the AppleScript scripts in the AppleScript subdirectory."""
    APPLESCRIPT_DIR = (Path(__file__).parent / "applescript").resolve()
    return applescript.run(APPLESCRIPT_DIR, name)


@ctx.action_class("user")
class ZoomUsActions:
    def zoomus_status() -> str:
        return zoomus_run_applescript("status")

    def zoomus_join_meeting(meeting_id: str, pwd: str) -> None:
        subprocess.run(
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
