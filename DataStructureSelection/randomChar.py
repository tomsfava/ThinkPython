import random
import sys
from Dictionaries.histogram import upgraded_histogram as histogram

def choose_from_hist(hist):
  """Random chooses from a string according to char proportions"""
  t = []
  for key, value in hist.items():
    t.extend([key]*value)
  return random.choice(t)

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Uso: python randomChar.py string')
  else:
    try:
      hist = histogram(sys.argv[1])
      print(choose_from_hist(hist))
    except TypeError:
      print('Por favor digite uma string válida')