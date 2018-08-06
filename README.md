#My-homework-1

#Task a

import math

print('Введите R, если хотите узнать длину окружности по радиусу, и D, если по диаметру')

x = input()

if x == 'R' or 'r':
  print('Введите значение радиуса')
  R = int(input())
  l = 2 * math.pi * R
  print(int(l))

elif x == 'D' or 'd': 
  print('Введите значение диаметра')
  
  D = int(input())
  
  L = math.pi * D
  print(int(D))
