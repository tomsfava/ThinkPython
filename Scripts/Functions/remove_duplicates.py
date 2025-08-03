def remove_duplicates(t):
  newList = []
  for item in t:
    if item not in newList:
      newList.append(item)
  return newList

if __name__ == '__main__':
  doubled = [2,2,4,4,6,6,8,8]
  print(remove_duplicates(doubled))