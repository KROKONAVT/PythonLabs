a = 1
print('Введите число, факториал которого требуется вычислить')
n = int(input())
if n < 0:
	print('Нет значения')
else:
	for b in range(1, n + 1):
		a = a * b
	print(a)