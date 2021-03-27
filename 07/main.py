print('Выберите способ вычисления площади треугольника:\n1. По трем сторонам\n2. По координатам точек')
change = int(input())
if change != 1 and change != 2:
    print('Ошибка')
elif change==1:
    print('Введите сторону а')
    a = float(input())
    print('Введите сторону b')
    b = float(input())
    print('Введите сторону c')
    c = float(input())
    if a + b > c and b + c > a and c + a > b:
        p = (a + b + c) / 2
        S = (p*(p - a)*(p - b)*(p - c))**(1/2)
        print('Площадь треугольника =', S)
    else:
        print('Треугольник не существует')
else:
    print('Введите координаты а (x y) через пробел')
    [ax, ay] = map(float, input().split())
    print('Введите координаты b (x y) через пробел')
    [bx, by] = map(float, input().split())
    print('Введите координаты c (x y) через пробел')
    [cx, cy] = map(float, input().split())
    a = ((bx - ax)**2+(by - ay)**2)**(1/2)
    b = ((cx - bx)**2+(cy - by)**2)**(1/2)
    c = ((ax - cx)**2+(ay - cy)**2)**(1/2)
    if a + b > c and b + c > a and c + a > b:
        p = (a + b + c) / 2
        S = (p*(p - a)*(p - b)*(p - c))**(1/2)
        print('Площадь треугольника =', S)
    else:
        print('Треугольник не существует')