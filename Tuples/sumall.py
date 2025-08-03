import sys

def sumall(*args):
  t = list(args)
  total = 0
  for i in t:
    total += i
  return total

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print('Uso: python e12_01 <número1> <número2> ...')
  else:
    try:
      numeros = [float(arg) for arg in sys.argv[1:]]
      print(sumall(*numeros))
    except ValueError:
      print('Erro, todos os argumentos devem ser números.')
    except TypeError:
      print('Erro de tipo inesperado.')