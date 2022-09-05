from logging import warning

from talon import Context, Module, actions

from user.util import csv

mod = Module()

mod.apps.vscode = """
os: linux
and app.name: Code
"""
mod.apps.vscode = """
os: mac
and app.bundle: com.microsoft.VSCode
"""
mod.apps.vscode = """
os: windows
and app.name: Visual Studio Code
os: windows
and app.exe: Code.exe
"""

ctx = Context()
ctx.matches = r"""
app: vscode
"""

# support for #user.editor_snippets
HEADER = ("Programming language", "File extension", "Spoken form", "Icon")

for lang, ext, spoken_form, icon in csv.read_rows("language_modes.csv", HEADER):
    try:
        ctx_for_lang = Context()
        csv.register_spoken_forms(
            csv_file=f"code/{lang}/snippets_vscode.csv",
            ctx=ctx_for_lang,
            list_name="user.snippet",
            value_name="Snippet name",
        )
        ctx_for_lang.matches = f"""
        app: vscode
        and tag: user.{lang}_forced
        app: vscode
        tag: user.auto_lang
        and code.language: {lang}
        """
    except FileNotFoundError:
        pass


@ctx.action_class("app")
class AppActions:

    # support for #user.tabs
    def tab_close():
        actions.user.vscode("workbench.action.closeActiveEditor")

    def tab_detach():
        pass  # don't allow detaching tabs

    def tab_next():
        actions.user.vscode("workbench.action.nextEditorInGroup")

    def tab_open():
        actions.user.vscode("workbench.action.files.newUntitledFile")

    def tab_previous():
        actions.user.vscode("workbench.action.previousEditorInGroup")

    def tab_reopen():
        actions.user.vscode("workbench.action.reopenClosedEditor")

    # support for app
    def window_close():
        actions.user.vscode("workbench.action.closeWindow")

    def window_open():
        actions.user.vscode("workbench.action.newWindow")

    def preferences():
        actions.user.vscode("workbench.action.openGlobalSettings")


@ctx.action_class("code")
class CodeActions:
    # support for #user.code_comment
    def toggle_comment():
        actions.user.vscode("editor.action.commentLine")

    # support for #user.code_suggest
    def complete():
        actions.user.vscode("editor.action.triggerSuggest")


@ctx.action_class("edit")
class EditActions:
    # overwrite default edit commands
    def save():
        actions.user.vscode("workbench.action.files.save")

    def save_all():
        actions.user.vscode("workbench.action.files.saveAll")

    def line_swap_up():
        actions.user.vscode("editor.action.moveLinesUpAction")

    def line_swap_down():
        actions.user.vscode("editor.action.moveLinesDownAction")

    def line_clone():
        actions.user.vscode("editor.action.copyLinesDownAction")

    def line_insert_up():
        actions.user.vscode("editor.action.insertLineBefore")

    def line_insert_down():
        actions.user.vscode("editor.action.insertLineAfter")

    def delete_line():
        actions.user.vscode("editor.action.deleteLines")

    def indent_more():
        actions.user.vscode("editor.action.indentLines")

    def indent_less():
        actions.user.vscode("editor.action.outdentLines")

    # support for #user.editor_jump
    def jump_line(n: int):
        actions.user.vscode("workbench.action.gotoLine")
        actions.insert(n)
        actions.key("enter")
        actions.edit.line_start()

    # support for #user.editor_find
    def find_next():
        actions.user.vscode("editor.action.nextMatchFindAction")

    def find_previous():
        actions.user.vscode("editor.action.previousMatchFindAction")

    # support for #user.zoom
    def zoom_in():
        actions.user.vscode("workbench.action.zoomIn")

    def zoom_out():
        actions.user.vscode("workbench.action.zoomOut")

    def zoom_reset():
        actions.user.vscode("workbench.action.zoomReset")


@ctx.action_class("user")
class UserActions:
    # support for #user.editor_format
    def editor_format():
        actions.user.vscode("editor.action.formatDocument")

    # support for #user.splits
    def split_window_right():
        actions.user.vscode("workbench.action.moveEditorToRightGroup")

    def split_window_left():
        actions.user.vscode("workbench.action.moveEditorToLeftGroup")

    def split_window_down():
        actions.user.vscode("workbench.action.moveEditorToBelowGroup")

    def split_window_up():
        actions.user.vscode("workbench.action.moveEditorToAboveGroup")

    def split_window_vertically():
        actions.user.vscode("workbench.action.splitEditor")

    def split_window_horizontally():
        actions.user.vscode("workbench.action.splitEditorOrthogonal")

    def split_flip():
        actions.user.vscode("workbench.action.toggleEditorGroupLayout")

    def split_window():
        actions.user.vscode("workbench.action.splitEditor")

    def split_clear():
        actions.user.vscode("workbench.action.joinTwoGroups")

    def split_clear_all():
        actions.user.vscode("workbench.action.editorLayoutSingle")

    def split_next():
        actions.user.vscode_and_wait("workbench.action.focusRightGroup")

    def split_last():
        actions.user.vscode("workbench.action.focusLeftGroup")

    # def split_number(index: int):
    #     """Navigates to a the specified split"""

    # support for #user.multiple_cursor
    def multi_cursor_undo():
        actions.user.vscode("cursorUndo")

    def multi_cursor_redo():
        actions.user.vscode("cursorRedo")

    def multi_cursor_add_above():
        actions.user.vscode("editor.action.insertCursorAbove")

    def multi_cursor_add_below():
        actions.user.vscode("editor.action.insertCursorBelow")

    def multi_cursor_add_to_line_ends():
        actions.user.vscode("editor.action.insertCursorAtEndOfEachLineSelected")

    def multi_cursor_disable():
        actions.key("escape")

    def multi_cursor_enable():
        # NOTE: vscode has no explicit mode for multiple cursors
        actions.skip()

    def multi_cursor_select_all_occurrences():
        actions.user.vscode("editor.action.selectHighlights")

    def multi_cursor_select_fewer_occurrences():
        actions.user.vscode("cursorUndo")

    def multi_cursor_select_more_occurrences():
        actions.user.vscode("editor.action.addSelectionToNextFindMatch")

    def multi_cursor_skip_occurrence():
        actions.user.vscode("editor.action.moveSelectionToNextFindMatch")

    # support for #user.snippets
    def snippet_search(text: str):
        actions.user.vscode("editor.action.insertSnippet")
        actions.insert(text)

    def snippet_insert(text: str):
        """Inserts a snippet"""
        actions.user.vscode("editor.action.insertSnippet")
        actions.insert(text)
        actions.key("enter")

    def snippet_create():
        """Triggers snippet creation"""
        actions.user.vscode("workbench.action.openSnippets")

    # support for #user.editor_find
    def find_file(text: str = None):
        actions.user.vscode("workbench.action.quickOpen")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    def find_everywhere(text: str = None):
        actions.user.vscode("workbench.action.findInFiles")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    def find_replace(text: str = None):
        """Find and replace in current file/editor"""
        actions.user.vscode("editor.action.startFindReplaceAction")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    def find_replace_everywhere(text: str = None):
        """Find and replace in entire project/all files"""
        actions.user.vscode("workbench.action.replaceInFiles")
        if text:
            actions.sleep("50ms")
            actions.insert(text)

    # support for #user.version_control
    def version_control_stage_everything():
        actions.user.vscode("git.stageAll")

    def version_control_commit(message: str):
        actions.user.vscode("git.commit")

    def version_control_push():
        actions.user.vscode("git.push")

    def version_control_pull():
        actions.user.vscode("git.pull")
