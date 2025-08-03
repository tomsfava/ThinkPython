import sys

def ack(m, n):
  if m == 0:
    return n + 1
  if m > 0 and n == 0:
    return ack(m - 1, 1)
  if m > 0 and n > 0:
    return ack(m-1, ack(m, n-1))

cache = {}

def ackermann(m, n):
  if m == 0:
    return n + 1
  if m > 0 and n == 0:
    return ackermann(m-1, 1)
  if (m, n) in cache:
    return (cache[m, n])
  else:
    cache[m, n] = ackermann(m-1, ackermann(m, n-1))
    return cache[m, n]


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Uso: python ackermann.py <m> <n>")
  else:
    try:
      m = int(sys.argv[1])
      n = int(sys.argv[2])
      print(f"Ackerman({m}, {n}) = {ackermann(m,n)}")
    except RecursionError:
      print("Erro: profundidade de recursão excedida.")
    except ValueError:
      print("Por favor, forneça dois números inteiros.")