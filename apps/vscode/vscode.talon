app: vscode
-
tag(): user.code_comment
tag(): user.code_format
tag(): user.code_snippet
tag(): user.code_suggest
tag(): user.find
tag(): user.line_commands
tag(): user.multiple_cursors
tag(): user.splits
tag(): user.tabs
tag(): user.zoom

# Alignment
align by [<user.text>]:
    user.vscode("align.by.regex")

cursor align:
    user.vscode("yo1dog.cursor-align.alignCursors")

# Snippets
snip last:                       user.vscode("jumpToPrevSnippetPlaceholder")
[snip] next:                     user.vscode("jumpToNextSnippetPlaceholder")

# Language features
suggest param:                   user.vscode("editor.action.triggerParameterHints")
imports organize:                user.vscode("editor.action.organizeImports")
problem next:                    user.vscode("editor.action.marker.nextInFiles")
problem last:                    user.vscode("editor.action.marker.prevInFiles")
problem fix:                     user.vscode("editor.action.quickFix")
refactor this:                   user.vscode("editor.action.refactor")

# Sidebar
bar (show | hide):               user.vscode("workbench.action.toggleSidebarVisibility")
bar explorer:                    user.vscode("workbench.view.explorer")
bar extensions:                  user.vscode("workbench.view.extensions")
bar outline:                     user.vscode("outline.focus")
bar debug:                       user.vscode("workbench.view.debug")
bar search:                      user.vscode("workbench.view.search")
bar source:                      user.vscode("workbench.view.scm")
bar file:                        user.vscode("workbench.files.action.showActiveFileInExplorer")
bar collapse:                    user.vscode("workbench.files.action.collapseExplorerFolders")
ref last:                        user.vscode("references-view.prev")
ref next:                        user.vscode("references-view.next")

# Panel
panel (show | hide):             user.vscode("workbench.action.togglePanel")
panel (large | small):           user.vscode("workbench.action.toggleMaximizedPanel")
panel control:                   user.vscode("workbench.panel.repl.view.focus")
panel output:                    user.vscode("workbench.panel.output.focus")
panel problems:                  user.vscode("workbench.panel.markers.view.focus")
panel terminal:                  user.vscode("workbench.action.terminal.focus")
panel debug:                     user.vscode("workbench.debug.action.toggleRepl")
panel clear:                     user.vscode("workbench.debug.panel.action.clearReplAction")

# Focus editor
focus editor:                    user.vscode("workbench.action.focusActiveEditorGroup")

# Hide sidebar and panel
hide all:
    user.vscode("workbench.action.closeSidebar")
    user.vscode("workbench.action.closePanel")
    user.vscode("closeFindWidget")

# Files / Folders
folder open:                     user.vscode("workbench.action.files.openFolder")
folder add:                      user.vscode("workbench.action.addRootFolder")
folder new:                      user.vscode("explorer.newFolder")
file open:                       user.vscode("workbench.action.files.openFile")
file new:                        user.vscode("explorer.newFile")
file open folder:                user.vscode("revealFileInOS")
file copy path:                  user.vscode("copyFilePath")

# Folding
fold this:                       user.vscode("editor.fold")
unfold this:                     user.vscode("editor.unfold")
fold recursive:                  user.vscode("editor.foldAllMarkerRegions")
unfold recursive:                user.vscode("editor.unfoldRecursively")
fold all:                        user.vscode("editor.foldAll")
unfold all:                      user.vscode("editor.unfoldAll")
fold comments:                   user.vscode("editor.foldAllBlockComments")

# Selection
take last:                       user.vscode("editor.action.addSelectionToPreviousFindMatch")
take all these:                  user.vscode("editor.action.selectHighlights")

# Find session
scout sesh [<user.text>]$:
    user.vscode_find_recent(text or "")

pop sesh <user.text>$:
    user.vscode_find_recent(text)
    key(enter)

pop sesh:
    user.vscode_find_recent("", 1)
    key(enter)

# Find a symbol
scout symbol [<user.text>]$:
    user.vscode("workbench.action.gotoSymbol")
    "{text}"

scout all symbol [<user.text>]$:
    user.vscode("workbench.action.showAllSymbols")
    "{text}"

open settings json:
    user.vscode("workbench.action.openSettingsJson")

please [<user.text>]$:
    user.vscode("workbench.action.showCommands")
    "{user.text or ''}"