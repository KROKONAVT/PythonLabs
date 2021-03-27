print('Введите значение a')
a = float(input())
print('Введите значение b')
b = float(input())
print('До обмена:')
print('a = ', a)
print('b = ', b)
temp = a
a = b
b = temp
print('После обмена через буферную переменную:')
print('a = ', a)
print('b = ', b)
[a,b]=[b,a]
print('После второго обмена без буферной переменной:')
print('a = ', a)
print('b = ', b)