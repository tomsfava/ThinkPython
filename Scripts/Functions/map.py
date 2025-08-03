def capitalize_all(t):
  res = []
  for s in t:
    res.append(s.capitalize())
  return res

def capitalize_nested(t):
  res = []
  for subt in t:
    res.append(capitalize_all(subt))
  return res

if __name__ == '__main__':
  letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  listasDeLetras = [['a','z'], ['b', 'y'], ['c', 'x']]

  print(capitalize_all(letras))
  print(capitalize_nested(listasDeLetras))