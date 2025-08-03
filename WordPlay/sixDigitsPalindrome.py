from Scripts.Functions.palindrome import is_palindrome

def six_digits_palin_patt(intervalo):
  applies = list()
  for n in intervalo:
    s1 = str(n)
    if is_palindrome(s1[2:6]):
      s2 = str(n+1)
      if is_palindrome(s2[1:6]):
        s3 = str(n+2)
        if is_palindrome(s3[1:5]):
          s4 = str(n+3)
          if is_palindrome(s4):
            applies.append(n)
  return applies, len(applies)

if __name__ == '__main__':
  intervalo = range(100000, 999999)
  resultados, quantidade = six_digits_palin_patt(intervalo)
  print('Números que atendem ao padrão', resultados)
  print('Total:', quantidade)