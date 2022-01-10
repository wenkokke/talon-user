from talon import Context, actions
from talon.mac import applescript
from pathlib import *
import subprocess


ctx = Context()
ctx.matches = r"""
os: mac
"""

ZOOMUS_STATUS = r"""
    if application "zoom.us" is running then
        tell application "System Events"
            try
                tell application process "zoom.us"
                    if exists (menu item "Mute audio" of menu 1 of menu bar item "Meeting" of menu bar 1) then
                        return "on,unmuted"
                    else
                        return "on,muted"
                    end if
                end tell
            on error
                return "off"
            end try
        end tell
    else
        return "off"
    end if
    """

ZOOMUS_TOGGLE = r"""
    if application "zoom.us" is running then
        tell application "System Events"
            try
                tell application process "zoom.us"
                    if exists (menu item "Mute audio" of menu 1 of menu bar item "Meeting" of menu bar 1) then
                        click menu item "Mute audio" of menu 1 of menu bar item "Meeting" of menu bar 1
                        return "on,muted"
                    else
                        click menu item "Unmute audio" of menu 1 of menu bar item "Meeting" of menu bar 1
                        return "on,unmuted"
                    end if
                end tell
            on error
                return "off"
            end try
        end tell
    else
        return "off"
    end if
    """

ZOOMUS_MUTE = r"""
    if application "zoom.us" is running then
        tell application "System Events"
            try
                tell application process "zoom.us"
                    if exists (menu item "Mute audio" of menu 1 of menu bar item "Meeting" of menu bar 1) then
                        click menu item "Mute audio" of menu 1 of menu bar item "Meeting" of menu bar 1
                        return "on,muted"
                    else
                        return "on,muted"
                    end if
                end tell
            on error
                return "off"
            end try
        end tell
    else
        return "off"
    end if
    """

ZOOMUS_UNMUTE = r"""
    if application "zoom.us" is running then
        tell application "System Events"
            try
                tell application process "zoom.us"
                    if exists (menu item "Unmute audio" of menu of menu bar item "Meeting" of menu bar 1) then
                        click menu item "Unmute audio" of menu 1 of menu bar item "Meeting" of menu bar 1
                        return "on,unmuted"
                    else
                        return "on,unmuted"
                    end if
                end tell
            on error
                return "off"
            end try
        end tell
    else
        return "off"
    end if
    """


@ctx.action_class("user")
class ZoomUsActions:
    def zoomus_status() -> str:
        global ZOOMUS_STATUS
        return applescript.run(ZOOMUS_STATUS)

    def zoomus_join_meeting(meeting_id: str, pwd: str) -> None:
        subprocess.run(
            f'open "zoommtg://zoom.us/j/join?action=join&confno={meeting_id}&pwd={pwd}"',
            shell=True,
        )

    def zoomus_toggle() -> None:
        status = actions.user.zoomus_status()
        if status == "on,unmuted":
            actions.user.zoomus_mute()
        if status == "on,muted":
            actions.user.zoomus_unmute()

    def zoomus_mute() -> None:
        global ZOOMUS_MUTE
        status = applescript.run(ZOOMUS_MUTE)
        actions.user.keybow2040_set_zoom_led(status == "on,unmuted")

    def zoomus_unmute() -> None:
        actions.user.talon_sleep()
        global ZOOMUS_UNMUTE
        status = applescript.run(ZOOMUS_UNMUTE)
        actions.user.keybow2040_set_zoom_led(status == "on,unmuted")
