mode: all
-

# The purpose of the optional phrase is to force Talon
# to ignore whatever you say after saying 'drowse'
^drowse [<phrase>]$:
    user.talon_sleep()

^wake up$:
    user.talon_wake()
