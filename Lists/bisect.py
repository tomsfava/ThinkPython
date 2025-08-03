import sys
from pathlib import Path
from .wordList import list_of_words_append

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'


def bisect(t, word, low=0, high=None):
  """Search by sections if a given word is in a given sorted list"""
  if high is None:
    high = len(t) - 1

  if low > high:
    return -1, False

  mid = (low + high) // 2
  if t[mid] == word:
    return mid, True

  if t[mid] < word:
    return bisect(t, word, mid + 1, high)
  else:
    return bisect(t, word, low, mid - 1)

if __name__ == '__main__':
  fin = open(path)
  t = list_of_words_append(fin)
  fin.close()
  result = bisect(t, sys.argv[1])
  print(result)
