def right_justify(s):
  length = len(s)
  return ' '*(70-length)+s

print(right_justify('Hello'))