import logging
from typing import Sequence

from talon import Context, Module, actions

from user.util import csv
from user.util.phrase_replacer import PhraseReplacer

mod = Module()
ctx = Context()

# The setting "dictate.word_map" is used by `actions.dictate.replace_words`
# to rewrite words Talon recognized. Entries in word_map don't change the
# priority with which Talon recognizes some words over others.

WORDS_TO_REPLACE = csv.read_spoken_forms(
    "words_to_replace.csv", value_name="Replacement"
)
PHRASE_REPLACER = PhraseReplacer(WORDS_TO_REPLACE)
ctx.settings["dictate.word_map"] = WORDS_TO_REPLACE


# The phrase replacer allows phrases of more than one word to be specified in
# words_to_replace.csv for replacement after recognition, e.g., get hub -> github.
#
# You can achieve multi-word 'replacement' during recognition by altering
# user.vocabulary via additional_words.csv. However, this affects recognition
# priority, and a large vocabulary increases DFA times.
#
# Post-recognition phrase replacement also opens up other applications. For
# example, it offers an easy and DFA-free way to implement abbreviations.
#
# <https://github.com/knausj85/knausj_talon/pull/641>


@mod.action_class
class Actions:
    def replace_phrases(words: Sequence[str]) -> Sequence[str]:
        """Replace phrases according to words_to_replace.csv"""
        global PHRASE_REPLACER
        try:
            return PHRASE_REPLACER.replace(words)
        except:
            # fall back to dictate.replace_words for error-robustness
            logging.error("phrase replacer failed!")
            return actions.dictate.replace_words(words)
