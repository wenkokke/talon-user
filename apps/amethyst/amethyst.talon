user.running: amethyst
-
window layout next:
    # Cycle layout forward
    key("alt-shift-space")

window layout last:
    # Cycle layout lastwards
    key("ctrl-alt-shift-space")

window shrink:
    # Shrink the main pane
    key("alt-shift-h")

window grow:
    # Expand the main pane
    key("alt-shift-l")

window more:
    # Increase main pane count
    key("alt-shift-,")

window less:
    # Decrease main pane count
    key("alt-shift-.")

window focus next:
    # Move focus clockwise
    key("alt-shift-k")

window focus last:
    # Move focus counter clockwise
    key("alt-shift-j")

window swap next:
    # Swap focused window clockwise
    key("ctrl-alt-shift-k")

window swap last:
    # Swap focused window counter clockwise
    key("ctrl-alt-shift-j")

window swap main:
    # Swap focused window with main window
    key("alt-shift-enter")

window throw left:
    # Throw focused window to space left
    key("ctrl-alt-shift-left")

window throw right:
    # Throw focused window to space right
    key("ctrl-alt-shift-right")

window throw <number>:
    # Throw focused window to space <number>
    key("ctrl-alt-shift-{number}")

screen focus <number>:
    # Focus Screen <number>
    user.amethyst_screen_focus(number)

window throw screen <number>:
    # Focus Screen 1
    user.amethyst_screen_throw(number)

window float this:
    # Toggle float for focused window
    key("alt-shift-t")

window layout show:
    # Display current layout
    key("alt-shift-i")

window layout tall:
    # Select tall layout
    key("alt-shift-a")

window layout wide:
    # Select wide layout
    key("alt-shift-s")

window layout (full|fullscreen):
    # Select fullscreen layout
    key("alt-shift-d")

window layout column:
    # Select column layout
    key("alt-shift-f")

screen focus next:
    # Move focus to clockwise screen
    key("alt-shift-n")

screen focus last:
    # Move focus to counter clockwise screen
    key("alt-shift-p")

screen swap next:
    # Swap focused window to clockwise screen
    key("ctrl-alt-shift-l")

screen swap last:
    # Swap focused window to counter clockwise screen
    key("ctrl-alt-shift-h")

window manager redo:
    # Force windows to be reevalulated
    key("alt-shift-z")

window manager restart:
    # Relaunch Amethyst
    key("ctrl-alt-shift-z")