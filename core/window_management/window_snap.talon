snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap {user.running} <user.window_snap_position>:
    user.snap_app(running, window_snap_position)
snap {user.running} [screen] <number>:
    user.move_app_to_screen(running, number)