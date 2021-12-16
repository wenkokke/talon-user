#!/usr/bin/osascript
tell application "System Events"
  tell application process "Firefox"
    return value of UI element 1 of combo box 1 of toolbar "Navigation" of first group of front window
  end tell
end tell