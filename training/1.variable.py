name = '니힐'
age = 33
girl = None
job = True
money = False

print(f'{name}은 {age}살입니다. 여자친구는 {girl}입니다. 직업은 {job}입니다. 돈은 {money}입니다.')

print(type(name))
print(type(age))
print(type(girl))
print(type(job))
print(type(money))

a, b, c = 1, 2, 3

print(a, b, c)

x = y = z = 0

print(x, y, z)

print(isinstance(name, int))

print(isinstance(name, str))

numberString = '123'
number = int(numberString)

print(numberString, type(numberString), number, type(number))
print(f'{numberString}은 {type(numberString).__name__}입니다. {number}은 {type(number).__name__}입니다.')