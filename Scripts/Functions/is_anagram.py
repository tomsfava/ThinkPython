def is_anagram(word1, word2):
  if len(word1) != len(word2):
    return False

  list1 = []
  for c in word1:
    if 'A' <= c <= 'Z':
      c = chr(ord(c) + 32)
    list1.append(c)

  list2 = []
  for c in word2:
    if 'A' <= c <= 'Z':
      c = chr(ord(c) + 32)
    list2.append(c)

  for letter in list1:
    found = False
    for i in range(len(list2)):
      if list2[i] == letter:
        list2[i] = None
        found = True
        break
    if not found:
      return False
  return True

def built_in_is_anagram(word1, word2):
  return sorted(word1.casefold()) == sorted(word2.casefold())




if __name__ == '__main__':
  result = is_anagram('Tomas', 'Samot')
  print(result)
  result2 = built_in_is_anagram('Tomas', 'Samot')
  print(result2)