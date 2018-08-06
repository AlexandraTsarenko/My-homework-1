import math

print('Введите R, если хотите узнать длину окружности по радиусу, и D, если по диаметру')

x = input()

if x == 'R' or x == 'r':
  print('Введите значение радиуса')
  r = int(input())
  l = 2 * math.pi * r
  print(l)

elif x == 'D' or x =='d': 
  print('Введите значение диаметра')
  d = int(input())
  l = math.pi * d
  print(l)
  
else:
  print('Ошибка! Запустите еще раз')
