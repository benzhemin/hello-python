def fabnacci(n):
  a, b, counter = 0, 1, 0
  while counter < n:
    counter += 1
    print(a)
    a, b = b, a+b

fabnacci(10)

def fab_generator(n):
  a, b, counter = 0, 1, 0
  while counter < n:
    yield a
    a, b = b, a+b
    counter += 1

fab = fab_generator(10)

for value in fab:
  print(value)