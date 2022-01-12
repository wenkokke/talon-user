from talon import Module

mod = Module()
mod.tag("version_control", desc="Tag for enabling generic version control commands")


@mod.action_class
class VersionControlActions:
    def version_control_stage_everything():
        """Stage all changes to files already are in the repository (e.g., git add -u)."""

    def version_control_commit(message: str):
        """Commit all staged changes (e.g., git add -m <message>)."""

    def version_control_push():
        """Push all commits to remote host."""

    def version_control_pull():
        """Pull all commits from remote host."""
