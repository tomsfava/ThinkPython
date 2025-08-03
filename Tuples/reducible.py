from pathlib import Path
from Lists.wordList import list_of_words_append

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'

def is_reducible(word, wordList, memo):
  if word in memo:
    return memo[word]
  if word == "":
    memo[word] = False
    return False
  if len(word) == 1:
    result = word in wordList
    memo[word] = result
    return result
  for i in range(len(word)):
    child = word[:i] + word[i+1:]
    if child in wordList and is_reducible(child, wordList, memo):
      memo[word] = True
      return True
  memo[word] = False
  return False

def is_reducible_set(word, wordSet, memo):
  if word in memo:
    return memo[word]
  if word == "":
    return False
  if len(word) == 1:
    if word in wordSet:
      memo[word] = True
      return True
    else:
      memo[word] = False
      return False
  for i in range(len(word)):
    child = word[:i] + word[i+1:]
    if child in wordSet and is_reducible_set(child, wordSet, memo):
      memo[word] = True
      return True
  memo[word] = False
  return False

if __name__ == "__main__":
  fin = open(path)
  wordList = list_of_words_append(fin)
  fin.close()

  memo = {}
  wordSet = set(wordList)

  reducible_words = []
  for word in wordSet:
    if is_reducible_set(word, wordSet, memo):
      reducible_words.append(word)

  longest = ""
  for word in reducible_words:
    if len(word) > len(longest):
      longest = word

  print("Lista de palavras redutíveis:", reducible_words)
  print("Total de", len(reducible_words), "palavras redutíveis.")
  print("Maior palavra redutível:", longest)


