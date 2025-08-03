def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d

def upgraded_histogram(s):
  d = dict()
  for c in s:
    d[c] = d.get(c, 0) + 1
  return d

if __name__ == '__main__':
  print(upgraded_histogram('Tomás e Marina se amam infinito'))