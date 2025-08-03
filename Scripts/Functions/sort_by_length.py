import random
from pathlib import Path
from Lists.e10_10 import list_of_words_append

path = Path(__file__).parent.parent.parent / 'WordPlay' / 'words.txt'

def sort_by_length(words):
  t = []
  for word in words:
    t.append((len(word), word))
  t.sort(reverse=True)
  res = []
  for length, word in t:
    res.append(word)
  return res

def sort_by_length_random(words):
  """Sort a list of words in reverse order by length.

  It is unstable because if two words have the same length,
  their order in the output list is random.

  Works by extending the list of tuples with a column
  of random numbers; whe there is a tie in the first column,
  the random column determines the output order.

  words: list of strings

  Returns: list of strings
  """

  t=[]
  for word in words:
    t.append((len(word), random.random(), word))

  t.sort(reverse=True)

  res = []
  for length, _, word in t:
    res.append(word)
  return res

if __name__ == '__main__':
  fin = open(path)
  words = list_of_words_append(fin)
  length_sorted = sort_by_length_random(words)
  print(length_sorted)