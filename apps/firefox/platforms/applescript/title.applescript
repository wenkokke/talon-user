#!/usr/bin/osascript
try
  tell application "Firefox"
    return name of front window
  end tell
on error
  return ""
end try