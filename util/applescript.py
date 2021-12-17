from pathlib import *
import subprocess
import inspect

def run(applescript_directory: Path, applescript_name: str) -> str:
    """Runs an AppleScript scripts in the AppleScript directory."""
    app = applescript_directory / f"{applescript_name}.app"
    script = applescript_directory / f"{applescript_name}.applescript"
    if not app.exists() or script.lstat().st_mtime > app.lstat().st_mtime:
        subprocess.run(["osacompile", "-o", app, script])
    resp = subprocess.check_output(["osascript", app])
    resp = resp.decode().strip()
    return resp

