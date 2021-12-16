# My Talon User

I'm in the process of slowly migrating from knausj.

# Organization


```
apps:
  Contains concrete .talon files and their associated .py files for specific application contexts.

global:
  Contains concrete .talon files and their associated .py files which are always active.

tags:
  Contains abstract .talon files which define tags and the .py files which define their associated modules.
```

TODO: Reorganize by putting all the files that you're allowed to depend on—e.g. sleep_mode, app_running, language_mode, and text—in core, and enforcing a strict policy that nothing is allowed to depend on anything outside core unless it is behind a tag.