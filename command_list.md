# generic_editor.talon
`find it`
: Open Find dialog, optionally searching for text.

`next one`
: Select next Find result.

`go word left`
: Move cursor left one word.

`go word right`
: Move cursor right one word.

`go left`
: Move cursor left one column.

`go right`
: Move cursor right one column.

`go up`
: Move cursor up one row.

`go down`
: Move cursor down one row.

`go line start`
: Move cursor to start of line.

`go line end`
: Move cursor to end of line.

`go way left`
: Move cursor to start of line.

`go way right`
: Move cursor to end of line.

`go way down`
: Move cursor to end of file (start of line).

`go way up`
: Move cursor to start of file.

`go bottom`
: Move cursor to end of file (start of line).

`go top`
: Move cursor to start of file.

`go page down`
: Move cursor down one page.

`go page up`
: Move cursor up one page.

`select line`
: Select entire line `<n>`, or current line.

`select all`
: Select all text in the current document.

`select left`
: Extend selection left one column.

`select right`
: Extend selection right one column.

`select up`
: Extend selection up one full line.

`select down`
: Extend selection down one full line.

`select word`
: Select word under cursor.

`select word left`
: Extend selection left one word.

`select word right`
: Extend selection right one word.

`select way left`
: Extend selection to start of line.

`select way right`
: Extend selection to end of line.

`select way up`
: Extend selection to start of file.

`select way down`
: Extend selection to end of file.

`indent [more`
: Add a tab stop of indentation.

`(indent less | out dent)`
: Remove a tab stop of indentation.

`clear line`
: Delete line under cursor.

`clear left`
: Press backspace.

`clear right`
: Press delete.

`clear up`
: Extend selection up one full line; Delete selection.

`clear down`
: Extend selection down one full line; Delete selection.

`clear word`
: Delete word under cursor.

`clear word left`
: Extend selection left one word; Delete selection.

`clear word right`
: Extend selection right one word; Delete selection.

`clear way left`
: Extend selection to start of line; Delete selection.

`clear way right`
: Extend selection to end of line; Delete selection.

`clear way up`
: Extend selection to start of file; Delete selection.

`clear way down`
: Extend selection to end of file; Delete selection.

`clear all`
: Select all text in the current document; Delete selection.

`copy all`
: Select all text in the current document; Copy selection to clipboard.

`copy word`
: Select word under cursor; Copy selection to clipboard.

`copy word left`
: Extend selection left one word; Copy selection to clipboard.

`copy word right`
: Extend selection right one word; Copy selection to clipboard.

`copy line`
: Select entire line `<n>`, or current line; Copy selection to clipboard.

`cut all`
: Select all text in the current document; Cut selection to clipboard.

`cut word`
: Select word under cursor; Cut selection to clipboard.

`cut word left`
: Extend selection left one word; Cut selection to clipboard.

`cut word right`
: Extend selection right one word; Cut selection to clipboard.

`cut line`
: Select entire line `<n>`, or current line; Cut selection to clipboard.

# find_and_replace.talon

`hunt this`
: Finds text in current editor.

`hunt this <user.text>`
: Finds text in current editor.

`hunt all`
: Finds text across project.

`hunt all <user.text>`
: Finds text across project.

`hunt case`
: Toggles find match by case sensitivity.

`hunt word`
: Toggles find match by whole words.

`hunt expression`
: Toggles find match by regex.

`hunt next`
: Navigates to the next occurrence.

`hunt previous`
: Navigates to the previous occurrence.

`replace this [<user.text>]`
: Search and replace for text in the active editor.

`replace all`
: Search and replaces for text in the entire project.

`replace <user.text> all`
: Search and replaces for text in the entire project.

`replace confirm that`
: Confirm replace at current position.

`replace confirm all`
: Confirm replace all.

`clear last <user.text> [over]`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Delete selection.

`clear next <user.text> [over]`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Delete selection.

`clear last clip`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Delete selection.

`clear next clip`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Delete selection.

`comment last <user.text> [over]`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Toggle comments on the current line(s).

`comment last clip`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Toggle comments on the current line(s).

`comment next <user.text> [over]`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Toggle comments on the current line(s).

`comment next clip`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Toggle comments on the current line(s).

`go last <user.text> [over]`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Move cursor right one column.

`go last clip`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Move cursor right one column.

`go next <user.text> [over]`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Move cursor right one column.

`go next clip`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Move cursor right one column.

`paste last <user.text> [over]`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Move cursor right one column; Paste clipboard at cursor.

`paste next <user.text> [over]`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Move cursor right one column; Paste clipboard at cursor.

`replace last <user.text> [over]`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs; Paste clipboard at cursor.

