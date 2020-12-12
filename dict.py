dict = {
  'name': 'Jack',
  'Age': '20',
  'class': 'First',
  'sex': 'male',
}

print(dict['name'])
print(dict['Age'])

print(dict)

value = dict.pop('sex')
print(value)

print(dict)

for key in dict:
  print(key)

for key,value in dict.items():
  print(key, value)

hello = "HelloWorld"
for c in hello:
  print(c, ord(c))

