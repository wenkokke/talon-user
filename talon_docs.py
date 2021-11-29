from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:

  def get_docstring_action(text: str) -> str:
    """Get the docstring for an action"""
    docstring = repr(eval(f"actions.{text}"))
    docstring_lines = docstring.splitlines()[1:]
    docstring_lines = [ln[4:] for ln in docstring_lines]
    docstring = "\n".join(docstring_lines)
    return docstring

  def get_docstring_actions(text: str) -> str:
    """Get the docstring for a list of actions"""
    return "; ".join(actions.user.get_docstring_action(t.strip()) for t in text.split(';'))

  def insert_docstring(text: str):
    """Insert the docstring for an action"""
    actions.insert(actions.user.get_docstring_actions(text))

