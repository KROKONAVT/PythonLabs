print('Введите число S и два диапазона [l1..r1] [l2..r2] через пробел')
[s, l1, r1, l2, r2] = map(int, input().split())
if l1 > r1 or l2 > r2:
    print('Ошибка ввода')
elif l1 + l2 > s or r2 + r1 < s:
    print('-1')
else:
	print(l1, s - l1)