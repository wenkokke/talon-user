# Defines the commands that sleep and wake Talon.
mode: all
-

# The purpose of the optional phrase is to force Talon
# to ignore whatever you say after saying 'drowse'
^drowse [<phrase>]$:
    user.talon_sleep()

^wake up$:
    user.talon_wake()

^command mode$:
    user.talon_command_mode()

^dictation mode$:
    user.talon_dictation_mode()
