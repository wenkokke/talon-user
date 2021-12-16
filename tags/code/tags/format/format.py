from talon import Module

mod = Module()
mod.tag("code_format", desc="Tag for commands for formatting code")

@mod.action_class
class FormatActions:
    def code_format():
        """Format the current document."""
