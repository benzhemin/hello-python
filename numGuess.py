number = 5
guess = -1

while guess != number:
  guess = int(input('input number please'))
  if guess > number:
    print('greater')
  elif guess < number:
    print('smaller')
  else:
    print('guess!')

print('end')