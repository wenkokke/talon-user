# Organization

- `apps/` contains Talon scripts associated with applications, e.g., Firefox;
- `core/` contains Talon scripts which are always running;
- `tags/` contains Talon scripts which are activated by a certain tag;
- `tags/code/` contains Talon scripts which are associated with a programming language, e.g., Haskell;
- `tags/code/tags/` contains Talon scripts which abstract over programming language features, e.g., comments.
- `util` contains Python scripts which may be imported

# TODO

+ Extract lists to CSV files
  - `delimiters.py`: `delimiters_spaced`
  - `delimiters.py`: `delimiter_pair`
  - `keys.py`: `key_special`
  - `keys.py`: `key_modifier`
  - `keys.py`: `key_punctuation`
  - `keys.py`: `key_symbol`
  - `formatters.py`: `formatter_code`
  - `formatters.py`: `formatter_prose`
  - `formatters.py`: `formatter_word`
+ Enable VSCode to pick up snippets based on the programming language mode, by subscribing to `languages.csv`
+ Migrate snippet help into its own file, and make it consistent with the remainder of the help functions
+ Debug Talon HUD