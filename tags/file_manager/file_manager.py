# from typing import Optional, Sequence
# from talon import Module, Context, actions, app, registry, ui
# from pathlib import Path
# from user.util.speech import create_spoken_form

# mod = Module()
# mod.tag("file_manager", desc="Tag for enabling generic file management commands")

# mod.list(
#     "file_manager_directories", desc="List of subdirectories in the current directory"
# )
# mod.list("file_manager_files", desc="List of files in the current directory")

# ctx = Context()
# ctx.lists["self.file_manager_directories"] = {}
# ctx.lists["self.file_manager_files"] = {}
# current_working_directory: Optional[Path] = None
# current_working_directory_directories: Sequence[Path] = []
# current_working_directory_files: Sequence[Path] = []


# def file_manager_lists_clear():
#     global ctx
#     global current_working_directory
#     global current_working_directory_directories
#     global current_working_directory_files

#     current_working_directory = None
#     current_working_directory_directories.clear()
#     current_working_directory_files.clear()
#     ctx.lists["self.file_manager_directories"] = {}
#     ctx.lists["self.file_manager_files"] = {}


# def file_manager_update_lists():
#     global ctx
#     global current_working_directory
#     global current_working_directory_directories
#     global current_working_directory_files

#     # Skip if file_manager tag is not set
#     if not "user.file_manager" in registry.tags:
#         file_manager_lists_clear()
#         return

#     # Skip if working directory has not changed
#     updated_working_directory = Path(actions.win.filename())
#     if updated_working_directory == current_working_directory:
#         return
#     current_working_directory = updated_working_directory

#     # Skip if 'actions.win.filename' is not a directory
#     if not current_working_directory.is_dir():
#         file_manager_lists_clear()
#         return

#     # Update global lists for directories and files
#     for child in current_working_directory.iterdir():
#         if child.is_dir():
#             current_working_directory_directories.append(child)
#         if child.is_file():
#             current_working_directory_files.append(child)

#     # Update lists with spoken forms
#     ctx.lists["self.file_manager_directories"] = {
#         create_spoken_form(dir.name): dir
#         for dir in current_working_directory_directories
#     }
#     ctx.lists["self.file_manager_files"] = {
#         create_spoken_form(file.name): file for file in current_working_directory_files
#     }


# def win_event_handler(window):
#     # Skip if event did not come from active application
#     if window.app.exe and window == ui.active_window():
#         file_manager_update_lists()


# # Delay registering event handler to avoid error messages during startup
# def register_events():
#     ui.register("win_title", win_event_handler)
#     ui.register("win_focus", win_event_handler)


# app.register("ready", register_events)


# @mod.action_class
# class FileManagerActions:
#     pass
