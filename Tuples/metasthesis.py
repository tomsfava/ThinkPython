from pathlib import Path
from Tuples.e12_04 import list_of_words_append, group_anagrams

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'

def word_distance(word1, word2):
  """Computes the number of differences between two words.

  word1, word2: strings

  Returns: integer
  """
  assert len(word1) == len(word2)

  count = 0
  for c1, c2 in zip(word1, word2):
    if c1 != c2:
      count += 1
  return count

def metasthesis_pairs(t):
  """Print all pairs of words that differ by swapping two letters.

  t: list os lists of anagrams
  """
  for group in t:
      for i in range(len(group)):
          for j in range(i + 1, len(group)):
              word1 = group[i]
              word2 = group[j]
              if word_distance(word1, word2) == 2:
                  print(word1, word2)

if __name__ == '__main__':
  fin = open(path)
  wordList = list_of_words_append(fin)
  t = group_anagrams(wordList)
  metasthesis_pairs(t)