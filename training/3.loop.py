num = 0

while num < 10:
  num+=1
  if num == 5:
    continue
  print(num)


list = ["apple", "banana", "cherry"]
for index, item in enumerate(list):
  print(f'{index}: {item}')