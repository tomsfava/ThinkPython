def only_upper(t):
  res = []
  for s in t:
    if s.isupper():
      res.append(s)
  return res

if __name__ == '__main__':
  saudacoes = ['Oi', 'OI', 'OIE', 'oieee', 'OLÁ']
  print(only_upper(saudacoes))
  print(saudacoes)