def middle(t):
  del t[0]
  del t[-1]
  return t

if __name__ == '__main__':
  coisas = ['trem', 'coisa', 'negocio', 'bagulho']
  print(middle(coisas))