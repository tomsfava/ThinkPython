def invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    if val not in inverse:
      inverse[val] = [key]
    else:
      inverse[val].append(key)
  return inverse

def concise_invert_dict(d):
  inverse = dict()
  for key in d:
    val = d[key]
    inverse.setdefault(val, []).append(key)
  return inverse


if __name__ == '__main__':
  d = {'a': 1, 'b': 2, 'c': 1, 'd': 4}
  print(invert_dict(d))
  print(concise_invert_dict(d))
  print(d)