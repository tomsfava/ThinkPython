def chop(lista):
  if len(lista) >= 2:
    del lista[0]
    del lista[-1]
  elif len(lista) == 1:
    del lista[0]

if __name__ == '__main__':
  lista = [1, 2, 3]
  print(chop(lista))
  print(lista)
