from pathlib import Path
from typing import Callable, Mapping, Optional
from talon import Module, Context, actions, app, fs
import csv

mod = Module()

settings_directory = mod.setting(
    "settings_directory",
    type=str,
    default="settings",
    desc="The directory to use for settings CSVs relative to Talon user directory",
)

def watch(csv_file: str, header: list[str], cb: Callable[[list[list[str]]], None]) -> None:
    def on_ready():
        csv_path = get_csv_path(csv_file)
        cb(get_csv_list(csv_path, header))
        def on_change(path, flags):
            if csv_path.match(path):
                cb(get_csv_list(csv_path, header))
        fs.watch(csv_path.parent, on_change)
    app.register("ready", on_ready)

def csv_sanitize(text: str) -> Optional[str]:
    text = text.strip()
    if text == '-':
        return None
    else:
        return text

def get_csv_list(csv_path: Path, header: list[str] = []) -> list[list[str]]:
    with csv_path.open(newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        csv_header, *csv_rows = [[csv_sanitize(fld) for fld in row] for row in reader]
        assert header == csv_header
        return csv_rows

def get_csv_path(csv_file: str) -> Path:
    user_dir = Path(actions.path.talon_user())
    settings_dir = Path(settings_directory.get())
    if not settings_dir.is_absolute():
        settings_dir = user_dir / settings_dir
    return (settings_dir / csv_file).resolve()
