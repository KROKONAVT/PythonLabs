print('Введите количество элементов n')
n = int(input())
print('Введите n чисел')
arr = list(map(int, input().split()))
if len(arr) != n:
	print('Введено неверное количество элементов')
	exit()
	
for i in range(0, n):
	print()
	for j in range(0, i + 1):
		if j == 0:
			continue
		else:
			for j in range(0, i + 1):
				for x in range(0, i):
					if arr[x] > arr[x + 1]:
						arr[x], arr[x + 1] = arr[x + 1], arr[x]
	size = i
	if size > 4:
		size = 4
	for k in range(size, -1, -1):
		print(arr[k], end = ' ')