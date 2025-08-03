from pathlib import Path
import time

path = Path(__file__).parent.parent / 'WordPlay' / 'words.txt'

def list_of_words_append(fin):
  t = []
  for line in fin:
    word = line.strip()
    t.append(word)
  return t

def list_of_words_sum(fin):
  t = []
  for line in fin:
    word = line.strip()
    t = t + [word]
  return t


if __name__ == '__main__':
  start = time.time()
  fin = open(path)
  list_of_words_append(fin)
  fin.close()
  end = time.time()
  print(f'Time Taken with append: {end - start:.4f} segundos')
  start = time.time()
  fin = open(path)
  list_of_words_sum(fin)
  fin.close()
  end = time.time()
  print(f'Time Taken with sum: {end - start:.4f} segundos')
