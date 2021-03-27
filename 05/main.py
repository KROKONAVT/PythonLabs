print('Введите x0, v0 и t через пробел')
[x0, v0, t] = map(float, input().split())
a = -9.8
print('Результат x0 + v0 * t - a * t * t / 2:', x0 + v0 * t - a * t * t / 2)