# Letters [A-Z]
<self.letters>: insert(letters)

# Symbol keys: !, %, _
{user.key_symbol}: key(key_symbol)

# Digits [0-9]
{user.key_number}: key(key_number)

# Press a key with optional modifiers
firm: key(enter)

press <user.key_unmodified>: key(key_unmodified)

press <user.key_modifiers> <user.key_unmodified>:
    key("{key_modifiers}-{key_unmodified}")
