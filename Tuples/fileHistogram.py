import sys

def histogram(word):
  d = {}
  for c in word:
    d[c] = d.get(c, 0) + 1
  return d

def most_frequent(string):
  """Takes a string and prints the letters in decreasing order of frequency."""

  hist = histogram(string)
  t = []
  for x, freq in hist.items():
    t.append((freq, x))

  t.sort(reverse=True)

  res = []
  for freq, x in t:
    res.append(x)

  return res

def read_file(filename):
  return open(filename).read()

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: python e12_03.py <filename>')
  else:
    try:
      filename = sys.argv[1]
      string = read_file(filename)
      print(most_frequent(string))
    except FileNotFoundError:
      print('File not found')


