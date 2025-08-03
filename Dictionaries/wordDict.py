from pathlib import Path

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'

def wordlist_as_dict(fin):
  words_dict = {}
  for line in fin:
    word = line.strip()
    words_dict[word] = 'bleber'
  return words_dict

if __name__ == '__main__':
  fin = open(path)
  words_dict = wordlist_as_dict(fin)
  print(len(words_dict))
  print('love' in words_dict)