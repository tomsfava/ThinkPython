def reduce_map(t):
  res = []
  total = 0
  for i in t:
    total += i
    res.append(total)
  return res

if __name__ == '__main__':
  print(reduce_map([1, 2, 3]))
  print(reduce_map([1, 2, 4]))