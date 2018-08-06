import math

print('Введите значение "а"')

a = int(input())

print('Введите значение "b"')

b = int(input())


print('Введите значение "c"')

c = int(input())

x1 = -b + math.sqrt(b**2 - (4 * a * c)) / 2 * a

x2 = -b - math.sqrt(b**2 - (4 * a * c)) / 2 * a

print(x1)
print(x2)
