#!/usr/bin/osascript
tell application "System Events"
  try
    tell application process "Firefox"
      return value of UI element 1 of combo box 1 of toolbar "Navigation" of first group of front window
    end tell
  on error
      return ""
  end try
end tell
