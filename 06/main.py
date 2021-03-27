print('Введите коэффициент а')
a = float(input())
print('Введите коэффициент b')
b = float(input())
print('Введите коэффициент c')
c = float(input())
if a == 0 and b == 0 and c == 0:
    print('х-любое число')
elif a == 0 and b == 0 and c != 0:
    print('Уравнение не существует')
elif a == 0 and b != 0 and c !=0:
    x1 = (-c) / b
    print('x =', x1)
elif a == 0 and b != 0 and c == 0:
    print('x = 0')
elif a != 0 and b == 0 and c == 0:
    print('x = 0')
else:
    D = b * b - 4 * a * c
    if D < 0:
        print('Корней нет')
    elif D == 0:
        x1 = -b / (2 * a)
        print('x =', x1)
    else:
        x1 = (-b + D ** (1/2)) / (2 * a)
        x2 = (-b - D ** (1/2)) / (2 * a)
        print('x1 =', x1)
        print('x2 =', x2)