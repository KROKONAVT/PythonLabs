print('Введите выражение в формате [число операция число]')
[x1, s, x2] = input().split()
x1 = float(x1)
x2 = float(x2)
if s == '+':
    result = x1 + x2
elif s == '-':
    result = x1 - x2
elif s == '/':
    if x2 == 0:
        print('На 0 делить нельзя!')
        exit()
    result = x1 / x2
elif s == '*':
    result = x1 * x2
else:
    print('Неизвестная операция')
    exit()
print(result)