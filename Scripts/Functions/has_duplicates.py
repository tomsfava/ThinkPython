from random import randint

def has_duplicates(t):
  newList = []
  for i in range(len(t)):
    if t[i] in newList:
      return True
    else:
      newList.append(t[i])
  return False

def has_duplicates_allen(t):
  """Returns True if any element appears more than once in a sequence

  t:list

  returns: bool
  """
  #make a copy of t to avoid modifying the parameter
  s = t[:]
  s.sort()

  #check for adjacente elements that are equal
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      return True
  return False

def has_duplicates3(t):
  d = {}
  for x in t:
    if x in d:
      return True
    d[x] = True
  return False

def has_duplicates4(t):
  return len(set(t)) < len(t)

def birthdays_generator(n):
  birthdays = []
  for i in range(n):
    day = randint(1, 365)
    birthdays.append(day)
  return birthdays

def birthday_paradox_simulation(num_simulations):
  count_with_duplicates = 0
  for _ in range(num_simulations):
    group = birthdays_generator(23)
    if has_duplicates(group):
      count_with_duplicates += 1
  probability = count_with_duplicates / num_simulations
  return probability


if __name__ == '__main__':
  list1 = [1,2,3,4,5]
  list2 = [1,2,3,4,5,6,1]

  print(has_duplicates(list1))
  print(has_duplicates(list2))

  list3 = birthdays_generator(23)
  print(list3)
  print(has_duplicates(list3))

  print(birthday_paradox_simulation(1000))