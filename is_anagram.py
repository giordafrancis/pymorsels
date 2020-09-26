"""
is_anagram

unicode decomposing 
Normalize string based on unicode characters decomposition
The last bonus is a bit harder. We were supposed to ignore accents on accented Latin characters.
We'll need to normalize our unicode data to such that characters are decomposed into parts (so accents are treated separately from the character they accent). If we look up unicode normalization or search for how to ignore accent marks in unicode strings we'll find NFKD form. The unicodedata module can help us normalize our strings into NFKD form
"""

import unicodedata
from typing import Counter

def remove_accents(input_str:str) -> str:
    """Return decomposed form of the given string"""
    return unicodedata.normalize('NFKD', input_str)

def letters_in(word: str)-> Counter:
    """Return Counter object f letters in a given string"""
    return Counter(
        char
        for char in word.lower()
        if char.isalpha()
        )

def is_anagram(str_1:str, str_2:str) -> bool:
    str_1, str_2 = remove_accents(str_1), remove_accents(str_2)
    return letters_in(str_1) == letters_in(str_2)


assert is_anagram("cardiografía", "radiográfica")
assert is_anagram("a diet", "I'd eat")
assert is_anagram("coins kept", "in pockets")