def is_reverse(word, word2):
  if len(word) != len(word2):
    return False
  i = 0
  j = len(word2) - 1
  while j >= 0:
    if word[i] != word2[j]:
      return False
    i += 1
    j -= 1
  return True

def is_palindrome(word):
  return is_reverse(word, word)

if __name__ == '__main__':
  print(is_palindrome('hello'))
  print(is_palindrome('radar'))