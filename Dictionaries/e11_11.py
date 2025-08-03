"""
one syllable, five-letter word
when the first letter is removed the remaining letters
form a homophone of the original word, a word that sounds
exactly the same.
Replace the first letter, and remove the second one, the
result is yet another homophone.
What's the word?
"""

from pathlib import Path
from Dictionaries.e11_01 import wordlist_as_dict

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'
