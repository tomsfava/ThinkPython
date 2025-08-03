def delete_head(t):
  del t[0]

def bad_delete_head(t):
  t = t[1:]
  return t

tt = [1,2,3]

delete_head(tt)
print(tt)
bad_delete_head(tt)
print(tt)
tt = bad_delete_head(tt)
print(tt)