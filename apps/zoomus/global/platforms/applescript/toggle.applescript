#!/usr/bin/osascript
property muteAudio : "Mute audio"
property unmuteAudio : "Unmute audio"

if application "zoom.us" is running then
	tell application "System Events"
		tell application process "zoom.us"
			if exists (menu item muteAudio of menu 1 of menu bar item "Meeting" of menu bar 1) then
				click menu item muteAudio of menu 1 of menu bar item "Meeting" of menu bar 1
				return "+mute"
			else
				click menu item unmuteAudio of menu 1 of menu bar item "Meeting" of menu bar 1
				return "-mute"
			end if
		end tell
	end tell
else
	return ""
end if
