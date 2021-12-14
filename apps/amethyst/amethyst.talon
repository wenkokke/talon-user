user.running: amethyst
-

# NOTE: these are all the standard shortcuts with command added

window layout next:
    # Cycle layout forward
    key("alt-shift-cmd-space")

window layout last:
    # Cycle layout lastwards
    key("ctrl-alt-shift-cmd-space")

window shrink:
    # Shrink the main pane
    key("alt-shift-cmd-h")

window grow:
    # Expand the main pane
    key("alt-shift-cmd-l")

window more:
    # Increase main pane count
    key("alt-shift-cmd-,")

window less:
    # Decrease main pane count
    key("alt-shift-cmd-.")

window focus next:
    # Move focus clockwise
    key("alt-shift-cmd-k")

window focus last:
    # Move focus counter clockwise
    key("alt-shift-cmd-j")

window swap next:
    # Swap focused window clockwise
    key("ctrl-alt-shift-cmd-k")

window swap last:
    # Swap focused window counter clockwise
    key("ctrl-alt-shift-cmd-j")

window swap main:
    # Swap focused window with main window
    key("alt-shift-cmd-enter")

window throw left:
    # Throw focused window to space left
    key("ctrl-alt-shift-cmd-left")

window throw right:
    # Throw focused window to space right
    key("ctrl-alt-shift-cmd-right")

window throw <number>:
    # Throw focused window to space <number>
    key("ctrl-alt-shift-cmd-{number}")

screen focus <number>:
    # Focus Screen <number>
    key("alt-shift-cmd-f{number}")

window throw screen <number>:
    # Throw focused window to screen <number>
    key("ctrl-alt-shift-cmd-f{number}")

window float this:
    # Toggle float for focused window
    key("alt-shift-cmd-t")

window layout show:
    # Display current layout
    key("alt-shift-cmd-i")

window layout tall:
    # Select tall layout
    key("alt-shift-cmd-a")

window layout wide:
    # Select wide layout
    key("alt-shift-cmd-s")

window layout (full|fullscreen):
    # Select fullscreen layout
    key("alt-shift-cmd-d")

window layout column:
    # Select column layout
    key("alt-shift-cmd-f")

screen focus next:
    # Move focus to clockwise screen
    key("alt-shift-cmd-n")

screen focus last:
    # Move focus to counter clockwise screen
    key("alt-shift-cmd-p")

screen swap next:
    # Swap focused window to clockwise screen
    key("ctrl-alt-shift-cmd-l")

screen swap last:
    # Swap focused window to counter clockwise screen
    key("ctrl-alt-shift-cmd-h")

window manager redo:
    # Force windows to be reevalulated
    key("alt-shift-cmd-z")

window manager restart:
    # Relaunch Amethyst
    key("ctrl-alt-shift-cmd-z")