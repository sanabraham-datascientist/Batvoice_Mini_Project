from django.core.exceptions import ValidationError
import re

character_set = [
    " ",
    "(",
    ")",
    "'",
    "a",
    "A",
    "-",
    "à",
    "À",
    "?",
    "â",
    "Â",
    ",",
    "b",
    "B",
    ".",
    "c",
    "C",
    ";",
    "ç",
    "Ç",
    ":",
    "d",
    "D",
    "!",
    "e",
    "E",
    "é",
    "É",
    "è",
    "È",
    "ê",
    "Ê",
    "ë",
    "f",
    "F",
    "g",
    "G",
    "h",
    "H",
    "i",
    "I",
    "î",
    "Î",
    "ï",
    "j",
    "J",
    "k",
    "K",
    "l",
    "L",
    "m",
    "M",
    "n",
    "N",
    "o",
    "O",
    "ô",
    "Ô",
    "p",
    "P",
    "q",
    "Q",
    "r",
    "R",
    "s",
    "S",
    "t",
    "T",
    "u",
    "U",
    "ù",
    "û",
    "v",
    "V",
    "w",
    "W",
    "x",
    "X",
    "y",
    "Y",
    "z",
    "Z",
]
"""
The rules for validation are as follows:
Rule1=> all characters belong to a given character set; this character set should be stored in DB to allow for
some modifications in the future; this character set should be initialized with ()&#39;aA-
àÀ?âÂ,bB.cC;çÇ:dD!eEéÉèÈêÊëfFgGhHiIîÎïjJkKlLmMnNoOôÔpPqQrRsStTuUùûvVwWxXyYzZ [NB:
numbers are voluntarily excluded, but space should be included even if it cannot be seen here]
Rule2=> capital letters are allowed only as a first word letter or if all the letters in the word are upper case
Rule3=>there can be only zero or one space between two characters
Rule4=>characters ?.! should be end of text or followed by one space and an uppercase character
Rule5=>characters ,;: should be end of text of followed by one space
"""


# Rule1 : all charcters have to be in the character set.
def check_character_set(transcript_text):
    for character in transcript_text:
        if character not in character_set:
            raise ValidationError(f"{character} is a not valid")
    return True


# Rule3 : There can be only zero or one space between two characters
def check_space(transcript_text):
    result = re.fullmatch(r"\S+( ?\S+)*", transcript_text.strip())
    if result is None:
        raise ValidationError(
            "There can be only zero or one space between two characters"
        )
    return True


# Rule2 :capital letters are allowed only as a first word letter or if all the letters in the word are upper case
def check_capital_letters(transcript_text):
    words = transcript_text.split(" ")
    for word in words:
        if not (word == word.title() or word == word.upper() or word == word.lower()):
            raise ValidationError(
                "Capital letters are allowed only as a first word letter or if all the letters in the word are upper case"
            )
    return True


# Rule 4 characters ?.! should be end of text or followed by one space and an uppercase character ,
# characters ,;: should be end of text of followed by one space"
def check_the_end_text(transcript_text):
    result = re.search(r".+[,;:]\s?$", transcript_text) or re.search(
        r".+[?.!]\s[A-Z]$", transcript_text
    )
    if result is None:
        raise ValidationError(
            "characters '?.!' should be end of text or followed by one space and an uppercase character ,characters ',;:' should be end of text of followed by one space"
        )
    return True
