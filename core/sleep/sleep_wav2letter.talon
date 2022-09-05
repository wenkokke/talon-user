mode: sleep
speech.engine: wav2letter
-
# This exists solely to prevent Talon from waking up super easily
# in sleep mode with wav2letter.
<phrase>: skip()
