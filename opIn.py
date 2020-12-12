list = [1, 2, 3, 4, 5]
a = 4
flag = False

for i in list:
  if i == a:
    flag = True
    break

if flag:
  print("Found a")

if a in list:
  print('A is already in list')
