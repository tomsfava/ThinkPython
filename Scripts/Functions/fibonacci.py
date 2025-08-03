import sys

known = {0:0, 1:1}

def fibonacci(n):
  if n in known:
    return known[n]
  res = fibonacci(n-1) + fibonacci(n-2)
  known[n] = res
  return res


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Uso: python fibonacci.py <n>")
  else:
    try:
      n = int(sys.argv[1])
      print(f"Fibonacci({n}) = {fibonacci(n)}")
    except ValueError:
      print("Por favor, forneça um número inteiro.")