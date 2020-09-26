"""
I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure) that has words as the keys and the number of times each word was seen as the values.

It should work as below:
count_words("oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
"""

from collections import Counter
from typing import Dict
import re

REGEX = r"\b[A-Za-z']+\b"

def count_words_mine(text: str)-> Dict[str, int]:
    words = (
        word.lower()
    for word in re.findall(REGEX, text)
    )
    return Counter(words)

# Treys solution
# flag lower in findall

REGEX = r"\b[\w'-]+\b"
def count_words(text: str)-> Dict[str, int]:
    return Counter(re.findall(REGEX, text.lower()))
    

assert count_words("oh what a day what a lovely day") == {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
assert count_words("oh what a day what a lovely day!") == {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
assert count_words("oh What a day what a lovely day!") == {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
assert count_words("don't stop believing") == {"don't": 1, 'stop': 1, 'believing': 1}




