from histogram import upgraded_histogram as histogram

def print_hist(h):
  for c in h:
    print(c, h[c])

def print_alphabetical_hist(h):
  for c in sorted(h):
    print(c, h[c])

if __name__ == '__main__':
  h = histogram('parrot')
  print_hist(h)
  print_alphabetical_hist(h)

