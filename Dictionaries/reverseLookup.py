from histogram import upgraded_histogram

def reverse_lookup(d, v):
  for k in d:
    if d[k] == v:
      return k
  raise ValueError('No such key')

def reverse_lookup2(d, v):
  """Search for keys that appear v times in a histogram"""
  keys = []
  for k in d:
    if d[k] == v:
      keys.append(k)
  return keys

if __name__ == '__main__':
  h = upgraded_histogram('parrot')
  print(reverse_lookup2(h, 1))