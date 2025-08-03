def add_all(t):
  total = 0
  for x in t:
    total += x
  return total

def nested_sum(t):
  total = 0
  for sublist in t:
    for num in sublist:
      total += num
  return total

if __name__ == '__main__':
  valores = [1,2,3,4,5]
  print(f'a soma dos valores {valores} é igual a {add_all(valores)}')
  print(sum(valores))
  listaDeLista = [[1,2], [3,4], [5,6]]
  print(nested_sum(listaDeLista))