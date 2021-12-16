from pathlib import Path
from typing import Callable, Optional
from talon import Module, Context, actions, app, fs
import csv

mod = Module()

settings_directory = mod.setting(
    "settings_directory",
    type=str,
    default="settings",
    desc="The directory to use for settings CSVs relative to Talon user directory",
)


def register(csv_file: str, list_name: str, column_name: str, ctx: Context) -> None:
    """Register a CSV file as the source for a Talon list.

    Note:
        Assumes a 2-column table, where the first column is the value of interest,
        and the second column is an optional spoken form.
    """

    def on_ready_and_change(csv_table: list[list[str]]):
        csv_dict = {}
        for csv_row in csv_table:
            try:
                v, k = csv_row
                csv_dict[k] = v
            except ValueError:
                (k,) = csv_row
                csv_dict[k] = k
        ctx.lists[list_name] = csv_dict

    watch(csv_file, [column_name, "Spoken form"], on_ready_and_change)


def watch(
    csv_file: str, header: list[str], cb: Callable[[list[list[str]]], None]
) -> None:
    """Watch a CSV file for changes, and calls a callback with the new values when the file is changed.

    Note:
        If you simply wish to update a Talon list, see `register`.
    """

    def on_ready():
        csv_path = get_path(csv_file)
        cb(get_csv_list(csv_path, header))

        def on_change(path, flags):
            if csv_path.match(path):
                cb(get_csv_list(csv_path, header))

        fs.watch(csv_path.parent, on_change)

    app.register("ready", on_ready)


def csv_sanitize(text: str) -> Optional[str]:
    text = text.strip()
    if get_path(text).exists():
        return str(get_path(text).absolute())
    else:
        return text


def get_path(text: str) -> Path:
    user_dir = Path(actions.path.talon_user())
    settings_dir = Path(settings_directory.get())
    if not settings_dir.is_absolute():
        settings_dir = user_dir / settings_dir
    return (user_dir / settings_dir / text).resolve()


def get_csv_list(csv_path: Path, header: list[str] = []) -> list[list[str]]:
    with csv_path.open(newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        csv_header, *csv_rows = [[csv_sanitize(fld) for fld in row] for row in reader]
        assert header == csv_header
        return csv_rows
