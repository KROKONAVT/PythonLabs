a = 0
print('Введите число больше 0')
x = int(input())
if x <= 0:
    print('Некорректный ввод')
elif x == 2:
	print('Число простое')
elif x == 1:
	print('Число не простое и не составное')
else:
    for i in range(2, x):
        a = 0
        a = x % i
        if a > 0:
            continue
        else:
            break
    if a > 0:
        print('Число простое')
    else:
        print('Число составное')