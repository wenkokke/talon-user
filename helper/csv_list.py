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

def register(name: str, ctx: Context = Context(), cb: Optional[Callable[[], None]] = None, ) -> None:
    def on_ready():
        csv_path = get_csv_list_path(name)
        def on_change(path, flags):
            if csv_path.match(path):
                mapping = get_csv_list(csv_path)
                ctx.lists[name] = mapping
                if cb:
                    cb()
        fs.watch(csv_path.parent, on_change)
    app.register("ready", on_ready)

def get_csv_list_path(name: str) -> Path:
    assert not name.startswith('self.')
    filename = f"{name.removeprefix('user.').replace('.', '/')}.csv"
    user_dir = Path(actions.path.talon_user())
    settings_dir = Path(settings_directory.get())
    if not settings_dir.is_absolute():
        settings_dir = user_dir / settings_dir
    return (settings_dir / filename).resolve()

def get_csv_list(path: Path) -> Mapping[str, str]:
    mapping = {}
    with path.open(newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader) # dump header
        for row in reader:
            row = list(map(str.strip, row))
            try:
                v, k = row
                mapping[k] = v
            except ValueError:
                v, = row
                mapping[v] = v
    return mapping