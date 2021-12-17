
from typing import Mapping
from talon import registry

def active_list(list_name: str) -> Mapping[str, str]:
    result = {}
    for ctx in registry.active_contexts():
        try:
            for k, v in ctx.lists[list_name].items():
                result[v] = k
        except KeyError:
            pass
    return result