import time
from pathlib import Path
from .wordList import list_of_words_append
from .bisect import bisect
from Scripts.Functions.palindrome import is_reverse


path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'

def find_reverse_pairs(t):
  reverse_pairs = []
  for i in range(len(t)):
    for j in range(i + 1, len(t)):
      if is_reverse(t[i], t[j]):
        reverse_pairs.append((t[i], t[j]))
  return reverse_pairs

def find_reverse_pairs_fast(t):
  reverse_pairs = set()
  words_set = set(t)
  for word in t:
    reversed_word = word[::-1]
    if reversed_word in words_set and word != reversed_word:
      pair = tuple(sorted((word, reversed_word)))
      reverse_pairs.add(pair)
  return list(reverse_pairs)

def reverse_pair(word_list, word):
  reverse_word = word[::-1]
  _index, found = bisect(word_list, reverse_word, 0, None)
  return found

def find_reverse_pairs_bisect(t):
  reverse_pairs = []
  for word in t:
    rev = word[::-1]
    if rev != word and reverse_pair(t, word):
      if word < rev:
        reverse_pairs.append((word, rev))
  return reverse_pairs

if __name__ == '__main__':
  start = time.time()
  fin = open(path)
  t = list_of_words_append(fin)
  fin.close()
  reverse_pairs = find_reverse_pairs_fast(t)
  print(reverse_pairs, len(reverse_pairs))
  end = time.time()
  print(f'Time Taken with Set: {end - start:.4f} seconds')
  start = time.time()
  fin = open(path)
  t = list_of_words_append(fin)
  fin.close()
  reverse_pairs = find_reverse_pairs_bisect(t)
  print(reverse_pairs, len(reverse_pairs))
  end = time.time()
  print(f'Time Taken with Bisect: {end - start:.4f} seconds')


