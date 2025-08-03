from pathlib import Path

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'

def group_anagrams(wordList):
  d = {}
  for word in wordList:
    key = tuple(sorted(word))
    if key not in d:
      d[key] = [word]
    else:
      d[key].append(word)
  res = []
  for key in d:
    if len(d[key]) > 1:
      res.append(d[key])
  return res

def group_anagrams_sorted(wordList):
  d = {}
  for word in wordList:
    key = tuple(sorted(word))
    if key not in d:
      d[key] = [word]
    else:
      d[key].append(word)
  t = []
  for key in d:
    if len(d[key]) > 1:
      t.append((len(d[key]), d[key]))
  t.sort(reverse=True)
  res = []
  for length, group in t:
    res.append(group)
  return res

def group_anagrams_8_lettered(wordList):
  d = {}
  for word in wordList:
    key = tuple(sorted(word))
    if len(key) == 8:
      if key not in d:
        d[key] = [word]
      else:
        d[key].append(word)
  t = []
  for key in d:
    if len(d[key]) > 1:
      t.append((len(d[key]), d[key]))
  t.sort(reverse=True)
  res = []
  for length, group in t:
    res.append(group)
  return res

def list_of_words_append(fin):
  t = []
  for line in fin:
    word = line.strip()
    t.append(word)
  return t

if __name__ == '__main__':
  fin = open(path)
  wordList = list_of_words_append(fin)
  print((group_anagrams_8_lettered(wordList), len(group_anagrams_8_lettered(wordList))))