from talon import Module, Context, actions
from user.util import csv

mod = Module()
ctx = Context()

DIGITS = "0 1 2 3 4 5 6 7 8 9".split()

ALPHABET = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

# Blackboard Bold

BLACKBOARD_LOWER = "𝕒 𝕓 𝕔 𝕕 𝕖 𝕗 𝕘 𝕙 𝕚 𝕛 𝕜 𝕝 𝕞 𝕟 𝕠 𝕡 𝕢 𝕣 𝕤 𝕥 𝕦 𝕧 𝕨 𝕩 𝕪 𝕫".split()
BLACKBOARD_LOWER = dict(zip(ALPHABET, BLACKBOARD_LOWER))
BLACKBOARD_UPPER = "𝔸 𝔹 ℂ 𝔻 𝔼 𝔽 𝔾 ℍ 𝕀 𝕁 𝕂 𝕃 𝕄 ℕ 𝕆 ℙ ℚ ℝ 𝕊 𝕋 𝕌 𝕍 𝕎 𝕏 𝕐 ℤ".split()
BLACKBOARD_UPPER = dict(zip(map(str.upper,ALPHABET), BLACKBOARD_UPPER))
BLACKBOARD = BLACKBOARD_LOWER | BLACKBOARD_UPPER

@mod.capture(rule="blackboard <self.letters>")
def blackboard(m) -> str:
    """One or more letters in blackboard bold"""
    global BLACKBOARD
    return "".join(BLACKBOARD.get(letter,letter) for letter in m.letters)


# Math Calligraphy

MATH_SCRIPT_LOWER = "𝒶 𝒷 𝒸 𝒹 ℯ 𝒻 ℊ 𝒽 𝒾 𝒿 𝓀 𝓁 𝓂 𝓃 ℴ 𝓅 𝓆 𝓇 𝓈 𝓉 𝓊 𝓋 𝓌 𝓍 𝓎 𝓏 ".split()
MATH_SCRIPT_LOWER = dict(zip(ALPHABET, MATH_SCRIPT_LOWER))
MATH_SCRIPT_UPPER = "𝒜 ℬ 𝒞 𝒟 ℰ ℱ 𝒢 ℋ ℐ 𝒥 𝒦 ℒ ℳ 𝒩 𝒪 𝒫 𝒬 ℛ 𝒮 𝒯 𝒰 𝒱 𝒲 𝒳 𝒴 𝒵".split()
MATH_SCRIPT_UPPER = dict(zip(map(str.upper,ALPHABET), MATH_SCRIPT_UPPER))
MATH_SCRIPT = MATH_SCRIPT_LOWER | MATH_SCRIPT_UPPER


@mod.capture(rule="math script <self.letters>")
def math_script(m) -> str:
    """One or more letters in math script or cursive"""
    global MATH_SCRIPT
    return "".join(MATH_SCRIPT.get(letter,letter) for letter in m.letters)


MATH_SCRIPT_BOLD_LOWER = "𝓪 𝓫 𝓬 𝓭 𝓮 𝓯 𝓰 𝓱 𝓲 𝓳 𝓴 𝓵 𝓶 𝓷 𝓸 𝓹 𝓺 𝓻 𝓼 𝓽 𝓾 𝓿 𝔀 𝔁 𝔂 𝔃".split()
MATH_SCRIPT_BOLD_LOWER = dict(zip(ALPHABET, MATH_SCRIPT_BOLD_LOWER))
MATH_SCRIPT_BOLD_UPPER = "𝓐 𝓑 𝓒 𝓓 𝓔 𝓕 𝓖 𝓗 𝓘 𝓙 𝓚 𝓛 𝓜 𝓝 𝓞 𝓟 𝓠 𝓡 𝓢 𝓣 𝓤 𝓥 𝓦 𝓧 𝓨 𝓩".split()
MATH_SCRIPT_BOLD_UPPER = dict(zip(map(str.upper,ALPHABET), MATH_SCRIPT_BOLD_UPPER))
MATH_SCRIPT_BOLD = MATH_SCRIPT_BOLD_LOWER | MATH_SCRIPT_BOLD_UPPER


@mod.capture(rule="math script bold <self.letters>")
def math_script_bold(m) -> str:
    """One or more letters in bold math script or cursive"""
    global MATH_SCRIPT_BOLD
    return "".join(MATH_SCRIPT_BOLD.get(letter,letter) for letter in m.letters)


# Greek letters

mod.list("greek_ALPHABET", desc="The spoken Greek ALPHABET")

GREEK_ALPHABET = csv.read_spoken_forms("symbols/greek.csv", value_name="Greek letter")
ctx.lists["self.greek_ALPHABET"] = GREEK_ALPHABET

# TODO: bind alternative sigma and lambda
greek_lower_sigma_alt = "ς"
greek_lower_lambda_alt = "ƛ"


@mod.capture(rule="{self.greek_ALPHABET}")
def greek_lowercase(m) -> str:
    """One lowercase letter in the Greek ALPHABET"""
    return str(m).lower()


@mod.capture(rule="<self.greek_lowercase>+")
def greek_lowercases(m) -> str:
    """One or more lowercase letters in the Greek ALPHABET"""
    return "".join(m.greek_lowercase_list)


@mod.capture(rule="{self.greek_ALPHABET}")
def greek_uppercase(m) -> str:
    """One uppercase letter in the Greek ALPHABET"""
    return str(m).upper()


@mod.capture(rule="ship <self.greek_uppercase>+ [sink]")
def greek_uppercases(m) -> str:
    """One or more lowercase letters in the Greek ALPHABET"""
    return "".join(m.greek_uppercase_list)


@mod.capture(rule="greek (<self.greek_lowercases> | <self.greek_uppercases>)+")
def greek(m) -> str:
    """One or more letters in the Greek ALPHABET"""
    return "".join(m[1:])


# Subscripts and superscripts

SUBSCRIPT = "₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉".split()

@mod.capture(rule="subscript <self.digit>")
def subscript_digit(m) -> str:
    """One or more subscript digits"""
    global SUBSCRIPT
    return SUBSCRIPT[m.digit]

SUPERSCRIPT = "⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹".split()

@mod.capture(rule="superscript <self.digit>")
def superscript_digit(m) -> str:
    """One or more superscript digits"""
    global SUPERSCRIPT
    return SUPERSCRIPT[m.digit]