`replace next <user.text> [over]`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs; Paste clipboard at cursor.

`select last <user.text> [over]`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs.

`select next <user.text> [over]`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs.

`select last clip`
: Selects the previous occurrence of the text, and suppresses any find/replace dialogs.

`select next clip`
: Selects the next occurrence of the text, and suppresses any find/replace dialogs.

# line_commands.talon

`lend`
: Move cursor to end of line.

`bend`
: Move cursor to start of line.

`go <number>`
: Move cursor to line `<n>`.

`go <number> end`
: Move cursor to line `<n>`; Move cursor to end of line.

`comment [line] <number>`
: Selects lines from line_start to line line_end; Toggle comments on the current line(s).

`comment <number> until <number>`
: Selects lines from line_start to line line_end; Toggle comments on the current line(s).

`clear [line] <number>`
: Move cursor to line `<n>`; Selects lines from line_start to line line_end; Delete selection.

`clear <number> until <number>`
: Selects lines from line_start to line line_end; Delete selection.

`copy [line] <number>`
: Selects lines from line_start to line line_end; Copy selection to clipboard.

`copy <number> until <number>`
: Selects lines from line_start to line line_end; Copy selection to clipboard.

`cut [line] <number>`
: Selects lines from line_start to line line_end; Cut selection to clipboard.

`cut [line] <number> until <number>`
: Selects lines from line_start to line line_end; Cut selection to clipboard.

`(paste | replace) <number> until <number>`
: Selects lines from line_start to line line_end; Paste clipboard at cursor.

`(select | cell | sell) [line] <number>`
: Selects lines from line_start to line line_end.

`(select | cell | sell) <number> until <number>`
: Selects lines from line_start to line line_end.

`tab that`
: Add a tab stop of indentation.

`tab [line] <number>`
: Move cursor to line `<n>`; Add a tab stop of indentation.

`tab <number> until <number>`
: Selects lines from line_start to line line_end; Add a tab stop of indentation.

`retab that`
: Remove a tab stop of indentation.

`retab [line] <number>`
: Selects lines from line_start to line line_end; Remove a tab stop of indentation.

`retab <number> until <number>`
: Selects lines from line_start to line line_end; Remove a tab stop of indentation.

`drag [line] down`
: Swap the current line with the line below.

`drag [line] up`
: Swap the current line with the line above.

`drag up [line] <number>`
: Selects lines from line_start to line line_end; Swap the current line with the line above.

`drag up <number> until <number>`
: Selects lines from line_start to line line_end; Swap the current line with the line above.

`drag down [line] <number>`
: Selects lines from line_start to line line_end; Swap the current line with the line below.

`drag down <number> until <number>`
: Selects lines from line_start to line line_end; Swap the current line with the line below.

`clone (line|that`
: Create a new line identical to the current line.

# multiple_cursors.talon

`cursor multiple`
: Enables multi-cursor mode.

`cursor stop`
: Disables multi-cursor mode.

`cursor up`
: Adds cursor to line above.

`cursor down`
: Adds cursor to line below.

`cursor less`
: Removes selection & cursor at last occurrence.

`cursor more`
: Adds cursor at next occurrence of selection.

`cursor skip`
: Skips adding a cursor at next occurrence of selection.

`cursor all`
: Adds cursor at every occurrence of selection.

`cursor lines`
: Adds cursor at end of every selected line.

# generic_snippets.talon

`snip {user.snippets}`
: Inserts a snippet.

`snip hunt <user.text>`
: Triggers the program's snippet search.

`snip hunt`
: Triggers the program's snippet search.

`snip create`
: Triggers snippet creation.

`snip show`
: Toggles UI for available snippets.

# splits.talon

`split right`
: Move active tab to right split.

`split left`
: Move active tab to left split.

`split down`
: Move active tab to lower split.

`split up`
: Move active tab to upper split.

`split (vertically | vertical)`
: Splits window vertically.

`split (horizontally | horizontal)`
: Splits window horizontally.

`split flip`
: Flips the orietation of the active split.

`split window`
: Splits the window.

`split clear`
: Clears the current split.

`split clear all`
: Clears all splits.

`split next`
: Goes to next split.

`split last`
: Goes to last split.

`go split <number>`
: Navigates to a the specified split.

# tabs.talon

`tab (open | new)`
: Open a new tab.

`tab (last | previous)`
: Switch to previous tab for this window.

`tab next`
: Switch to next tab for this window.

`tab close`
: Closes the current tab.

`tab (reopen|restore`
: Re-open the last-closed tab.

`go tab <number>`
: Jumps to the specified.

`go tab final`
: Jumps to the final tab.
