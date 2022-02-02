from talon import Module, Context, actions
from user.util import csv

mod = Module()
ctx = Context()

alphabet = "abcdefghijklmnopqrstuvwxyz".split()

# Blackboard Bold

blackboard_bold_lower = [
    "𝕒",
    "𝕓",
    "𝕔",
    "𝕕",
    "𝕖",
    "𝕗",
    "𝕘",
    "𝕙",
    "𝕚",
    "𝕛",
    "𝕜",
    "𝕝",
    "𝕞",
    "𝕟",
    "𝕠",
    "𝕡",
    "𝕢",
    "𝕣",
    "𝕤",
    "𝕥",
    "𝕦",
    "𝕧",
    "𝕨",
    "𝕩",
    "𝕪",
    "𝕫",
]
blackboard_bold_lower = dict(zip(alphabet, blackboard_bold_lower))

blackboard_bold_upper = [
    "𝔸",
    "𝔹",
    "ℂ",
    "𝔻",
    "𝔼",
    "𝔽",
    "𝔾",
    "ℍ",
    "𝕀",
    "𝕁",
    "𝕂",
    "𝕃",
    "𝕄",
    "ℕ",
    "𝕆",
    "ℙ",
    "ℚ",
    "ℝ",
    "𝕊",
    "𝕋",
    "𝕌",
    "𝕍",
    "𝕎",
    "𝕏",
    "𝕐",
    "ℤ",
]
blackboard_bold_upper = dict(zip(alphabet, blackboard_bold_upper))

# Math Calligraphy

mathcal_upper = [
    "𝒜",
    "ℬ",
    "𝒞",
    "𝒟",
    "ℰ",
    "ℱ",
    "𝒢",
    "ℋ",
    "ℐ",
    "𝒥",
    "𝒦",
    "ℒ",
    "ℳ",
    "𝒩",
    "𝒪",
    "𝒫",
    "𝒬",
    "ℛ",
    "𝒮",
    "𝒯",
    "𝒰",
    "𝒱",
    "𝒲",
    "𝒳",
    "𝒴",
    "𝒵",
]
mathcal_upper = dict(zip(alphabet, mathcal_upper))
mathcal_lower = [
    "𝒶",
    "𝒷 ",
    "𝒸",
    "𝒹",
    "ℯ",
    "𝒻 ",
    "ℊ",
    "𝒽",
    "𝒾",
    "𝒿",
    "𝓀",
    "𝓁",
    "𝓂",
    "𝓃",
    "ℴ",
    "𝓅",
    "𝓆",
    "𝓇",
    "𝓈",
    "𝓉",
    "𝓊",
    "𝓋",
    "𝓌",
    "𝓍",
    "𝓎",
    "𝓏 ",
]
mathcal_lower = dict(zip(alphabet, mathcal_lower))

mathcal_bold_upper = [
    "𝓐",
    "𝓑",
    "𝓒",
    "𝓓",
    "𝓔",
    "𝓕",
    "𝓖",
    "𝓗",
    "𝓘",
    "𝓙",
    "𝓚",
    "𝓛",
    "𝓜",
    "𝓝",
    "𝓞",
    "𝓟",
    "𝓠",
    "𝓡",
    "𝓢",
    "𝓣",
    "𝓤",
    "𝓥",
    "𝓦",
    "𝓧",
    "𝓨",
    "𝓩",
]
mathcal_bold_upper = dict(zip(alphabet, mathcal_bold_upper))
mathcal_bold_lower = [
    "𝓪",
    "𝓫",
    "𝓬",
    "𝓭",
    "𝓮",
    "𝓯",
    "𝓰",
    "𝓱",
    "𝓲",
    "𝓳",
    "𝓴",
    "𝓵",
    "𝓶",
    "𝓷",
    "𝓸",
    "𝓹",
    "𝓺",
    "𝓻",
    "𝓼",
    "𝓽",
    "𝓾",
    "𝓿",
    "𝔀",
    "𝔁",
    "𝔂",
    "𝔃",
]
mathcal_bold_lower = dict(zip(alphabet, mathcal_bold_lower))

# Greek

mod.list("greek_alphabet", desc="The spoken Greek alphabet")

GREEK_ALPHABET = csv.read_spoken_forms("symbols/greek.csv", value_name="Greek letter")
ctx.lists["self.greek_alphabet"] = GREEK_ALPHABET

greek_lower_sigma_alt = "ς"
greek_lower_lambda_alt = "ƛ"


@mod.capture(rule="{self.greek_alphabet}")
def greek_lowercase(m) -> str:
    """One lowercase letter in the Greek alphabet"""
    return str(m).lower()


@mod.capture(rule="<self.greek_lowercase>+")
def greek_lowercases(m) -> str:
    """One or more lowercase letters in the Greek alphabet"""
    return "".join(m.greek_lowercase_list)


@mod.capture(rule="{self.greek_alphabet}")
def greek_uppercase(m) -> str:
    """One uppercase letter in the Greek alphabet"""
    return str(m).upper()


@mod.capture(rule="ship <self.greek_uppercase>+ [sink]")
def greek_uppercases(m) -> str:
    """One or more lowercase letters in the Greek alphabet"""
    return "".join(m.greek_uppercase_list)


@mod.capture(rule="(<self.greek_lowercases> | <self.greek_uppercases>)+")
def greek_letters(m) -> str:
    """One or more letters in the Greek alphabet"""
    return "".join(m)
