import csv
from pathlib import Path
from typing import Any, Callable, Dict, Sequence, TypeVar

from talon import Context

SETTINGS_DIR = Path(__file__).parents[1] / "settings"


def read_rows(csv_file: str, header: Sequence[str]) -> Sequence[Sequence[str]]:
    """
    Read a CSV file as a sequence of rows, each of which is a sequence of strings.

    Note:
        The first row in the CSV file is expected to be the header,
        which is checked against the header argument and then discarded.
        This function does not check that each row has the expected number of values.
    """
    assert csv_file.endswith(".csv")
    global SETTINGS_DIR
    csv_file = (SETTINGS_DIR / csv_file).resolve()
    if csv_file.exists():
        with csv_file.open(newline="") as csv_handle:
            # Or, to use talon resource API:
            # with resource.open(str(csv_file), "r") as csv_handle:
            reader = csv.reader(csv_handle, delimiter=",")
            csv_header, *csv_rows = tuple(
                tuple(sanitize(fld) for fld in row) for row in reader
            )
            assert header == csv_header
            return tuple(csv_rows)
    else:
        return ()


Key = TypeVar("Key")
Value = TypeVar("Value")


def read_list(
    csv_file: str, value_name: str, value_type: Callable[[str], Value] = str
) -> Sequence[str]:
    """
    Read a CSV file as a simple list.

    Note:
        Assumes a 1-column table.
    """
    return tuple(
        map(lambda row: value_type(row[0]), read_rows(csv_file, (value_name,)))
    )


def read_dict(
    csv_file: str,
    key_name: str,
    value_name: str,
    key_type: Callable[[str], Key] = str,
    value_type: Callable[[str], Value] = str,
) -> Dict[Key, Value]:
    """
    Read a CSV file as a dictionary of keys to values.

    Note:
        Assumes a 2-column table, where the first column is the key and the
        second column is a value.
    """
    return {
        key_type(key): value_type(value)
        for key, value in read_rows(csv_file, (key_name, value_name))
    }


def read_spoken_forms(
    csv_file: str, value_name: str, value_type: Callable[[str], Value] = str
) -> Dict[str, Value]:
    """
    Read a CSV file as a dictionary of spoken forms to values.

    Note:
        Assumes a 2-column table, where the first column is the value of interest,
        and the second column is an optional spoken form.
        If the spoken form is missing, the value is used as the spoken form.
        NB. The order of values in the CSV file is flipped!
    """
    return {
        row[-1]: value_type(row[0])
        for row in read_rows(csv_file, (value_name, "Spoken form"))
    }


def register_spoken_forms(
    csv_file: str,
    ctx: Context,
    list_name: str,
    value_name: str,
    value_type: Callable[[str], Value] = str,
):
    """
    Register a CSV file as the source for a Talon list.

    Note:
        Assumes a 2-column table, where the first column is the value of interest,
        and the second column is an optional spoken form.
    """
    ctx.lists[list_name] = read_spoken_forms(
        csv_file, value_name=value_name, value_type=value_type
    )


def sanitize(text: str) -> str:
    text = text.strip()
    path = SETTINGS_DIR / text
    if path.exists():
        return str(path.absolute())
    else:
        return text
