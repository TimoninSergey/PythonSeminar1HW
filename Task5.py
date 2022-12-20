"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
"""
import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return dist

X1 = int(input('Введите X1: '))
X2 = int(input('Введите X2: '))
Y1 = int(input('Введите Y1: '))
Y2 = int(input('Введите Y2: '))

print('Расстояние равно {}'.format(round(distance(X1, Y1, X2, Y2),3)))