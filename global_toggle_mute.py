from talon import Module, app, actions, speech_system

mod = Module()

@mod.action_class
class Actions:
  def toggle_mute():
    """Toggle mute/unmute on various videoconferencing apps."""
    actions.key('shift-ctrl-alt-cmd-m')