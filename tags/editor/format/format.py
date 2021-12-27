from talon import Module

mod = Module()
mod.tag("editor_format", desc="Tag for commands for formatting code")

@mod.action_class
class FormatActions:
    def editor_format():
        """Format the current document."""
