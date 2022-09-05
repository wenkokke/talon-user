from talon import Context, Module, actions

mod = Module()
ctx = Context()

mod.list("delimiters_spaced", desc="List of delimiters with trailing white space")
ctx.lists["self.delimiters_spaced"] = {
    "drippy": ",",
    "drace": ",",
    "stacky": ":",
    "stace": ":",
    "dottie": ".",
    "snowy": "*",
}

mod.list("delimiter_pair", desc="List of matching pair delimiters")
matching_pairs = {
    "round": ["(", ")"],
    "square": ["[", "]"],
    "angle": ["<", ">"],
    "curly": ["{", "}"],
    "single": ["'", "'"],
    "double": ['"', '"'],
    "brick": ["`", "`"],
}
ctx.lists["self.delimiter_pair"] = matching_pairs.keys()


@mod.capture(rule="{user.delimiter_pair}")
def delimiter_pair(m) -> list[str]:
    return matching_pairs[m.delimiter_pair]


@mod.action_class
class Actions:
    def delimiters_pair_insert(pair: list[str]):
        """Insert matching pair delimiters"""
        actions.insert(f"{pair[0]}{pair[1]}")
        actions.edit.left()

    def delimiters_pair_wrap_selection(pair: list[str]):
        """Wrap selection with matching pair delimiters"""
        selection = actions.edit.selected_text()
        text = f"{pair[0]}{selection}{pair[1]}"
        actions.user.insert_paste(text)
