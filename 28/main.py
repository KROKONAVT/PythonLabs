def print_factorization(n: int) -> None:
	i = 0
	if n == 1:
		print('-')
	elif n < 1:
		print('Ошибка')
	else:
		for j in range(2, n + 1):
			while n % j == 0:
				n = n / j
				i+=1
			if i > 1:
				print(j, '^', i, sep = '', end='')
				if n != 1:
					print('*', end='')
			elif i != 0:
				print(j, end='')
				if n != 1:
					print('*', end='')
			i = 0

print('Введите положительное целое число')
a = int(input())
print_factorization(a)
