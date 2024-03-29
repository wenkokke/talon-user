from dataclasses import dataclass

from talon import Module, actions, clip, imgui
from talon.skia.image import Image


@dataclass
class ClipItem:
    text: str
    image: Image


mod = Module()
mod.mode("clipboard_manager", "Indicates that the clipboard manager is visible")

setting_clipboard_manager_max_rows = mod.setting(
    "clipboard_manager_max_rows",
    type=int,
    default=20,
)
setting_clipboard_manager_max_cols = mod.setting(
    "clipboard_manager_max_cols",
    type=int,
    default=50,
)

clip_history: list[ClipItem] = []
ignore_next: bool = False


@imgui.open()
def gui(gui: imgui.GUI):
    max_rows = setting_clipboard_manager_max_rows.get()
    max_cols = setting_clipboard_manager_max_cols.get()
    gui.text(f"Clipboard ({len(clip_history)} / {max_rows})")
    gui.line()

    for i, item in enumerate(clip_history):
        if item.image:
            text = f"Image(width={item.image.width}, height={item.image.height})"
        else:
            text = item.text.replace("\n", "\\n")
            if len(text) > max_cols + 4:
                text = text[:max_cols] + " ..."
        gui.text(f"{i+1}: {text}")

    gui.spacer()
    if gui.button("Hide"):
        actions.user.clipboard_manager_hide()


@mod.action_class
class Actions:
    def clipboard_manager_toggle():
        """Toggle clipboard manager"""
        if gui.showing:
            actions.user.clipboard_manager_hide()
        else:
            actions.mode.enable("user.clipboard_manager")
            gui.show()

    def clipboard_manager_hide():
        """Hide clipboard manager"""
        actions.mode.disable("user.clipboard_manager")
        gui.hide()

    def clipboard_manager_update():
        """Read current clipboard and add to manager"""
        global clip_history, ignore_next
        if ignore_next:
            ignore_next = False
            return

        text = clip.text()
        if text:
            # Remove duplicates
            indexes = [i for i, item in enumerate(clip_history) if item.text == text]
            if indexes:
                clip_history.pop(indexes[0])

        try:
            image = clip.image()
        except:
            image = None

        if text or image:
            clip_history.append(ClipItem(text, image))
            shrink()

    def clipboard_manager_ignore_next():
        """Ignore next copy for clipboard manager"""
        global ignore_next
        ignore_next = True

    def clipboard_manager_remove(numbers: list[int] = None):
        """Remove clipboard manager history"""
        global clip_history
        # Remove selected history
        if numbers:
            for number in reversed(sorted(numbers)):
                validate_number(number)
                clip_history.pop(number - 1)
        # Remove entire history
        else:
            clip_history = []
            actions.user.clipboard_manager_hide()

    def clipboard_manager_split(numbers: list[int]):
        """Split clipboard content on new line to add new items to clipboard manager history"""
        global clip_history
        for number in numbers:
            validate_number(number)
        new_history = []
        for i, item in enumerate(clip_history):
            if i + 1 in numbers and item.text:
                for line in item.text.split("\n"):
                    line = line.strip()
                    if line:
                        new_history.append(ClipItem(line, None))
            else:
                new_history.append(item)
        clip_history = new_history
        shrink()

    def clipboard_manager_paste(numbers: list[int], match_style: bool = False):
        """Paste from clipboard manager"""
        texts = []
        images = []
        for number in numbers:
            validate_number(number)
            item = clip_history[number - 1]
            if item.image:
                images.append(item.image)
            else:
                texts.append(item.text)
        actions.user.clipboard_manager_hide()
        if texts:
            text = "\n".join(texts)
            clip.set_text(text)
            if match_style:
                actions.edit.paste_match_style()
            else:
                actions.edit.paste()
        for image in images:
            clip.set_image(image)
            actions.edit.paste()


def validate_number(number: range):
    if number < 1 or number > len(clip_history):
        msg = f"Clipboard manager #{number} is out of range (1-{len(clip_history)})"
        actions.user.notify(msg)
        raise ValueError(msg)


def shrink():
    global clip_history
    max_rows = setting_clipboard_manager_max_rows.get()
    if len(clip_history) > max_rows:
        clip_history = clip_history[-max_rows:]
