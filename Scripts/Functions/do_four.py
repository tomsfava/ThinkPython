def do_twice(f):
  f()
  f()

def print_twice(s):
  print(s)
  print(s)

def do_four(f):
  do_twice(f)
  do_twice(f)
