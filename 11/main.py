print('Число, возводимое в степень')
x = int(input())
print('Степень числа')
n = int(input())
y = x
if n > 0:
    for i in range(1, n):
        y = y * x
    print(y)
elif n < 0:
    for i in range(-1, n, -1):
        y = y * x
    y = 1 / y
    print(y)
elif n == 0:
    print('1')